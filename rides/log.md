# Ride log

One row per ride. Distance and speed from GPS tracks (Open GPX Tracker on iOS; keep the location permission on
"Always" and the screen on, or the track has gaps). Current, cell voltages and warnings from the ANT BMS system log
(Settings → System log export). ANT log times are run-time since BMS boot; convert with the `Run Time` field in the
export header (= wall clock of the export). **The run-time counter runs ~0.4 % fast** (export 10-31 → 11-08: +45 min
over 8.2 days; 11-08 → 11-10: +13 min over 2.1 days), so convert each ride with the export taken right after it; an
event N days older than the export lands ~6 min × N too early. The log is a 200-event ring buffer: export after every
ride or the oldest rides fall off. ANT current reads ~10 % high vs the AF1200 (uncalibrated). Event snapshots are
not simultaneous: the current field can be sampled after throttle release while the cell voltages still belong to
the full-throttle moment (e.g. "cell 16 3.089 V at 5.6 A"), so never read a cell-vs-current relation from a single event.

Bike state through 2026-11-08: 30S Gotion LFP, Sevcon battery limit **not written** (full throttle = 78–82 A),
no odometer, CT-22 not connected. Energy model: `episode3.md`.

| Date | Time (local) | Distance | Moving / total | Avg moving | GPS max | Elev gain | ANT: max A, min cell | SOC before → after | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-08 | 15:55–16:03 | ≥ 1.15 km (track incomplete) | – / 7.5 min | – | ≈ 44 km/h (valid), 152 km/h artefact | ≈ 40 m | 82.6 A; cell 16 3.093 V | – | Loop from home, Laguna Niguel. Two gaps of 3.7 and 2.3 min (phone backgrounded). Steep ~14 % descent at 25–44 km/h |
| 2026-11-08 | 17:26–17:37 | 5.65 km | 7.7 / 11.0 min | 44 km/h | **88–90 km/h (55 mph)** on a ~2 % descent; 75–86 km/h held on the flat | 155 m (80–180 m) | 90 A (81 A sustained); cell 16 3.076 V, spread 0.068 V | – | Loop from home, 7 stops of 15–36 s. Descent stretch at 85–90 km/h produced no 60 A warning (< 60 A); flat stretch at 80 km/h = 81 A. Owner: "almost stopped accelerating, still had potential"; 106/117 km/h points at 17:27:00 are a GPS catch-up artefact |
| 2026-11-10 | ≈ 09:12–09:19 (ANT) | not tracked; the ANT event pattern (7 min, 78–84 A bursts) looks like the standard 5.65 km loop | – | – | – | – | 84 A; cell 16 **3.038 V** (lowest ever), spread 0.071 V | – | First ride on the Honda 43351-MBN-671 rear disc: pads bedded, no pulsing, pad track centred on the swept face. Brake-test ride. Owner estimate for the day's untracked riding was 2–3 mi; the ANT log shows two sessions (this and 12:18) |
| 2026-11-10 | ≈ 12:18–12:30 (ANT) | not tracked (second loop, ~12 min of riding) | – | – | – | – | 87.7 A; cell 16 3.056 V | – | Then from the app: MOSFETs toggled 12:35 (CtrlChgSw1/CtrlDsgSw1), back on 12:59; **charge 13:08–14:03, 60 min at 8.8 A max ≈ 8.7 Ah ≈ +17 % SOC**, stopped at 3.381 V max cell (not a full charge — unplugged to ride); a 2-min 82–83 A burst at 14:50 |
| 2026-11-10 | 18:19–18:28 | **5.72 km** (home → "LT") | 7.2 / 8.75 min | 48 km/h | **81–83 km/h** (5-s rolling 81) on the 1.4 % climb 18:25:15–18:26:10; 118 and 239 km/h points at 18:26:21 / 18:27:41 are artefacts | ≈ 72 m (home 125 m → 71 m → 128 m) | **90.6 A** at 18:25:56 (≈ 80 km/h, climbing); cell 16 3.068 V at 85.6 A, spread 0.081 | – | **First real commute, leg 1.** One traffic light (two stops, 31 + 28 s at 18:24). Full throttle 18:21:15–18:23:30 at 68–73 km/h avg / 80 max = 83–89 A continuous; 16 ANT warnings in 9 min |
| 2026-11-10 | 19:12–19:23 | **5.84 km** ("LT" → home) | 7.4 / 10.4 min | 48 km/h | **85–87 km/h** at 19:19:00–19:19:36 at the bottom of the descent (70 m); the 83 km/h at 19:12:24 (first fix after a gap) is an artefact | ≈ 86 m (129 m → 70 m → 141 m) | **87.4 A** at 19:18:20; cell 16 **3.046 V** at 85.7 A, spread **0.088 V** (largest yet) | – | **Commute leg 2.** 68 s stop at 19:13:56 (light at the start), 20 s at 19:15:28. Full throttle 19:15:51–19:19:40 for 3.8 min: 70–76 km/h avg on a −1.3 % descent still draws 81–87 A (on 11-08 the −2 % descent at 85–90 km/h drew < 60 A — wind or rolling grade, note it next time). 22 ANT warnings in 10 min; the last two UV events (19:21:11, 19:22:21) carry identical values (3.092 V / 80.1 A / 0.066) — a re-logged warning, not a new one |
| 2026-11-11 | 10:17–10:50 | **18.24 km** (home → PCH → Laguna Beach → Park Ave → Top of the World, Alta Laguna Park) | 26.1 / 32.6 min | 42 km/h | 81–86 km/h on PCH (10:22–10:24, 10:27–10:28); 98 km/h at 10:27:17 is an artefact | ≈ 400 m real (GPS sums 466; 130 m → 8 m at Laguna Beach → 305 m) | **91.3 A** on PCH (10:29 corr.), **91.1 A on Park Ave**; cell 16 3.056 V at 91.3 A, 3.071–3.075 V on the climb, spread 0.080 | – | **Episode-3 reconnaissance, Route A.** 12 stops (lights, Laguna Beach traffic 10:35–10:41 at 13–30 km/h). **Park Ave climb 10:42:12–10:45:00: 2.44 km, +237 m (9.7 % average, 12–18 % sections) at full throttle the whole way, 78–91 A in ANT; speed 64 km/h at the bottom, 45–53 on the 14–18 % section, 31–41 km/h on the last 12 %, 17 km/h at the top** (owner: "slowed down at wide-open throttle at the end"). Seven GPS gaps of 22–42 s; the "stop" 10:19:40–10:20:45 is a fix loss while descending (ele 103 → 82) |
| 2026-11-11 | ≈ 11:00–11:20 (ANT) | not tracked; same route back ≈ 18 km (approximated from the outbound track) | – | – | – | – | **97.1 A** (ANT record, ≈ 88 A real) at ≈ 11:09 with cell 16 3.064 V, spread 0.085; 80–90 A bursts through 11:20 | – | **Return from Top of the World.** The Park Ave descent registered as a 2-min "charge" in ANT (EndOfChg ≈ 11:00: max 9 A, 2 min) = regen on the descent peaks at only ≈ 9 A with the current weak neutral braking; 58 warnings on the way back |

## Mileage

| | km | mi | Basis |
|---|---|---|---|
| GPS-confirmed (tracks in this log) | 36.6 | 22.8 | the two 2026-11-08 tracks (first one incomplete) + the 11-10 commute (11.56 km) + the 11-11 Top of the World outbound (18.24 km) |
| Estimated total on the pack since 2026-10-25 | ~120 | ~74 | site odometer 25 mi as of 11-03 (owner estimate) + ~12 mi on 11-08 (owner: the tracked part was roughly a third of the day's riding) + ~7 mi on 11-10 before the commute (two untracked sessions in the ANT log, 09:12 and 12:18, each the length of the standard loop — owner to confirm) + 7.2 mi commute + 22.7 mi Top of the World return trip on 11-11 (outbound tracked, return assumed equal) |

Rides were not all tracked before 2026-11-08; from here on every ride gets a GPS track until the ESP32 odometer
exists. The site odometer (`site/landing/odometer.json`) is the owner's estimate, the table above says what is
measured.

**2026-11-09: road testing paused** — rear brake rotor runout (unsafe), waiting for the part. Episode 3 after that.

**2026-11-10: back on the road** — first ride on the Honda 43351-MBN-671 rear disc: pads bedded, no pulsing, pad track
centred on the swept face. The old disc's runout had been bad enough that the rear wheel locked and released under
braking. Not tracked (owner estimate 2–3 mi on the standard home loop; the ANT log shows two sessions, rows above).
Second Honda disc bought for the front.

**2026-11-10 evening: first real commute**, 11.6 km in two legs (GPS, rows above), tracks `10-Nov-2026-1828-to-lt.gpx`
and `10-Nov-2026-1922-from-lt.gpx`, ANT export 19:24:15. What the day's log says:
- Full throttle is **81–87 A sustained, 90.6 A peak**, at 70–80 km/h regardless of grade (climb 1.4 %, flat, descent
  −1.3 %): the controller sits on whatever caps it at ~81–82 A and the ANT 60 A warning fires on every opening.
  96 warnings since the 11-08 export (56 cell-UV, 40 discharge-OC) over roughly 40 min of riding. Nothing new
  versus 11-08, but the first day with four rides and a mid-day top-up, i.e. the daily-use pattern step 7a has to serve.
- **Cell 16 under load: 3.038 V** at 84 A (09:19), 3.046 V at 85.7 A with a 0.088 V spread (19:17:52) — new lows,
  54 mV above the ANT 2.80 V cut even with the jumper I·R in the reading. Charge-side confirmation of the jumper
  theory: at **−8.7 A (BatChgOn 13:08) cell 16 was the *highest* cell, 3.329 V vs 3.321 V min (cell 1)** → +8 mV at
  8.7 A ≈ 0.9 mΩ, the predicted sign and size. The Connection Resistance fix (≈ 0.8–0.9 mΩ on cell 16) is now
  justified from both directions; at the 14:03 end of charge (0 A) the spread was 6 mV.
- Oldest event still in the buffer: the first charge 10-25/26 ended by **cell 13 over-voltage protection at 3.651 V**
  (CellOVPP, spread 0.224 V, before the top balance) — the one protection trip in the log is a bench charge, not a ride.
  Everything since: warnings only, no trips, no temperature events.

**2026-11-11: Top of the World (Route A reconnaissance)**, 18.24 km tracked outbound, same way back untracked, ANT
export 2026-11-12 08:07:51 (`11-Nov-2026-1050-to-totw.gpx`, `SystemLog_20261112_080751.txt`). Clock note: with the
export 22 h after the ride the raw conversion lands ~5 min early, exactly the 0.4 % drift; +5 min is what aligns the
Park Ave cluster (ANT 10:36:33–10:40:49 raw) with the GPS climb (10:42:12–10:45:00). Findings:
- **Park Ave is a full-throttle climb, not a 20 mph street** (the 11-11 note in `episode3.md` saying otherwise was
  wrong and is corrected): 2.44 km at 9.7 % average with 12–18 % sections, ANT 78–91 A for ~3 min, speed falling
  from 64 km/h at the bottom to 31–45 km/h on the steep part and 17 km/h at the top. By physics the climb needs
  ≈ 4 kW at the wheel on average (220 kg, 1.4 m/s vertical, rolling + aero at 45 km/h) against ≈ 7 kW drawn from
  the pack — either the GPS grade/speed buckets exaggerate, or motor + controller efficiency at 1300–2000 rpm and
  high torque is ~60 %. Worth a look at Sevcon motor current / temperature (5100h, motor thermistor) on the next
  climb before trusting either number.
- **New ANT current record 97.1 A** (≈ 88 A real) on the way back at ≈ 11:09; 91.3 A on PCH outbound. Cell 16
  3.056–3.064 V at those peaks. Still no trips, no temperature events.
- **Regen on the descent is ≈ 9 A at most** (the BMS logged the Park Ave descent as a 2-min charge, max 9 A): the
  neutral-braking torque is low, the 40 A regen cap is nowhere near; the descent is friction brakes. Step 5a
  (regen paddle / footbrake object) is what changes this.
- **The pack is not top-balanced — the 11-10 overnight charge was ended by cell 13 over-voltage protection**
  (BatChgOn ≈ 19:27 at 8.8 A → CellVDiffWarn 0.151 V → CellOVPWarn 3.602 V → **CellOVPP cell 13 at 3.652 V,
  spread 0.221 V, min cell 25 at 3.431 V**, 166 min / ≈ 24 Ah in → recovery 10 min later at 3.45 V, spread still
  0.094 V, charge MOS back on, no restart). The first charge on 10-25/26 ended the same way on the same cell
  (CellOVPP cell 13, spread 0.224 V). The "balanced to 3 mV" of 10-27 was read after the cells had relaxed into
  the flat part of the OCV curve, where 3 mV says nothing about SOC; at the top of charge the spread is 0.22 V,
  i.e. cell 13 is ≈ 0.5–1 Ah ahead of the pack. ANT balances only above 3.40 V and the pack spends ~15 min per
  charge there before the trip → ~40 mAh of bleed per night, 15–25 nights to converge. Options in CLAUDE.md
  (Blocking). Side effect: every "full" charge now ends at ≈ 98 % by a protection trip, not by the charger's
  taper, and the coulomb counter resync to 52 Ah is doubtful.
- Jumper theory, third data point: at −8.8 A (BatChgOn) cell 16 is again the highest cell (+8 mV), cell 1 the lowest.
- Export totals: 200-event buffer now starts at 2026-11-10 19:27 (the 11-10 commute and everything before has
  fallen off — the 11-10 export is the only record of it). Since the 11-10 export: 70 discharge-OC warnings,
  61 cell-UV warnings (all cell 16), the cell-13 OV trip, 2 EndOfChg.

## From the ANT log before GPS tracking started

| Date | Events | Max A | Min cell (pos) | Notes |
|---|---|---|---|---|
| 2026-10-30 18:57 | 2 | – | – | Manual MOSFET toggles from the app (bench) |
| 2026-10-31 09:46–12:02 | 24 | 83.5 A | 3.316 V | Manual MOSFET toggles 09:46–11:21 (bench), then first rides |
| 2026-11-01 16:50–20:22 | 23 | 89 A | **3.059 V** (16) | The ~20 km solo + two-up rides of the "first spontaneous test rides" |

Totals in the log (export 2026-11-08 17:43): 43 discharge-overcurrent warnings (> 60 A), 27 cell-undervoltage
warnings (< 3.10 V, 23 of them cell 16, 2 cell 1), 0 temperature events, 0 protection trips on rides.
Export 2026-11-10 19:24 (200-event buffer, oldest = first charge 10-25): 83 discharge-overcurrent warnings, 83 cell-UV
warnings (every one with a position = cell 16), 0 temperature events; one protection trip = cell 13 OV on the first
bench charge.

## Open items from these rides

- Step 7a in CLAUDE.md: read 4623h / 2870h (what caps at ~81 A), then write 52 A or accept 78 A + hot-day validation.
  The commute makes it concrete: a 5.7 km leg = 2–4 min at 81–87 A, four times a day.
- Cell 16 reads low under load because of the 2 × AWG8 mid-pack jumper (0.7–0.85 mΩ) between taps 15 and 16, not
  because of the cell: set ANT Connection Resistance ≈ 0.8–0.9 mΩ for cell 16 (and cell 1 for the B− lead), verify
  CellVoltDiff under 80 A drops to ~0.01 V. Charge-side sign confirmed 11-10 (+8 mV at 8.7 A). Touch-check the jumper
  connector after rides (~5 W at 80 A).
- Record ANT SOC before and after each ride (column is empty so far) — on 11-10 the only SOC trace is the 1-hour
  8.8 A top-up (≈ +17 %); without before/after readings the commute's Wh/km cannot be computed.
- Confirm the two untracked 11-10 sessions (09:12 and 12:18) and their routes; GPS-track every ride, including loops.
- Name the "LT" destination in the log (a regular 5.7 km commute leg; coordinates kept out of the public log).
- Top-balance cell 13 (see CLAUDE.md Blocking); until then expect every full charge to end in a cell-13 OV trip at ≈ 98 %.
- Track the return legs too (11-11 return is approximated).
- Calibrate ANT current against a clamp meter (AF1200 8.00 A read as 8.90 A).
