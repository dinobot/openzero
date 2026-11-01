# OpenZero — 2014 Zero FX Conversion Project

## Project Summary

Complete wiring conversion of a 2014 Zero FX electric motorcycle. All proprietary Zero modules
(MBB, CCU, Zero BMS CAN integration) eliminated. Sevcon Gen4 motor controller retained and rewired
from scratch to run standalone from a DIY LiFePO4 96V battery pack with ANT BMS.

**Spec sources rule (owner, 2026-10-21):** only manufacturer documents count — they live in `manuals/`.
Marketplace listings (AliExpress etc.) are not sources: the 52 Ah listing was wrong on dimensions, C-rate
and cycle life.

---

## Current Status

### Working
- Contactor closes correctly (GX11-013, 120V DC coil)
- Controller powers up, reaches NMT Operational
- DSP402 statusword 0x0437 = Operation Enabled confirmed
- Digital inputs confirmed via DVT status tree (raw inputs hex value changes on switch)
- Forward direction input (pin 18, DI1) working — wired to B−, always asserted
- FS1 killswitch (pin 19) working — motor enables after FS1 closes post power-on
- Motor spins and responds to throttle input

### Blocking / In Progress
- **Throttle**: Magura 0–5K resistive pot confirmed bad (floating wiper, erratic readings)
  → Replacing with hall-effect throttle from 2016+ Zero FXE (see below)
- **Throttle calibration**: Pot 1 min/max not yet set in DVT
- **Inching**: 0x4886 fault on button press — caused by throttle not reading zero at rest
  (will self-resolve once throttle replaced and calibrated)
- **Inching parameters**: Not fully configured yet (speed, timeout, torque limit)
- **Power supply**: Testing with weak DC adapter causes "supply critical" faults under load
  → Must test with actual 96V LiFePO4 pack for all further testing
- **NVM save**: Parameters are not being saved across restarts
  → Must write 0x65766173 to object 1010h sub 01h (or use DVT Save button) after every change

---

## Next Steps (in order)

1. **Source hall throttle** from 2016+ Zero FXE — wire to pins 34/22/B−
2. **Calibrate throttle** in DVT — set Pot 1 min (~0.8V) and max (~4.2V)
3. **Configure throttle fault thresholds** — below 0.5V = break fault, above 4.5V = short fault
4. **Configure inching** in DVT (object 2905h):
   - Inching speed: 5–10% of max
   - Inching timeout: 1–2 seconds
   - Inching torque limit: 20–30%
   - Inching mode: speed mode (throttle bypassed)
5. **Wire proper killswitch** to pin 19 (FS1) on handlebar
6. **Save all parameters to NVM** (1010h sub 01h = 0x65766173)
7. **Wire and commission ANT BMS** — DONE 2026-10-25: pack built in an aluminium box, BMS live, all 30 cells
   read correctly, protections set (see "ANT settings as configured"), first full charge done and pack
   top-balanced to 3 mV (2026-10-27). Left: rested-spread check, SOC/52 Ah resync check, password, MOSFET toggle
   test, box isolation check, V/A calibration vs DMM, NTC channel check, fuse location, box edge trim
7a. **Set Sevcon battery current limit** in DVT (2870h sub 01h = 0x01; 4623h sub 02h = discharge, sub 03h =
    charge/regen). BMS does not enforce cell C-rate; the limit is static (no peak timer). **Plan (owner 2026-10-21):**
    - First rides: **52 A discharge** (1C, the datasheet's continuous test condition) / **40 A regen**.
    - Validation ride on a hot day (≥30 °C ambient, ≥30 min sustained load: hills or highway) with ANT logging.
      Pass = cell NTCs < 45 °C, MOS temp < 60 °C, no ANT warnings.
    - If passed: raise discharge to **78 A** (1.5C) and repeat the validation. **78 A is the ceiling, never higher**
      (datasheet rates >1C only as 30 s pulses; 2.0C at 45 °C, 1.0C at 55 °C).
    - Regen stays 40 A (0.77C; datasheet 15 s feedback limit 0.8–1.4C at 25 °C). Below 10 °C: regen 25 A,
      discharge 52 A.
    - While in DVT: note node ID and units of 4623h; set under/over-voltage cutback start points ~91 V / ~107 V so
      Sevcon tapers before the ANT hard-cuts. (Testing whether 4623h accepts writes while Operational is optional
      now that the BMS bridge is dropped.)
7b. **Test with 96V LiFePO4 battery pack**
7c. **Battery box enclosure** — model done (`battery_box/enclosure.py`, README there). Print test
    coupons, measure fuse block + frame mounts, fill MEASURE_ME values, then print the full set
8. **Disable MBB/CCU RPDOs** (objects 1400h–1403h, set bit 31 in COB-ID subindex)
9. **Configure NMT auto-start** (object 1F80h = 0x04) — currently requires manual NMT start
10. **Configure contactor PWM** (object 46A1h): pull-in 100%, hold 25–30%, pull-in time 50ms
11. **Consider masking forward direction** via object 2918h → remove pin 18 physical wire
12. **Build speed converter** (ESP32 + CAN → pulse output to CT-22 gauge; decided 2026-10-21 — no wheel Hall sensor)
13. **Install ClearView display**

---

## Hall Throttle Adoption (Zero FXE 2016+)

Replacing failed Magura 0–5K resistive pot with hall-effect throttle sourced from 2016+ Zero FXE.

**Why:** Resistive pots wear, get dirty contacts, and float on wire break. Hall throttle stays
within 0.8–4.2V range on failure — enables proper failsafe configuration.

**Wiring:**
| Hall throttle wire | Sevcon pin | Function |
|-------------------|------------|----------|
| +5V (red) | 34 | Pot 1 supply |
| Signal (white/green) | 22 | Pot 1 wiper |
| Ground (black) | B− | Reference |

**DVT calibration:**
- Pot 1 minimum: ~0.8V (throttle closed)
- Pot 1 maximum: ~4.2V (throttle full open)
- Fault below: 0.5V (wire break detection)
- Fault above: 4.5V (short to supply detection)

---

## Sevcon 35-Pin Connector — Final Wiring

All digital inputs are **active-low (to B−)**. Confirmed via DVT raw input status.

| Pin | Keep | Function | Notes |
|-----|------|----------|-------|
| 1, 6 | ✓ | Key switch / logic power from traction battery | No 12V needed |
| 2 | ✓ | B− reference | Jumpered to pin 24 internally in OEM loom |
| 3 | ✓ | Contactor low-side out | Was absent in OEM (Zero BMS controlled contactor) |
| 4 | ✓ | Contactor supply+ | Was absent in OEM |
| 15 | ✓ | Brake / regen input | |
| 16 | ✓ | CAN High | DVT / ClearView / speed converter |
| 18 | ✓ | DI1 — forward direction | Wired to B−, always asserted. Consider masking via 2918h later |
| 19 | ✓ | DI3 — FS1 killswitch | Active-low, handlebar killswitch |
| 22 | ✓ | Pot 1 wiper — throttle signal | Hall throttle signal wire |
| 24 | ✓ | CAN Low (internal) | Jumpered from pin 2 in OEM loom, leave as-is |
| 27 | ✓ | CAN Low (external) | External CAN wire to DVT / ClearView |
| 31 | ✓ | DI4 — inch forward button | Active-low, momentary starter-style button |
| 32 | ✓ | Encoder supply | Do not remove |
| 33 | ✓ | Encoder GND | Do not remove |
| 34 | ✓ | Pot 1 supply (5V) | Throttle supply |
| 35 | ✓ | Verify in manual | Confirm function before removing |
| 26, 28 | ✓ | Encoder A/B | Motor position sensing — do not remove |

**Pins confirmed removed:** 20 (DI5), 21, pin 18 future candidate after 2918h mask applied

---

## Critical DVT Object Reference

| Object | Function | Value / Action |
|--------|----------|----------------|
| 1010h sub 01h | Save parameters to NVM | Write 0x65766173 |
| 1400h–1403h sub 01h | Disable MBB/CCU RPDOs | Set bit 31 (OR with 0x80000000) |
| 1F80h sub 00h | NMT auto-start to Operational | Write 0x04 |
| 1016h | Heartbeat consumer | Zero out MBB/CCU node entries |
| 100Ch, 100Dh | Node guarding | Set both to 0 |
| 2905h | Inching configuration | Speed 5–10%, timeout 1–2s, torque 20–30% |
| 2914h | FS1 configuration | Set to None to bypass, or assign pin 19 |
| 2918h | Sequence fault masking | Mask forward direction requirement to remove pin 18 |
| 3300h | VPDO digital input mapping | DI4 (pin 31) → inch forward |
| 4680h | Digital input polarity | Active-low (default, likely no change needed) |
| 46A1h | Contactor PWM control | Pull-in 100%, hold 25–30%, time 50ms |
| 5900h | CAN baud rate | Consider 500kbps for MCP2515 compatibility (irrelevant on ESP32) |
| 6040h | DSP402 controlword | 0x0006→0x0007→0x000F to enable drive |
| 6041h | DSP402 statusword | 0x0437 = Operation Enabled (confirmed) |
| 6042h | Target velocity | Test: write 100 RPM to command motion from DVT |
| 6061h | Modes of operation display | Read to confirm current drive mode |
| 2870h sub 01h | Battery current limit mode | 0x01 = manual (values from 4623h); 0x02 = compatible CAN BMS; 0x04 = power limit |
| 4623h sub 02h/03h | Battery current limit values | sub 02h discharge / sub 03h regen. 52 A / 40 A first; 78 A / 40 A after hot-day validation; 78 A is the ceiling (step 7a). Static, no I²t |
| 2871h | Torque cutback on battery limit | Enable so TracApp does not request torque the limit cannot deliver |
| 5100h | Battery current readout | Monitor actual pack current (regen negative) |
| 2910h / 2911h | Throttle / footbrake config | NOT current limits (earlier note was wrong). 2910h sub 21 = throttle wire-off threshold |
| 2C00h | Nominal battery voltage | 96 (stock Zero: 102) — cutbacks are referenced to it |
| 2C01h | Over-voltage start cutback / limit | regen taper start ~106–107 V, cut-out ~112 V (Gen4 manual 6-37) |
| 2C02h / 2C03h | Under-voltage start cutback / limit / delay | start ~91 V, cut-out ~86 V (ANT UV cut is 84 V); keep default delay |
| 2C30h sub 06h | BDI cell count | 0 = BDI disabled (manual caution; SOC comes from ANT) |
| 5820h / 5821h | Precharge level (% of battery V, 50–90) / min capacitor V to close contactor | 90 %; the earlier "~86 V" note was this percentage, not an absolute |
| 4624h | Trip speed (overspeed fault) | leave stock |

---

## Contactor — GX11-013 (120V DC coil)

- Pull-in duty: 100% (full bus voltage ~96V, sufficient for 120V rated coil)
- Hold duty: 25–30% (~24–29V at 96V bus)
- Pull-in time: 50ms
- **Precharge**: external 100Ω resistor in parallel with main contactor required
- Precharge threshold in DVT: 5820h = 90 % of battery voltage (object is a percentage, 50–90 %); 5821h = minimum capacitor voltage for the contactor to close

---

## Speed Converter (decided 2026-10-21: build it; wheel Hall sensor rejected as non-OEM + extra wire)

Reads motor RPM from Sevcon CAN TPDO → outputs Hall-sensor-style pulse signal to the CT-22 gauge.

**Hardware:** ESP32 + CAN transceiver (SN65HVD230) preferred over Arduino Uno + MCP2515: built-in CAN
controller, spare hardware UARTs (Uno's only UART is taken by USB), LEDC timer for the pulse output, BLE/Wi-Fi
for logging. Leave a 4-pin UART header free for the optional BMS bridge below. If staying on Uno + MCP2515,
the module must use a 16 MHz crystal for 1 Mbps.

**Key parameters:**
- Sevcon TPDO1 ID: 0x180 + node ID (check node ID in DVT)
- Velocity object: 606Ch (actual velocity, 4 bytes, signed int32, RPM)
- Gear ratio: ~8.9:1 motor-to-wheel (verify in OM-FX-MY14.pdf on Desktop)
- CAN baud: match Sevcon setting (configure 5900h first)
- Output pin: D9 (timer-driven square wave, NPN open-collector to speedometer)

**No additional Sevcon pins needed** — speed converter taps existing CAN bus wires (pins 16/27).

### CT-22 gauge (`manuals/CT-22-MANUAL.pdf`, board CY1874D_MB110D)
- Speed input: pulse. Parameter `0-0420` = 420 Hz ↔ 60 km/h (range 0–999 Hz) → converter outputs
  **7.0 Hz per km/h**; keep the default and calibrate against GPS. Password 6610 enters the parameter menu.
- Supply/pinout not documented. Factory battery thresholds are 125–152 V, so the board is built for ~144 V
  scooters and most likely sits directly on the traction bus and measures its own supply (= HV wire to the
  handlebar). Bench-test before wiring: current-limited PSU, ramp from 10 V, note turn-on voltage and draw;
  check for a separate sense wire. A 96→12 V DC-DC is needed anyway (lights).
- Battery gauge is voltage-only: 6 thresholds per set (0/20/40/60/80/100 %, 0.1 V steps), two sets —
  charging 2–6 + D, discharging 7–B + E (the manual's labels are garbled, map by index). Extra logic:
  `C` = seconds to hold "full" after charging, `F` = "charging memory", `J` = judge time (a big voltage step
  is applied only after it persists J seconds; small steps apply at once). Set **J ≈ 20–30 s** (longer than
  one acceleration, shorter than a red light, so stops refresh the display with the rested value — the
  factory 30 s is about right; bench-check what step size counts as "big"), **C = 0, F = 0, charging set =
  copy of the discharging set** so regen cannot switch tables.
- **Owner decision 2026-10-27: SOC by voltage does not work for LFP** (and is a crutch for any chemistry).
  The gauge is not an SOC scale — it is configured as a **two-mode lamp** (reserve / empty) for the ride,
  see "SOC by voltage" under Battery Pack. "Full" is deliberately not shown: the smart charger and the ANT
  app before the ride cover it. Real SOC lives in the ANT app.
- Alternatives considered (2026-10-26, not chosen): (1) 12 V dash with a fuel-sender input, SOC from ANT via
  BLE emulated as sender resistance by the speed-converter ESP32 — this is what Zero itself did in 2013 with
  a Koso RX-1N (`zeromanual/wiki/XMX_Platform/Unofficial_Service_Manual.md`); gives 10+ segments and no HV
  at the bars. (2) Feeding the CT-22 a synthesised voltage from the ESP32 — only worth it if the bench test
  shows it runs from ~12 V with low thresholds accepted, or has a separate sense wire; a programmable
  95–110 V supply for 5 segments is not. Revisit (1) if the lamp scheme proves annoying on real commutes.

### BMS bridge (dropped 2026-10-21 — section kept for reference)

Owner decision 2026-10-21: static limits in Sevcon + ANT thresholds; no bridge. If ever revived: the ANT
30ZHB7 speaks the new protocol (0x7E 0xA1) over UART **and BLE**; `syssi/esphome-ant-bms` supports both.
BLE from the ESP32 needs no wires but ANT holds one connection, so the phone app is blocked while the
ESP32 is connected; the UART header is normally occupied by the Bluetooth dongle.

**What Gen4 can do with a BMS.** Nothing standard (no CiA 418/419, no named BMS profile). The only hook is
2870h sub 01h = 0x02 "battery current limit controlled by compatible BMS": an external CANopen node writes the
discharge/charge limits into 4623h sub 02h/03h by SDO (or mapped RPDO); 2871h makes TracApp cut torque to match.
Sevcon never sees cells, SOC or temperature and sends nothing back. Zero's MBB did exactly this on this controller
(MBB log entries "discharge current limited (XX%)"). Manual 177/52701 V3.3 confirms "dynamically change the
allowed battery current by exchanging CAN messages with a compatible BMS".

**ANT BMS cannot do it directly.** Its CAN output is a proprietary telemetry broadcast; it does not write SDOs.
Its UART (same port the Bluetooth module uses, 9600 8N1, ~140-byte reply with every cell voltage, pack current,
SOC, up to 6 NTCs, MOSFET state, protection flags) is fully documented in open code:
syssi/esphome-ant-bms (both protocol generations), RoboDurden/AntBms-Arduino. Read ANT over UART, not CAN —
the one CAN bus on the board belongs to the Sevcon.

**Bridge design (same board as the speed converter):**
```
ANT BMS ──UART──► ESP32 ──CAN──► Sevcon   (reads TPDO 606Ch → speedo pulses; writes SDO → 4623h limits)
```
- Loop at 1–2 Hz: poll ANT → compute limits → SDO expedited write (cmd 0x2B for 16-bit, index 0x4623 LE,
  sub 02h/03h) on 0x600+node, expect 0x60 ack / 0x80 abort on 0x580+node.
- Limit table (starting point): base 78 A; min cell < 2.9 V or SOC < 10 % → taper to 20 A; cell T > 45 °C →
  reduce; T < 0 °C → charge (regen) limit 0; T < 5 °C → discharge 40 A; any ANT protection flag or 3 missed
  replies → 20 A; max cell > 3.55 V → regen 0.
- Fail-safe: NVM holds the conservative static limit; bridge may only move it within 20–78 A; if the bridge
  dies, Sevcon keeps the last value (worst case 78 A = agreed cap). Bridge never touches contactor or enable.
  Do NOT make Sevcon a heartbeat consumer of the bridge (1016h) — a bridge glitch would fault the drive on the road.
- Optional: bridge publishes SOC / temperature as its own TPDO for ClearView.

**The one unknown — verify in DVT during step 7a:** does 4623h sub 02h/03h accept an SDO write while
Operational (with 2870h = 0x02), and does 5100h show the new limit taking effect? If the write aborts
(e.g. 0x06010002, pre-op only), fall back to 2870h = 0x03: limits scaled by profile factors (4623h sub 04h/05h),
with the bridge switching driveability profiles via VPDO (3300h) instead of writing amps.
Also needed from DVT: Sevcon node ID, units of 4623h (A, 1/16 A or %), baud at 5900h.

**Why not now.** It covers three situations: (1) graceful limp mode instead of an ANT hard cut on a weak /
empty cell; (2) regen into a full or cold pack (ANT cuts charge → bus voltage spike → Sevcon overvoltage →
abrupt loss of regen, and of drive too on common-port ANT variants); (3) allowing 78 A only when warm and
healthy. Sevcon's own under/over voltage cutbacks (pack-voltage based) plus ANT thresholds set outside the
Sevcon envelope cover most of (1) and (2) with zero code. Cost: weeks of firmware work on a bike that has not
yet moved on the pack. Revisit if: ANT has ever cut power while riding, a single cell consistently sags first in
ANT logs, or 78 A with temperature gating is wanted. Building the speed converter on ESP32 with a free UART
keeps the door open at no cost.

---

## Battery Pack

### Configuration
- Chemistry: LiFePO4, 30s1p, nominal 96 V (30 × 3.2 V), 5.0 kWh
- Cells: **Gotion (Hefei Guoxuan) IFP28148115A-52Ah**, spec Q/GX 030-2019 rev 2021-01-29 →
  `manuals/ifp52.pdf`. Only valid cell source (cells scan as Gotion IFP52; owner to confirm height with calipers).
- Cell: 148 × 28.2 × 118.6 mm (W × T × H incl. terminals), 966 ± 30 g → 30 cells = 29 kg
- Voltage window 2.0–3.65 V (1.8 V floor below 0 °C)
- **Continuous: 1C = 52 A** is the datasheet test condition; nothing above 1C is rated continuous
- Pulse discharge, 30 s (table A.9): 25 °C 1.6C (SOC < 10 %) … 3.8C (SOC > 80 %); 45 °C 2.0C; 55 °C 1.0C;
  0 °C 0.5–1.7C
- Pulse regen, 15 s (table A.10): 25 °C 0.8–1.4C; 10 °C 0.5–0.9C; 45 °C 1.1–2.0C
- DC resistance, 3C/30 s (table A.5): 1.9 mΩ @25 °C 50 % SOC; 2.9 mΩ @10 % SOC; 4.2 mΩ @0 °C; 10 mΩ @0 °C
  10 % SOC → pack ≈ 57 mΩ warm (sag 1.4 V @25 A, 3.0 V @52 A, 4.4 V @78 A)
- Charge: 0.5C = 26 A CC to 3.65 V, cut-off 2.6 A, 10–45 °C; below 0 °C only 0.05–0.2C stepped (table A.1.2)
- Temperature: optimum 10–35 °C; discharge −30…60 °C (cell ≤ 60 °C). Gotion BMS thresholds (A.2):
  55 °C warn / 60 °C cut; −20 / −30 °C cold; OV 3.7 / 3.8 V; UV 2.2 / 2.0 V
- Cycle life 2000 @25 °C 1C/1C to 80 %; calendar 8 y @25 °C 50 % SOC. Storage ≤35 °C at 30–50 % SOC
- Compression 20–250 kgf at 5 % SOC (datasheet marks it TBD)
- Can insulation: factory blue film only is acceptable cell-to-cell when the stack is clamped and cannot move;
  plates, centre plate and rods must be insulated; check can-to-can open circuit before fitting busbars
- Max continuous power: 96 V × 52 A ≈ **5 kW** (≈ 7.5 kW at 78 A after thermal validation, see step 7a)
- All further testing must use the actual pack — DC adapter insufficient for any loaded motor testing

### SOC by voltage (datasheet table A.4, 25 °C, rested OCV × 30) and the go-home rule

| SOC | V/cell | Pack V | SOC | V/cell | Pack V |
|-----|--------|--------|-----|--------|--------|
| 100 % (rested after charge) | 3.375 | 101.3 | 30 % | 3.284 | 98.5 |
| 95 % | 3.329 | 99.9 | 25 % | 3.272 | 98.2 |
| 90–75 % | 3.328 | 99.8 | 20 % | 3.253 | 97.6 |
| 65 % | 3.324 | 99.7 | 15 % | 3.230 | 96.9 |
| 60 % | 3.310 | 99.3 | 10 % | 3.210 | 96.3 |
| 50 % | 3.290 | 98.7 | 5 % | 3.180 | 95.4 |
| 40 % | 3.288 | 98.6 | 0 % | 2.928 | 87.8 |

80 % → 20 % is only 2.2 V on the pack; throttle sag (1.4 V at 25 A, 4.4 V at 78 A, double that at 0 °C)
is as large as the whole range. Rested OCV of LFP barely depends on temperature; what grows in the cold is
sag. The lower knee (3.21 → 3.18 → 2.93 V over the last 10 %) is the only sharp feature.

**Owner decision 2026-10-27: SOC by voltage does not work for LFP** (and is a crutch for any chemistry).
To make the CT-22 an error-free instrument signal the SOC scale is turned into a **two-mode lamp** for the
ride: the three upper thresholds are dummies hugging each other, the three lower ones are spaced ≥ 1.1 V
apart so an unknown ADC error or 0.1–0.2 V/cell imbalance cannot move a state. **"Full" is not shown on
the dash at all** (owner 2026-10-27): the smart charger and the ANT app before the ride cover it. The gauge
exists to say "go home" as accurately as pack voltage allows while riding.

Thresholds are calibrated to **rested OCV**, so the lamp can only err low (safe), never high. Under load the
same segment count means a higher SOC; the shift is the sag (≈ 57 mΩ warm, rising to ≈ 85 mΩ below 20 %):

| Segments lit | CT-22 params (discharging set) | At a stop / coasting (rested) | Steady cruise ≈ 25 A (~60 km/h) |
|---|---|---|---|
| 5 / 4 / 3 | B = 99.5, A = 99.4, 9 = 99.3 | ≥ 60 % | ≥ ~80 % (rarely lit on the move) |
| 2 | 8 = 98.4 | 25–60 % | 45–80 % |
| 1 = **reserve lamp** | 7 = 97.3 | 15–25 % (= ANT level-1 warning) | 25–45 % |
| 0 = **empty lamp** | E = 96.1 | < 12 % | < ~25 % → this is "go home" on the highway |

Reading rule: **at a light, 1 segment = go home (≈ 1 kWh, 10–12 km calm), 0 = roll home without
accelerating. On a steady cruise with no stops, 0 segments = go home.** At 16 A (~50 km/h) the cruise
column shifts ~0.5 V up, at 40 A (~80 km/h) ~1 V down; in the cold the sag doubles. Never read it
mid-acceleration. In-ride accuracy is capped at about one state by speed and temperature; if that is ever
not enough, the fix is real SOC from ANT (fuel-sender emulation, see CT-22 section), not more thresholds.
Charging set (2–6, D) = copy of the discharging set; C = 0, F = 0, J ≈ 20–30 s (see CT-22 section).
What the lamp cannot see: one weak cell (pack sum stays high) — that is ANT's job.

**Before trusting it (both mandatory):** (1) bench: find the real switching voltage of each segment with a
lab PSU and shift the thresholds by the measured ADC offset; (2) first rides: at every stop compare segments
with ANT SOC and adjust.

**Go-home rule:**
1. **Go home** = ANT app SOC 20 % (its level-1 warning) or the CT-22 reserve lamp (1 segment) while stopped,
   or coasting, or the empty lamp (0 segments) on a steady cruise (never judge it mid-acceleration).
   ≈ 1 kWh left ≈ 10–12 km at a calm pace. Empty lamp at a stop = < 12 %: no more accelerating.
2. **Stop accelerating** = power fades under throttle: that is the Sevcon under-voltage cutback (~91 V under
   load ≈ 5 % SOC). Roll home gently.
3. **ANT cut** at 2.8 V/cell (84 V) only happens under load near empty — if it ever fires, the two signals
   above were ignored. Do not park below 10 %; charge only above 10 °C.

### Power Budget vs Original

| | Original Zero FX 2014 | This build (30s1p Gotion) |
|--|----------------------|--------------------------|
| Cell chemistry | Farasis NMC pouch | Gotion LiFePO4 prismatic |
| Cell capacity | 25Ah | 52Ah |
| Max discharge rate | 3–5C continuous | 1C continuous, ≤3.8C for 30 s |
| Pack voltage | ~102V nominal | 96V nominal |
| Max continuous current | ~125A (5C) | 52A (1C); 78A after thermal validation |
| Max continuous power | ~12.7kW | ~5kW (7.5kW at 78A) |
| Motor peak capability | ~33kW (44hp) | ~33kW (44hp, but battery-limited) |
| Effective output | ~44hp peak / ~17hp continuous | **~6.7hp continuous** |

**Root cause:** Gotion rates the IFP28148115A (EV + ESS cell) at 1C continuous with >1C only as 30 s
pulses. Original Farasis NMC cells were traction cells rated 3–5C. The 52Ah capacity is generous but
C-rate is the limit.

### Path to More Power
1. **2p configuration** → 104A → ~10kW (~13hp) — doubles cell count
2. **3p configuration** → 156A → ~15kW (~20hp) — starts feeling like a motorcycle
3. **EV-grade LiFePO4** (CATL, EVE) — same chemistry, 3–5C rated, drop-in upgrade
4. **NMC cells** — reclaims original performance but sacrifices LiFePO4 safety/longevity
   (see "NMC alternative (28s)" below)
5. **Bought pack: Amorge 26S NMC 21700** — the only off-the-shelf pack found that fits the bay; stock-level
   power without any building. Rejected 2026-10-28 on price (see "Bought-pack alternative — Amorge 26S" below)

### NMC alternative (28s) — researched 2026-10-20, not planned

Stock Zero 2014 pack is 28s NMC (102 V nominal, ~116 V full), so a DIY NMC pack would be **28s**;
the Sevcon, contactor and precharge threshold are already sized for that voltage.

Approximate cell prices (Alibaba / Made-in-China listings, small lots of 8–50 pcs, 2026-10-20):

| Cell | Per cell | 28 cells | Pack (28s1p) |
|------|----------|----------|--------------|
| CATL 51Ah prismatic | ~$29 | ~$810 | 5.2 kWh, ~26 kg |
| CALB 58Ah prismatic | ~$25 | ~$690 | 6.0 kWh |
| CATL 60Ah prismatic | ~$29 | ~$810 | 6.2 kWh |
| Generic 50Ah, small lot | $37–50 | $1000–1400 | |

Add $200–400 lithium freight to the US plus possible duties → **~$1000–1300 landed for 28 cells**.
Energy is about the same as the current 30s1p LiFePO4 (5.0 kWh); the gain is C-rate: listed
2–3C gives 100–150 A battery current (~10–15 kW) vs 52–78 A now. Caveats: listings state C-rate
loosely, "EV-grade 3C" must be confirmed with the seller, and "CATL" on Alibaba often means
B-grade or re-sorted cells.

**Decision (2026-10-20): stay on LiFePO4 as long as a 1.5C / 78 A / ~7.5 kW ceiling is enough.**
At that power level LiFePO4 is the better chemistry for this build, not a compromise:
- Safety: thermal runaway onset ~270 °C and no oxygen release from the cathode, vs ~210 °C and
  self-sustaining fire for NMC. Matters for a sealed printed box, a DIY assembly and a BMS that
  does not enforce cell C-rate.
- Cycle life: 3000–6000 cycles vs 1000–2000 for NMC.
- Lower cost per kWh, and the cells are already bought.
- 96 V vs 102 V nominal is only ~6% less power at the same current.

Costs to live with: ~6 kg heavier for the same energy; flat discharge curve so SOC must come from
the ANT BMS coulomb counter (drifts without periodic full charges); no charging below 0 °C and
reduced power below ~5 °C; larger sag at high current, which is why 1.5C is the sensible cap.

**Revisit NMC only if** stock-level power (12+ kW) is wanted without going 2p/3p. Then 28s × 50–60 Ah
NMC fits roughly the same volume as the current pack and costs ~$1000–1300. Also compare against
EV-grade LiFePO4 (item 3 above) first: same safety, 3C rated, similar money.

**Build differences if NMC is ever chosen.** With prismatic NMC in aluminium cans the mechanical
build is the same as now: cell-to-cell stack, threaded rods, steel end plates, copper strip busbars.
What changes:
- Prismatic only. Pouch cells (the stock Farasis format) need per-cell frames, full-face pressure
  and welded/clamped tabs — the current scheme does not transfer. Order the **threaded-stud terminal
  version**; many CATL/CALB prismatics ship with flat laser-weld pads that cannot take a bolted bar.
- Thermal barrier between cells is mandatory (mica, ceramic paper or aerogel, 1–2 mm): NMC runaway
  propagates cell-to-cell. Adds 30–55 mm to the stack and changes the compression calc.
- Vent path: NMC cells vent hot gas and flame through the top valve. Do not cover the valve with a
  busbar or cover; the box needs a gas exit away from the rider. A sealed printed box is a poor fit.
- Geometry: 28 cells, 14 × 2 layout, cell ~148 × 26 × 90–100 mm (shorter than Gotion's 129 mm) —
  enclosure must be re-derived.
- Settings: hard 4.20 V cell ceiling, ANT BMS NMC profile, charger CV 117.6 V, Sevcon precharge
  threshold ~92 V, at least 2–4 NTCs in the stack.
Same as now: compression (both need it, same order of force), rod insulation from cans, aluminium
positive terminal vs copper bar (bimetal bar or tinned Cu + plated washers), fuse/contactor/precharge,
BMS B−/P− split. Only upside: NMC's sloped voltage curve makes passive balancing and SOC much easier.

**Why LiFePO4 is the DIY-friendly choice here (2026-10-20).** The hands-on work is nearly identical;
the difference is what a mistake costs:
- Overcharge: LFP taken to ~4.0 V degrades and gases, rarely ignites. NMC above ~4.3 V is dangerous,
  above ~4.5 V runaway is likely. A wrong BMS/charger setting is the most common DIY error.
- Single-cell runaway: LFP smokes at ~300–400 °C, often no flame, neighbours survive. NMC burns at
  600–900 °C and chains through the stack in seconds — hence mandatory barriers and vents above.
- Mechanical damage (puncture, dent from a drop, assembly short): LFP almost always survives it.
- Bench accidents (dropped nut on terminals, under-torqued bar): LFP = spark and a scare; NMC can
  mean a 50 Ah cell on fire in the garage.
- Tooling: LFP needs a multimeter and the BMS app. NMC properly needs per-cell checks before
  assembly and temperature monitoring through the first cycles.
Where LFP is worse: flat curve (SOC drift, balancer blind until end of charge), ~20% more weight and
volume, earlier power loss in cold. None of that is a safety issue.
Conclusion: a self-built, non-welded pack in a printed plastic box, with a BMS that does not enforce
C-rate, ridden sat on top of — that is exactly where chemistry margin outweighs 6 kg. NMC DIY packs
exist, but with barriers, vent ducts, metal boxes and EV-grade discipline. LFP is the right call on
the merits, not out of caution.

### Bought-pack alternative — Amorge 26S (researched 2026-10-28, not chosen)

Owner asked whether a ready-made pack could replace the DIY build. Amorge (Shenzhen; Sur-Ron / Talaria /
EM-5 market) sells 26S NMC 21700 packs in a metal box with an ANT Bluetooth BMS: https://www.amorge.com/96v-26s-battery
(also on Alibaba). Worth keeping on record: it is the first off-the-shelf pack found that physically fits the FX
bay, and it is a genuine answer to the 1C power problem. Numbers below are from Amorge's product pages
(manufacturer-stated, not cell datasheets — confirm against Samsung 50S / Molicel P50B sheets before relying on them).

**What it is.** 26S = 93.6 V nominal (Amorge rounds to "96 V"), 109.2 V full, ~78 V empty. Cell choice: Samsung
50S, Molicel P42A/P45B/P50B, EVE 40P/50PL, BAK 45D. QS8/QS10 discharge + XT60 charge leads, 1-year warranty,
dimensions and connectors "customizable". Stated continuous current 250–420 A depending on cells, i.e. 24–40 kW.

| Model (P50B / 50S) | Box, mm (stood on the 6 in face) | Energy | Fit in the 457 × 254 × 178 bay |
|---|---|---|---|
| 26S8P 40 Ah | 152 × 248 × 254 | 3.7 kWh | fits, 3 mm per side |
| 26S9P 45 Ah | 159 × 235 × 286 | 4.2 kWh | fits outright, 9 mm per side |
| 26S10P 50 Ah | 159 × 267 × 279 | 4.7 kWh | 6.5 mm overhang per side in the lower zone (allowed up to 18.7) |
| 26S13P 65 Ah | 152 × 267 × 337 | 6.1 kWh | same overhang; 120 mm spare length; ~35 kg (scaled from their 28 kg for 10P) |

A custom 13P at 11 cells across (~152 × 250 × 355 mm) would fit the bay with no overhang. Still unknown: whether
the quoted sizes include the box, which face the leads exit (only ~26 mm headroom above a 152 mm pack), per-cell
fusing, NTC count, nickel gauge, and whether the BMS is common-port (an XT60 charge lead hints at a separate
charge port, which cannot block regen into a full or cold pack).

**Range comparison** (consumption from the stock ZF5.7 table in `OM-FX-MY14.pdf` p. 1.7: city 44, mixed 57,
88 km/h 70, 112 km/h 104 Wh/km; usable energy = nominal minus the go-home reserve):

| | Gotion 30S (4.25 kWh usable) | Amorge 9P (3.8) | Amorge 10P (4.2) | Amorge 13P (5.5) |
|---|---|---|---|---|
| City | ~95 km | ~85 | ~95 | ~125 |
| Mixed | ~75 km | ~65 | ~75 | ~95 |
| 88 km/h | cannot hold it at 52 A (needs ~6.2 kW; cap ~80 km/h, ~95 km/h at 78 A) | ~55 | ~60 | ~80 |

Energy of 30S LFP and 26S10P is the same (5.0 vs 4.7 kWh), so range is the same; only 13P adds ~30 %.
Amorge buys power and highway speed, not range.

**If it were ever bought, what changes on the bike:** Sevcon under-voltage cutback 91/86 V → ~83/78 V (91 V is
3.5 V/cell ≈ half charge on NMC); over-voltage taper 106–107 V stays; AFU charger reset from 109.5 V (= 4.21 V/cell
on 26S) to ≤ 109.2 V, ideally ~108 V; check contactor pull-in at a 78 V bus; 4623h limits become the controller's
own ratings instead of cell protection, the whole 52 → 78 A validation plan disappears; CT-22 becomes a real SOC
gauge because the NMC curve slopes; insist on common-port BMS. The LFP safety argument above was about a DIY,
non-welded pack — a welded, boxed factory pack removes most of it, what remains is NMC chemistry in a dense 21700
block with unknown cell fusing.

**Why not (owner 2026-10-28).** Alibaba price for 13P is **$2,924** before lithium freight (~$200–400) and
duties, ≈ $3,300–3,500 landed. The whole DIY 30S LFP build (cells + ANT BMS + box) was about one third of that:
~$200/kWh vs ~$550/kWh. Amorge wins only on $/kW, and that power is exactly what the FX chassis cannot use
pleasantly above ~95 km/h (owner: not a pleasant riding experience at highway speed). A pack costing more than
the rest of the motorcycle, as a black box with a 1-year warranty, changes the philosophy of the project — open,
understood, repairable, cheap. In the same philosophy the same money buys a second 30S Gotion string (2p: 104 A,
10 kW, 10 kWh) with a volume problem to solve, not a chemistry or trust problem.

**Verdict.** 30S LFP at 52 A, then 78 A after the hot-day validation, covers the owner's comfort ceiling
(~80 km/h at 52 A, ~95 km/h at 78 A; launch torque is phase-current limited and unaffected). It pinches on long
climbs / headwind at 70+ km/h with a passenger, and below 5 °C. **Revisit Amorge only if** a season of ANT logs
shows power running out on the daily route (which segments, how often), or if a 2p LFP string turns out not to
fit — then 26S9P (fits outright) or a custom-width 13P is the shortest path to stock-level power.

### For Proof of Concept
Current 30s1p is sufficient to validate all systems. Bike will move and all Sevcon functions
can be tested. Performance validation requires higher C-rate cells or more parallel strings.

---

## BMS — ANT BMS 30S Smart

**Model:** ANT BMS **30ZHB7**, 21S–30S smart, 72–130 V LiFePO4/Li-ion/LTO — product page:
https://antbms.vip/product/ant-bms-30s-180a-380a-smart-112v-lifepo4-li-ion-lto-battery-protection-board/
Shipped without a manual. `manuals/ANT-BMS-APP-User-Manual-English.pdf` is the app manual (applies);
`manuals/Ant BMS Smart Bluetooth Relay ... User Manual.pdf` is a manuals.plus compilation for the RELAY line
and only partly applies.  
**Variant on hand:** 220 A continuous / 550 A 10 s (owner-confirmed 2026-10-20), board 190 × 111 × 16 mm,
2 NTC inputs, 100 mA passive balance, Bluetooth. CAN/RS485 are wholesale-only; retail has TTL UART at the
Bluetooth-module header. 220 A over 170 A was the right call: more MOSFETs in parallel = less heat at 78 A.  
**MOSFET vs relay (verify once):** almost certainly MOSFET (10 s peak rating, board size). Test: balance leads
connected, toggle OnDisCHG/OffDisCHG in the app → continuity B−↔P− must switch. Check for a third C− lug: a
separate charge port cannot block regen, so for the bike a **common port** (charger and Sevcon both on P−) is
required.

### Fit vs Pack
| Parameter | BMS spec | Pack requirement | Verdict |
|-----------|----------|-----------------|---------|
| Cell count | 21S–30S | 30S | ✓ exact max |
| Chemistry | LiFePO4/Li-ion/LTO | LiFePO4 | ✓ |
| Voltage range | 72V–130V | 75V–109.5V | ✓ |
| Continuous current | 220A | 52A (1C cell limit) | ✓ not the bottleneck |
| Peak current (10s) | 550A | Sevcon peak demand | ✓ |

### Key Limitation — BMS Does Not Enforce Cell C-Rate
The BMS allows 220A continuous; the Gotion cells are only rated 1C = 52A. The BMS will pass
through whatever the Sevcon demands — it will not cut off at 52A. **Cell overcurrent protection
must be configured in DVT** (Sevcon current limit parameters), not relied upon from the BMS.

### Smart Features
- Bluetooth app (ANT BMS): per-cell voltage, SOC (coulomb counter, < 8 % error claimed), temperature,
  protection/fault log, manual MOSFET control
- Data out: UART (new protocol 0x7E 0xA1) and BLE — both supported by `syssi/esphome-ant-bms`. No CAN.
- Passive balancing 100 mA/channel, charging-only by default. At 52 Ah a 1 % drift takes days to correct —
  **top-balance the cells before assembly**, the BMS cannot do it for you.

### ANT settings as configured 2026-10-25 (pack built, BMS live; HW 30ZHB7TB220A, FW 30ADUB00-250102A)

Pack assembled in a sheet-aluminium box (not the printed enclosure), Anderson SB output, BMS on top under a
green insulating sheet. First connection: 30 cells at 3.208–3.215 V (≈8–10 % SOC), harness order confirmed by
cell sum = pack V. Factory state was **Ternary** profile, 50 Ah, no password — all corrected below. Parameter
names are as shown in the app (Settings → BMS, tabs Voltage / Temp&Hum / Current / Balance / Battery pack).
Save = "Save changes permanently", then Refresh to confirm the board took it.

| Tab / parameter | Factory (LFP one-click) | Set |
|-----------------|-------------------------|-----|
| **Shortcut**: Battery Type ("Iron phosphate" = LiFePO4; "LMFP" is a different chemistry) | Ternary | LiFePO4 |
| Number of Battery Cells / Battery Physical Capacity | 30S / 50 Ah | 30S / **52 Ah** |
| **Voltage**: Cell Overvoltage Protection / Recovery | 3.650 / 3.450 | unchanged |
| Secondary Overvoltage Protection / Recovery | 3.800 / 3.700 | unchanged |
| Cell Voltage Difference Protection / Recovery | 0.800 / 0.600 | **0.300 / 0.200** |
| Pack Overvoltage Protection / Recovery | 114.0 / 109.5 | **110.0 / 105.0** |
| Cell Undervoltage Protection / Recovery | 2.600 / 2.900 | **2.800 / 3.000** |
| Secondary Undervoltage Protection / Recovery | 1.900 / ? | **2.500 / 2.800** |
| Cell Undervoltage Warning / Recovery | 3.000 / 3.100 | **3.100 / 3.200** |
| Cell Voltage Difference Warning / Recovery | 0.600 / 0.400 | **0.150 / 0.100** |
| Pack Undervoltage Warning / Recovery | 1.0 / 1.0 (off) | unchanged (cell-level has priority) |
| **Temp&Hum**: High Temp Charge Protection / Recovery | 60 / 55 | **50 / 45** |
| High Temp Discharge Protection / Recovery | 60 / 55 | **55 / 50** |
| MOS High Temp Protection / Recovery, Warning / Recovery | 80 / 65, 70 / 67 | unchanged |
| Low Temp Charge Protection / Recovery | −2 / 2 | **0 / 5** (regen is charging — cold regen stops here) |
| Low Temp Discharge Protection / Recovery | −10 / −5 | unchanged |
| High Temp Charge Warning / Recovery | 55 / 53 | **45 / 42** |
| High Temp Discharge Warning / Recovery | 55 / 53 | **45 / 42** (hot-day validation pass criterion) |
| Low Temp Charge Warning / Recovery | 0 / 2 | **5 / 7** |
| Low Temp Discharge Warning / Recovery | −5 / −3 | unchanged |
| Humidity Alarm | 6553.5 % (= off, no sensor) | unchanged |
| **Current**: Charge Overcurrent Protection / Delay | 100 A / 5 s | **60 A** / 5 s |
| Discharge Overcurrent Protection / Delay | 400 A / 5 s | **120 A** / 5 s |
| Second-Level Discharge Overcurrent Protection / Delay | 500 A / 1000 ms | **200 A** / 1000 ms |
| Short Circuit Protection Current / Delay | 0 A / 1200 µs | try 300 A; if it reverts to 0 the threshold is hardware-fixed. Raise delay +200 µs if contactor close trips it |
| Charge Overcurrent Warning / Recovery | 80 / 70 | **50 / 45** |
| Discharge Overcurrent Warning / Recovery | 200 / 180 | **60 / 55** at the 52 A stage (diagnostic: a warning means the Sevcon limit is not enforcing); **85 / 75** at 78 A |
| SOC Level 1 / Level 2 Warning | 20 / 5 | unchanged |
| **Balance** (all factory values matched the plan) | | Limit 3.650, Current 180N (100 %), Control Start 3.400, Start Diff 0.020, End Diff 0.005, Balance Charging Current 10 A (balancing only when charge current < 10 A) |
| **Battery pack**: Remaining Capacity | 50 Ah (bogus 96–100 %) | **5 Ah** once at first power-up; full charge resets to 52 |
| 30 % / 20 % / 10 % / 0 % Single Cell Voltage | 3.260 / 3.170 / 3.100 / 3.000 | **3.284 / 3.253 / 3.210 / 2.950** (Gotion A.4; generic table overstated SOC at the knee) |
| 100 % … 40 % Single Cell Voltage | 3.50 / 3.43 / 3.38 / 3.35 / 3.32 / 3.31 / 3.30 | unchanged (flat region; high top points keep charge voltage from fooling the resync) |
| Automatic Shutdown Voltage / SOC Calibration Method / Connection Resistance 1–30 | 2.900 V / 3 / 0.0 mΩ | unchanged |
| **System**: level-5 password | none | set a 12-digit password; the BMS_ID string at the top of the screen is the recovery key — copy it first |
| TempsensorShield | 0 | app shows T1–T4 all plausible (22–24 °C) although the board was thought to have 2 NTCs — warm each probe to find the live channels; mask phantoms with 4 + 8 = 12 only if they ever read −40 |
| Sleep (NoCurautoSleepTime) | 1800 s | unchanged (Bluetooth only; power path stays closed) |
| Firmware | | do not update (bricks the board if interrupted, per the manual) |

Still to verify once: MOSFET vs relay (OffDisCHG → B−↔P− continuity), box-to-B+/B− isolation, app V/A vs DMM /
clamp (first charge showed charger 97.44 V / 8.00 A vs app 97.83 V / 8.90 A — one of them is off; calibrate on
System tab), NTC placement between cells. `DV/CV/DSV 12.9/12.5/0.0 V` on the home screen is undocumented
(probably gate-driver voltages).

**Charger:** AFU AF1200, 30S LiFePO4 version, Mode: Lithium, Vfull 109.5 V, CC 8 A (0.15C, below the 10 A
balance gate so balancing can run the whole top end). First charge 2026-10-25 from 8 %: ~5 h; charge only with
the Sevcon disconnected (Gen4 manual: isolate from charger).

**Balance status 2026-10-27:** after the first full charge, with the pack sitting on the bench, the passive
balancer brought the cell spread to **0.003 V** (End Diff is 0.005, so it will now idle until the spread
reaches Start Diff 0.020). Cell 13, the high cell at first connection, now sits with the rest; the "highest
cell" marker moved to cell 23 — at a 3 mV spread that marker is ADC noise (1 mV resolution), do not chase it.
Still to do: (1) disconnect the charger, rest 1–2 h, re-read the spread — under charge the highest reader is
the highest-resistance cell, not the most charged one; a rested spread ≤ 5 mV confirms the balance; (2) check
ANT shows SOC 100 % and Remaining Capacity 52 Ah after the full charge (coulomb-counter resync); (3) the real
capacity-match test is the bottom: on the first ride to ~20 % app SOC watch which cell sags first (3.1 V
warning). Do not leave the pack full on the bench for weeks — storage is 30–50 % SOC (halogen load below). Bench discharge load for storage (~50 %, 26 Ah out):
one 500 W / 120 V halogen T3 work light ≈ 3.5 A at 100 V DC, switched only via OnDisCHG/OffDisCHG in the app
(the lamp's own switch is AC-rated), 5 A fuse in the lead.

### Integration Notes
- BMS sits in main power path (MOSFET-based disconnect) — adds second disconnect alongside
  Sevcon contactor. Precharge circuit must bring bus up through BMS before contactor closes.
- 30S is the BMS maximum — no headroom for future cell count changes without replacing the BMS.
- Wire BMS B− to pack negative; BMS P− to system negative (Sevcon B−, contactor return).
- Verify BMS charge/discharge port separation (some ANT models have separate C− and P− ports).
- The MOSFET bank dissipates a few watts at 78 A and the board cuts at 80 °C MOS temperature: the box needs
  an air path or a heat spreader for it (VENTS is still empty in the enclosure model).
- **No BMS→Sevcon bridge** (owner 2026-10-21). Graceful behaviour comes from Sevcon voltage cutbacks + ANT
  thresholds set outside the Sevcon envelope.

---

## Drivetrain / Gearing

### Stock Configuration
- Drive type: belt drive
- Overall gear ratio: ~8.9:1 (verify exact figures in OM-FX-MY14.pdf on Desktop)
- Stock front (drive) pulley: verify tooth count in service manual

### Gearing Decision — keep stock (2026-10-20)

An earlier note recommended a 22T front pulley. Withdrawn: with the pack limited by battery
power (52 A ≈ 5 kW), gearing does not change acceleration in the range that matters.

**Why stock gearing is fine on a power-limited pack:**
- Launch torque (0–~10 km/h) is set by Sevcon *motor phase* current, not battery current — the
  controller steps 52 A battery into hundreds of phase amps at low speed. Owner confirmed: stock
  gearing + 52 A limit on the original pack already gives wheelie-capable launches.
- From ~10 km/h up, thrust = P / v regardless of ratio. A shorter ratio adds nothing here.
- Top speed is capped by power (~75–80 km/h), far below the motor RPM limit (137 km/h stock,
  ~125 km/h with 22T) — overspeed is a non-issue either way, so no RPM reason to re-gear.
- Thermal/efficiency effect of 22T is a few percent at most; not worth a new pulley and belt.

**Use software instead of hardware:**
- Tame launch / wheelie: max torque and acceleration ramp in baseline profile 2920h; progressive
  throttle curve in 2910h.
- Speed cap / eco mode: max speed in 2920h (scaled via 2915h), or a switched profile 2921h.

**Revisit only if:** the pack grows to ~15–20 kW (2p/3p or higher-C cells) and the motor starts
hitting its RPM limit at a speed actually reached, or the bike becomes a dedicated low-speed
off-road crawler. Then recalculate ratio from desired top speed and motor RPM limit.

---

## Battery Box Enclosure

Spec: `battery_box/SPEC.md` — build brief for a parametric, 3D-printable (build123d) two-zone
enclosure for the 30s1p pack. Read the spec in full before touching enclosure code; this section
is only a summary and a list of known issues.

**Key inputs (from spec):**
- Pack envelope: 444.5 × 279.4 × 152.4 mm (17.5 × 11 × 6 in), lying on its widest face
- Chassis bay: 457.2 × 254.0 × 177.8 mm (18 × 10 × 7 in) — bounds the narrow upper zone
- Lower zone intentionally overhangs the bay in depth (~18.7 mm per side incl. wall) as crash zone
- Upper zone (outer depth 254 mm) carries frame mounts, ANT BMS, and a 100 A Class T fuse block
- Walls: 5.0 mm long walls / floor, 4.0 mm elsewhere; CLEARANCE 1.0 mm; 45° shoulder, no supports
- Printer: Bambu Lab P2S, max part 240 × 240 × 240 mm; outer face on bed; flush exterior
- Fasteners: M3/M4 heat-set inserts, removable floor tiles and top service cover
- Placeholders still TODO/MEASURE_ME: BMS size + hole pattern, fuse block size + holes,
  MOUNT_POINTS, TERMINAL_CUTOUTS, VENTS, CABLE_ZONE position

**Cell dimensions — CORRECTED 2026-10-21 from `manuals/ifp52.pdf`:** 148 × 28.2 × 118.6 mm (W × T × H incl.
terminals), 966 g. The 148 × 26 × 129 mm used by SPEC.md and `enclosure.py` came from a marketplace listing
and are wrong. Layout stays **2 rows × 15, cells on their side, bottom-to-bottom, terminals to the long walls**,
but the proportions change:
- Length: 15 × 28.2 = 423 mm + two end plates + 14 cell gaps. Bay 457.2 − 2 × 5 wall − 2 × 1 clearance = 445.2 mm
  → only **~22 mm for both end plates and all gaps**. Works with ≤6 mm plates and factory film only (no
  inter-cell sheets); otherwise the box must grow in length.
- Depth: 2 × 118.6 = 237 mm + ~5 mm centre plate = 242 → + 2 × 5 walls + 2 × 1 clearance = **254 mm = bay width**.
  The crash-zone overhang and the 45° shoulder are no longer needed; a straight box inside the bay works.
- Height: 148 mm + 4.4 → unchanged; 4 mm more headroom than the old 152.4 figure.
- Cells 29 kg; expect ~32 kg pack.

**Do not print anything until SPEC.md and `enclosure.py` are re-derived from these dimensions.** Owner to
confirm cell height with calipers first (118.6 vs 129 mm is unmistakable).

Enclosure consequences of this orientation:
- Terminals and busbars sit on the two long faces, 1 mm from the 5 mm crash walls, and those
  faces are exactly where the shell overhangs the bay. Insulation between busbars and wall is
  mandatory (pack-side cover or a printed liner); do not rely on the 1 mm air gap.
- Main leads and the balance harness leave the pack sideways, then route up the long walls to
  the top-front CABLE_ZONE. Leave a wire channel along the shoulder for them.
- Terminal faces must stay accessible: pack removal is via the floor, so the long walls need no
  service opening, but the compression plates must not be bolted through the shell.

**Height budget (clarified):** the 7 in / 177.8 mm bay figure is the **inner cavity** height
(pack 6 in + 1 in upper section) and does **not** include the box floor and roof. So:
- Outer box height = 177.8 + floor 5.0 + roof 4.0 = **186.8 mm**; floor and roof sit outside the
  7 in frame window. Spec line "Outer height <= 177.8 mm (MAX_OUTER_HEIGHT)" is wrong as written —
  change it to MAX_INNER_HEIGHT = 177.8 (or MAX_OUTER_HEIGHT = 186.8) before scripting, otherwise
  the script will fail its own height check.
- Free height above pack = 25.4 − 1.0 clearance = **24.4 mm**
- BMS 12.7 + 3 standoff = 15.7 mm → **fits**, 8.7 mm spare
- Fuse block placeholder 50 + 3 = 53 mm → does **not** fit on paper. Confirmed to fit on the bike,
  so the 50 mm placeholder is far too tall — **measure the real block** (with cover) and set
  FUSE_BLOCK height. If it is > ~21 mm it only fits via FUSE_POCKET (roof bump above the frame
  window), which is exactly what that option is for.
- The 45° shoulder (291.4 → 254 mm outer depth) uses 18.7 mm of the 25.4 mm upper section, so the
  straight 254 mm-wide narrow section is only ~6.7 mm tall plus the 4 mm roof. Frame mounts
  (MOUNT_POINTS, TODO) will have to land on the shoulder or the roof edge, not on a tall flat wall.

**Other review notes:**
- Not in the spec: contactor GX11-013, 100 Ω precharge resistor, main B+/B− terminals, charge
  port. Decide whether they live in this box (TERMINAL_CUTOUTS) or with the Sevcon.
- ANT BMS 220A is a MOSFET disconnect with a heatsink; a sealed printed box with VENTS = []
  gives it no heat path. Size vents or a heat spreader once the BMS is measured.
- Floor tiles carry the full ~32 kg pack plus crash loads through heat-set inserts in printed
  wall edges; the whole mass hangs from upper-zone mounts. Treat floor-to-wall joints and
  mount bosses as the primary structural check, not the walls.
- Cable zone (80 × 120 mm) must pass the 31-wire balance harness plus main leads and BMS
  B−/P− split — check the area is enough before fixing CABLE_ZONE defaults.
- 100 A / 150 VDC Class T fuse is consistent with the ≤52 A Sevcon limit and 109.5 V max pack.

**Model status (built 2026-10-14):** `battery_box/enclosure.py` generates the full enclosure;
`battery_box/README.md` is the authoritative description (parts, deviations, print and
assembly order, MEASURE_ME list). Run it from the project venv (build123d 0.13 installed):

```
cd battery_box && ../.venv/bin/python enclosure.py
```

- 16 printed pieces (10 unique), all within 240 x 240 x 240; outputs in `battery_box/output/`,
  plus `assembly.step` (ghost pack/BMS/fuse coloured) and `test_coupons.stl`
- Every spec assertion passes: length fit, no pack intrusion, 1 mm clearance, no part overlaps
- `VARIANT = "spec"` (default, owner's choice 2026-10-14): wall thicknesses exactly per SPEC.md
  (5/4/4/5/4). `VARIANT = "thick"` keeps the heavier 8/4/6/12/6 set. The report warns that with
  spec thicknesses the wall-bottom M3 inserts have 0.5 mm of plastic per side and tile-to-tile
  screws cannot exist (plain half-laps instead)
- Design choices: BMS/fuse hang from the service cover; cover split into main + strip with a lap;
  several joints are tongue-and-groove without screws (see README)
- Still open: fuse block height (placeholder 50 mm does not fit, FUSE_POCKET option exists),
  MOUNT_POINTS (frame mounts not modelled, do not invent), VENTS, TERMINAL_CUTOUTS
- Renders for a quick look: `battery_box/renders/spec/` and `renders/thick/`

---

## Unofficial Zero Manual (zeromanual.com) — offline mirror

`zeromanual/` holds a Markdown mirror of the community wiki zeromanual.com, recovered from the
Wayback Machine (site is offline; archive may vanish). Scope: Main Page + every page it links
directly (45 pages) + all their images. The key document is
`zeromanual/wiki/Unofficial_Service_Manual.md` (full Gen2 service manual, ~7.5k lines, with
pictures) and `zeromanual/wiki/XMX_Platform/Unofficial_Service_Manual.md` (FX-specific).

**How to use it:** start at `zeromanual/INDEX.md` (all pages with one-line summaries), then grep
`zeromanual/wiki/`. Every page has front matter with the original URL and the exact Wayback capture;
cite those when quoting. Content describes *stock* bikes (MBB/CCU/Zero BMS present) — mechanical,
Sevcon, motor, belt, brake and harness facts transfer to OpenZero; MBB/app/dash behaviour does not.
Links to wiki pages outside the mirror point at `web.archive.org`. Regeneration steps and known gaps
are in `zeromanual/README.md`.

## Files on Desktop

- `GEN4-Product-Manual-V3-3.pdf` — Sevcon Gen4 manual (superseded by V3.4 in `manuals/`)
- `OM-FX-MY14.pdf` — Zero FX 2014 owner's manual (gear ratio, mechanical specs)
- `Gotion 3.2V 52AH...pdf` — printed AliExpress listing, NOT a datasheet; superseded by `manuals/ifp52.pdf`

## Public repository and website (2026-11-01)

The repo is public on GitHub; the site openzero.u65.info is built from `site/` by `.github/workflows/pages.yml`
(landing page + odometer + MkDocs version of `zeromanual/wiki`). Rules that follow from that:
- `manuals/` and `tmp/` are git-ignored (copyrighted PDFs / scratch photos). Cite manuals by name as before;
  README "Documents you need" lists them for other people.
- Licences: GPL-3.0-or-later for code, CC BY-SA 4.0 for text/models, zeromanual content attributed, no licence claimed.
- Odometer: `site/landing/odometer.json` (`miles`, `updated`); the landing page reads it on load.
- Manual pages are generated by `site/manual/build_manual.py` (splits manuals per H2, rewrites anchors); do not
  hand-edit `site/manual/docs/` or `site/manual/mkdocs.yml`, edit `zeromanual/wiki/` or `mkdocs.base.yml`.

## Files in Repo

- `manuals/` — component documents (the only valid spec sources):
  - `ifp52.pdf` — Gotion IFP28148115A-52Ah cell spec Q/GX 030-2019 (dimensions, pulse tables, SOC-OCV, BMS thresholds)
  - `Gen4 Product Manual V3 4.pdf` — Sevcon Gen4 manual, primary reference. New vs V3.3: charger-isolation
    warning (isolate Gen4 from the charger when powered); Size 4 pin 10 became a 5 V/100 mA output in 2014
    (part 634A44103 vs 634A44101 — check the label); BDI disable note (2C30h sub 6 = 0)
  - `ANT-BMS-APP-User-Manual-English.pdf` — ANT app manual (parameter pages, permissions, firmware warning)
  - `Ant BMS Smart Bluetooth Relay ... User Manual.pdf` — manuals.plus compilation for the ANT relay line;
    wiring/figures only partly apply to the MOSFET 30ZHB7
  - `CT-22-MANUAL.pdf` — CT-22 gauge button/parameter instructions (no pinout)
- `battery_box/SPEC.md` — battery box enclosure build spec (build123d, Bambu P2S)
- `battery_box/enclosure.py` — parametric build123d model; `battery_box/README.md` — parts, deviations,
  print/assembly instructions, MEASURE_ME list; `battery_box/output/` — STLs in print orientation
