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
- **12 V system is stock and fully working** (owner 2026-11-03): the OEM DC-DC converter Sevcon 622-11202
  (Zero 60-04015) is on the bike and feeds lights and instruments. The 12 V rail for the speed converter,
  CT-22 (if it accepts 12 V) and any 12 V accessory already exists — no new DC-DC to buy or wire
- **Bike rides on the 30S LFP pack** (first spontaneous test rides, by 2026-11-02): ~20 km solo and two-up
  (one ~10 km ride with a passenger), ANT SOC 100 → 78 %. ≈ 1.1 kWh / 20 km ≈ 55 Wh/km, matching the stock
  "mixed" figure (57 Wh/km) — the ANT coulomb counter looks honest and the ~75 km mixed-range estimate holds.
  Pack left on the bike at 78 % for a week (2026-11-02 → 11-09): fine for LFP; note SOC/pack V before and
  after to get the first BMS standby-drain figure.
- **First GPS-logged rides (2026-11-08, `rides/log.md`):** 5.65 km loop, **88–90 km/h (55 mph) GPS max** on a
  ~2 % descent, 75–86 km/h held on the flat at full throttle. ANT log matched to the second: full throttle =
  **78–82 A battery current, 90 A peaks** (ANT reads ~10 % high vs the charger, so ~72–80 A real) ≈ 7.5 kW — the
  bike is riding the "78 A stage" because the 52 A limit was never written (see Blocking). The 85–90 km/h stretch
  on the descent produced no 60 A warning, i.e. needs < 60 A there. No temperature events, no protection trips.
- **First real commute (2026-11-10, `rides/log.md`):** home → "LT" and back, 5.72 + 5.84 km, 7.2 + 7.4 min moving,
  48 km/h average moving, 81–87 km/h GPS max. ANT: 81–87 A sustained at 70–80 km/h on climb, flat and a −1.3 %
  descent alike, peaks 90.6 / 87.4 A; cell 16 down to 3.038 V (morning loop) / 3.046 V at 85.7 A, spread 0.088 V.
  Four rides that day plus a 1-hour 8.8 A top-up at 13:08 (≈ +17 % SOC). No trips, no temperature events. The ANT
  run-time counter runs ~0.4 % fast and the log is a 200-event ring buffer: export right after each ride.
- **Regen is weak since the 40 A limit was written (owner 2026-11-12):** the owner recalls writing the 40 A regen
  limit into the controller (4623h sub 03h) and that coast/neutral-braking drag became much weaker afterwards; every
  descent is on the friction brakes, and ANT saw ≈ 9 A of regen at most on Park Ave. Gen4 manual (Battery Current
  Limit): *"regen currents flowing back to the battery are specified as negative numbers"* — a **+40** in sub 03h
  is the likely cause (wrong sign → near-zero regen allowance), and the same text says sub 03h also carries a
  cutback-aggressiveness / correction factor in some firmware layouts. It also means 2870h sub 01h is probably 0x01
  already, so whatever sits in sub 02h is what caps discharge at ~81 A. **In DVT: read 4623h all sub-indices and
  2870h, log 5100h on a descent, then write sub 03h = −40 (and sub 02h per step 7a).**
- **Top of the World (2026-11-11, `rides/log.md`):** 18.2 km out via PCH and Laguna Beach, same way back. **Park Ave
  is a full-throttle climb:** 2.44 km, +237 m, 9.7 % average with 12–18 % sections, ANT 78–91 A for ~3 min, 64 km/h at
  the bottom falling to 31–45 km/h on the steep part and 17 km/h at the top. New ANT peak 97.1 A (≈ 88 A real) on the
  way back. Regen on the descent peaked at ≈ 9 A (weak neutral braking, no paddle). No trips, no temperature events.

### Blocking / In Progress
- **Rear brake rotor runout — FIXED 2026-11-09, CONFIRMED ON THE ROAD 2026-11-10 (Honda 43351-MBN-671).** First ride
  on the Honda disc: pads bedded in, no pulsing at the pedal, no problems. The pad leaves a clean, even track centred on
  the swept face and never runs off the edge — owner: it fits as if it belonged there from the factory, arguably better
  than OEM. Before the swap the runout was genuinely dangerous: the pedal kicked, the rear wheel alternately locked and
  released, and the rear brake had to be avoided almost entirely. **Second identical disc bought for the front
  (2026-11-10)** — front hub is M6 (90-03477-8), so it should bolt on without drilling; do the front checks listed
  below. Still to do on the rear: re-check the 4 rotor bolts after this first ride, note the MIN TH stamp.
  The disc was the problem, not the hub. Honda holes are M6 (~6.5 mm) and the FX
  rear hub is M8 (catalogue: rear rotor bolts 90-07274 = ISO 7380 button head M8×25 8.8, qty 4; front 90-03477-8 =
  M6×15, the line with the bogus qty 6 — so the Honda disc may bolt straight onto the front hub, check with a bolt), so
  the four holes were opened to 8.5 mm with a hand drill in 0.5 mm steps, using the old Zero disc stacked and clamped
  on top as a drill bushing (same PCD, holes already 8.5), then chamfered 0.3–0.5 mm by hand. Torque for these bolts:
  ~20 N·m (8.8) / 23–25 N·m (10.9) with medium threadlocker, never above 25 in the aluminium hub; no Zero figure exists
  in OM-FX-MY14 or the zeromanual. Before the first ride: pump the pedal (disc 0.5 mm thinner, pistons must come out),
  bed the pads gently for 10–15 km, re-check the bolts after the ride, note the MIN TH stamp on the Honda disc.
  **Rotors (owner 2026-11-09):** front and rear FX hubs take the same disc interface — 4 bolts, same PCD, 240 mm, same
  design (the catalogue lists different numbers, front 25-06282 → 25-08063, rear 25-07621 "with counterbore", and a
  "qty 6" front bolt line that is a catalogue error — its own drawing shows 4 holes). **Replacement: Honda
  43351-MBN-671** (XR650R 2000–07 rear disc, 240 × 4 mm, 4 holes) trial-fits the FX hub, apparently front or rear.
  Rear checks done on the road 2026-11-10 (centred in the caliper, pads on the swept band, no runout felt); still worth a
  dial-gauge reading once for the record. Buchanan's email corrected to 4 bolts.
  OM-FX-MY14 p. 1.7 gives **both** rotors as 240 mm × 4.5 mm, wear limit 3.85 mm; the Honda disc is 4.0 mm new, so it
  starts 0.5 mm thinner than stock on either axle — go by the min-thickness stamp on the Honda disc, not Zero's 3.85.
  Front fitment (owner question 2026-11-09, disc bought 2026-11-10): acceptable once PCD is confirmed — same OD, 4-bolt,
  flat, non-directional OE stainless disc, same checks as the rear plus: front pads fully on the swept band, heads clear
  the fork-side caliper carrier, bed in gently. Use the stock M6×15 front bolts (90-03477-8) if the Honda hole is a plain
  6.5 mm through-hole with no countersink; the Honda disc expects M6 × 17, so check thread engagement in the hub.
  **Front bolts seized (owner 2026-11-13):** the rear recipe (40 s torch, then impact) strips the 5 mm hex on the
  M6 front bolts instead of turning them. Next steps in order: hammered-in Torx T30/T27 + hammer-type impact driver
  (axial force, no electric impact); Dremel slot + flat bit; MIG a nut on (heat goes into the bolt); drill the head
  off with a 6.5–7 mm bit and spin the unloaded stub out with pliers after heat. Then tap M6, new bolts, medium
  threadlocker, **~10 N·m for M6 in the aluminium hub** (the 20 N·m figure is for the rear M8).
  **Solved the same day:** hammered-in Torx and the hammer-type impact driver did nothing (bit spun in the socket);
  **Dremel slot across the head + wide flat bit + electric impact right after a 30–40 s torch** turned every bolt at
  the first try. For any seized small-hex bolt on this bike go straight to the slot, skip Torx and the hammer driver.
- **Sevcon battery current limit NOT enforcing (found 2026-11-08 from the ANT log):** every ride since 2026-10-31 ran
  78–82 A at full throttle (peaks 83.5 / 89 / 90 A on 10-31 / 11-01 / 11-08); the ANT 60 A discharge warning fired
  exactly as the diagnostic it was set up to be. The cap is suspiciously flat (80–82 A from 22 to 75 km/h), so some
  battery limit is already in 4623h — read it. Step 7a moves to the front of the queue: either write 52 A as planned
  or consciously keep ~78 A and do the hot-day validation. Until then: no full throttle below 20 % SOC or in the
  cold — cell 16 under 80 A sits 0.2 V below rest, the ANT cut is 2.80 V.
- **"Cell 16 sags" is the mid-pack jumper, not the cell (owner 2026-11-08):** 23 of 27 cell-UV warnings (3.10 V
  threshold) are cell 16, at 3.06–3.10 V under 78–82 A, 55–68 mV below the rest. Cell 16 is the first cell of the
  left row and joins cell 15 through the 2 × AWG8 jumper with the connector that splits the pack into two 48 V
  halves for service. Tap 15 sits on the cell-15 side, so the jumper's I·R drop is subtracted from cell 16's
  reading on discharge (added on charge). 55–68 mV / 78–82 A = **0.7–0.85 mΩ**, exactly 30–40 cm of doubled
  AWG8 (~1 mΩ/m) plus a connector and four crimps. The two cell-1 warnings are the same effect on the B− lead.
  Verify: rested cell 16 = the rest ±3 mV; at 8 A charge it reads ~6 mV *high*. **Charge side confirmed 2026-11-10:**
  at −8.7 A (BatChgOn event) cell 16 was the *highest* cell, 3.329 V vs 3.321 V min = +8 mV ≈ 0.9 mΩ; at 0 A after
  the charge the spread was 6 mV. Fix: ANT **Connection Resistance**
  (Battery pack tab, currently 0.0 mΩ for all) → ~0.8–0.9 mΩ for cell 16, and cell 1 by its own under-load delta; confirm
  on the next ride that CellVoltDiff at 80 A drops from 0.06 to ~0.01 V (that also checks the sign convention).
  Until then ANT cuts cell 16 ~65 mV early under load — conservative, acceptable. The jumper dissipates ~5 W at
  80 A: connector must be rated 80 A continuous; touch-check after rides. Balancing is unaffected (6 mV at 8 A,
  2 mV in the CV tail, Start Diff is 20 mV).
- **Pack is not top-balanced — cell 13 trips over-voltage protection on every full charge (found 2026-11-12 in the
  ANT log):** the 11-10 overnight charge (8.8 A, 166 min) ended by CellOVPP on cell 13 at 3.652 V with a 0.221 V
  spread (min cell 25 at 3.431 V); the first charge on 10-25/26 ended the same way on the same cell (0.224 V). The
  "0.003 V spread" of 10-27 was read after relaxation into the flat OCV region and was never a top balance. Cell 13 is
  ≈ 0.5–1 Ah ahead of the pack (or that much smaller). ANT balances only above 3.40 V, which the pack reaches ~15 min
  before the trip → ~40 mAh/night, 15–25 nights to converge on its own, each night ending in a protection trip at
  ≈ 98 % instead of the charger's taper (coulomb-counter resync doubtful). **Fix, cheapest first:** (1) at the next
  charge, screenshot all 30 cells when the spread warning fires and confirm the balancer icon is active on cell 13;
  (2) bleed cell 13 manually: ~3.3 Ω / 5 W resistor across its terminals ≈ 1 A, 30–60 min at a time, recharge, repeat
  until the spread at > 3.6 V is < 30 mV — then the ANT 100 mA balancer can hold it; (3) only if (2) is not wanted:
  leave the charger connected overnight so trip → recover → restart cycles keep bleeding (check first that the AF1200
  restarts after the ANT charge-MOS reopens — through the diode port it will not). Also check the cell-13 balance
  lead and tap bolt: a high reading that appears only under current would be contact resistance, but 0.094 V at 0 A
  ten minutes after the trip says the imbalance is real.
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
5a. **Regen paddle** (owner 2026-11-05, near-term): momentary button on the bar to B− → footbrake switch
    object **2130h** mapped to a free DI, proposed **DI5 = pin 20** (wire already removed; pin 30/DI2 kept for a
    future reverse switch). Gen4 manual 6-22: a mapped footbrake switch applies *maximum foot braking* while
    closed; released = normal neutral braking (coast). Set in DVT: 2920h footbraking torque 20–30 % + ramp
    (neutral braking torque stays low, 5–10 %); 2911h min speed for braking ~2–3 km/h, drive/brake priority =
    brake, priority timeout; 290Eh brake feathering to 0 at stop. Regen stays capped by 4623h sub 03h (40 A).
    Bonus: brake-light object 2404h on a free low-side output (pin 7 or 11) lights on footbrake → regen stop
    lamp without the ESP32. **Before touching the connector:** confirm the DI number with the DVT raw-input tree
    (short pin 20 to B−), and resolve the pinout discrepancy noted under "Sevcon 35-Pin Connector". Step two if
    liked: a 0–5 V hall lever on Pot 2 (pin 23 wiper / 35 supply, object 2221h) for proportional regen.
6. **Save all parameters to NVM** (1010h sub 01h = 0x65766173)
7. **Wire and commission ANT BMS** — DONE 2026-10-25: pack built in an aluminium box, BMS live, all 30 cells
   read correctly, protections set (see "ANT settings as configured"), first full charge done and pack
   top-balanced to 3 mV (2026-10-27). Left: rested-spread check, SOC/52 Ah resync check, password, MOSFET toggle
   test, box isolation check, V/A calibration vs DMM, NTC channel check, fuse location, box edge trim
7a. **Set Sevcon battery current limit** in DVT (2870h sub 01h = 0x01; 4623h sub 02h = discharge, sub 03h =
    charge/regen). BMS does not enforce cell C-rate; the limit is static (no peak timer). **NOW FIRST IN LINE
    (2026-11-08): the limit was never written and rides run at ~80 A** — read 4623h/2870h first to learn what caps
    at ~81 A today, then decide 52 A per plan vs. staying at 78 A with the validation below. **Plan (owner 2026-10-21):**
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
7b. **Test with 96V LiFePO4 battery pack** — DONE by 2026-11-02 (see "Working": ~20 km incl. passenger,
    22 % used, ~55 Wh/km). ANT log pulled 2026-11-08 (`rides/log.md`): max 89 A on 11-01, cell 16 to 3.059 V
    under load, no temperature events, no trips. Distance: GPS tracks from 2026-11-08 on (Open GPX Tracker, location
    permission "Always" or the track has gaps); odometer once the speed converter exists
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

**Pinout discrepancy to resolve (2026-11-05, Gen4 manual V3.4 Table 2 vs this table):** the manual lists pin 15 =
encoder supply − (0 V), 14/25 = encoder A/B, 26 = encoder supply +, 28 = CAN power +, 32 = DI7, 33 = motor
thermistor, 30 = DI2 (reverse), 20 = DI5, 9 = DI6, 21 = DI8. This table says 15 = brake/regen input, 26/28 =
encoder A/B, 32/33 = encoder supply/GND. Either the Zero loom labels differ or the rows above are wrong. Check
with the DVT raw-input tree and the manual before adding the regen-paddle wire (step 5a) or removing anything.
**Resolved on paper (2026-11-09) by the 2016 FX wiring diagram rev 1.1 (`zeromanual/images/2016_FX_Wiring_1-1-preview.png`,
Sevcon block): 1 = ORN/RED, 2 = CAN TERMINATE (jumpered to 24 = CAN LOW SERVICE — that jumper is the Sevcon's
internal 120 Ω terminator, not a B− reference), 6 = KEY SWITCH, 15 = 0 V, 16 = CAN HIGH, 18 = FORWARD, 21 = SIN
input, 22 = THROTTLE, 23 = ANALOG INPUT 2, 26 = +10 V, 27 = CAN LOW, 28 = CAN POWER, 30 = DIGITAL IN 2, 33 = MOTOR
THERMISTOR, 35 = COS input.** So the FX motor runs a sin/cos encoder on 21/35 with 26 = supply and 15 = 0 V; the
table rows "15 brake/regen", "26/28 encoder A/B", "32/33 encoder supply/GND" are wrong — the wires are right (the
bike runs), the labels are not. Pin 15 is the analogue/encoder ground: never use it for the regen paddle. Confirm
on the bike with the raw-input tree before editing the table.

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
| 2130h | Footbrake switch (regen paddle) | Map to DI5 (pin 20); closed = max footbraking per 2920h, open = neutral braking (step 5a) |
| 2911h | Footbrake characteristics | min speed for braking, drive/brake priority + timeout (step 5a) |
| 290Eh | Brake feathering | neutral/foot braking torque → 0 near standstill, no roll-back |
| 2404h | Brake-light output | map to a free low-side output; on during footbrake and direction-change braking |
| 2221h | Footbrake analogue voltage | Pot 2 (pins 35/23) for a proportional regen lever, later |
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
| 5000h sub 01h/02h/03h | Access level / password / user ID | Login without DVT: write password to sub 02h, user ID to sub 03h, read level from sub 01h (need ≥ 4; checked against OEM key 5001h). The DVT sends it in clear on CAN: capture once |
| 2800h | Request pre-operational | 1 = pre-op (needed for PDO COB-IDs and other protected objects), 0 = operational. Refused while driving |
| 5110h | NMT state readout | 05 = operational, 7F = pre-operational |
| 5610h | Fault text | write fault ID to sub 01h, read description from sub 02h |

All of the above is plain CANopen SDO: any CAN adapter on any OS (or the speed-converter ESP32 over Wi-Fi) replaces
IXXAT + DVT + Windows for configuration; only firmware upload and the motor wizards stay DVT-only. Sequence and
caveats in `ideas/README.md` ("ESP32 bridge: web interface to Sevcon settings").

---

## Contactor — GX11-013 (120V DC coil)

- Pull-in duty: 100% (full bus voltage ~96V, sufficient for 120V rated coil)
- Hold duty: 25–30% (~24–29V at 96V bus)
- Pull-in time: 50ms
- **Precharge**: external 100Ω resistor in parallel with main contactor required
- Precharge threshold in DVT: 5820h = 90 % of battery voltage (object is a percentage, 50–90 %); 5821h = minimum capacitor voltage for the contactor to close
- Stock part (`manuals/14fx.pdf` ZEV0010 #16): Gigavac "contactor 12/40 VDC modular", Zero 45-08091 (superseded by
  45-08135) — a low-voltage coil driven by the Zero BMS. The Sevcon pin 3/4 output switches bus voltage, hence the
  120 V-coil GX11-013 instead

---

## Speed Converter (decided 2026-10-21: build it; wheel Hall sensor rejected as non-OEM + extra wire)

Reads motor RPM from Sevcon CAN TPDO → outputs Hall-sensor-style pulse signal to the CT-22 gauge.

**Hardware (ordered 2026-11-01, Adafruit):** ESP32 Feather V2 with headers (PID 5900), CAN Pal TJA1051T/3
transceiver (PID 5708, 3.3 V logic, on-board 120 Ω termination switch), MPM3610 buck 6–21 V → 5 V (PID 4739,
feeds the Feather's USB/VBUS pin from the existing 12 V rail), PN2222 + 1 kΩ as open-collector output to the
CT-22 speed input, breadboard + jumpers for the first build. Rationale over Uno + MCP2515: built-in CAN
controller (TWAI), spare hardware UARTs, LEDC timer for the pulse output, Wi-Fi/BLE for logging/OTA. Leave a
4-pin UART header free for the optional BMS bridge below.
**Power rules:** Sevcon pins cannot feed the board — pin 34/35 are 10 V / 15 mA (pot supply, monitored → throttle
fault if loaded), pin 10 is 5 V / 100 mA only on 634A44103 Size 4. Use the stock 12 V rail (Sevcon 622-11202 DC-DC, working,
feeds lights and instruments) → buck → 5 V, switched by key, fused; ESP32 GND = Sevcon B−. CT-22 speed input only via optocoupler until the bench test shows its
ground is B−. CAN mode must be normal (not listen-only): with DVT unplugged the ESP32 is the only node that ACKs.
**Firmware plan:** stage 1 blink + 420 Hz LEDC; stage 2 TWAI receive + SDO poll of 606Ch at 10 Hz printed to
serial (TPDO mapping in 1800h/1A00h later); stage 3 RPM → Hz → output with 500 ms timeout, |RPM| only, off
below ~2 km/h; then 12 V power, log 5100h/temps/EMCY, regen brake light, odometer in NVS, OTA, NMT start.

**Key parameters:**
- Sevcon TPDO1 ID: 0x180 + node ID (check node ID in DVT)
- Velocity object: 606Ch (actual velocity, 4 bytes, signed int32, RPM)
- Gear ratio: **5.28:1** (132T/25T belt, OM-FX-MY14 p. 1.7 and parts catalogue `manuals/14fx.pdf` ZEV0009; the
  earlier ~8.9 figure was wrong). **Rear tyre on the bike: 120/80-18 on a 2.15 × 18 rim** (owner, read off the
  wheel 2026-11-08; the catalogue tyre is IRC GP-110 4.10-18, Ø ≈ 665 mm, and the 14MY kit rim is listed as 2.50 —
  this bike has 2.15). Ø = 457.2 + 2 × 96 = **649 mm**, circumference ≈ 2.04 m → **km/h ≈ motor RPM × 0.0232**; with
  the CT-22 default 7.0 Hz per km/h: **f_out ≈ RPM × 0.162 Hz** (60 km/h = 2590 RPM = 420 Hz). Calibrate against GPS
- CAN baud: match Sevcon setting (configure 5900h first)
- Output pin: D9 (timer-driven square wave, NPN open-collector to speedometer)

**No additional Sevcon pins needed** — speed converter taps existing CAN bus wires (pins 16/27).

### CT-22 gauge (`manuals/CT-22-MANUAL.pdf`, board CY1874D_MB110D)
- Speed input: pulse. Parameter `0-0420` = 420 Hz ↔ 60 km/h (range 0–999 Hz) → converter outputs
  **7.0 Hz per km/h**; keep the default and calibrate against GPS. Password 6610 enters the parameter menu.
- Supply/pinout not documented. Factory battery thresholds are 125–152 V, so the board is built for ~144 V
  scooters and most likely sits directly on the traction bus and measures its own supply (= HV wire to the
  handlebar). Bench-test before wiring: current-limited PSU, ramp from 10 V, note turn-on voltage and draw;
  check for a separate sense wire. The bike's stock 12 V rail (Sevcon 622-11202 DC-DC) is working and available.
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

**App will not connect after the pack sat idle (2026-11-08, after a week at 78 %):** the BMS shows in the app's
device list, "connecting" runs, then the app drops back to the list with no error. Phone reboot did not help. What
did: force-quit the ANT app, Bluetooth off/on in the phone settings, reopen the app and scan afresh — connected
at once. Most likely two things stacked: the board was asleep (NoCurautoSleepTime 1800 s; wakes on charge or
discharge current, e.g. key on / charger) and the phone held a stale BLE state. Recipe in order: key on or charger
in for 10–20 s → quit app → BT off/on → fresh scan. Only then consider reseating the Bluetooth module or pulling the
balance harness for 30 s (the ANT power cycle). Both manuals in `manuals/` say nothing about wake-up.

**Charger:** AFU AF1200, 30S LiFePO4 version, Mode: Lithium, Vfull 109.5 V, CC 8 A (0.15C, below the 10 A
balance gate so balancing can run the whole top end). First charge 2026-10-25 from 8 %: ~5 h; charge only with
the Sevcon disconnected (Gen4 manual: isolate from charger).

**Balance status 2026-10-27 — superseded 2026-11-12, see Blocking "Pack is not top-balanced":** after the first full
charge, with the pack sitting on the bench, the app showed a cell spread of **0.003 V** — but that was read after the
cells had relaxed into the flat OCV region (≈ 3.33–3.37 V), where 3 mV carries no SOC information; at the top of the
next full charge (11-10) the spread was 0.221 V and cell 13 tripped OV protection again, exactly as on 10-25/26. Cell 13, the high cell at first connection, now sits with the rest; the "highest
cell" marker moved to cell 23 — at a 3 mV spread that marker is ADC noise (1 mV resolution), do not chase it.
Still to do: (1) disconnect the charger, rest 1–2 h, re-read the spread — under charge the highest reader is
the highest-resistance cell, not the most charged one; a rested spread ≤ 5 mV confirms the balance; (2) check
ANT shows SOC 100 % and Remaining Capacity 52 Ah after the full charge (coulomb-counter resync); (3) the real
capacity-match test is the bottom: on the first ride to ~20 % app SOC watch which cell sags first (3.1 V
warning) — **2026-11-08: cell 16 reads lowest under load, but that is the mid-pack jumper's I·R, not the cell**
(see Blocking); after the Connection Resistance fix the question is open again. Do not leave the pack full on the bench for weeks — storage is 30–50 % SOC (halogen load below). Bench discharge load for storage (~50 %, 26 Ah out):
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

## Charging (researched 2026-11-02; details and BOM in `charging/road_kit.md`)

**Daily regime (owner 2026-11-02):** ride the pack through the day, charge at home overnight with the AFU
AF1200 at 8 A. This is the intended use, not a compromise: 20 → 100 % in ~5 h; below the ANT 10 A balance
gate so every night is a full top-balance; 0.15C is the kindest rate for the cells; the daily full charge
resyncs the ANT coulomb counter. Only charge above 10 °C. Do not leave the bike at 100 % for weeks (storage
30–50 %). Fast / public charging matters only on days > ~75 km mixed or for a second ride the same day —
the odometer will show after a season whether such days exist.

**On-bike charge port with a series diode (owner 2026-11-05).** An Anderson SB50 sits in the stock charge-port
location; its positive lead runs through a rectifier module **MD 110A-16** (110 A / 1600 V, isolated baseplate),
so the port is dead when unmated and the charger's input capacitors never spark on the contacts. Unmated, an SB50
is only IP10 (not finger-safe; IP20 is mated only, `manuals/Anderson-DS-SB50-REV9.pdf`), so the diode is physics
where a cap is procedure. **Decision: keep the diode, add the Anderson Environmental Boot with cover** (3-6054P2
Load / 3-6055P2 Source, IP64 mated and unmated; the plain dust cover 134G1 is dust-only, "not a hermetic seal").
Consequences:
- Forward drop ≈ 0.8 V under current: ~6 W at 8 A (AF1200), ~15 W at 18 A (E22) for the whole CC phase. Bolt
  the module to the aluminium pack box with thermal paste (base is isolated — verify with a DMM first). Bare, it
  would run > 100 °C over ambient.
- The pack ends ~0.6 V below the charger's CV: ~108.9 V = 3.63 V/cell instead of 3.65. Harmless, slightly kinder
  to the cells; balancing (starts 3.40 V) is unaffected. **Do not raise the charger CV to compensate** — ANT pack
  over-voltage protection is 110.0 V, there is no room.
- The charger sees 0 V before it starts. **The AF1200 does NOT start into the dead port (owner 2026-11-08)** — the
  earlier "charges through it" note was an assumption. Battery-detect needs to see pack voltage, not current, so the
  fix under consideration is a sense path across the diode, not its removal: (1) a high-value resistor anode→cathode
  (start at 100 kΩ = 1.1 mA touch current, within the IEC 61010 2 mA DC limit; go down to 47 / 22 / 10 kΩ only if the
  charger's detect divider needs it — test by feeding the charger output from the pack through the resistor with
  clips before soldering; two 1 W 250 V resistors in series on the module terminals); (2) a 200 V DC reed relay +
  1 kΩ across the diode, reed at the socket, magnet in the charger plug — port stays dead unless the charger is
  mated; (3) a momentary "start" button + 100 Ω — works but forgetting it means no overnight charge. Until one is
  fitted, charge at the pack SB50 (road-kit procedure). Same requirement for the **E22: must start into a dead
  output** or get the same sense path — YILEIDE checklist in `charging/road_kit.md`.
- The AF1200-vs-ANT discrepancy (97.44 V / 8.00 A vs 97.83 V / 8.90 A) is not explained by the diode but made
  worse: with it the pack should read ~1 V *below* the charger, the app read 0.4 V above, so one meter is ~1.2 V
  off. Calibrate both against a DMM.
- The port is input-only. Load / V2L use goes through the pack's SB50 or a DC-rated bypass, see
  `backup_power/README.md`.
- Charging through this port leaves the Sevcon on the bus (the stock Zero arrangement, charged to 116 V), unlike
  the road-kit procedure that unplugs the bike's SB50 at the pack. Port negative must be on P− through the ANT so
  the BMS can stop the charge.

**What a charger must do for 30S LFP** (all of "smart" that the pack needs): CC ≤ 26 A (0.5C, Gotion
table A.1.2) → CV 109.5 V (3.65 V/cell) → **stop** at ≈ 2.6 A (0.05C). No float, no lead-acid stages, no
temperature compensation; balancing and the cold cut-off are ANT's job. ANT (110.0 V pack / 3.65 V cell) is
the backstop, never the normal terminator. Useful knobs beyond that: current 8 ↔ 12 ↔ 26 A (balance nights /
120 V outlets / fast) and a CV "storage" endpoint ~3.5 V/cell. The AF1200 "30S LiFePO4" is a fixed CC/CV/stop
unit with the right numbers out of the box — verify CV and cut-off with a DMM once (first charge showed
charger 97.44 V / 8.00 A vs ANT 97.83 V / 8.90 A; one of them is off).

**Public charging formats (US):**
- **Level 1** = 120 V outlet (NEMA 5-15/5-20, ≤ 1.4–1.9 kW): what the AF1200 (100–120 V input only) uses.
- **Level 2 = SAE J1772**, 208–240 V single-phase (US split-phase L1/L2, no neutral), 6–7 kW typical: nearly
  every public post, Tesla Destination via a NACS → J1772 adapter, home wall EVSE. The post is a contactor plus
  a 1 kHz pilot; the vehicle answers with a diode + 2.74 kΩ (state B, 9 V) and 1.3 kΩ in parallel (state C,
  6 V). The charger is on the vehicle side and must accept 208–240 V. Pilot duty cycle encodes current only,
  never voltage: an adapter cannot tell 120 from 240 V. Zero sold exactly this for the stock FX (onboard charger: 2 × Meanwell HLG-320H-54A in series, ~650 W,
  CC/CV, terminated by the CCU; S/DS had four for 1.3 kW)
  (J1772 → C14 adapter, `zeromanual/wiki/Chargers.md`). Ready-made "J1772 to NEMA 6-20 / 14-50 / IEC" adapters
  exist (EVSE Adapters, TucsonEV, unbranded, $60–250); never a J1772 → 5-15 "120 V" adapter (returns current
  through PE). Map: PlugShare (J-1772 = Level 2 group; 120 V = "Wall Outlet"), ChargePoint app/RFID, AFDC.
- **DC fast (CCS1 / NACS-J3400 / CHAdeMO): rejected**, three independent reasons: a 96 V pack is below the
  ~150–200 V floor of DC stations (would need a custom 400 → 100 V isolated DC-DC); needs an ISO 15118 /
  DIN 70121 vehicle controller; and the cells take 26 A = 2.7 kW at most, so no station beats a brick.

**Chosen road / fast charger (owner 2026-11-03): YILEIDE E22**, built to order for 30S LFP after a direct
conversation with the seller (their listings are useless; get the sheet or a nameplate photo into
`manuals/YILEIDE-E22.pdf` before paying). Universal input, **11 A on 120 V, 18 A on 240 V** (~2 kW, 0.35C),
fixed CC/CV/stop, no CAN. **26 A is not pursued**: 18 A is half an hour slower on a 20 → 100 % charge
(~2.5 h vs ~2 h) and ~15 km less per hour at a post, while the Elcon tier costs 3–5×, 6 kg, an EVCC and
12 V for it. ~9 A AC at 240 V works on any J1772 post, 6-15/6-20 or dryer outlet; the passive adapter box
is enough. No CAN is no loss (the pack needs CC → CV 109.5 V → stop only). **AF1200 stays for the 8 A
nights** (0.15C is the kindest daily rate, margin on a 15 A circuit, already owned). Balancing is not the
reason: ANT balances only while cells are > 3.4 V (= under CV) *and* the instantaneous current is < 10 A,
so any charger balances only in its CV tail. AF1200 gets the whole tail (~30–60 min ≈ 50–100 mAh/cell),
the E22 the part below 10 A (~15–30 min) — half the minutes, not zero (corrected 2026-11-03). Do not
raise the gate above 10 A (IR drop at 11 A ≈ 20 mV/cell = Start Diff). Ask YILEIDE for a current selector; 120 V side draws ~11 A AC,
so use a 20 A outlet. Verify in writing: 100–240 V nameplate and no derating at 208 V, CV 109.5 V, cut-off
≈ 2.6 A with no float and no auto-restart, isolation, load-dump tolerance, PFC/fan/IP/weight/connector.
Checklist and reasoning in `charging/road_kit.md` ("YILEIDE E22").

**Options on record:**
- **Road kit, 8 A (simplest PoC):** AFU AF1200 in its 220–240 V version + a J1772 adapter, output to the
  pack's SB50 with the bike side unplugged (that is the Gen4 isolation). Covers posts and Tesla Destination,
  not 120 V outlets; check the AFU datasheet tolerates 200–208 V (commercial sites). 1 h at a post = ~15 km,
  so only worth it for multi-hour stops. A universal 100–240 V charger covers posts *and* outlets in one box.
- **26 A home/fast:** needs ~3.1 kW from the mains → a 240 V circuit (NEMA 6-20, or a dryer 14-30 / range
  14-50 pigtail — same single-phase supply as the posts); no 120 V outlet can do it (80 % rule: 1.4 / 1.9 kW).
  Candidate: **Elcon HK-J-H132-32** (`manuals/Elcon-HK-J-H132-32-verA.pdf`, 2015 verA — request a current
  sheet): 85–265 V in, 33–132 V / 32 A out, 3300 W @220 V / 1600 W @110 V, IP67, 3.9 kg bare, Anderson 50 A
  out, 12.5 V / 5 A aux, CAN-controlled (output stops on CAN loss) or factory-fixed curve with enable pin.
  Order with 26 A limit, not 32; on 120 V outlets command ≤ 12 A (1600 W is ~14 A AC). CAN version + the
  speed-converter ESP32 = one charger for 8 A nights, 26 A fast, 12 A outlets, temperature taper from ANT.
  Fixed-curve version keeps the AF1200 for nights. 0 → 100 % at 26 A ≈ 2–2.5 h.
- **Market survey 2026-11-02** (table in `charging/road_kit.md`): universal-input chargers that reach 109.5 V are
  Elcon HK-J-H132-32 (26 A, $459–899), Thunderstruck TSM2500 96 V (15 A, $555 / $855 with EVCC), Delta-Q
  XV3300 120 V (40 A, J1772 interface built in, OEM channel), Danl VL9610L-class 10 A bricks ($140–180, sheet
  mandatory). Not qualifying: Zivan NG1/NG3 (115 *or* 230 V variants), Grin Satiator (103 V max), QuiQ.
  **Thunderstruck/Dilithium EVCC v3 ($270)** is the J1772 vehicle side plus CAN charger controller in one box:
  pilot diode, proximity drive-away protection, duty-cycle-limited current, profiles (240 V / 26 A vs 120 V /
  12 A), `maxv / maxc / termc`. Inlet + EVCC + CAN charger makes both the DIY adapter box and the ESP32
  charging firmware unnecessary; 12 V for it can come from the Elcon's 12.5 V aux output.
- **Delta-Q QuiQ 1000 96 V (912-9600, the Zero "Quick Charger"): not worth it.** Right form (945 W / 8.5 A,
  85–265 V, IP66, fanless) but the curve is fixed at purchase (lead-acid ~115–118 V or Zero's 28S NMC
  ~116 V), algorithms load only from Delta-Q's library via the QuiQ Programming Kit, no public 30S LFP file,
  no open reverse engineering of the format or the QuiQ-dci CAN, and Delta-Q warns reprogramming OEM units
  may brick them. One e-mail to a distributor can check for a 109.5 V LFP profile; do not plan on it.

---

## Backup power (researched 2026-11-05; details in `backup_power/README.md`)

The pack as a household / camping energy source. Power is not the limit (52 A × 96 V = 5 kW, more than a
household circuit); range is: **every 1 kWh spent at camp = 18 km less ride home**. Three ways out: a 96 V-input
pure-sine inverter (a standard off-grid tier, 1–5 kW, ≤ 3 kW chosen, LV cut-off 88–90 V above the ANT 84 V
cut), an isolated 72–120 V → 12 V buck for 12 V camping gear, or the garage trick of DC into "100–240 V"
switch-mode bricks. Fridge + Starlink + gadgets + cooking ≈ 3 kWh/day; resistive space heating is out. Connection
is the pack's SB50 with the bike unplugged (no Sevcon isolation needed for a load; own DC fuse per load;
precharge for big inverter capacitors). The on-bike charge port is input-only because of the diode; a bypass,
if ever wanted, is a rotary PV DC isolator (32 A / 1000 V DC) across the diode, or a contactor keyed by a magnet
in the load plug — never remove the diode. Nothing bought (owner 2026-11-05).

## Street mode (started 2026-11-04; details in `street_mode/README.md`)

Owner's term for an FXS-style road setup of the 2014 FX (lower seat height, road suspension). Researched so
far: **rear shock and lowering** (2026-11-03). The FX has no linkage (shock bolts frame tube → swingarm,
≈ 1:2 to the axle), so lowering = shorter shock only. Stock 22-06105 Fastace BFA57RC is 319 mm eye-to-eye,
M10, 475–585 lb/in. The 2015+ Showa 22-05879 is the same length (320 mm) and came with a new frame
(26-08080), swingarm (21-07748) and a 60 mm instead of 70 mm upper bolt — not a documented bolt-on and no
lowering. Options in order: spacer in the Fastace (3/4 in → ~1.5 in, forum-proven on a 2013 FX), Ikon
3610-1104 (made for the 2016 FXS, −2 in version), made-to-length shock (~300 mm), Fox Podium RC2 (Zero
accessory for 2013–14 FX, stock height). Measure eye/lug widths and spring clearance first.
**Front wheel 21 → 19/18 (2026-11-07):** a used Zero XU 2011–13 front wheel is 19 × 1.85 (no Zero wheel is 18 × 1.85;
220 mm rotor, same end-bolt axle family as the FX); hub interchange with the 2014 FX is likely but unproven — check
bearing bore (6904 = 20 mm), hub width and rotor PCD vs the FX 240 mm rotor before buying. Documented alternative:
2014 DS 2.15 × 19 wheel 23-07213 (same axle/spacer/bearings/rotor bolts in the catalogues). Tyres: BT46 100/90-19 57H
(H, not V, on a 1.85 rim) + 120/80-18 rear; front drops only 10 mm, stance stays stock. Details in `street_mode/README.md`.
**Owner 2026-11-07: no fussing with 18/19 — wait for a 2013–14 S/SR/DS 17 in cast pair.** Rear 23-04859-1 is the
wheel Zero used on the 2016 FXS (both ends), same axle/pulley/rotor as the FX, right spacer 20-07324; front S cast with
the FX 240 mm rotor (not the FXS front: hollow axle, 320 mm). Front −50 mm, rear −18 mm → level with ~30–40 mm at the
shock = seat −45 mm. Keep the 21/18 set for Catalina dirt. Open: 140/70-17 vs belt/2014 swingarm, front rotor PCD. **Front rotor on the S
cast wheel (2026-11-10, 2014 S catalogue `14s.pdf` ZEV0002, not in `manuals/` yet):** the 2013–14 S/DS front is a **313 mm
floating rotor 25-03541 on 6 × M6 bolts 90-07290** (supersedes 90-03477 — the same bolt family as the FX front), caliper
Nissin 272-C00-363 25-04164, so the S front hub is 6-hole and the FX 4-bolt 240 mm disc will NOT bolt to it — either run
the S 313 mm rotor + S caliper on that wheel, or re-check the FX front hole count. The zeromanual "matches KTM 450SMR"
note for this rotor is plausible but unverified: KTM 450 SMR 2004–14 (and SX/EXC 2011–19) front disc 25009260000 is
310 mm floating, KTM hubs are 6 × 6.5 mm holes on ~143–144 mm PCD; Zero's PCD, offset and thickness (313 × 4 mm per
press specs) are not documented anywhere found — measure before buying.
**Forks (2026-11-07):** FX/S/DS 2014 are three different Fastace sets on different clamps (shared: axle, spacer, Nissin
caliper, M8×40 bolts). S 2012–13 and XU 2011–13 share the **Fastace ALX07RC** (38 mm, 135–140 mm travel) with different
brake-side legs (313 vs 221 mm lugs); the 2013 XU ran it in the FX frame (48 mm clamps) → the XU fork is Zero's own short
road fork for the XMX clamps, the S fork the same with 313 lugs for the S 17 in wheel. Details in `street_mode/README.md`.
**Rear shocks (2026-11-07):** XU and S shocks are different parts (S = BDA58RC 260 mm, 11/16 in bottom bushing, not
for the FX clevis). The 2013 XU sits on the 2013 FX frame 20-06390 and "FX/XU swingarm" 21-05493-1, so its **"XU 16/19"
shock 22-05487** (+ fork set 22-05488) is Zero's own lowered pair for this chassis, special order via Koup's; same BFA57RC
mount family as the 2014 FX shock 22-06105. Length unknown (est. 40–55 mm shorter), full XU stance, matched with the fork.

---

## Drivetrain / Gearing

### Stock Configuration
- Drive type: belt drive
- Overall gear ratio: **5.28:1** — 132T rear / 25T front pulley, Poly Chain GT Carbon belt (OM-FX-MY14 p. 1.7)
- Part numbers (`manuals/14fx.pdf` ZEV0009): front pulley 25T 8 mm pitch 15 mm wide 30-03656 on tophat 20-05453,
  rear 132T 8 mm pitch 17 mm wide 30-04051, belt 220T × 8 mm × 14 mm wide 30-08084 (≈ 1760 mm), motor "75-5"
  replacement kit 12-08033. The same catalogue lists a 520-chain option (12T 30-04890 / 65T 30-05090 on the 132 mm
  bolt circle) — the chain route if a re-gear is ever wanted

### Drive belt — replace by condition, carry a spare; Gates 8MGT-1760-12 is acceptable (2026-11-10)

- **Zero's own rule (OM-FX-MY14 p. 5-2 / 5-13):** check slack and condition at every service; replace a worn/damaged
  belt; "check for cracking and/or replace the belt every 25K mi (40K km)". Replace at once on: cuts, damage to the
  belt centre, exposed tensile cords on the tooth side (= worn pulley teeth), cracks at the tooth base, stone punctures
  on the ribbed back, or after any ratcheting (teeth skipping — damages the carbon cords). Edge bevelling = misalignment.
  Tension 20–30 kg on the Krikit gauge, or 96–124 Hz plucked (Gates Carbon Drive app, zeromanual Belt Tension Check).
- **Decision for this bike:** no mileage-based replacement (mileage is unknown anyway, ~10–15 thousand km estimated);
  inspect the tooth side with a light every few hundred km, keep alignment, and **buy the spare now** — a belt failure
  strands the bike. The 2014 belt is PU + carbon cord, not rubber; age alone is not a reason, cracks are.
- **Belt:** Zero 30-08084 (= 30-03673) is a Gates Poly Chain GT Carbon 8MGT, 220 T, 1760 mm, **14 mm** — a custom width
  Gates makes only for Zero. The standard catalogue width is **12 mm: 8MGT-1760-12** (same pitch, profile, cord, PU).
  Pulleys are 15 mm (front 25T) / 17 mm (rear 132T) wide, so a 12 mm belt has 3–5 mm of lateral room: alignment and
  flanges matter more than with 14 mm. 21 mm does not fit the pulleys.
- **Rating (Gates design manual, 12 mm, 25-groove small sprocket, × 1.17 length factor for 8MGT-1760,
  `manuals/Gates-Poly-Chain-GT-Carbon-Drive-Design-Manual.pdf` p. 46):** ~8 hp / 6 kW at 1000 rpm, ~15 hp / 11 kW at
  2000 rpm, ~22 hp / 16 kW at 3000 rpm, i.e. ~59 N·m rated at the motor pulley (industrial continuous rating before
  the 1.3–2.0 service factor). The 14 mm OEM belt is ~17 % stronger. Stock FX ran 44 hp / 95 N·m on the 14 mm belt for
  the 25K-mile schedule, so vehicles run these belts well above the industrial design point on short peaks.
- **This build vs the belt:** 7.5 kW at 78 A is half the 12 mm continuous rating above 60 km/h (2590 rpm) and a quarter
  of stock peak; the only place the 12 mm belt is *more* stressed than OEM-on-stock is launch, where torque is
  phase-current limited (stock-level, ~17 % more belt stress than OEM). Mitigate in 2920h (max torque / ramp, already
  planned) and never land a jump on the throttle. **Verdict: 12 mm Gates is fine as the working belt**; keep the
  Zero 14 mm as the preferred spare if one comes up cheap. Tension a 12 mm belt at the low end of Zero's range
  (~20–22 kg; or compute with the Gates app for 12 mm × 1760) — Zero's 20–30 kg was set for 14 mm.

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
- Frame interfaces for MOUNT_POINTS = the stock module hardware (`manuals/14fx.pdf` ZEV0008 "Frame (Right)"):
  module support platform 20-06863, module sliders 20-05773 (general) and 20-05774 (front horizontals),
  separator block 20-05153, battery retaining rail 20-06404 with two C9101-2112 panel latches 20-05296, bike-side
  module connector holder 20-05912. Measure these on the bike and reuse them; the exploded view shows how they sit
- Renders for a quick look: `battery_box/renders/spec/` and `renders/thick/`

---

## Stock 2014 FX parts (`manuals/14fx.pdf`, added 2026-11-03)

AF1 Racing's Zero parts diagram for the 2014 FX (the `14FX.pdf` linked from `zeromanual/wiki/Exploded_Views.md`),
37 pages, 10 exploded views: ZEV0001 Lighting, 0002 Brakes, 0003 Wheels, 0004 Steering, 0005 Body trim, 0006 Rear
suspension, 0007/0008 Frame (left/right), 0009 Motor and drive, 0010 Electronics. Each view = drawing + callout
table (Zero part number, name, qty); "PA-xxx" = not sold separately. Use it to name stock parts, order
replacements and locate frame mounting points. It carries no harness, connector or electrical data.

Electrical part numbers worth knowing (ZEV0010 unless noted):
- Sevcon Gen4 Size 4 controller 60-07007 ("include VIN for programming"), heatsink XMX MY14 20-06553 on mount
  20-05036 with bash guard 20-03863 (ZEV0007), Formex insulating top 24-05783, controller covers 24-06190/-06191
- 12 V supply: **DC-DC converter Sevcon 622-11202 non-EMC, Zero 60-04015** — on the bike and working on the 96 V
  pack (lights + instruments, owner 2026-11-03); the source for the speed converter's 12 V
- Contactor Gigavac 12/40 VDC 45-08091 → 45-08135 (see Contactor section); power-pack fuse PA-112 with cover
  20-05629; power pack ZF3.3 46-08032 (2014–2016 FX/FXS/MMX); BMS module 41-06419-08; MBB 40-06462; CCU 40-06495;
  on-board charger "XMXFX charger 2S configuration" 40-05326 on Meanwell brackets 20-05289/-05290 and
  Meanwell + aux-charge-port bracket 20-06910, aux charge mount 20-06862-1 (ZEV0008) — all VIN-locked modules
  that OpenZero removed; the catalogue entries explain why they were never reusable
- Controls: throttle 40-04069 "0-5K 4-way" (the failed Magura pot), kill/mode/start switch 40-06054, left
  handlebar switch 45-02693, Zadi key switch 45-02692, kickstand switch PA-115, brake switches in the master
  cylinders (not sold separately), dash LCD 40-08030 (14–16MY)
- Lighting/horn for the 12 V budget (ZEV0001): headlight low beam 65-06401, high beam 65-06400, tail light
  65-00600, turn signals 65-03462/-03463, horn K70/H12 45-06774
- Wheels (ZEV0003): front 1.60×21 (IRC GP-110 3.00-21), rear 18 in (IRC GP-110 4.10-18; this bike: 2.15 rim,
  120/80-18, see Speed Converter) with the 14MY upgrade
  wheel kit 12-08076; bearings 6904 2RS, seals 25×37×7

## Chassis mileage and the stock MBB / dash (2026-11-09)

**Mileage is unknown.** The Sevcon stores none; the stock odometer lives in two places (zeromanual Gen2 dash
"Indications" table and the app's "Odometer" row): the dash keeps its own figure in its memory, the MBB keeps
another and reports it to the app and in its log ("may not always agree"). **Both the MBB (label "MY 2014" +
serial) and the dash were found (owner 2026-11-09)**, with the cut harness and its MBB connectors — reading
the odometer is a bench job, not a reverse-engineering project.

**Wear-based estimate, as a cross-check only.** DOT date codes read 2026-11-10: **front IRC GP-110 3.00-21 = 2616**
(week 26 of 2016, so NOT the original tyre — the bike is a 2014 MY), **rear Bridgestone BT46 120/80-18 = 3223** (week 32
of 2023). Both tyres are replacements, so neither counts the whole life of the bike:
- Front, fitted ≈ 2016–17, centre tread ~10 % left = about one full front life since then, ~10–15 thousand km.
- Rear, fitted ≈ late 2023, well worn = ~5–10 thousand km in the last two years. That pace (several thousand km a year) does
  not match the front's ~1.5 thousand km/year average, so use was uneven: the bike probably sat for years and then commuted
  daily — or the front simply has more life left than it looks.
- The original front (2014 → 2016/17) is unaccounted for: a front normally outlasts a rear, so if it wore out it adds
  another ~10 thousand km; if it was replaced for damage or age, less.
Net: **~15–25 thousand km, most likely ~20**, up from the earlier 10–15 estimate. Rotors agree with "a lot": front has a
wear lip, rear was warped. Firm it up with tread depth in mm vs new on both, and the front rotor wear lip measured with
a micrometer in four places (lip height = wear directly; stock 4.5 mm, limit 3.85 mm; ~0.1 mm = a few thousand km,
0.2–0.3 mm ≈ 10–20 thousand, ≥ 0.4 mm = 20+) — now the only wear witness that has been on the bike since 2014.
Other sources: Zero dealer/support by VIN (service and app-upload records), VIN history (NMVTIS, CycleVIN).

**How the MBB is powered (2016 FX wiring diagram rev 1.1, `zeromanual/images/2016_FX_Wiring_1-1-preview.png`,
1650 px, readable when cropped; the 2013 trace is the wiki's "Main Bike Board Connections" + DC-DC table):**
the MBB runs **directly from the traction battery** through its own "MBB FUSE 4A", upstream of the contactor
(that is why it is partly alive with the key off and why it can enable the DC-DC). The 12 V side is a separate,
isolated pair fed back from the DC-DC output. Pin numbers differ between the 2013 trace and the 2016 drawing
(the wiki itself notes the DC-DC enable moved 21 → 20 between 2013 and 2015); the 2014 FX is electrically a
2013-type bike (CCU + Meanwell), but identify pins by wire, not by year:

| MBB 1 (34-pin, harness side) | 2013 trace (Burton, S) | 2016 FX drawing |
|---|---|---|
| Battery + (~100 V, via 4 A) | 7, Orange/Blue **16 AWG** | 18, ORN/BRN |
| Battery − | 5, Orange/Black | 7, ORN/BLK |
| Key-on signal (= battery + through the key) | 4, Orange/White | 15, YEL/GRN |
| +12 V from DC-DC output | ? | 4, BLUE |
| 12 V common | ? | 29, BLK/BLU |
| DC-DC enable (not needed on the bench) | 21 | 1 or 20, ORN/RED |

**Verified on the 2016 drawing 2026-11-10 (legend colours):** MBB 1 pin 18 ORN/BRN is drawn red = "BATTERY + DIRECT",
fed from "MBB FUSE ABC 4A" off battery-module connector pin 1 ORANGE; pin 7 ORN/BLK is drawn violet = "BATTERY −";
pin 4 BLUE is drawn blue = "+12V ISOLATED" (DC-DC OUTPUT+ pin 4 BLUE); pin 29 BLK/BLU is drawn brown = "12V COMMON"
(DC-DC OUTPUT− pin 5 BLACK). Key switch (4-pin, two used): harness YEL/GRN (pin 1) ↔ YEL/GRY (pin 2); YEL/GRN runs
to MBB 1 pin 15, YEL/GRY runs to battery-module connector pin 4 (front and rear modules in parallel) — so in 2016
the key joins a BMS-side line to the MBB key input; in the 2013 trace it is battery + through the key. Bench: battery +
(via the 1 A fuse) onto MBB 1 pin 15 YEL/GRN. CAN on MBB 2 (40-pin): 21 BLU/GRY + 22 WHT/GRY = Sevcon (matches Sevcon
pins 27/16 — never connect on the bench); WHITE/BLUE pairs 6/7, 23/24, 25/26 are the other CAN taps (dash, OBD-II,
charger/BMS — which is which not traced). Dash CAN = dash pins 11 WHITE (H) / 12 BLUE (L), same colour convention as
OBD-II pin 6 WHITE CAN HIGH / 14 BLUE CAN LOW; ring the dash pair to find its MBB 2 pair, or use OBD-II 6/14 if that
connector is still on the cut harness. 120 Ω across H/L.

Verification on the cut harness: battery + is the only 16 AWG orange wire on MBB 1 and rings to the 4 A fuse
holder near the pack connector; battery − has the same colour as DC-DC INPUT− (5-pin DC-DC connector pin 3,
ORN/BLK) and rings to it; the key wire runs to the Zadi switch, whose other contact sits on battery +. On the
MBB itself battery − must ring to OBD-II CAN GND and UART GND, and diode-test between − and + must show a
junction, not 0 Ω (polarity check before power).

**Bench recipe:** ~100 V DC at a few watts — the weak DC adapter used for Sevcon logic tests is ideal — with a
1 A fuse in the + lead (or the pack via the SB50 with the same fuse); key-on = battery + to the key pin; 12 V to
the 12 V pins from any adapter or the bike's rail. **Never connect this MBB's CAN to the Sevcon bus**: RPDOs
1400h–1403h are still enabled in the Sevcon and the MBB will command it. Bench only, Sevcon unpowered.

**Reading the odometer, cheapest first:**
1. **Dash alone on 12 V.** 16-pin connector, 2016 drawing: +12 V pin 16 BROWN (fuse 6 "RUN LT 5A"), ground
   pin 9 BLACK, CAN probably 11 WHITE / 12 BLUE. The dash stores its own odometer, so it may show ODO with no
   MBB at all. Zeros or dashes = the figure comes over CAN; then join dash CAN to MBB CAN (120 Ω termination)
   and read it on the dash, no terminal needed.
   **What is documented (2026-11-09, zeromanual Gen2 dash "Indications" + OM-FX-MY14 p. 3-6/3-7):** the dash is
   on the 12 V rail (backlight fault-finding = check the running-lights fuse); the clock is internal with its own
   non-replaceable battery; the **odometer is "stored in the unit's memory"** (the MBB only pushes updates, a
   frozen ODO = misconfigured MBB model data); speed, SOC, charge time, mode, meters, Bluetooth symbol and the
   error-code display come from the MBB over CAN; SEL/ADJ are the dash's own buttons; the other 16-pin wires are
   discrete 12 V tell-tales (turn signals, high beam …). Nobody has written down what the LCD shows on 12 V alone,
   so it is a 2-minute test, not a fact: expect backlight + clock, probably ODO, and blanks or dashes in the CAN
   fields. The dash never had a Mode button — Mode is on the right handlebar and goes to the MBB.
   **Result 2026-11-10 (owner, bench, 12 V on pin 16 BROWN / pin 9 BLACK, pins verified on the 2016 drawing):
   backlight comes on, the LCD shows nothing at all — no clock, no ODO, no segments.** The dash renders only
   when the MBB talks to it over CAN; "stored in the unit's memory" does not mean "displayed without the MBB".
   So option 1 is closed and option 2/3 (MBB powered from ~100 V, dash CAN joined to MBB CAN with 120 Ω) is the
   path to the odometer. Easiest CAN tap on the cut harness: OBD-II pin 6 (CAN H, WHITE) / 14 (CAN L, BLUE) →
   dash pins 11 / 12.
2. **Zero app over Bluetooth.** With the MBB powered, pair and read Performance → Odometer. Risk: the legacy app
   may be gone from the stores or need an account.
   **Pairing needs the Mode button (OM-FX-MY14 p. 3-13 "Bluetooth Pairing", same text in zeromanual for 2014+;
   2013 bikes toggled the SPORT/ECO switch 12×):** bike keyed ON and *not armed* (kickstand down, run switch in
   Stop), then **hold Mode ≥ 5 s** until the Bluetooth symbol on the dash blinks → discoverable as
   `ZeroMotorcyclesXXXXX` (last 5 of the VIN). iOS pairs in **Settings → Bluetooth with a six-digit code** (so it is
   classic Bluetooth, not BLE — a BLE scanner app will not see it); Android pairs from the Zero app's Settings tab.
   Solid symbol = paired. Pairing is per phone, so a new phone always needs the button; without a dash on the bench
   the phone's scan list is the only indication. **On the bench the button is a jumper:** the right-bar pod
   (kill/mode/start switch 40-06054) is a 4-pin connector, 2016 drawing: pins 1–2 = RUN toggle (harness RED and
   RED/BLK, RED/BLK lands on MBB 1 pin 24 — the 2013 table's "white, pin 24"), pins 3–4 = MODE momentary (harness
   BLU/BLK and RED). 2014 colours may differ: ring the pod connector's MODE pair back to MBB 1 pins and short those
   two pins for 5 s after key-on. Leaving the RUN pair open *is* "Stop" and an unplugged kickstand sensor reads
   as down / faulted — both are the not-armed state the procedure asks for, and nothing can arm on the bench anyway
   (no BMS, no contactor). Give the MBB its 12 V pair as well; a stock bus without the Sevcon has lost the
   Sevcon's own terminator (pins 2–24, see the pinout note), so put 120 Ω across CAN H/L if the dash is joined.
3. **OBD-II serial console** (2016 pins: 4 = 12 V common BLK/BLU, 5 = UART GND, 6 = CAN H WHITE, 8 = UART RX
   RED/BLK, 9 = UART TX GRY/BLK, 11 = CAN GND, 12 = UART "RED", 14 = CAN L BLUE). USB-TTL on 5/8/9, try 115200
   then 57600; commands `help`, `status`, `bbhist`. The wiki warns the port's own supply is weak: short cable.
   Logs parse with `zero-log-parser` (GitHub); "Riding" entries carry the odometer. Gen2/MBB Console and Log
   Extraction pages are not in the mirror (web.archive.org links in `zeromanual/wiki/Interfacing.md`).

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
  - `Elcon-HK-J-H132-32-verA.pdf` — Elcon HK-J 3.3 kW sealed CAN charger datasheet (2015-04-11 verA), the
    26 A fast-charge candidate; from elconchargers.com
  - `Thunderstruck-EVCC-v3.1.3.pdf` — Dilithium Design / Thunderstruck EV Charge Controller v3 manual (J1772 pilot
    + proximity handling, duty-cycle current limit, CAN control of Elcon/TC and TSM2500 chargers, profiles)
  - `Delta-Q-XV3300-presentation.pdf` — Delta-Q XV3300 3-in-1 charger (60–120 V model, 40 A, built-in J1772
    interface, 500 W DC-DC); OEM-channel reference only
  - `Anderson-DS-SB50-REV9.pdf` (2026, andersonpower.com) / `Anderson-DS-SB50-REVC4.0-2014.pdf` — SB50 connector
    datasheet, the pack's output connector (added 2026-11-05). The connector has no own amp rating: it is rated by
    temperature (housing −20…105 °C) with whatever wire the contact takes. Wire-to-wire with 6 AWG contact 5900
    and 105 °C cable: UL 1977 120 A, CSA 50 A (< 30 °C rise), hot-plug 50 A / 250 cycles at 120 V DC, IEC 50 A,
    0.2 mΩ mated. "Temperature Rise at Constant Current" curve for 6 AWG (25 °C ambient): ≈ 8 °C at 30 A, 15 at
    40, 23 at 50, 30 at 60, 40 at 70, 55 at 80 A (≈ 0.009·I²); IEC 60512-5-2 derating: 95 A at 25 °C ambient,
    ~87 A at 40 °C, 80 A at 50 °C. For the bike: 52 A → ~+24 °C, 78 A → ~+53 °C, both inside the 105 °C limit;
    120 A ANT trip is a seconds-long pulse, thermally irrelevant. The "75 A" seen in listings is the NEC 90 °C
    ampacity of 6 AWG cable (or the seller rating of the 8 AWG contact 5952), not an Anderson figure.
    `Anderson-SB-assembly-1S1030A.pdf` — crimp/solder sheet: SB50 strip 14 mm, hand tool 1309G4, single crimp
    ≥ 6.35 mm from the barrel end, stranded Cu only; wrong tooling voids UL/CSA
  - `14fx.pdf` — Zero FX 2014 parts catalogue (exploded views ZEV0001–ZEV0010 with Zero part numbers; AF1 Racing
    `14FX.pdf`, added 2026-11-03). Stock part numbers, frame/module mounting hardware, drivetrain. No wiring,
    connectors or electrical specs. Summary in "Stock 2014 FX parts"
  - `15fx.pdf`, `16fxs.pdf` — the 2015 FX and 2016 FXS catalogues (same AF1 Racing source), used to compare
    frame / swingarm / shock part numbers across the Fastace → Showa change (see "Street mode")
  - `Gates-Poly-Chain-GT-Carbon-Drive-Design-Manual.pdf` — Gates design manual (gates.com, added 2026-11-10): 8MGT
    horsepower rating tables (12 mm table p. 46 = the Zero belt family), length correction factors, tensioning
  - `14s.pdf` — the 2014 Zero S catalogue (repuestoszero.es print version of the AF1 Racing `14s.pdf`, added 2026-11-10):
    S/DS front brake (313 mm floating rotor 25-03541, 6 × M6 bolts 90-07290, Nissin caliper 25-04164), 17 in S cast wheel
    23-03929-1 — the donor side of the street-mode wheel swap
- `rides/log.md` — ride log: GPS distance/speed per ride + ANT log extremes (current, weakest cell, warnings),
  started 2026-11-08; `rides/episode3.md` — ride plans and the energy model
- `street_mode/README.md` — FXS-style road setup of the FX: rear shock geometry 2014 vs 2015+, lowering options,
  open measurements (added 2026-11-04)
- `backup_power/README.md` — the pack as a backup / camping power source: converters, load table with range
  cost, connection point, charge-port bypass options (added 2026-11-05)
- `ideas/README.md` — parking lot of engineering ideas beyond the plan (reverse gear, regen paddle, range
  extender string, ESP32 features, PTO…), none decided (added 2026-11-05); includes "ESP32 bridge: web
  interface to Sevcon settings over Wi-Fi" — DVT-free configuration by SDO (login 5000h, pre-op 2800h, the
  MBB-removal sequence as a python-canopen script, caveats)
- `charging/solar.md` — solar charging PoC sizing (300 W for daily use, ~1.2 kW for a full pack per SoCal day), 96 V MPPT
  controller question, PV string voltages (added 2026-11-07)
- `charging/road_kit.md` — public-charging design: J1772 adapter box (BOM, pilot circuit, procedure), charger
  selection (AF1200-EU, universal, Elcon HK-J, QuiQ verdict), buy-vs-build
- `battery_box/SPEC.md` — battery box enclosure build spec (build123d, Bambu P2S)
- `battery_box/enclosure.py` — parametric build123d model; `battery_box/README.md` — parts, deviations,
  print/assembly instructions, MEASURE_ME list; `battery_box/output/` — STLs in print orientation
