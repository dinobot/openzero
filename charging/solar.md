# Solar charging PoC (started 2026-11-07)

Owner's question: used panels from an OfferUp listing — can the sun charge the pack in a day?

## Sizing (30S LFP, 5.0 kWh nominal, ~4.3 kWh usable 20 → 100 %)

| Need | Energy into the pack | Panel power for one SoCal day (≈ 5 peak-sun hours × 0.8 system factor = 4 kWh per kW) |
|---|---|---|
| Daily use (20–25 %, ≈ 1.1 kWh) | ~1.2 kWh | **~300 W** |
| Full charge 20 → 100 % | ~4.5 kWh | **~1.1–1.3 kW** (summer; winter ≈ half) |

Charge current at 1.2 kW is ~11 A at 105 V — far below the 26 A (0.5C) cell limit and the ANT 60 A charge trip.

## The real question is the charge controller, not the panels

The pack needs CC → CV 109.5 V → stop (see "Charging" in CLAUDE.md). Mainstream MPPT controllers (Victron, EPever,
Renogy) stop at 48 V batteries. Options:
1. **96 V MPPT charge controller** (Chinese "MPPT 96V" units for e-scooter/e-trike packs, 10–30 A, PV input up to
   150–200 V Voc, LFP profile with settable CV). Cheapest PoC; quality and the end-of-charge behaviour (float or stop?)
   must be checked — a float at 109.5 V is not acceptable for LFP, set CV ≈ 108 V or rely on the ANT 110.0 V backstop
   only as a backstop.
2. **PV → the on-bike charge port** through the series diode (input-only port, ~0.8 V drop): fine, the controller output
   goes to the SB50 like any charger; negative on P− so the ANT can stop it.
3. PV → microinverters → AC → AF1200: does not work off-grid (microinverters need a grid to sync).

PV string for a buck MPPT into a 96–110 V pack: Vmp must stay > ~115 V on a hot panel → **4 × 60-cell** (Vmp ≈ 120–128 V,
Voc ≈ 150 V) or **4 × 72-cell** (Vmp ≈ 150 V, Voc ≈ 190 V, controller must take ≥ 200 V); 3 × 72-cell (Vmp ≈ 111–120 V)
is marginal in summer heat. A boost-type 96 V controller would allow 2–3 panels but is rarer.

## What to read off a listing before buying

Panel wattage, Voc, Vmp, Isc, cell count (60 / 72), quantity, condition (microcracks, delamination, hail), price per
watt (used ≤ $0.20–0.30/W is normal), frame/mounting, and whether they are matched (same model for a series string).
OfferUp pages cannot be fetched from here — paste the listing text.

## The OfferUp panels (owner 2026-11-07): 250 W, Voc 37.44 V, Isc 8.8 A

Voc/37.44 → a 60-cell poly panel (Vmp ≈ 30.5 V, Imp ≈ 8.2 A, ~1.65 × 0.99 m, ~18 kg, 2012–16 era). Fit:
- **5 in series** is the clean string: 1,250 W, Vmp ≈ 152 V at STC, ≈ 128 V at 65 °C cell (−0.4 %/K), Voc ≈ 187 V at
  25 °C and ≈ 200 V on a 10 °C morning → the controller's PV input must be rated **≥ 200 V**. ≈ 5 kWh on a summer day,
  ~12 A into the pack — a full charge in a day.
- 4 in series (1 kW) works at the start of charge (pack 97–100 V) but on a hot day Vmp sags to ≈ 102 V, below the
  109.5 V CV: the MPPT then runs off-MPP between Vmp and Voc (≈ 126 V hot) at a fraction of the power for the last
  part of the charge. OK for a PoC, inefficient; 150 V-class controller suffices. ≈ 4 kWh/day.
- String current is the panel's 8.8 A Isc; controller output ≈ 12 A → a **96 V / 20 A MPPT** is enough.
- Price check: used 250 W poly is typically $40–60 each (≈ $0.2/W); 5 panels ≈ 8 m² ground mount at home.
Controller search terms: "MPPT solar charge controller 96V lithium 20A", PV ≥ 200 V, settable CV (set ≈ 108 V) and a
real charge stop (no float); units of the MakeSkyBlue type advertise 96 V battery support — verify the max PV voltage
and the LFP end-of-charge behaviour in the manual before buying.

## Minimal off-grid: panels straight into the diode port, no controller (owner 2026-11-07)

Direct coupling works only if the string's I–V curve does the terminating, and that depends on panel temperature
(Voc ≈ −0.3 %/K, Vmp ≈ −0.4 %/K; cells in sun run 45–65 °C). Pack during charge: 97 → 109.5 V.

| String | Voc 25 / 45 / 65 °C | Vmp 25 / 45 / 65 °C | Into a 100–109 V pack |
|---|---|---|---|
| **3S** (750 W) | 112 / 105 / 99 V | 92 / 84 / 77 V | Self-limiting: current tapers to zero as the pack nears the string Voc (≈ 105–108 V), ANT never needed, balancing window (< 10 A, > 3.4 V) hit naturally. But nothing at all in summer midday heat (Voc 99 V < pack), ≈ 300–500 W in cool conditions → ~1–2.5 kWh/day: covers daily use, never a full charge |
| **4S** (1 kW) | 150 / 141 / 132 V | 122 / 112 / 102 V | Charges in any weather at ≈ 6–8 A, but never stops: at 109.5 V the string still pushes 5–8 A, so the ANT cell-OV cut (3.65 V, recovery 3.45 V) becomes the terminator and toggles at the top — the BMS-as-charger case rejected for daily use. Acceptable once for a demo with the app open and a hand on the plug |
| 5S | 187 V+ | 152+ | Only with a controller |

The diode on the port already does the classic blocking-diode job (no reverse flow at night). One string → no string fuse
needed; add a DC-rated switch or just mate/unmate the SB50 (hot-plug rated 50 A). Charge only above 10 °C (ANT cuts
charge at 0 °C anyway).

**One cheap part makes 4S correct without MPPT:** a CC/CV step-down module (eBay "DC-DC buck constant current constant
voltage 200 V 1800 W" class, $30–60) between string and port, set to CV 105–108 V (3.5–3.6 V/cell) and CC 8 A. Not
MPPT (the panel sits wherever the demanded current puts it), but it caps current and tapers to ~0 at CV instead of
tripping the BMS. Verdict: 3S direct = safe seasonal trickle; 4S + CC/CV module = the minimal honest PoC; MPPT 96 V
controller + 5S = the "full pack per day" build.

## Controller shortlist (researched 2026-11-07)

No mainstream brand makes a 96 V-battery MPPT: Victron, EPever, Renogy, Morningstar, Midnite stop at 48 V (Midnite
Classic 72 V). What exists:

| Unit | Price | PV input | Battery / settings | Verdict |
|---|---|---|---|---|
| **MakeSkyBlue 96V 30A V118** (makeskyblue.com, Amazon B07KP9QDHJ) | $85–90 | Voc 120–190 V (max 200), ≤ 3 kW | "96 V only" manual mode, absorption and float settable 96–136 V for lithium, 3-stage with float, fixed OVP 117 V, fan, IP21, −20…55 °C | Cheapest manual-mode unit → **4S string** (5S Voc ≈ 196 V on a cold morning exceeds 190). Reputation is poor: Syonyk's teardown (sevarg.net 2018) — random MPP misses needing power cycles, display 0.2 V off, a unit that ignored its lithium max-voltage setting; diysolarforum: 2 of 3 failed, a 96V 45A faulted after a year. Usable only because the ANT (110.0 V pack / 3.65 V cell) and the diode port stand behind it |
| SOLAFANS 96V 45A (Amazon B095YM1S74) | $170 | 180 V max, 4.5 kW | 48/96 V auto, 60/72/84 manual, lithium type, "dead battery reactivation", CE/PSE | 4S only (180 V); manual not found online — settable CV and persistence unverified |
| POWLAND / SOGTICPS / EcoSolLi 120A 12–96 V auto, PV 230 V | $230–295 | 230 V → 5S possible | **auto-detect only**, 3-stage, custom settings **do not survive a power disconnect** (review) | Rejected: auto-detect of a 97–110 V LFP pack plus volatile settings is exactly the wrong failure mode |
| Xindun 96V 50A (manufacturer, Shenzhen) | quote | 300 V max, MPPT 120–240 V | lead-acid defaults (113.6 / 110.4 V) adjustable | Alibaba route, untested |
| **AERL CoolMax SRX HV 300/30-120** (Australia) | $1,900–2,300 | 600 V, MPP range 215–540 V → ≥ 9 panels in series | battery 90–170 V, pro-grade, ground-fault detection | The only serious 96–120 V unit; not for a PoC |
| Genasun GVB-8 custom voltage (boost) | ~$200/unit | 8 A / 350 W input per unit | factory-programmed CV | too small; several in parallel is silly |

**Wiring catch found while shortlisting:** every MPPT powers itself from the battery terminals and reads the pack to
start (and to auto-detect). Through the on-bike port's series diode it sees **0 V** and will not start — same issue
as flagged for the E22 charger. For the PoC connect the controller to the **pack's SB50 directly** (bike side
unplugged, as in the road-kit / backup-power procedure); the controller's own blocking diode handles night reverse
flow. If the bike port must be used, the "dead-battery reactivation" units (SOLAFANS) are the only ones claiming to
start into 0 V, and that is not the same as detecting the right voltage bin.

**Settings for whichever unit (30S LFP):** battery type lithium/user, system voltage 96 V manual, absorption (CV)
108.5–109.0 V, absorption time ~30 min, float 105 V (3.5 V/cell; keeps the balancer window open at tiny current),
equalisation off, temperature compensation 0, OVP ≤ 112 V if settable. Controller CC = the 8.8 A string anyway.

**Recommendation for the PoC:** MakeSkyBlue 96V 30A + 4 × 250 W in series, connected at the pack SB50, with the ANT
app open for the first full cycle to confirm it really holds 109 V and drops to float. Budget ≈ $90 + 4 panels. If
"full pack per day" is wanted later, the honest step is not a bigger cheap controller but the AERL class, which is
not worth it against the E22 charger on a J1772 post. The CC/CV buck module (previous section) remains the
no-firmware alternative at $30–60.

Not bought (2026-11-07). Grid energy for a full pack costs ≈ $1.25; the PoC is about independence/camping (see
`backup_power/README.md`), not savings.
