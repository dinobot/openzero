# Road charging kit — J1772 public posts for a 30S LiFePO4 pack

Designed 2026-11-02. Goal: the *ability* to charge at public AC posts (J1772 Level 2, Tesla
Destination via adapter) and at any wall outlet, with nothing added to the bike. Amps are not the
goal — the kit lives in a tail bag and is used on the days the ~75 km range is not enough.

DC fast charging (CCS1 / NACS-J3400 / CHAdeMO) was rejected the same day for three independent
reasons: a 96 V pack is below the ~150–200 V output floor of DC stations (a 400 → 100 V isolated
DC-DC on the bike would be a custom build); the station side needs an ISO 15118 / DIN 70121
vehicle controller; and the Gotion cells accept 0.5C = 26 A at most, so no station can beat a
2.7 kW brick anyway. AC Level 2 is the only format worth adapting to, and it is what Zero itself
sold for the stock FX (J1772 → C14 adapter cord, see `zeromanual/wiki/Chargers.md`). The stock 2014 FX
onboard charger was two Meanwell HLG-320H-54A LED-driver supplies in series, ~650 W, plain CC/CV with
no CAN, terminated by the CCU board (`zeromanual/wiki/XMX_Platform/Unofficial_Service_Manual.md`); the
S/DS ran four of them for 1.3 kW. The AF1200 at 8 A is already faster than the stock FX charger.

## How it works

A J1772 post is not a charger. It is a contactor plus a 1 kHz ±12 V "pilot" signal. The vehicle
tells the post it is connected (9 V) and ready (6 V) by loading the pilot through a diode and two
resistors; the post then puts 208–240 V single-phase (US split-phase L1/L2, no neutral) on the
power pins. The charger is on our side, so it must accept 100–240 V.

```
 J1772 post ──plug──► [ADAPTER BOX] ──6-20 cord──► [CHARGER 100–240 V in] ──SB50──► pack
                        inlet + pilot                 30S LFP, 109.5 V CV          (bike side
                        circuit + fuses               YILEIDE E22: 11 A @120 V,     unplugged)
                                                      18 A @240 V
```

The AFU AF1200 (100–120 V input only) cannot be used at posts; the kit needs a universal-input
charger, which then also replaces the AF1200 at home and at wall outlets.

## Bill of materials

| # | Part | Spec | Notes | ≈ USD |
|---|------|------|-------|-------|
| 1 | J1772 vehicle inlet | SAE J1772-2017 Type 1, 32 A, panel mount, with dust cap | ITT Cannon, Phoenix Contact, Dostar, Duosida or similar. Needs 5 wires out: L1, L2, PE, CP, PP | 40–100 |
| 2 | Enclosure | IP65 ABS/PC box ≈ 150 × 100 × 70 mm | Inlet on one face, receptacle on the opposite | 15 |
| 3 | Output receptacle | NEMA 6-20R flange/panel mount | 240 V-only pattern so a 120 V-only device can never be plugged in by mistake | 10 |
| 4 | Pilot diode | 1N4007 (or 1N4148) | Posts verify the diode on the negative half-wave | 1 |
| 5 | Pilot resistors | 2.74 kΩ and 1.3 kΩ, 1 %, ≥ 0.25 W | Standard J1772 vehicle values: 2.74 k alone = state B (9 V), both in parallel = state C (6 V) | 1 |
| 6 | CHARGE switch | SPST toggle, panel mount, any rating | Puts the 1.3 kΩ in circuit. Off = state B = post opens its contactor | 3 |
| 7 | Line fuses | 2 × 15 A (one per hot) in panel holders, or a 2-pole 16 A DIN breaker | Protects the 14 AWG cord; posts are breakered at 30–80 A | 10–20 |
| 8 | Indicator | 240 V neon/LED panel lamp across L1–L2 | Shows the post has energised | 3 |
| 9 | Charger cord | 14 AWG SJOOW 3-conductor, 1.5–2 m, NEMA 6-20P to the charger's input | Hardwire or IEC C13/C19 depending on charger | 20 |
| 10 | Wall-outlet cord | NEMA 5-15P to the same charger input | For 120 V outlets; the universal charger derates itself | 10 |
| 11 | Charger | 100–240 V 50/60 Hz input, isolated output, 30S LiFePO4 curve: CV 109.5 V, cut-off ≈ 2.6 A (0.05C). Chosen 2026-11-03: **YILEIDE E22**, 11 A @120 V / 18 A @240 V | See "YILEIDE E22" below. Confirm input range and curve from the **manufacturer sheet or nameplate**, not a listing | to confirm |
| 12 | DC lead | 10 AWG, ≤ 1 m, Anderson SB50 in the pack's colour/key, 20 A fuse (ATO/MIDI) at the connector | SB50 is 50 A continuous | 20 |
| 13 | NACS → J1772 adapter (optional) | Lectron / TeslaTap / A2Z class, AC only | Opens Tesla Destination chargers (hotels). Not Superchargers | 50–150 |
| 14 | Lock cable | any | The charger sits on the ground for hours | 15 |

Total without charger ≈ $150–200; with charger ≈ $350–700.

## Buy instead of build

The adapter box is a stock product category, "J1772 to NEMA adapter": EVSE Adapters (US; 6-20,
6-50, 14-50, L6-30, IEC outputs, 16–40 A, $120–250, some models with a charge switch), TucsonEV
(made the "J1772 to Zero" adapter), the discontinued Zero SAE J1772 Charging Adaptor (J1772 →
C14, second-hand in the community), and unbranded $60–120 units. All contain the same diode and
two resistors. Caveats: most are fixed state C (power pins go live on plug-in and die only when
the plug is pulled, so switch the load off first); never buy a J1772 → NEMA 5-15 "120 V" adapter
— J1772 has no neutral, those return current through PE and trip the post's ground-fault
detection; a 14-50 output has an empty neutral pin, fine for a 240 V-only load. Building the box
costs $60–100 and adds the switch, fuses and indicator the cheap ones lack.

## Adapter box wiring

```
          J1772 inlet (vehicle side)
          ┌──────────────────────────┐
   L1 ────┤ L1                       │
   L2 ────┤ L2                       │
   PE ────┤ PE                       │
   CP ────┤ CP (pilot)               │
   PP ────┤ PP (proximity) — unused  │
          └──────────────────────────┘

   L1 ──[fuse 15 A]──┬──────────────► 6-20R hot
   L2 ──[fuse 15 A]──┼──────────────► 6-20R hot
                     └──[neon lamp]──┘ (across L1–L2)
   PE ───────────────────────────────► 6-20R ground, box ground stud

   CP ──►|── 1N4007 ──┬── 2.74 kΩ ──► PE
                       └── SW ── 1.3 kΩ ──► PE        SW = CHARGE toggle
```

Diode anode to CP, cathode to the resistor node. Both resistors return to PE (the inlet's ground
pin). Nothing else is needed: the post reads the pilot peak voltage, closes its contactor in
state C, and opens it when the switch goes back to state B or the plug is pulled.

Current advertised by the post (pilot duty cycle) is ignored. That is safe as long as the
charger draws less than the smallest Level 2 offer: at 2.5 kW / 208 V = 12 A, which every public
post exceeds. Do not put a > 2.5 kW charger behind this adapter without reading the duty cycle.

PP is left unconnected. On a car, pressing the plug's release button changes PP and the car
stops drawing current before the pins separate. This box has no such logic, so **the CHARGE
switch is turned off before the plug is pulled** (see procedure). Commercial J1772-to-outlet
adapters have the same limitation.

## What "smart charger" means for this pack

The term comes from lead-acid, where a charger runs many stages (bulk, absorption, float, equalise,
desulfation pulses, temperature compensation). A 30S LiFePO4 pack needs exactly three steps and
nothing else:

1. **CC** — constant current, ≤ 26 A (0.5C, Gotion table A.1.2), until the pack reaches the ceiling.
2. **CV** — hold 109.5 V (3.65 V/cell); the current tapers by itself.
3. **Stop** at ≈ 2.6 A (0.05C). No float: LFP must not be held at 3.65 V; after the stop the cells
   relax to ~3.37 V on their own.

A lab supply does the first two but not the third; a lead-acid "smart" charger does all of it wrong
(115–118 V ceiling, float, pulses). Balancing is the ANT's job (charging-only, below 10 A), so is
the cold cut-off (0 °C protection, 10 °C owner rule); no temperature compensation is needed. The ANT
(110.0 V pack / 3.65 V cell) is the backstop and must never be the normal terminator.

The only two knobs worth having beyond that: **current** (8 A for balance nights, ≤ 12 A on 120 V
outlets, 26 A fast) and a **CV endpoint** (~3.5 V/cell, ~95 %, for a bike that will not be ridden
tomorrow; the ANT balancer still runs since it starts at 3.40 V). A fixed CC/CV/stop charger such
as the AF1200 "30S LiFePO4" has neither knob and is correct for one scenario; a CAN charger has no
modes at all — it executes the voltage and current it is told every second, and the three steps
live in the controller (the ESP32). "CV / CT" on the Elcon sheet means the same CC/CV pair.

## Charger choice

Requirements, in order of importance:

1. **Input 100–240 V, 50/60 Hz**, written on the nameplate. Many 96 V / 3 kW bricks are
   220–240 V only; they do not work at wall outlets and defeat the point of the kit.
2. **Galvanic isolation** mains → output. The pack and frame float; a non-isolated charger would
   reference them to the post's wiring.
3. **30S LiFePO4 curve**: CV 109.5 V (3.65 V/cell), CC 8–12 A for the bag version, cut-off
   ≈ 2.6 A. ANT pack OV is 110.0 V and cell OV 3.65 V, so the charger must stop first.
4. **Survives load dump**: the ANT common-port MOSFET opens under full current if one cell hits
   3.65 V before the pack reaches 109.5 V. Industrial chargers handle this by design; check the
   datasheet of a budget one.
5. Weight ≤ 3 kg and some splash protection for the tail bag.

Budget branch: a second AFU AF1200 in its 220–240 V version (same 8 A curve as the home unit)
covers posts and Tesla Destination but **not** 120 V wall outlets, so the bag then holds the EU
unit and the home AF1200 stays home; check in the AFU datasheet that the EU version tolerates
the 200–208 V found at commercial sites. Carrying both AF1200s is pointless. The universal
charger below is what buys "posts and outlets" in one 2–3 kg box.

Delta-Q QuiQ 1000, 96 V model (912-9600; Zero sold it as the "Quick Charger" for 2010–2014 bikes,
`zeromanual/wiki/Chargers.md`): 945 W, max 8.5 A, max output 135 V, 85–265 V input, IP66, no fan,
isolated (stackable). Physically the ideal bag charger, but the charge algorithm is fixed at
purchase: generic "96 V" units carry lead-acid curves (~115–118 V) and Zero's units the 28S NMC
curve (~116 V, plus an enable-line circuit on the DC connector), both above the 109.5 V this pack
needs. Usable only if a Delta-Q distributor loads a 30S LFP algorithm (109.5 V CV, 2.6 A cut-off)
or with the CAN-controlled QuiQ-dci variant driven by the ESP32. The QuiQ line is discontinued
(IC series successor; check whether a 96 V IC model exists).

Candidates: TC Charger / Elcon PFC 1500–2500 in the "96 V" model with the LFP 30S curve ordered
(universal input, IP-rated, sold in the US by Thunderstruck Motors — the family the Zero
aftermarket used); Zivan NG1/NG3 96 V (230 V only in most configs, so check); generic universal-
input "96 V 10 A lithium" bricks (cheapest, datasheet mandatory). A CAN-controlled TC model can
later be driven by the speed-converter ESP32 (current taper by cell temperature / max cell from
ANT over BLE), but a fixed curve is fine for this kit.

Current vs. what a stop buys (5 kWh pack, 55 Wh/km):

| Charger | 1 h stop | 3 h stop | 20 → 100 % |
|---|---|---|---|
| 8 A / 0.8 kW | ~15 km | ~45 km | ~5 h |
| 11 A / 1.2 kW (E22 on a 120 V outlet) | ~19 km | ~60 km | ~4 h |
| 12 A / 1.2 kW | ~20 km | ~65 km | ~3.5 h |
| 18 A / 2.0 kW (E22 on 240 V / J1772, 0.35C) | ~30 km | ~95 km | ~2.5 h |
| 26 A / 2.7 kW (cell ceiling, 5–6 kg brick, needs 240 V) | ~50 km | full | ~2 h |

The 8–12 A bag version only pays off at stops of several hours (work day, hotel). That is the
intended use. The last two rows differ by about half an hour on a full charge and ~15 km per hour
of stop; that gap is what the 26 A tier costs $700, 6 kg and a CAN controller for.

## Market survey, 2026-11-02 — universal-input (120 V and 200–240 V) chargers for 30S LFP

Criteria: 109.5 V reachable, input covers 120 V *and* 208–240 V, isolated, CC/CV/stop. Prices are US
retail as listed on the day; specs are from the maker's page or sheet unless marked.

| Charger | AC input | Output | Current | Control / curve | Weight, IP | Price | Verdict |
|---|---|---|---|---|---|---|---|
| **Elcon / TC HK-J-H132-32** ("UHF 3.3 kW 132 V") | 85–265 V (EV West lists 90–260 V, 0.2–16 A) | 33–132 V | 32 A max → order/command 26 A | CAN (Elcon protocol 0x1806E5F4 / 0x18FF50E5, 250 or 500 kbps) or enable-pin fixed curve | 3.9 kg bare, ~6.2 kg as sold (13.75 lb, EV West); IP67 | $459 (evcomponents) – $899 with EVCC (EV West) | **the 26 A answer.** 3300 W @220 V, 1600 W @110 V. 12.5 V / 5 A aux output |
| **Thunderstruck TSM2500, 96 V model** (TS-CHRG-96) | 110–240 V | 48–130 V | 1–15 A | CAN (tsm2500 type in EVCC), sold with EVCC | IP66 | $555 charger / $855 with EVCC (EV West) | **the 12–15 A middle.** At 109.5 V max ≈ 1.6 kW; 20 → 100 % ≈ 2.7 h |
| **Delta-Q XV3300, 120 V model** | 85–265 V | 60–120 V, 19–34 cells | 40 A | CANopen / J1939 from a BMS, or Delta-Q algorithms; **J1772 pilot/proximity interface built in**, plus 500 W DC-DC | 7 kg, IP66/67 | OEM channel, quote | technically the whole kit in one casting (charger + EVSE interface + 12 V rail). Sales via OEM inquiry; 7 kg; needs CAN control. Keep on file, not for a one-off |
| Zivan NG1 96 V / NG3 96 V | **115 V or 230 V, ordered variant**, not universal | 96 V nominal | 9 A / 25 A | dealer-programmed profiles, CAN option | 2.2 kg / 5.5 kg | quote | fails the universal-input criterion |
| Grin Satiator HV | 100–240 V | 20–103 V | 5 A, 360 W | fully user-programmable, 20 profiles | ~1.8 kg, IP65 | ~$300 | **103 V max = 24S; cannot reach 109.5 V** |
| Danl New Energy VL9610L (brand VLDL, made-in-china.com) | 90–264 V PFC | listed 116.8 V (32S); order 109.5 V | 10 A, 1200 W | fixed MCU CC/CV, "floating or automatic cut-off" — insist on cut-off | 4.5 kg, IP65/66, fan | $139–179, MOQ 1 | **the budget 10 A universal**; maker page, still get the sheet and confirm 109.5 V + cut-off |
| **YILEIDE E22**, built to order for 30S LFP (seller conversation 2026-11-03; listings are poor, numbers are the seller's words, sheet pending) | "any", i.e. 100–240 V; 208 V behaviour to confirm | 109.5 V ordered | **11 A at 120 V, 18 A at 240 V** (~2 kW, 0.35C) | fixed CC/CV/stop, no CAN | to confirm (fan, IP, weight, DC connector) | to confirm | **chosen 2026-11-03** (see "YILEIDE E22" below). Sits between Danl and TSM2500 and beats both on current; makes the EVCC and the 26 A tier unnecessary |
| AFU AF1200 | 100–120 V (ours) or 220–240 V variants; universal version not confirmed | 109.5 V | 8 A | fixed | ~2 kg | ~$100 | ask the AFU store for an 85–265 V variant before buying anything else |
| Delta-Q QuiQ 1000 96 V | 85–265 V | fixed algorithm | 8.5 A | no 30S LFP algorithm available | IP66, fanless | used | rejected (see above) |

**Thunderstruck / Dilithium Design EVCC v3 ($270, `manuals/Thunderstruck-EVCC-v3.1.3.pdf`)** changes the
picture: it is the J1772 vehicle side *and* the charger controller in one box. It drives the pilot diode
and reads proximity (drive-away protection, stop before unplug), **measures the pilot duty cycle and
reduces the commanded charge current to what the post offers** (assumes 110 V below 18.5 A line current,
else 220 V; derates 10 % for charger efficiency), commands Elcon/TC and TSM2500 chargers over CAN
(`set maxv 109.5`, `set maxc 26`, `set termc 2.6`), and holds up to four profiles chosen by a switch —
e.g. profile 1 = 240 V / 26 A, profile 2 = 120 V outlet, linec 12. Needs 12 V (always-on + ignition);
the Elcon HK-J's own 12.5 V aux output is the obvious source (verify it is live before CAN enable).
With it the DIY adapter box and the ESP32 charging firmware are both unnecessary: inlet + EVCC +
CAN charger is a finished, documented product stack.

**Recommendation by budget (2026-11-02, superseded by the E22 decision below):**
1. ~$150: Danl VL9610L-class 10 A universal brick + ready J1772 adapter. Posts and outlets, 1 kW.
2. ~$850: TSM2500 96 V + EVCC. 15 A, IP66, pilot-aware, no firmware.
3. ~$900: Elcon HK-J-H132-32 + EVCC (EV West bundle). 26 A from 240 V, 12 A from outlets via
   profile, one charger for everything, replaces the AF1200 at home. Chosen if 26 A is wanted at all.

## YILEIDE E22 — chosen 2026-11-03

Owner talked to YILEIDE directly (their marketplace listings are useless; the conversation is the
source until the sheet arrives). They will build the E22 for 30S LiFePO4: universal input, **11 A on
120 V, 18 A on 240 V**, fixed CC/CV/stop curve, no CAN. Decision: **this is the road and fast
charger; 26 A is not pursued.** Reasons:

- 18 A = 0.35C. 20 → 100 % (42 Ah) takes ~2.5 h versus ~2 h at 26 A; an hour at a post buys ~30 km
  instead of ~45 km. That half hour is all the Elcon tier offers for 3–5× the price, 6 kg, an EVCC
  ($270) and a 12 V supply for it.
- ~2.2 kW from the mains is ~9 A at 240 V (~11 A at 208 V): any J1772 post, Tesla Destination, a
  NEMA 6-15/6-20 or a dryer pigtail. 26 A needs ~13 A at 240 V and a dedicated 20 A circuit.
- The cell ceiling is 0.5C; 0.35C keeps margin to the ANT 45 °C charge warning on a hot day.
- No CAN is no loss: the pack needs CC → CV 109.5 V → stop, nothing else ("What smart charger
  means"). CAN only mattered to make one Elcon do 8 / 12 / 26 A. With a fixed charger under 2.5 kW the
  passive adapter box above is enough and the EVCC is not needed.
- It fills the hole between Danl 10 A and TSM2500 15 A with more current than either.

**Balancing with it (corrected 2026-11-03).** The ANT balances only while a cell is above 3.400 V
(Control Start) *and* the instantaneous charge current is below 10 A. Cells sit above 3.4 V only under
the charger's CV, so with any charger the balancing window is the CV tail at 109.5 V, never the night.
AF1200: the whole tail (8 A → 2.6 A cut-off), ~30–60 min ≈ 50–100 mAh per cell per charge. E22: the
part of the tail below 10 A (10 → 2.6 A), ~15–30 min; a 120 V outlet (12 A) reaches the gate a little
earlier than 240 V (20 A). So the E22 balances about half as many minutes per cycle, not zero — enough
to hold a 3 mV spread. The **AF1200 stays for the 8 A overnight charge** because 0.15C is the kindest
daily rate, it has margin on a 15 A circuit, and it is already owned; not because the E22 cannot
balance. Ask YILEIDE whether a current selector (half current) can be fitted; if yes, one charger does
both. Do **not** raise the ANT balance-current gate above 10 A: at 0.21C the IR drop per cell is
~20 mV, equal to the 0.020 V Start Diff, so the balancer would chase resistance spread instead of
charge. To balance a pack that has drifted (≥ 1 %, ~5 h of balancer time): several full charges, or
power-cycle the charger after cut-off to get another 10–20 min of CV each time.

**120 V caveat:** 11 A out ≈ 1.35 kW in ≈ 11 A AC, right under the 12 A continuous limit of a 15 A
circuit. Use a 20 A outlet (5-20) or a circuit with nothing else on it; the AF1200 at ~7.5 A AC has
margin, the E22 does not. PFC on the input is required for that figure (confirm below).

**To get in writing before paying** (then save the sheet / nameplate photo as `manuals/YILEIDE-E22.pdf`):

1. Input range on the nameplate (100–240 V) and that output is not derated at 208 V.
2. CV = 109.5 V (3.65 V/cell) and its tolerance.
3. Cut-off current (want ≈ 2.6 A, 0.05C); **no float / trickle after the stop**; no automatic restart
   on voltage relaxation until power is cycled.
4. Galvanic isolation mains → output.
5. Survives load dump: the ANT common-port MOSFET can open at full current.
6. PFC input, fan, IP rating, weight, DC connector (Anderson SB50 preferred), input cord type.
7. Current selector option and price; warranty.

**First charge:** verify CV and cut-off with a DMM as with the AF1200, and log charger vs ANT readings
(the AF1200 discrepancy 97.44 V / 8.00 A vs 97.83 V / 8.90 A is still unresolved). Check cell NTCs
and the max cell in the ANT app during the 18 A CC phase; expect the CV tail to be short at 0.35C.

## Procedure at a post

1. Key off, kill switch, unplug the bike's SB50 from the pack (Gen4 manual: isolate the
   controller from the charger). Plug the charger's DC lead into the pack's SB50, charger still
   unpowered.
2. Start the session in the network app / RFID if the post needs it, before plugging in.
3. Plug the charger cord into the adapter box, CHARGE switch **off**, then the post's plug into
   the inlet. Pilot goes to state B; nothing is live yet.
4. CHARGE switch on → post closes its contactor → neon lights → charger starts. Check the ANT
   app: current flowing, max cell, temperature.
5. To stop: CHARGE switch off (post opens, pins dead), then pull the J1772 plug, then the AC cord,
   then the SB50. Reconnect the bike's SB50.

Only charge above 10 °C (cell datasheet / owner rule). On 120 V wall outlets use cord #10; the
charger derates on its own.

## Field notes to collect on the first uses

- Which networks accept the adapter without complaint (some posts expect a short state B
  before C; the switch gives that naturally).
- Charger input current at 208 V vs 240 V posts and at 120 V outlets.
- Whether the charger's fan can live inside the tail bag with the lid open.
- Per-hour vs per-kWh billing on the posts actually used: at 1 kW, $1.50/h is $1.50/kWh.

## Not done on purpose

- No proximity logic, no duty-cycle reading, no microcontroller: a switch does the job.
- No on-bike inlet or drive interlock: the SB50 unplug is the interlock.
- No 26 A charger at all (owner 2026-11-03: the E22's 18 A is enough, see "YILEIDE E22"). If a 26 A
  charger is ever bought anyway, the candidate is the **Elcon
  HK-J-H132-32** (`manuals/Elcon-HK-J-H132-32-verA.pdf`, 2015-04-11, from elconchargers.com; request a
  current one): 85–265 V
  in, 33–132 V / 32 A out, 3300 W at 220 V / 1600 W at 110 V, IP67, 3.9 kg bare, Anderson 50 A
  output, 12.5 V / 5 A aux, CAN-controlled (125/250/500 kbps, output stops on CAN loss) or a
  factory-fixed curve with an enable pin. Order notes: limit must be 26 A, not 32; on 120 V
  outlets command ≤ 12 A (1600 W draws ~14 A AC, over the 12 A continuous limit of a 15 A
  circuit); CAN version lets one charger do 8 A nights (ANT balancing), 26 A from 240 V, 12 A
  from outlets, and temperature taper from ANT over BLE via the speed-converter ESP32. Fixed-curve
  version is simpler but then the AF1200 stays for 8 A nights. 26 A is ~3.1 kW from the mains, which no 120 V outlet can supply (80 % rule:
  1.4 kW on 5-15, 1.9 kW on 5-20). It needs a 240 V circuit (NEMA 6-20, or a dryer 14-30 /
  range 14-50 pigtail — the same single-phase split-phase supply the posts deliver) and a 5–6 kg
  brick such as a TC/Elcon PFC 3300 "96 V". Home overnight charging at 8 A is the better daily
  regime anyway: ANT balances only below 10 A, and 0.15C is the kindest rate for the cells.
