# Ride plans — episode 3 and beyond (planned 2026-11-05)

Start/finish: central Laguna Niguel. Bike as of 2026-11-05: 30S Gotion LFP pack, Sevcon limit 52 A
(≈ 5 kW, ~80 km/h ceiling), measured ~55 Wh/km mixed, no odometer yet (speed converter not built),
CT-22 lamp thresholds not yet calibrated. Chargers: AFU AF1200 (120 V input only); YILEIDE E22 and the
J1772 adapter box ordered / BOM only. **So public J1772 charging is not possible on episode 3** — it
is the point of episode 4.

## Energy model used here

- 55 Wh/km (measured 2026-11-02, mixed, partly two-up). Pure PCH at 50–60 km/h should be a bit less.
- Climb: ≈ 0.07 kWh per 100 m (≈ 220 kg, 85 % drivetrain); regen on the descent returns ≈ 0.03 kWh/100 m.
- Usable energy = 5.0 kWh minus the go-home reserve at 20 % → ≈ 4.0 kWh for planning. "Finish SOC"
  below assumes a start at 100 %.
- Public post with the E22 (18 A at 240 V): ≈ 30 km per hour of charge. AF1200 at a 120 V outlet: ≈ 15 km/h.

## Road status checked 2026-11-05

- USFS Trabuco Ranger District (page updated 2026-11-02): **Maple Springs Rd 5S04 closed**, Trabuco Canyon
  Rd 6S13 closed, Harding Truck Trail closed to motor vehicles, Black Star and Skyline hike/bike only.
  **South Main Divide 6S07 open** (access limited by weekend Caltrans closures of SR-74).
- Trabuco Creek Rd (to Holy Jim) closed indefinitely since the Airport Fire.
- SR-74 Ortega Hwy: $96 M widening between Monte Vista St and Grand Ave (Lake Elsinore side); nightly
  closures 8 pm – 5 am, periodic 55-hour weekend full closures; Gibby Fire (Sept 2026, 230 acres at
  Gibby Rd) is contained, road open.
- San Onofre State Beach: "Bluffs Restrictions – updated 2026-10-23" advisory is live — open the link on
  parks.ca.gov before a ride there. Day use $15 ($20 holidays/weekends), bluffs 6 am – sunset.

Legal dirt in Orange County is therefore closed for now. The only open forest road (South Main Divide)
starts at the Ortega summit, 50 km and 800 m of climbing away — episode 5 territory, with the E22.

## Route A — Coast + Top of the World  → **episode 3**

| Leg | km | Notes |
|---|---|---|
| Crown Valley Pkwy → PCH → Laguna Beach downtown | 16 | 35–45 mph zones, fine at the 80 km/h cap |
| PCH north → Crystal Cove, Los Trancos lot / El Moro bluffs | 8 | shots over the coves |
| back to downtown, Park Ave up to Alta Laguna Park (Top of the World) | 12 | ≈ 320 m climb; low speed at 5 kW is fine; 360° view = the hero shot |
| descent (regen), PCH south → home | 20 | first real regen log at 40 A |
| **Total** | **≈ 56** | **≈ 3.2 kWh → finish ≈ 35 %** |

Chargers on the route (for the episode-4 narrative, not usable with the AF1200):

| Site | Address | Ports | Price |
|---|---|---|---|
| The Ranch at Laguna Beach | 31106 S Coast Hwy | 2× J1772 L2 + 3× NACS | free |
| Laguna Beach Lot 11 (ChargePoint) | 505 Forest Ave | 7× J1772 L2 | $2/h |
| Glenneyre parking structure, lower level | 533 Glenneyre St | 2× J1772 L2 | $3/h |
| Montage Laguna Beach | 30801 S Coast Hwy | 4× NACS L2 | free (needs NACS→J1772 adapter, BOM #13) |

Why A: the hero shot (Top of the World = the high point with the ocean view) and many stops for the CT-22-vs-ANT
comparison; no fast roads (stay off Laguna Canyon Rd and I-5). **Ridden 2026-11-11 (owner, reconnaissance; `log.md`):** Park Ave is an open road with a steep, long climb, not a
20 mph street — the 11-11 "not a limit test" estimate was wrong. 2.44 km at 9.7 % average with 12–18 % sections,
wide-open throttle the whole way: ANT 78–91 A for ~3 min, 64 km/h at the bottom, 45–53 on the 14–18 % section,
31–41 on the last 12 %, 17 km/h at the top (owner: slowing at full throttle on the last short stretch; the rest of the
climb felt comfortable). So Route A *is* the sustained-current test on a grade — the longest full-throttle stretch
ridden so far. The descent, by contrast, is not a regen test yet: ANT saw ≈ 9 A of regen at most (weak neutral
braking, no paddle). Outbound 18.2 km with ≈ 400 m of climbing, 36 km return trip, 12 stops each way through Laguna
Beach traffic.

## Route B — Coast south to San Onofre Bluffs → **episode 4 (first J1772 test)**

| Leg | km | Notes |
|---|---|---|
| → Dana Point Harbor, new parking structure | 10 | 16× ChargePoint L2 on level 1, $5 surcharge after 3 h in an EV stall — adapter-box test #1 |
| PCH → Capistrano Beach → San Clemente pier | 12 | |
| El Camino Real / Old 101 → San Onofre State Beach, Old Highway 101 along the bluffs | 12 | gravel lots at Trails 1–6, the only "light dirt" available; bicycles only beyond the park |
| back | 34 | |
| **Total** | **≈ 68** | **≈ 3.7 kWh → finish ≈ 25 % without a charge; turn at the pier (44 km, ≈ 50 %) if no E22 yet** |

Chargers: Dana Point Harbor structure (above); San Clemente City Hall, 910 Calle Negocio, 2× J1772 L2,
$0.49/kWh, free parking 3 h; Outlets at San Clemente, J1772 L2, $0.25/kWh (reported partly out of order).

## Route C — Canyons: Live Oak → Cook's Corner → Santiago Canyon → Modjeska Grade → **episode 4 alternative**

≈ 68 km with ≈ 400 m of total climbing → ≈ 4.0 kWh, finish ≈ 20 %: needs a charge (L2 in Rancho Santa
Margarita / Foothill Ranch) → E22 only. Cook's Corner is the SoCal biker landmark; Modjeska Grade is the
scenic bit. No dirt: Maple Springs is closed (see above), Silverado Canyon Rd is paved to the gate.

## Route D — Ortega Hwy → El Cariso → South Main Divide → Lake Elsinore → **episode 5, two charges**

65 km one way, 800 m climb, 55 mph traffic on a bike that climbs at ~50 km/h at 5 kW, construction zone
on the Elsinore side. Only with the E22, a charge planned in Lake Elsinore, and Caltrans closures checked
that week. South Main Divide 6S07 is the one open dirt road in the district.

## Route E — PCH commute: City Hall → San Clemente DMV → home (owner's idea 2026-11-11) → **episode 3 candidate**

Laguna Niguel City Hall (30111 Crown Valley Pkwy, ≈ home) → Crown Valley Pkwy down to PCH at Monarch Bay →
PCH through Dana Point, Doheny, Capistrano Beach → Camino Capistrano → **San Clemente DMV, 2727 Via Cascadita**
(Mon/Tue/Thu/Fri 7–5, Wed 9–5) → same way back. Routed with OSRM through waypoints on PCH (no I-5, no Stonehill),
elevation from SRTM 30 m (± a few m):

| Leg | km | Profile | Energy (model above) |
|---|---|---|---|
| City Hall → DMV | 15.5 | 108 m → sea level by km 10 (Crown Valley −3.9 % over km 3–4, PCH −3.8 % at km 9), DMV at 14 m; 57 m up / 151 m down | ≈ 0.8 kWh |
| DMV → City Hall | 16.0 | flat to km 6, Crown Valley climb 3.5–3.8 % at km 6 and 11–14; 148 m up / 58 m down | ≈ 0.9 kWh |
| **Total** | **≈ 31.5** | | **≈ 1.7 kWh ≈ 35 % → finish ≈ 65 % from a full pack; fits the go-home rule from any start ≥ 60 %** |

OSRM car time 22–23 min per leg; speed limits 50 mph on Crown Valley, 40–45 on PCH, 35–40 on Camino Capistrano,
all inside the ~80 km/h comfort cap. Crown Valley Pkwy is the one fast arterial (traffic 55–60 mph in the right
lanes); the PCH stretch is the footage (Salt Creek, Dana Point Harbor, Doheny, Capo Beach pier).

**Verdict:** a good episode 3 — half the energy of Route A, a real-world errand instead of a sightseeing loop, and
the first ride long enough to measure Wh/km at road speed (two 15 km legs, SOC before/after each). Crown Valley Pkwy
home-bound (4 km at 50 mph on 3.5–3.8 %) is a second sustained-current stretch at road speed, Park Ave on Route A
(ridden 11-11) is the one on a steep grade. Not covered anywhere nearby: the ≥ 30 min hot-day validation (step 7a)
and regen near the 40 A cap. Same checklist as below; add: note SOC/pack V at City Hall, DMV and
home; export the ANT log at the DMV and at home (200-event buffer); the Crown Valley descent is the first real regen
log — read max charge current in the app.

## Pre-ride checklist (episode 3)

1. Pack has sat at 78 % since 2026-11-02: **record ANT SOC and pack V before charging** — first BMS
   standby-drain figure (CLAUDE.md "Working").
2. Charge to 100 % with the AF1200 (65 % of the pack is needed; a 78 % start does not fit the reserve rule).
3. At every stop: CT-22 segments vs ANT SOC (and pack V) → table for the lamp calibration.
4. Log from ANT after the ride: max discharge current on Park Ave, max regen on the descent, cell spread
   under load, cell/MOS temperatures, any warnings.
5. Distance by phone GPS (no odometer yet); update `site/landing/odometer.json`.
6. Go-home rule applies: 1 segment at a stop or ANT 20 % = head home.

## Station data APIs (for route tooling)

- NREL AFDC: `https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=…&latitude=…&longitude=…&radius=15&fuel_type=ELEC&access=public&status=E`
  — filters for connector types incl. `J1772`, `NEMA520`, `NEMA515` (120 V outlets). Free key at
  developer.nrel.gov/signup. On 2026-11-05 the host did not resolve from the owner's machine (local DNS?);
  `afdc.energy.gov` did.
- OpenChargeMap: `https://api.openchargemap.io/v3/poi/?key=…&latitude=…&longitude=…&distance=20&distanceunit=KM`
  — free key required since 2024.
- PlugShare: no public API; its "Wall Outlet" category (120 V, for the AF1200) must be browsed by hand.

## Sources

- USFS Trabuco Ranger District road/trail status — https://www.fs.usda.gov/r05/cleveland/alerts/forest-truck-trail-and-road-closures
- Trabuco Creek Road closed — https://www.alltrails.com/trail/us/california/trabuco-creek-road ; Holy Jim Trail — https://www.fs.usda.gov/r05/cleveland/recreation/trails/holy-jim-trail
- Maple Springs Road description — https://www.orangecountyoutdoors.com/get-out-there/scenic-drives/maple-springs-road
- Laguna Beach chargers — https://evhype.com/map/location/39400 ; https://chargehub.com/en/ev-charging-stations/united-states/california/laguna-beach/533-glenneyre-street-parking/electric-car-stations-near-me?locId=51727 ; https://chargehub.com/en/ev-charging-stations/united-states/california/laguna-beach/the-ranch-at-laguna-beach-tesla/electric-car-stations-near-me?locId=50185 ; https://chargehub.com/en/stations/ca/laguna-beach/montage-laguna-beach.html
- Dana Point Harbor parking structure — https://danapointharbor.com/plan-your-visit/parking/
- San Clemente chargers — https://chargehub.com/en/ev-charging-stations/united-states/california/san-clemente/san-clemente-city-hall/electric-car-stations-near-me?locId=78952 ; https://chargehub.com/en/ev-charging-stations/united-states/california/san-clemente/outlets-at-san-clemente/electric-car-stations-near-me?locId=86015
- San Onofre State Beach — https://www.parks.ca.gov/sanonofre/
- San Clemente DMV address/hours — https://dmvwaittimes.org/california/offices/san-clemente ; https://dmvofficescalifornia.com/offices/san-clemente/ ; routing router.project-osrm.org, elevation api.opentopodata.org (srtm30m)
- SR-74 widening — https://dot.ca.gov/caltrans-near-me/district-8/district-8-current-projects/sr-74-lane-widening-safety-project ; closures — https://patch.com/california/lakeelsinore-wildomar/ortega-highway-planned-closures-road-work-drivers-be-advised
- Gibby Fire — https://myvalleynews.com/blog/2026/09/02/gibby-fire-burns-216-acres-closes-ortega-highway/
