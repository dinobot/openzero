# Street mode — turning the 2014 FX into a road bike

Started 2026-11-04. "Street mode" is the owner's term for an FXS-style setup of the 2014 FX: lower
seat height, road-oriented suspension, and whatever else makes the bike comfortable for daily
commuting at the owner's ~60 mph ceiling. Each section records what was researched, the sources, and
the open measurements. Only manufacturer documents and the parts catalogues in `manuals/` count as
specs; forum posts are experience reports and are marked as such.

Zero's own answer to this question was the FXS (2016+): same XMX frame family, 17 in wheels, lowered
Showa suspension (forum report: the FX-to-FXS suspension difference was an internal spacer in the
shock, so an FXS converts to FX travel easily) and a lower seat. The 2016 FXS parts catalogue is in `manuals/16fxs.pdf` and is the reference for what Zero
changed.

## Rear shock and lowering (researched 2026-11-03)

### Stock part and geometry

| | 2014 FX | 2015 FX / 2016 FXS |
|---|---|---|
| Shock | 22-06105 Fastace BFA57RC, piggy-back, preload / compression / rebound | 22-05879 "FX shock 40 mm" Showa |
| Swingarm | 21-05849-1 | 21-07748 (superseded by 26-08068) |
| Frame | 20-06499 "XMX frame assembly 14MY" | 26-08080 "frame XMX complete assembly" |
| Upper shock bolt | 90-07295, M10 × 70 mm | 90-05711, M10 × 60 mm (same as lower) |
| Lower shock bolt | 90-05711, M10 × 60 mm | 90-05711, M10 × 60 mm |

Sources: `manuals/14fx.pdf`, `manuals/15fx.pdf`, `manuals/16fxs.pdf`, view ZEV0006 "Rear Suspension".

Fastace BFA57RC dimensions (zeromanual "Rear Shock Specifications", community-measured):
- 319 mm eye-to-eye, eye body 17.9 mm, bushing width 31.95 mm top and bottom, M10 bolts
- spring 475–585 lb/in, 181 mm long on the shock at minimum preload
- reservoir clocked 242° clockwise from 12 o'clock, reservoir reaches ~90 mm left of the shock centreline

Showa 22-05879 (zeromanual, from the Zero service data): free length 320 ± 2 mm, max 320.5, min 246 mm,
stroke 74.5 mm, spring 73.6–82.4 N/mm (≈ 420–470 lb/in), rebound 12 clicks, compression 9 clicks.

**No linkage.** The FX shock bolts directly between the frame centre tube and the swingarm; the
parts list has no link or rocker. Lever ratio shock : axle ≈ 1 : 2, so every 10 mm taken out of the
shock lowers the rear ≈ 20 mm. Lowering therefore means a shorter shock (or a shorter extension stop
inside it); there is no lowering-link option.

### Is the 2015+ Showa a bolt-on?

Not documented, and not useful for lowering:
- Length is the same (319 vs 320 mm), so it changes damping quality, not ride height.
- Zero changed the frame, the swingarm and the upper bolt (70 → 60 mm) in the same model year, so
  the upper eye or the frame lugs differ by ~10 mm. Expect spacer/bushing work, not a straight swap.
- Nobody on the forum or zeromanual reports having done it on a 2013–14 FX.

Verdict: only worth it as a damper upgrade if the Fastace fails and a used Showa is cheap; measure
the eye and lug widths first.

### Lowering options, cheapest first

1. **Internal spacer in the stock Fastace.** Forum report (2013 FX, "Has Anyone Lowered Their Zero
   Yet?", topic 4786): a shock shop fitted a nylon spacer of 3/4 in on the shaft, limiting extension
   by 3/4 in → ~1.5 in (38 mm) lower at the wheel. Shock must be opened and re-charged with nitrogen,
   so it is shop work. Travel is lost one-for-one with the spacer.
2. **Ikon 3610-1104.** The only Zero entry in Ikon's application list, made for the 2016 FXS (Showa
   era). Ikon offered a version lowered 2 in with a matched spring (forum, topic 6640, 2016 FXS).
   For the 2014 the eye widths and the 70 mm upper bolt must be checked against the table above.
   zeromanual's experience with the Ikon for the S: spring sits too wide at the top and must be
   compressed to fit; later orders may be fixed.
3. **Made-to-length shock** (Wilbers, YSS, TFX, EMC, Öhlins): specify eye-to-eye ≈ 300 mm for a
   ~40 mm drop, rider + bike weight, eye/bushing widths from the table. The only route that lowers
   without losing damping quality. Wilbers lists a "Zero" fitment but their length history is
   unreliable (zeromanual); send dimensions, do not trust the catalogue entry.
4. **Fox Podium RC2 "Zero FX rear shock by Fox".** Sold by Zero as an accessory for the 2013–2014 FX
   (37 mm body, 5/8 in DLC shaft, dual-speed compression, rebound, preload). Stock height, so a
   damper upgrade, not a lowering part. Still listed on zeromotorcycles.com without price; used only.
5. **Generic 320 mm shocks** (pit-bike / Chinese dual-sport, M10 eyes) match the length but nothing
   else is known to fit; the same approach on the S (260 mm) rode "like a trampoline" (zeromanual).
   Spring rate needs to be in the 475–585 lb/in class. Only with the shock in hand and a spring change
   budgeted.

Complementary measures (zeromanual "Ergonomics"):
- Front: slide the fork tubes up in the clamps by up to 1 in to keep the geometry level.
- Seat: Zero offered an unlisted "low seat accessory" for the 2013 FX, −2 in (41 mm); carving the
  stock foam gives ~1 in. Corbin's Zero seat narrows the front for easier reach.
- Forum threads to read when the archive is back (electricmotorcycleforum.com is offline, Wayback was
  temporarily offline on 2026-11-03): topics 4786 and 6304 (lowering), 6640 (2016 FXS on Ikon, −2 in),
  6721 ("30 mm rear lowering, the hard way, no loss of travel").

### Open measurements before buying anything

- Upper and lower eye widths and frame/swingarm lug spacing on the 2014 (explains the 70 vs 60 mm bolt).
- Spring outer diameter clearance to the frame and controller heatsink (the S Ikon and Yamaha R3
  shocks failed on spring width, not length).
- Reservoir position: the Fastace reservoir is clocked 242°; a shock with a different clocking may hit
  the battery box or the Sevcon.
- Rider sag with the current pack (~32 kg, heavier than the stock ZF3.3 module) before deciding how
  much to lower; the extra mass may already have taken part of the drop.

## Wheels: 21/18 → 18/18 (researched 2026-11-05)

### Stock wheels across the 2014 family (`manuals/14fx.pdf`, `14ds.pdf`, `14s.pdf`, `15fx.pdf`, `16fxs.pdf`, "Wheel Assy")

| | 2014 FX | 2014 DS | 2014 S | 2015 FX | 2016 FXS |
|---|---|---|---|---|---|
| Front wheel | 1.60 × 21 wire, 36 spokes (forum), IRC GP-110 3.00-21 51S | 2.15 × 19 wire, 4.00-19 tube | 3.00 × 17 cast, IRC RX-01 110/70-17 | 1.85 × 21 wire (23-08067) | 17 cast, 320 mm rotor |
| Front axle / spacer | 23-06388 (20 × 232 mm) / 23-02590 | same / same | same / same | 23-07491 hollow | 23-07491 hollow |
| Front rotor / caliper | 240 mm fixed, M6 × 15 bolts / Nissin 25-04164 | 313 mm floating 25-03541 / Nissin 25-04164 | same as DS | 240 mm 25-08063 / J.Juan | 320 mm / J.Juan |
| Rear wheel | 2.50 × 18 wire per catalogue (upgrade kit 12-08076), IRC GP-110 4.10-18 59S — **this bike: 2.15 × 18 rim with a 120/80-18** (owner 2026-11-08) | 3.00 × 17 wire, 5.00-17 tube | 3.50 × 17 cast 23-04859-1, RX-01 140/70-17 | 2.50 × 18 wire | 3.50 × 17 cast "SDS rear" |
| Rear axle / left spacer | 23-08032 / 23-05195 | 23-08032 / ? | 23-08032 / 23-05195 | 23-08032 | 23-08032 |
| Rear pulley / belt | 132T 30-04051 / 220T × 14 mm 30-08084 | same | same | same | same |

What the catalogues say about bolt-ons: the 2014 FX, DS and S share the front axle, axle spacer, rotor bolts and
caliper, so the DS 2.15 × 19 and S 3.00 × 17 front wheels are catalogue-level swaps (keep the FX 240 mm rotor and
its fork-leg caliper mount; the DS/S 313 mm rotor needs their caliper bracket). All five bikes share the rear axle
and the 132T pulley, and Zero itself put the "SDS" 3.50 × 17 cast rear on the 2016 FXS swingarm — so the 2014 S
3.50 × 17 rear is a near bolt-on (right spacer 20-07324 vs FX 23-04853 differs). Those are the 19/18 and 17/17
routes; this section is about keeping the 18 rear and matching the front.

### 18 in front: relace the stock hub

No one sells an 18 in front wheel for the FX, and there is no need to: the front hub, bearings, axle, spacers,
240 mm rotor and caliper all stay; only rim and spokes change. The 2015 FX front is 36 spokes, 9-gauge heavy sets
have been ordered from Buchanan's Spoke & Rim (Azusa, CA) for the FX (forum topics 10515, 11891) — count the
holes on the 2014 hub before ordering, the catalogue does not state it.

- **Rim: Excel Takasago 18 × 2.50, 36H** (part FFK422 black / FFS422 silver, $190–250 at Summit Racing, Chap Moto,
  Speed Addicts, Hooligan Racing). It is the standard enduro *rear* rim size, so it is always in stock, and it is
  the same size as the FX rear rim. 2.50 is the measuring rim for 100/90, 110/80 and 110/90 and is permitted for
  120/80, so every tyre below fits; 2.15 (18 × 2.15 36H, ~$180–215) only if the choice is fixed on 100/90-18.
  (The bike's own rear rim is 2.15 and carries a 120/80-18 — permitted range for 120/80 is 2.15–3.00.)
  Wider than 2.50 on a front hub is pointless at this bike's speeds. Spoke set: Buchanan's calculates the
  length for the hub/rim/offset; have them lace and true it (they list labour), or DIY with a truing stand.
- **Reusing the stock spokes (owner's question 2026-11-07): no.** Going 21 → 18 shortens every spoke by roughly
  35–40 mm (half the rim-diameter change, exact value from ERD and cross pattern), so the old spokes would need cutting
  and re-threading. Spoke threads are *rolled*, not cut: a die-cut thread on a 3.2 mm spoke (Zero "1065 3.2" front
  spokes) removes the cold-worked surface and leaves a stress riser at the most loaded spot, on a wheel that carries a
  32 kg pack and already has a spoke-breakage history on the forum (topic 10515). Motorcycle-gauge rolling heads exist
  only at spoke makers; bicycle rollers stop at ~2.3 mm. And length is not the whole problem anyway: the rim's nipple
  holes are drilled at angles for the hub it was made for (an Excel 18 × 2.50 is drilled for KTM/Husqvarna rear
  hubs), the nipple hole size must match the spoke gauge (10 g stock vs the 8–9 g the rim expects), and the spoke
  elbow/flange fit stays as it is. Buchanan's solves all three at once: they drill the rim to the Zero hub geometry,
  pick nipples, and roll a spoke set to measured lengths (~$100–150 for 36, the cheapest part of the job; the forum's
  FX owners went to their 9 g heavy sets). Send them: hub flange spoke-hole PCD on both sides, flange offsets from the
  hub centre, spoke-hole diameter, cross pattern (count on the stock wheel), rim ERD and offset or the rim itself.
- **DIY lacing vs shop (owner 2026-11-07).** With a custom spoke set the lacing itself is first-timer work: photograph
  and mark the stock pattern (inside/outside spokes per flange, cross count), measure rim offset to the hub seal faces
  before unlacing, lace, then true on the bike's own fork (zip-tie pointer) to ≤ 1 mm lateral/radial and bring the
  tension up evenly in rounds; 3–6 h. The parts that go wrong are offset and uneven tension, and uneven tension is
  how FX spokes break. Buchanan's lists lace-and-true labour (~$75–150) and is in Azusa, CA: sending them the bare hub
  (or dropping it off) returns a drilled rim, rolled spokes and a trued wheel in one go. Without a spoke set there is
  nothing to lace; a shop orders the same set. Verdict: let Buchanan's build it; DIY only as a skills project, and
  then have a shop check tension before the first ride.
- **Rim sourcing (2026-11-07):** no need to buy one. Buchanan's (805 W 8th St, Azusa CA 91702, (626) 969-4655) makes
  its own spokes, nipples and rims (Sun rims since 1987), stocks undrilled chrome-steel and aluminium rims and drills
  them on a fixture to the customer's hub at any spoke angle; "bring a hub, a rim, or a wheel" (Motorcycle Classics
  profile and lacing-process article). So: bring the bare FX front hub, ask for an 18 × 2.50 36H aluminium rim drilled
  to it, spokes and lacing. Buy an Excel FFK422 yourself only if that exact rim matters cosmetically — and then as
  undrilled stock or with the caveat that its KTM drilling is a compromise.
- **Spec to give Buchanan's (owner asked for "everything lightest", 2026-11-07): no.** Spokes: the heavy set (their
  9 g stainless, the one FX owners switched to after breakages, topic 10515), brass nipples, not a light 10 g set —
  the bike is heavier than stock (32 kg pack), rides two-up, and the fork still has 230 mm of dirt travel. Rim: a
  standard aluminium 18 × 2.50 36H (Sun/Excel class); there is no lighter class worth having, and 2.15 saves ~100 g
  while cutting tyre choice. No rim lock on a road front. Tube: standard, not heavy-duty. Where weight actually
  moves: the 21 → 18 rim change itself and the tyre (a 100/90-18 is lighter than a 110/90-18); that is the whole
  budget. Spoked vs cast in this build: spoked keeps the dual-sport / Catalina ability (bends, is retrued, takes
  hits), costs tubes (no plug repair, slower to fix on the road) and spoke-tension checks; cast (S 17 in) gives
  tubeless and zero maintenance but is the road-only FXS commitment and Zero's cast wheels are not light.
- **What to bring (2026-11-07):** Buchanan's takes "a hub, a rim, or a wheel"; the hub alone is the minimum, not a
  requirement. Bring the complete 21 in wheel: they unlace it (cheap labour), measure the stock rim offset from the
  hub seal faces before anything is cut, and the old rim and spokes come back as a spare set. Cutting the spokes with a
  grinder at home works too (cut mid-length, away from the hub and bearings, bearings and spacer stay in — the hub is
  centred on them in the stand; take the rotor off first, 4 bolts, Loctite) but then measure the offset yourself before
  cutting. Decision hidden in this step: the FX has one front hub. Relacing it to 18 in means the 21 in front wheel
  ceases to exist; keeping a 21/18 set for Catalina needs a second hub (a used FX front wheel, ~$150–300).
- **Is the 21 in needed for Catalina? (owner 2026-11-07)** No. The ride there is graded dirt roads that passenger
  cars use (Stage Rd, Airport Rd, Middle Ranch, Little Harbor, Two Harbors): washboard, loose gravel in corners, some
  steep grades — DS territory (19/17, 178 mm travel), not singletrack. The rocky singletrack of the owner's MTB trip was
  a shortcut, and it is closed to motor vehicles anyway (Conservancy: roads only). A 21 in only pays on rocks, ruts and
  sand. Consequence: one front hub, one wheel, no second set; choose the front for the real mix. Tyre choice decides
  more than rim size: an 18 in front is limited to road bias (BT46, Sport Demon, Roadrider) plus two scrambler
  options (MT60 110/80-18, Shinko 705 120/80-18); a **19 in** front opens the whole dual-sport catalogue in 100/90-19
  (Trailmax Mission, Anakee Adventure, Battlax AX41, TKC 80, Karoo, Mitas E-07, Shinko 705). For road-mostly with a few
  Catalina days: 19 in + 100/90-19 80/20 tyre (or BT46 100/90-19 and ride the gravel calmly); for road-only: 18 in BT46.
- **Buchanan's order, exact lines (site prices fetched 2026-11-07; `buchananspokes.com/categories/labor.asp`,
  `custom_spoke_sets.asp`, `rims_sun.asp`, `terms.asp`):**
  | Line | Part # | Price | Note |
  |---|---|---|---|
  | Lace & true motorcycle wheel, ≤ 40 spokes | **W3** | $145 | labour only; old spokes chopped free and scrapped; "bearings should be installed in hub prior to work" |
  | Rim, Sun WM3 2.15 × 18, 36H, drilled to the hub | RSWM318 / RSWM318B | $306 silver / $377 black | drilling of ≤ 40 holes included; Sun has no 2.50 (WM4.5 = 2.75, $328/$399) |
  | or: customer-supplied Excel 18 × 2.50 36H, drilled | W1HA | $2.00 × 36 = $72 | plus the rim itself $190–250 retail; Buchanan's also sells Excel (price on inquiry) |
  | Custom stainless spoke kit, 36, single gauge 9 ga (or 10 ga), stainless nipples | made-to-order | $135 | nickel/zinc nipples $123; swaged 8–9 ga $157; chrome not offered in 9/10 ga; ships 5–7 business days |
  | Remove tyre | W12 | $15.50 | or bring the bare wheel |
  | Mount tube-type tyre | W10 | $47 | only with their wheel work |
  | Balance | W14 | $47 | tyre mounted, bearings in |
  | Disassemble wire wheel (keep old spokes/nipples) | W2 | $46 | only if the 21 in rim should stay re-laceable with its original spokes |
  | Express handling | — | $40 | normal 3–5 business days, 2–3× in season; rims "cannot be drilled for same day shipment" |
  Total: ≈ $590–700 with a Sun 2.15 rim, ≈ $540–600 with an own Excel 2.50; tyre work +$110. Rim orders must be in
  writing (email/fax) with year, make, model, front, disc, brand, width, diameter, hole count. They have a spoke
  database by hub and can make spokes from samples; the bare FX hub with bearings is enough for the measuring.
  Other labour lines for reference: loose lace $42 (W5), straighten & true an existing wheel $145 (W8), straighten a
  bare rim $64 (W9), punch dimpled rim $61 (W1A). Contact: 805 W Eighth St, Azusa CA 91702, (626) 969-4655, fax
  (626) 812-0243, Mon–Fri 8:30–16:45, closed Nov 26–27 2026; prepaid only, no returns on custom work.
- **Cheap eBay Excel instead of the Sun rim (owner 2026-11-07):** only if it is an **undrilled blank**. Excel is a
  dimpled-style rim; Buchanan's punches a customer-supplied dimpled *blank* for $61 (W1A, ≤ 40 holes), but a rim that is
  already drilled for another bike's hub cannot be re-punched — the existing holes fix the spoke angles, and the
  Zero front hub has its own. $60 Excels on eBay are take-offs drilled for KTM/Honda/Yamaha hubs, often dinged (rim
  straightening $64, W9); a new blank 18 × 2.50 36H is $190–250 at retail. Best case with a true blank: $60 + $61 punch
  + $145 W3 + $135 spokes ≈ $400 vs $586 with the Sun. Ask the seller "undrilled / no spoke holes?" and for a photo of the
  rim well; if it has holes, skip it. Buchanan's also sells Excel with punching included (price on inquiry) — ask for
  that number before buying anything on eBay.
- **Tyres** (sizes verified on the makers'/retailers' catalogues 2026-11-05):

| Style | Front | Rear (on the stock 2.50 × 18) | Notes |
|---|---|---|---|
| Road, best handling | Bridgestone Battlax BT46 **100/90-18 56H** | BT46 **120/80-18 62H** (or 110/90-18 61H) | 120/80-18 BT46 is the Royal Enfield Classic 350 OE rear; 100/90-18 is the Triumph Bonneville T100/T120 front |
| Road, bias sport (Pirelli, 2008 design) | Pirelli Sport Demon **100/90-18 56H** (also 110/80-18, 110/90-18 fronts; 100/90-19 for the 19 in route) | Sport Demon **120/90-18 65V** (OD ≈ 673 mm, rim 2.50–3.00; the only Sport Demon rear that fits a 2.50 rim: 130/70, 130/80 and 140/70-18 need 3.00+; there is no 110/90 or 120/80-18 rear) | owner's candidate 2026-11-07; rear +8 mm OD vs stock 4.10-18 → speedo constant ≈ 0.0237; BT46 is the newer (2020) compound with the longevity/wet reputation, Sport Demon the sportier profile, same price class |
| Road, classic look, one size both ends | Avon Roadrider MkII 100/90-18 56H (universal) | Avon Roadrider MkII 110/90-18 61V (universal) | both marked front/rear; OD 642 / 663 mm per Avon |
| Scrambler / light dirt | Pirelli MT 60 (bias, not RS) **110/80-18** | Pirelli MT 60 **120/80-18 62T** | MT 60 RS 110/80 R18 (Ducati Scrambler OE) is the radial road version of the front |
| 80/20 dual-sport, one tyre both ends | Shinko 705 **120/80-18 62H** (marked front/rear) | Shinko 705 120/80-18 | cheapest; the 110/80-18 TKC80 and K60 Scout are rear-profile tyres, avoid on the front |

  Load: 100/90-18 56 = 224 kg, 120/80-18 62 = 265 kg per tyre; the bike two-up is ~280 kg total, so any of them.
  Speed index H/T is irrelevant at 80–95 km/h.
- **Geometry.** OD of the 3.00-21 is ≈ 685 mm; 100/90-18 ≈ 640, 110/80-18 ≈ 634, 110/90-18 ≈ 660 mm. The front
  axle therefore drops **≈ 25 mm** with the 100/90 or 110/80 (12 mm with 110/90), i.e. the fork tubes stay flush
  in the clamps and the rear should come down by about the same amount to keep the stance (see shock section).
  Rake steepens ≈ 1° plus the smaller-radius trail loss: quicker steering, the same direction Zero went with the
  17 in FXS. The 21 in fender gap grows by 25 mm (cosmetic). Front tube: 18 in, same as the rear.
- **Speedo.** Speed comes from the rear tyre, and the bike already runs a **120/80-18 on its 2.15 rim** (owner
  2026-11-08): OD ≈ 649 mm, converter constant **0.0232 km/h per RPM** (CLAUDE.md updated). Catalogue 4.10-18 was
  665 mm / 0.0234; 110/90-18 would be 655–663 mm. Recalibrate against GPS as planned, nothing else changes.

### 19 in front without lacing: XU 2011–13 or DS 2014 wheel (researched 2026-11-07)

Owner's question: a used 2011 Zero XU front wheel instead of relacing, giving 19/18 instead of 18/18. Facts
(2011 specs motorcycle.com / totalmotorcycle; 2012 X/MX/XU owner's manual; 2013 FX/MX/XU owner's manual;
`manuals/14fx.pdf`, `14ds.pdf`; OM-FX-MY14; Koup's catalogue):

| | XU 2011 / 2012 / 2013 | FX 2013 | FX 2014 (ours) | DS 2014 |
|---|---|---|---|---|
| Front wheel | **1.85 × 19**, 36 spokes? (unverified) | 1.60 × 21 | 1.60 × 21 | 2.15 × 19 (23-07213) |
| OE tyre | 90/90-19 (2011), 100/70-19 (2012 X/MX), MJ90-19 (2013) | 3.00-21 | 3.00-21 | Kenda K761 **100/90-19 57H** |
| Front rotor | 220 × 4 mm | 221 × 4.5 mm | **240** × 4.5 mm (25-06282 → 25-08063) | 313 mm floating |
| Front fork | 38 mm inverted | 38 mm inverted | 38 mm stanchion / 48 mm outer | 41 mm |
| Front axle | end-bolt type, 26 N·m; pinch 18 N·m | same (26 / 18) | 23-06388 20 × 232 mm, 26 / 13 N·m | 23-06388, same spacer 23-02590 |
| Hub parts | ? | ? | 2 × 6904 2RS, seals 25 × 37 × 7, spacer 23-02590 "SDS/XMX" | identical to FX, rotor bolts 90-07290 identical |

- **No Zero wheel is 18 × 1.85.** Every XU (2011–2013) is 19 × 1.85 front / 16 × 2.15 rear; FX/MX rear is 2.15 or
  2.50 × 18 (this 2014 FX: 2.15, read off the rim). "18 × 1.85" in a listing is a typo for 19 × 1.85 or a mislabelled wheel: read the rim stamping.
- **Hub interchange 2011 XU → 2014 FX is likely but not documented.** For: the 2012 XU wheel is catalogued as
  "1.85X19 **XMX** FRONT WHEEL LACED ASSY 12MY" (23-03527, Koup's), i.e. Zero files it in the same platform
  family as the FX; the 2014 FX axle spacer 23-02590 and seal 23-02626 carry 2011-era part numbers ("SDS
  FRONT/XMX AXLE SPACER"), so the FX hub interface (20 mm axle, 6904 bearings, 25 × 37 × 7 seals) dates from the
  2011/12 generation; the 2011–2013 X/MX/XU/FX share the end-bolt axle with identical torques and a 220/221 mm
  rotor on the same-torque caliper mount; the forum (topic 5507) treats a 2013 XU wheel as an FX option with the
  rotor size as the only caveat. Against: 2011 X/MX/XU had its own frame and fork, hub width and rotor PCD are
  nowhere in print, 2011 vs 2012 wheel part numbers are unknown. **Check before paying, with a caliper, both
  wheels side by side or by seller photos:** (1) bearing marking — 6904 = 20 mm bore, 6903/6203 = 17 mm;
  (2) hub width over the seal faces vs the FX wheel; (3) rotor bolt count and PCD vs the FX 240 mm rotor
  (4 bolts, same PCD as the FX rear — owner 2026-11-09; the catalogue's "qty 6" front rotor bolt line is wrong,
  its drawing shows 4 holes); (4) spoke count. If (1)–(3) match it is a bolt-on with the FX rotor and caliper.
- **Rotor.** Keep the FX 240 mm rotor and caliper on the new hub if the PCD matches. A 220 mm rotor needs the
  caliper 10 mm closer to the axle (2013-FX fork-leg position); do not shim a 240 mm caliper to a 220 mm disc.
  If the bike actually carries a 220 mm rotor (owner's words 2026-11-07; the MY14 manual and catalogue say
  240), measure it: then the XU disc and the existing caliper already match.
- **DS 2014 2.15 × 19 wheel (23-07213)** is the documented alternative: same axle, spacer, bearings, seals and
  rotor bolts as the FX in the 2014 catalogues, OE tyre is the same 100/90-19 the BT46 comes in, and the rim
  is the measuring rim for 100/90. Only the rotor PCD still has to be confirmed (DS runs a 313 mm floating disc
  on the same bolts). Harder to find used than an XU wheel but zero platform risk.
- **Tyres for 19/18.** BT46 19 in fronts are only **100/90-19 57H** (rim 1.85–2.75 in; the 57V version needs
  2.15 in, so take the H on a 1.85 rim) and **3.25-19 54H** (rim 1.85–2.50). Both OD 665 mm. Rear stays BT46
  120/80-18 62H (OD 650) or 110/90-18 61H (OD 655). No other 19 in BT46 front exists (90/90 is 18 in only).
- **Geometry.** 100/90-19 OD 665 vs 3.00-21 OD 685 → front axle down **10 mm**; 120/80-18 rear is −7.5 mm vs
  stock. Stance and rake (26.3°) stay practically stock, unlike the 18 in front (−25 mm). Lowering then comes
  only from the shock, and the front can stay as is. Speedo: unchanged (rear tyre).
- **Cost.** Used XU wheel $250–320 on eBay (2012 ones listed with tyre and 220 rotor) vs rim + spokes + lacing
  ≈ $400–500 for the 18 in relace. New 23-03527 is special order from Zero via Koup's (price on request).

### 17/17 cast from a 2013–14 S/SR/DS: the "do what Zero did" option (2026-11-07)

Owner's question: skip the 18/19 fuss and wait for a pair of S cast wheels. Catalogue facts (`14s.pdf`, `16fxs.pdf`):
- **Rear 23-04859-1 "3.50X17 S REAR CAST WHEEL ASSY 13MY"** (IRC RX-01 140/70-17) is the wheel Zero fitted to the
  2016 FXS at *both* ends ("3.50X17 SDS REAR CAST WHEEL ASSY 16MY", 110/70R17 front, 140/70R17 rear). Same rear axle
  23-08032, same left spacer 23-05195, same 132T pulley, same rear rotor 25-07621 (240 mm, so the FX rear caliper
  position is right); only the right spacer changes (20-07324). Open: 140 mm tyre vs belt and 2014 swingarm
  21-05849-1 (the FXS got its own swingarm 21-07748 in 2015 for other reasons; forum topics 5507 / 9214 "FX to FXS
  conversion" are the experience reports, offline).
- **Front "3.00X17 S FRONT CAST WHEEL ASSY 13MY"** (IRC RX-01 110/70-17): same axle 23-06388, spacer 23-02590,
  rotor bolts as the FX. The S/DS 313 mm floating rotor needs their fork and caliper bracket, so run the **FX 240 mm
  rotor** on the S hub (PCD check, rotor bolts are the same part). Do **not** buy the 2016 FXS front: hollow axle
  23-07491, 320 mm rotor on custom M8 shoulder bolts, Showa fork.
- **Geometry:** 110/70-17 OD ≈ 586 mm (−50 mm at the front axle vs 3.00-21), 140/70-17 ≈ 628 mm (−18 mm rear). Front
  drops without losing travel; the rear then wants ~30–40 mm from the shock to level the stance → seat ≈ −45 mm, which
  is the street-mode target in one go (FXS: 24.4° rake vs FX 26.3°). Sidestand: S "short" leg 20-05660.
- **Tyres:** the whole 17 in world, tubeless. BT46 110/70-17 54H + 140/70-17 66H (RE Hunter 350 sizes) or any
  sport-touring radial (FXS OE Diablo Rosso II). Speedo constant 0.0234 → ≈ 0.0224 km/h per RPM.
- **Cost of the decision:** the bike becomes an FXS — 17 in road tyres and −20 mm rear ground clearance are wrong for
  the Catalina dirt-road goal; keep the 21/18 set as a second pair, swapping takes 20 min. Used 2013–16 S/SR/DS cast
  wheels appear on eBay regularly (crashed S/SR); buy only as a pair from a 2013–14 bike (2015+ S front: check axle).
- **Rule (owner 2026-11-07):** no 18 in relace, no XU hunt; wait for a 2013–14 S/SR/DS cast pair at a sane price.
  Checks before paying: rear tyre/belt clearance photo from someone who did it (forum 9214) or measure the 2014
  swingarm inner width at the tyre; front rotor PCD vs the 240 mm FX rotor; both wheels straight, bearings 6904.

### Forks FX vs S/DS 2014: not the same legs (2026-11-07)

Owner asked whether the FX and S Fastace forks are the same legs with a different brake-side slider. Catalogues say
no: three fork sets — FX 22-06093 "FX fork set Fastace 14MY" (legs 22-06094 L / 22-06095 R, 38 mm stanchions /
48 mm clamp, 230 mm travel), S/SR 22-06864 (43 mm per Zero spec, 159 mm), DS 22-06867 "DS G2" APX16RC (legs
22-06868/69, 43 mm, 178 mm) — on different triple clamps (XMX 22-06114/06117 vs SDS 22-06126/06128). Shared across
all three: front axle 23-06388, spacer 23-02590, Nissin caliper 25-04164 and its M8 × 40 bolts 90-05038-2, i.e. the
lower legs are made for the same wheel and caliper, only the lug radius (240 vs 313 mm rotor) and the leg length
differ. Inconsistency: all three list the same seal kit 22-07494, which contradicts 38 vs 43 mm stanchions — one of the
two is catalogue sloppiness; measure before ordering seals. Consequences: an S/DS fork is a complete-unit swap with
its own clamps (or a clamp-bore check), not a leg mix; a 313 mm rotor on the FX fork means an adapter bracket, not an
S lower leg. Zero itself built the 2016 FXS with the DS 41 mm Showa fork (22-05877/78) on XMX 15MY clamps, not with
FX legs — the family swaps whole forks. (zeromanual "Front Suspension Specifications", Wayback copy; `14fx/14s/14ds.pdf`.)

### S 2012–13 and XU 2011–13: the same Fastace ALX07RC, different brake-side leg (2026-11-07)

Owner's correction: the shared Fastace number was seen on S and XU listings, not S and MX. Confirmed by the zeromanual
front-suspension table: **S 2012–2013 = Fastace ALX07RC**, Zero 22-05418-03 (legs 22-04464-05 R / 22-04463-05 L),
38 mm, 140 mm travel, 310/313 mm floating rotor; **XU = ALX07RC AP18A0179-B002, Zero 22-02749-01**, 38 mm, 135 mm
travel (2012 manual; the 2013 manual's "51 mm" is a typo), 220/221 mm rotor. Same Fastace model, different Zero part
numbers, no caliper bracket in either catalogue → the lower legs differ in the caliper lug (313 vs 221 mm) and
probably spring/damping; the stanchions and the 48 mm clamp are the same. The 2014 S/SR went to the 43 mm 22-06864,
so only 2012–13 S forks are in this family.

Why it matters: the **2013 XU sits on the FX frame with this fork** (XU 2013 manual: 38 mm stanchions, 48 mm clamping
diameter like the FX, 221 mm rotor like the 2013 FX, seat 790 mm vs FX 899, rake 25° vs 26.1°, trail 87 vs 112 mm,
rear travel 147 vs 227 mm). So the XU fork is Zero's own short road fork for the XMX triple clamps: ~95 mm less
travel at the front than the FX 230 mm fork, 221 mm rotor with the same Nissin caliper, no adapter. A 2012–13 S fork
is the same fork with 313 mm lugs: it takes the S 17 in cast wheel with its 313 mm floating rotor as a complete
front end. Either way the matching recipe is XU fork + 19 in XU/DS wheel + short shock (the XU itself), or S fork +
S 17 in wheel + 313 rotor (the 2016 FXS recipe, one generation earlier).

Open before buying a fork: free length of the ALX07RC vs the FX 22-06093 (sets the real drop; travel alone does not),
2013 XU fork part number (22-02749-01 is the 2011 number), spring rate vs the FX fork for a heavier bike, and the
fork guards/fender mounts on the XU legs. Sources: zeromanual "Front Suspension Specifications"; 2012 X/MX/XU and
2013 FX/MX/XU owner's manuals; Rider Magazine 2013 S road test (38 mm, 140 mm, 310 mm floating).

### Spoked 17/17 on Sun rims (owner's "just in case", 2026-11-07)

Sun 17 in widths: WM4.5 **2.75 × 17** ($328 silver / $399 black) and WM6 **3.50 × 17** ($372 / $443, deep drop centre).
2.75 is a normal width — the classic front / light-dual-sport rear size (XT250, Himalayan class) — but it is not a
sport 17 in: 120/70-17 (rim 3.00–3.75) and 140/70-17 (3.50–4.50) do not fit it. What fits a 2.75 (ETRTO permitted
ranges): 100/80, 110/70, 110/80, 110/90, 120/80, 120/90, and as a rear also 130/80 and 130/90-17. Zero's own 17/17
(S cast, FXS) is 3.00 front with 110/70-17 and 3.50 rear with 140/70-17, so the spoked copy is **2.75 front +
110/70-17** (BT46 110/70-17 54H, Diablo Rosso II 110/70R17; or 110/80-17) and **3.50 rear + 140/70-17** (BT46 140/70-17
66H), or 2.75 rear with 120/80-17 / 130/80-17 for a narrower, cheaper rear. Geometry: 110/70-17 OD ≈ 586 mm (−50 mm at
the front axle), 140/70-17 ≈ 628, 130/80-17 ≈ 640, 120/80-17 ≈ 624 mm. Cost reality: two wheel builds (front W3 +
2.75 rim + spokes ≈ $610, rear W3 + 3.50 rim + spokes ≈ $650, tyres extra) ≈ $1,250 before tyres — more than a used
S/SR cast pair, with tubes instead of tubeless. Spoked 17/17 only makes sense if cast pairs never turn up or the
spoked look is wanted.

### Rear shocks XU vs S: not the same, but the 2013 XU shock is the factory lowered FX shock (2026-11-07)

Owner asked whether the 2013 XU and S rear shocks are one part. No — different Zero numbers both years (AF1 Racing
2012/2013 listings, Wayback copies): 2012 XU 22-02750 vs S 22-02907 (vs DS 22-02908, MXE 22-02910); 2013 **"XU 16/19
shock by Fastace 13MY" 22-05487** vs "S rear shock 13MY" 22-04781 (DS 22-04782, "XMX shock 13MY" = FX 22-04421,
MX 22-05913). The S shock is a different animal anyway: Fastace BDA58RC, **260 mm** eye-to-eye, spring 550–805 lb/in,
top bushing ~1.25 in but bottom only 11/16 in (zeromanual) — it would not drop into the FX swingarm clevis (31.95 mm
both ends) without bushings, and 260 vs 319 mm is ~120 mm at the axle, far too much.

What the 2013 listing reveals instead: the 2013 XU is built on **"FRAME FX, MX, XU" 20-06390** and **"FX/XU SWINGARM"
21-05493-1** — the same frame and swingarm as the 2013 FX — with its own "XU 16/19" fork set 22-05488 (= ALX07RC above)
and its own "XU 16/19" shock 22-05487 (piggy-back, 147 mm rear travel vs 227 mm on the FX). So **22-05487 is Zero's own
short shock for the FX frame/swingarm**, the "made-to-length lowered shock for the 2013–14 FX" that the shock section
below says does not exist off the shelf. Both are special order from Zero via Koup's (`shop.koups.com`, 7–10 days
unless back-ordered, price on request); the 2012 XU shock 22-02750 is for the older X frame, not this one.

2013 → 2014 FX caveat: the frame (20-06390 → 20-06499) and swingarm (21-05493-1 → 21-05849-1) got new numbers, but
the shock stayed the same BFA57RC family (22-04421 "XMX shock 13MY" → 22-06105 "FX shock 14MY", both 319 mm per
zeromanual), so the shock eyes/mounts are the same and the XU shock should bolt to the 2014. Verify eye widths and
the 70 mm upper bolt. Expected drop: unknown length; from the XU geometry (seat 790 vs 899 mm, fork ~95 mm shorter,
16 in rear wheel −30 mm) the shock is roughly 40–55 mm shorter than 319 → ~80–110 mm at the axle, i.e. the full XU
stance, not the "25–40 mm" of the spacer route. With the 18 or 19 in rear wheel kept, that is too low for a level
bike unless the XU fork goes on too — the two XU parts are a matched pair (XU rake 25°, trail 87 mm). Spring: sized for
a 121 kg XU, our bike is heavier; check sag. Ask Koup's/Zero for the eye-to-eye length before ordering.

### Fastace vs Showa for this bike (owner 2026-11-07): it does not matter, and Showa is not a bolt-on

Suspension does not know about 5 kWh or 78 A; it knows mass (our pack is ~32 kg, heavier than the ZF5.7 modules),
rider load and road surface. For 90 % road at ≤ 95 km/h the Fastace BFA57RC piggy-back shock and the 38/48 mm fork are
adequate once serviced: fresh oil, seal kit 22-07494, sag set by preload, rebound/compression clicks. Fastace's
reputation (forum) is crude damping, weeping seals and thin rebuild support, Showa's is consistent damping, cartridge
rebuilds and tuners who know it (Race Tech etc.); that is a comfort and maintenance difference, not a safety one.
Going Showa means the complete 2015+ front end, not a fork swap: 41 mm fork (FX 22-05868/69 or the shorter FXS/DS
22-05877/78), 15MY XMX triple clamps 22-07625 / lower 15MY, hollow axle 23-07491 with the 2015 hub/bearings, 2015
rotor/caliper positions, fender mounts — and the 2015 frame 26-08080 replaced the 2014 20-06499, so the steering-stem
length is unverified. The rear Showa 22-05879 is the same 320 mm length with the 60 mm upper bolt issue (table above).
Verdict: keep and service the Fastace; lower via spacer or the XU shock. Showa only if a complete 2015+ FX/FXS front
end (fork + clamps + 17 in cast wheel + 320 mm brake) turns up cheap and the stem fits the 2014 head — then it is
the FXS street front end in one purchase, not a damping upgrade.

### Rear shock, "city, a bit lower": no off-the-shelf part for the 2014 (except the 2013 XU shock, see above)

Ikon's full application list (fetched 2026-11-05) has exactly one Zero line: **"Zero FXS 2016 — 3610-1104"**.
Nothing for the 2013–14 FX, and the 2016 frame/swingarm/upper-bolt differences (table above) are unverified
against it. Fox Podium RC2 (Zero 10-05738, special order via dealers such as Koup's) is stock height. YSS,
Wilbers, Hyperpro and Öhlins list nothing for the FX. So "ready-made and lower" does not exist; the practical
order for a 25–40 mm drop with the 18 in front:

0. **2013 XU shock 22-05487** (special order, see the XU section): the factory short shock for this frame and
   swingarm, but it drops the rear by the full XU amount and belongs with the XU fork 22-05488.
1. **Spacer in the stock Fastace BFA57RC** at a shock shop: 1/2 in spacer ≈ −25 mm at the wheel (matches the
   front drop exactly, fork tubes flush), 3/4 in ≈ −38 mm (forum-proven) with the tubes raised ~13 mm. Keeps the
   piggy-back damper, costs a service + nitrogen. Loses the same travel.
2. **Ikon 3610-1104** (lowered −2 in version per forum topic 6640): only after measuring eye widths / lug spacing
   against the Showa numbers above; ask Ikon USA whether the eyes match the 2014 (70 mm upper bolt).
3. **Made-to-length** (YSS/Wilbers, ~300–305 mm eye-to-eye): the clean solution, no stock part.

Sidestand after lowering: Zero's own shorter legs — DS "medium" 20-05661, S "short" 20-05660 (FX stock is "long"
20-05662, all `manuals/14*.pdf` ZEV0007/0008). Lowering ~30–40 mm makes the long leg stand the bike too upright.

Sources: Ikon application list `ikonsuspension.com/wp-content/uploads/full-ikon-shock-absorber-application-list.pdf`;
forum topics 10515 "FX Broken Spokes (again...)", 11891 "Where to find spokes compatible with Zero FX";
Buchanan's `buchananspokes.com`; Warp 9 (17 in supermoto sets from $500/wheel, no Zero fitment listed);
Bridgestone BT46, Pirelli MT 60 / MT 60 RS, Avon Roadrider MkII and Shinko 705 size lists; Excel rim listings. 19 in: motorcycle.com 2011 XU spec sheet; 2012 and 2013 X/MX/XU owner's manuals (Wayback copies of
media.zeromotorcycles.com); Koup's `shop.koups.com` part 23-03527; Bridgestone `bridgestone.com` BT46 size table
and chapmoto / tyretec listings; forum topic 5507 "converting an fx to fxs compatibility" (via search snippet only).
