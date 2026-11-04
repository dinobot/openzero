# OpenZero

**A 2014 Zero FX electric motorcycle, rebuilt to run without the manufacturer.**

The proprietary layer of the bike (Zero's MBB vehicle controller, Zero's BMS, the encrypted CAN that tied
them together, the dash, the cloud app) has been removed. What remains is the industrial hardware Zero built
the bike around: a Sevcon Gen4 motor controller, a PMAC motor, a contactor, a frame. On top of that sits a
home-built 96 V LiFePO4 pack with an off-the-shelf smart BMS. Everything in the power path can now be
inspected, measured, repaired and replaced with a multimeter, a wrench and a CAN adapter.

> The machine is not dead. The support contract is.

This repository is the engineering notebook of that conversion: decisions, measurements, wiring, controller
configuration, the battery enclosure model, and an offline mirror of the community Zero wiki. It is written
so that the next owner of a dead Zero can repeat it.

---

## Why

Zero's 2013–2016 bikes die one way: the battery "monolith" ages, the BMS inside it stops cooperating with
the vehicle controller, and a mechanically perfect motorcycle becomes scrap because the two proprietary
boxes no longer talk. The motor, the controller, the chassis are all fine. OpenZero removes the dependency
instead of replacing one black box with another.

The result is a slower motorcycle than stock (see *Numbers* below), owned and understood completely.

## Status (late October 2026)

Done:

- Sevcon Gen4 rewired from scratch and running standalone: key switch from the traction bus (no 12 V
  system needed for logic), contactor with external precharge, forward/killswitch/inch inputs, hall throttle.
- Controller configured over CAN with Sevcon DVT: reaches NMT Operational, DSP402 Operation Enabled,
  motor runs on throttle.
- 30s1p LiFePO4 pack built in a riveted sheet-aluminium box, ANT smart BMS commissioned, cells top-balanced
  to 3 mV, first full charge done.
- Battery current limit strategy, voltage cutbacks and BMS protection thresholds derived from the cell
  datasheet, not from the BMS defaults.

In progress / next:

- Riding on the pack and the thermal validation that decides whether the current limit goes from 52 A to 78 A.
- Speed signal for the gauge (ESP32 reading motor RPM from the Sevcon CAN bus).
- Saving all controller parameters to NVM, disabling the RPDOs that used to come from the removed modules,
  NMT auto-start.

What this is not yet: a proven, durable vehicle. The first rides prove that it moves. Reliability, weather
sealing and long-term cell behaviour are open questions, and the notebook says so where it matters.

## Architecture

```
 Stock 2014 FX                              OpenZero
 ─────────────────────────────              ─────────────────────────────
 Zero monolith (NMC, Zero BMS) ──CAN──┐     DIY 30s LiFePO4 pack
 Zero MBB (vehicle controller) ──CAN──┤     ANT smart BMS (MOSFET disconnect, Bluetooth app)
 Zero CCU / dash / app         ──CAN──┤           │ B+ / P−
                                      ▼           ▼
                                Sevcon Gen4 ◄── key, FS1, forward, inch, hall throttle (direct wires)
                                      │           ▲
                                      ▼           └── CAN: DVT laptop; ESP32 speed converter
                                 75-5 motor
```

Three principles drove every choice:

1. **No proprietary dependency in the power path.** Anything between battery and motor must have a public
   manual or be a passive part.
2. **Manufacturer documents only.** Cell, controller, BMS and gauge are specified from datasheets in
   `manuals/`. Marketplace listings were wrong on the cell dimensions, C-rate and cycle life and are not
   used as sources.
3. **Static, conservative limits over clever software.** No BMS-to-controller bridge: the Sevcon enforces a
   fixed battery current limit and voltage cutbacks, the BMS protects the cells outside that envelope.
   A cheap bike that has not yet moved does not need weeks of firmware.

## Numbers

| | Stock 2014 FX | OpenZero |
|---|---|---|
| Pack | 28s NMC, ~102 V, 5.7 kWh | 30s1p LiFePO4 (Gotion 52 Ah prismatic), 96 V, 5.0 kWh |
| Battery current, continuous | ~125 A | 52 A (1C), 78 A ceiling after hot-weather validation |
| Continuous power | ~12.7 kW | ~5 kW (7.5 kW at 78 A) |
| Launch torque | phase-current limited | same: unaffected by the battery limit |
| Realistic cruise | highway | ~80 km/h at 52 A, ~95 km/h at 78 A |
| Pack mass | ~33 kg | ~32 kg |

The power ceiling is a cell choice, not a platform limit: the controller and motor are untouched, and a 2p
string or higher C-rate cells would restore stock-level power. For a daily commuter on a chassis that is
not pleasant above ~95 km/h anyway, 1C LiFePO4 was judged the right trade: cheaper per kWh, 3000+ cycles,
and far more forgiving of a self-built, non-welded pack than NMC.

## Does this apply to other Zeros?

Yes, to every Zero built around a Sevcon Gen4: FX, FXS, FXE, S, DS, SR and DSR from 2013 onwards,
including the FX/FXS/FXE still sold new in 2026 (Zero's "550 amp 3-phase controller" is that Sevcon; "Cypher II"
is the name of the dash/MBB operating system, not of the controller). The 35-pin connector, the CANopen
object dictionary and the DVT workflow are the same across controller sizes. The S/DS battery bay is larger
than the FX bay, which makes a 2p pack realistic there.

It does **not** apply to the FST platform (SR/F, SR/S, DSR/X and newer bikes on that base), where the
inverter is Zero's own design with no public documentation. Removing the proprietary layer there means
replacing the controller, which is a different project.

Open point before claiming "as-is" for current-production bikes: confirming that a late Gen4.5 unit with Zero
firmware opens in DVT the same way the 2014 unit did.

## Repository map

| Path | What |
|---|---|
| `CLAUDE.md` | The full engineering notebook: wiring table, DVT object reference, BMS settings as configured, battery analysis, decisions with dates and reasons. Long and detailed by design. |
| `manuals/` | Manufacturer documents that count as specification. **Not in the repository** (copyrighted); see *Documents you need* below. |
| `site/` | The public site, openzero.u65.info: landing page with the manifesto and odometer, and the web version of the mirrored wiki (MkDocs). Built by GitHub Actions. |
| `battery_box/` | Enclosure work: `SPEC.md` (requirements), `enclosure.py` (parametric 3D-printable model, build123d), `ALU_BOX_RU.md` (the riveted aluminium box actually built), STL outputs and renders. |
| `charging/` | Public-charging notes: `road_kit.md` — a J1772 adapter box (pilot circuit, BOM, procedure) and charger selection for the 30S LiFePO4 pack; why DC fast charging was rejected. |
| `zeromanual/` | Offline Markdown mirror of the community "Unofficial Zero Manual" wiki, recovered from the Wayback Machine. Stock-bike mechanical, motor, belt and harness facts transfer; MBB/app behaviour does not. Start at `zeromanual/INDEX.md`. |

## Safety

This is a 96–110 V DC system with a 52 Ah pack behind it. The notebook records what was done and why, not
what is safe for you. In particular: the BMS does not enforce the cell C-rate (the controller limit does);
a fully assembled pack can deliver thousands of amps into a dropped tool; the charger must be isolated from
the controller while charging; and a sealed box without a drain and breather collects condensation. If any
of these sentences is new to you, read the Sevcon manual and the cell datasheet in `manuals/` before the
wiring tables.

## Companion video series

The build is also documented as a video series on YouTube: [Electric Savage](https://www.youtube.com/@ElectricSavage).
Episode 1 covers the battery build; Episode 2 covers fitting the pack and the first ride.

## Website

<https://openzero.u65.info/> — the manifesto, the odometer (miles ridden on the open pack, updated by hand
from `site/landing/odometer.json`) and the web version of the Unofficial Zero Manual at
<https://openzero.u65.info/manual/>. How it is built: `site/README.md`.

## Documents you need

The engineering notes cite manufacturer documents by page and table. They are copyrighted and are not
redistributed here; put them in `manuals/` (git-ignored) under these names:

| File | Document | Where |
|---|---|---|
| `Gen4 Product Manual V3 4.pdf` | Sevcon Gen4 Product Manual, 177/52701 V3.4 | Sevcon / BorgWarner dealer documentation; V3.3 circulates widely online |
| `ifp52.pdf` | Gotion (Hefei Guoxuan) IFP28148115A-52Ah cell specification Q/GX 030-2019, rev 2021-01-29 | from the cell seller on request |
| `ANT-BMS-APP-User-Manual-English.pdf` | ANT BMS app manual | antbms.vip |
| `Ant BMS Smart Bluetooth Relay ... User Manual.pdf` | ANT relay-line manual (manuals.plus compilation), partly applicable | manuals.plus |
| `CT-22-MANUAL.pdf` | CT-22 gauge parameter instructions | from the gauge seller |
| `Elcon-HK-J-H132-32-verA.pdf` | Elcon HK-J series 3.3 kW sealed CAN charger specification, 2015-04-11 verA | elconchargers.com (public download) |
| `Thunderstruck-EVCC-v3.1.3.pdf` | Thunderstruck Motors / Dilithium Design EV Charge Controller v3 manual | thunderstruck-ev.com (public download) |
| `Delta-Q-XV3300-presentation.pdf` | Delta-Q XV3300 3.3 kW charging system product presentation | delta-q.com distributors (public download) |
| `14fx.pdf` | Zero Motorcycles 2014 FX parts catalogue (exploded views with part numbers) | AF1 Racing parts lookup, `14FX.pdf` (public download; linked from `zeromanual/wiki/Exploded_Views.md`) |

## License

OpenZero exists so that a machine stays repairable by whoever owns it. The licences are chosen to keep it
that way: anyone may use and build on this work, and whatever they build on it stays open.

- **Code** (`battery_box/enclosure.py`, `zeromanual/tools/`, `site/`, future firmware):
  [GPL-3.0-or-later](LICENSE).
- **Text, documentation, drawings, models and their outputs** (`README.md`, `CLAUDE.md`, `battery_box/*.md`,
  STL/STEP files, the website text): [CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0).
- **`zeromanual/`** is community content from zeromanual.com, reproduced for preservation with attribution.
  The original wiki carried no licence; nothing here grants one. It will be removed on request of its authors.
- Manufacturer documents are not part of the repository (see *Documents you need*).

Not affiliated with or endorsed by Zero Motorcycles. Zero, FX and other names are trademarks of their owners
and are used only to identify the subject.
