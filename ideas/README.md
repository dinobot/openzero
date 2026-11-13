# Ideas — engineering beyond what Zero imagined

Brainstorm 2026-11-05. None of these is decided, scheduled or bought; this is the parking lot so the
good ones are not lost. Ingredients already on the bike: Sevcon Gen4 on CANopen, ANT BMS with BLE/UART,
an ESP32 with CAN (the speed converter), a 5 kWh LFP pack, a diode-isolated SB50 charge port.
Backup / camp power has its own note: `backup_power/README.md`.

Effort tags: **evening** (one pin or one DVT object), **weekend**, **project**, **wild** (physics
allows it, nothing else recommends it).

## The controller can do more than Zero allowed

| Idea | Effort | How |
|---|---|---|
| Reverse gear | evening | Gen4 DI2 is "reverse"; a button plus the inching limits. Rolls 30 kg of pack out of a canyon on Catalina without pushing. No Zero ever had it |
| Regen paddle | evening | **Moved to Next Steps 5a (2026-11-05).** Gen4 footbrake switch 2130h on DI5 (pin 20): held = max footbraking (2920h), released = neutral braking. Proportional version later via Pot 2 (2221h) |
| Cruise / hill descent | project, safety-critical | Sevcon velocity mode (6042h) from the ESP32 holds a speed downhill on regen; brake switch cancels. Only after the speed converter has lived a season |
| Launch / anti-wheelie | weekend | One magnet on the front wheel: motor accelerating while the front wheel does not → ESP32 switches to the weak profile. Stock gearing at 52 A already wheelies |
| Dyno mode | weekend | Log 6077h (torque) and 5100h (current) through an acceleration: a real power curve of the pack, i.e. the 52 → 78 A validation in numbers |

## Energy

| Idea | Effort | How |
|---|---|---|
| V2L / house UPS | weekend | See `backup_power/README.md` |
| Charge from someone else's EV | none | Ioniq / Kia / F-150 have a 220 V V2L outlet; the E22 has universal input |
| Range-extender string in a top box | project | A second 30S string, ORed through another MD110A (the same diode as the charge port). The 0.8 V drop spoils current sharing, so honestly two contactors and "connect only when ΔV < 1 V". Solves the 2p volume problem above the rear fender instead of in the bay |
| Pack heating | weekend | 12 V silicone heaters under the cells, ESP32 heats to 5 °C on ANT temperature before charging and holds it in frost. The only way to charge below 0 °C without hurting the cells |
| PTO | wild | The catalogue has a chain-drive option (12T 30-04890). A sprocket on the motor and 5 kW of shaft power at camp: water pump, winch, log splitter |

## The ESP32 is already an onboard computer (each an evening)

- **Odometer posts itself**: home Wi-Fi → `site/landing/odometer.json`; the landing page already reads it.
- **Range prediction**: ANT SOC over BLE plus a rolling Wh/km over the last 5 km → "N km left" on the
  ClearView. This is the real replacement for the CT-22 lamp scheme.
- **Standby drain measured**: while parked, log SOC and pack voltage hourly. The figure CLAUDE.md asks for.
- **TPMS**: $20 BLE pressure sensors; the ESP32 already hears them.
- **BLE immobiliser**: a relay on FS1 (pin 19) closes only near the phone. FS1, not key power: a BLE
  glitch while riding must only prevent re-opening the throttle, never kill the drive on the road.
- **DVT over Wi-Fi**: ESP32 as a CAN bridge, SocketCAN on the laptop; covers 90 % of what is now typed
  into objects by hand. Details below.
- **GPS logger for dirt**: track + current + cell temperatures on one chart. Catalina should be ridden with it.

### ESP32 bridge: web interface to Sevcon settings over Wi-Fi (researched 2026-11-05)

**Premise checked against Gen4 manual V3.4 (6-5/6-6 "Access authorization", "How NMT state affects access
to parameters"; 7-1 "Monitoring"):** DVT is nothing but a CANopen master. Every parameter and every status
variable is in the object dictionary and is read/written by SDO; the manual itself says "to login with other
configuration tools write your password to object 5000h". The "CAN can only change the current limits" note
in CLAUDE.md is about what a *BMS* can do on the move through 2870h, not about configuration. So the IXXAT +
DVT + Windows stack was never a technical requirement, only the convenient shell. Any CAN adapter on any OS
(CANable / gs_usb $20–40, `python-canopen` with the EDS) does the job today; the ESP32 only replaces the USB
cable with Wi-Fi. No new Sevcon wiring: CAN is on pins 16/27 where the DVT already sits.

What the shell needs, and where it comes from:

| Need | Source |
|---|---|
| Object names, types, ranges | EDS for this firmware, in the DVT installation (manual 6-3: one EDS per model and software version) |
| Access level ≥ 4 | password → 5000h sub 02h, user ID → sub 03h, level read back from sub 01h; verified against the OEM key 5001h, so generic Sevcon passwords may not fit a Zero unit. The DVT sends it in clear over CAN at every login: capture once with a logger (the ESP32 in listen-only) during a normal DVT session |
| Pre-operational for protected objects | write 1 to 2800h (0 = back to operational); state in 5110h (05 = op, 7F = pre-op). The controller refuses pre-op while driving |
| Save | 1010h sub 01h = 0x65766173 |
| Fault text | 5610h: write fault ID to sub 01h, read text from sub 02h |

Not covered: firmware upload (bootloader, DVT only) and the DVT wizards (motor characterisation, autotune),
which are scripted SDO sequences in an order we do not know. Both are already done on this bike.

**Worked example — the MBB removal, repeatable without DVT** (CLAUDE.md steps 8–9): login → 2800h = 1 →
1400h–1403h sub 01h |= 0x80000000 (RPDOs from MBB/CCU invalid) → 1016h entries = 0, 100Ch = 0, 100Dh = 0
(no heartbeat / node-guard wait) → 1F80h = 0x04 (NMT self-start) → 1010h sub 01h save → 2800h = 0 → power
cycle → 5110h reads 05.

```python
import canopen
net = canopen.Network()
net.connect(bustype="gs_usb", channel=0, bitrate=500000)   # bitrate = 5900h; or socketcan / slcan
n = net.add_node(NODE_ID, "gen4.eds")
n.sdo[0x5000][2].raw = PASSWORD
n.sdo[0x5000][3].raw = USER_ID
print("access level", n.sdo[0x5000][1].raw)
n.sdo[0x2800].raw = 1
for idx in range(0x1400, 0x1404):
    n.sdo[idx][1].raw |= 0x80000000
for sub in range(1, n.sdo[0x1016][0].raw + 1):
    n.sdo[0x1016][sub].raw = 0
n.sdo[0x100C].raw = 0
n.sdo[0x100D].raw = 0
n.sdo[0x1F80].raw = 4
n.sdo[0x1010][1].raw = 0x65766173
n.sdo[0x2800].raw = 0
```

Caveats the DVT hid: (1) a Gen4 alone on the bus gets no ACK for its TPDOs / heartbeat and goes bus-off, so
either keep the ESP32 on the bus in normal mode or also invalidate TPDOs (1800h–1803h bit 31, 1017h = 0);
(2) node ID and bitrate must be found first (heartbeat on 0x700 + ID at 125/250/500 kbit, or poll 1000h over
IDs 1–127); (3) write only in pre-op with the bike standing, and the web page must not be reachable while
riding; (4) the "parameters do not survive a restart" problem in CLAUDE.md smells like access level — read
5000h sub 01h after login before blaming 1010h.

Plan in order of effort: (a) USB-CAN + `python-canopen` on the laptop, one script per CLAUDE.md step — days;
(b) ESP32 as SLCAN-over-TCP bridge, same scripts over Wi-Fi — same hardware as the speed converter; (c) a web
page on the ESP32 with the object table from the EDS — the "DVT replacement" proper, only if (a)/(b) get used
often enough to deserve it.

## Pure wildness, physics does not object

- AVAS: a speaker driven by RPM from CAN, or a Geiger counter ticking on battery current.
- Brake light from an IMU: real deceleration, not the brake switch, including motor braking downhill.
- Trailer pack: another 5 kWh on a trailer through SB50 and a second ANT. Catalina and back without charging.

## Not worth it, and why

Solar into the pack (no 110 V MPPT), Sevcon as a mains inverter (phase outputs are not a sine),
jump-starting cars from the 12 V rail (DC-DC sized for lights), heating from HV directly (everything
that heats lives on 12 V).

## Ranking by wow per hour (2026-11-05)

Reverse gear, odometer to the site, dyno log, regen paddle.
