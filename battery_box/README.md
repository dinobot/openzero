# OpenZero battery box — printed enclosure

Parametric build123d model of the two-zone battery enclosure for the 30s1p LiFePO4 pack
(2014 Zero FX conversion). Requirements are in `SPEC.md`; this file covers what the model
actually does, where it deviates from the spec and why, how to print and assemble it, and
what still has to be measured.

```
python enclosure.py          # from the project venv (build123d 0.13)
```

Outputs:

| File | Content |
|------|---------|
| `output/*.stl` | one STL per unique part (active VARIANT), print orientation, quantity in the name |
| `assembly.step` | full assembly; ghost pack (blue), BMS (green) and fuse block (orange) are separate translucent bodies |
| `test_coupons.stl` | 8 small pieces on one plate: lap joint pair, corner joint pair, hole/insert block, boss plate, lip rabbet pair |
| stdout | geometry report: all assertions, warnings, part table with bounding boxes and volumes |

## Thickness variants

`VARIANT = "spec"` (default) uses the thicknesses written in SPEC.md: long walls 5.0, end walls
4.0, shoulder 4.0, floor 5.0, roof 4.0 mm. `VARIANT = "thick"` is the heavier set proposed during
design review (8 / 4 / 6 / 12 / 6) so that every heat-set insert has at least 2 mm of plastic
around it. Joint dimensions (lap tongues, groove widths, insert depths, standoff heights) are
derived from the thicknesses, so both build; the report prints a "fastener feasibility" block
that warns wherever an insert or countersink has less than 0.8 mm of material. Renders of both
are in `renders/spec/` and `renders/thick/`.

With the spec variant the report currently warns about two things:
- the M3 insert in the long-wall bottom edge leaves 0.5 mm of wall per side (4.0 mm hole in a
  5.0 mm wall);
- tile-to-tile lap screws are not modelled: a 5 mm floor leaves 1.8 mm for an insert. Floor tile
  joints are plain half-laps held by the wall screws only.

## Geometry summary (spec variant)

| | mm |
|--|--|
| Outer length | 454.5 (bay 457.2, 1.35 mm spare per end) |
| Outer depth, lower zone | 291.4 (overhangs the 254 bay by 18.7 per side, crash zone) |
| Outer depth, upper zone | 254.0 |
| Inner cavity height | 177.8 (= 7 in: pack 152.4 + 1 mm clearance + 24.4 mm upper zone) |
| Outer height | 186.8 (floor 5 + cavity 177.8 + roof 4) |
| Shoulder | 45°, from z = 158.4 to 177.1, slab 4 mm |
| Free height above pack | 24.4 — BMS (12.7 + 3) fits, fuse placeholder (50 + 5) does **not** |

Coordinates in the script: X = bike length (+X front), Y = depth, Z up, Z = 0 at the outer
bottom of the floor.

## Parts (16 printed pieces, 10 unique)

| Part | Qty | Print size, spec variant (mm) | Notes |
|------|-----|-------------------------------|-------|
| floor_tile_rear_left / mid_left / front_left | 1 each | ≤175 × 177 × 5 | −Y row, tongue on +Y edge |
| floor_tile_rear_right / mid_right / front_right | 1 each | ≤175 × 125 × 5 | +Y row, rabbet on −Y edge |
| long_wall_tongue | 2 | 229 × 179 × 38 | right-front and left-rear (180° rotation) |
| long_wall_groove | 2 | 226 × 179 × 38 | right-rear and left-front |
| end_wall_half_tongue | 2 | 181 × 148 × 14 | front-left and rear-right |
| end_wall_half_groove | 2 | 181 × 146 × 14 | front-right and rear-left |
| cover_rear_main / _strip | 1 each | 182 × 224 / 182 × 42 | BMS standoffs hang from the main half |
| cover_middle_main / _strip | 1 each | 142 × 224 / 142 × 42 | fuse bosses + insulating partition |
| cover_front_main / _strip | 1 each | 130 × 224 / 130 × 42 | cable zone thickened to 6 mm, engraved outline, no holes |

Everything fits 240 × 240 × 240. Solid volume ≈ 2.4 L (≈ 2.6 kg at 100 %) for the spec variant,
≈ 4.1 L for the thick one.

## Deviations from SPEC.md

1. **Height semantics.** Spec line 34 says "outer height ≤ 177.8". Owner clarified that 7 in is
   the *inner* cavity; floor and roof sit outside the frame window. Parameter is
   `MAX_INNER_HEIGHT = 177.8`.
2. **Components hang from the service cover** instead of standing on standoffs from the shell.
   The only shell surface above the pack is the 45° shoulder; a tray would have needed its own
   bridging part. Hanging the BMS and fuse from the cover keeps bosses out of the pack volume
   and means removing a cover segment brings its component out with it. Lift the **middle**
   cover before the rear one.
3. **Cover split lengthwise.** 254 mm is wider than the 240 mm part limit, so every cover segment
   is a 212 mm main half plus a 42 mm strip joined by a half-lap with screw bosses under the lap.
4. **Screw-less joints.** The spec asks for ≥2 screws per joint. These joints have none and
   rely on tongue-and-groove plus the parts around them:
   - long-wall panel to panel at x = 0 (vertical T&G; both panels screw to the same floor
     tile and the cover bridges the joint)
   - end wall to long wall corners (end wall is captive: bottom tongue in the floor groove,
     side tongues in the long-wall rabbets, 4 cover screws into its top pads)
   - end wall halves at y = 0 (vertical T&G)
   - cover segments to each other at x = −45 / 97.25 (plain butt)
   - floor tile to floor tile in the spec variant (see above)
   Inner corner bosses were impossible without entering the 1 mm pack clearance.
5. **Lower-zone exterior seams are stepped.** Floor tile laps show as a Z-shaped hairline on the
   side faces at x = ±75.75 and on the ends at y = 20. Exterior is still flush.
6. **Floor-edge chamfer 1.0 mm** (spec 2.0): the countersinks for the wall screws sit close to
   the edge. Everything else uses 2.0 mm.

## Warnings the script prints (and what to do about them)

- **Fuse block does not fit** — 55 mm needed (50 + 5 mm standoff for the M4 insert), 24.4 available. The 50 mm placeholder is
  `MEASURE_ME`. Measure the real ZOOKOTO block with its cover; if it is still too tall, set
  `FUSE_POCKET_ENABLE = True` and `FUSE_POCKET_EXTRA_HEIGHT` to at least the shortfall. The
  pocket is a 45° frustum on the middle cover; note that with the fuse along Y the pocket base
  crosses the cover split at y = 85, so either rotate the block (`FUSE_ROT = 0`) or move the
  split. A pocketed cover cannot lie flat on its outer face — it needs supports.
- **MOUNT_POINTS empty** — frame mounts are not modelled. The flat narrow section is only
  5.7 mm tall below the roof, so mounts will land on the shoulder slab or the roof edge.
  Measure the original mounts and add `(x, y, hole_d, boss_d)` entries; the script does not
  yet generate bosses for them (TODO once positions exist).
- **Shoulder wider than 254 mm between z = 158.4 and 177.1** — the first 18.7 mm of the
  1 in upper section is still wider than the bay. Verify the frame clears this on the bike.
- **Lower zone overhang 18.7 mm per side** — intended (spec), listed for completeness.

## Printing

**Material:** ASA (preferred: UV and heat resistant, this sits next to a 32 kg pack in the
sun) or PETG-FR. Dry the filament. Enclosed P2S, bed 95–100 °C for ASA.

**Slicer settings (Bambu Studio):**

| Setting | Value |
|---------|-------|
| Nozzle / layer | 0.4 mm / 0.2 mm |
| Walls | 4 perimeters (a 5 mm wall is 6 lines of 0.4 at 100 %; print the floor and long walls solid) |
| Top / bottom | 6 / 6 layers |
| Infill | floor tiles and long walls 100 %; covers and end walls 40 % gyroid |
| Supports | none — every part is oriented with its outer face on the bed and no overhang over 45° |
| Brim | 5 mm on the long walls (tall 45° slab) |
| Seam | aligned, hidden on the inner face |
| Hole compensation | leave off; test coupon decides |

**Print order:**

1. `test_coupons.stl` first. Check: M3 insert goes into the 4.0 hole with a soldering iron and
   holds; M4 into the 5.6 hole; countersunk M3 head sits flush; lap pair slides together by
   hand with no slop; corner pair tongue seats in the rabbet; lip strip seats in the rabbet
   sample. If fits are tight or loose, change `FIT` (0.25 per side) and rerun.
2. One `floor_tile_mid_right` and one `long_wall_groove` — dry fit them.
3. Remaining floor tiles, then long walls, then end walls, then covers.

## Assembly order

1. Press heat-set inserts: wall bottom edges (10 per long wall), shoulder pads (8 per long
   wall), end-wall pads (2 per half), tile rabbet laps, cover lap bosses, BMS and fuse bosses.
   Let them cool fully.
2. Lay the six floor tiles upside down on a flat surface, interlock the laps, drive the
   tile-to-tile screws from below (thick variant only; the spec variant has plain laps).
3. Stand the four long-wall panels on the floor (tongue panels into groove panels at x = 0)
   and drive the wall screws from below (M3 × 12 countersunk for the 5 mm floor, M3 × 20 for the 12 mm one).
4. Slide the end-wall halves down into the long-wall rabbets and the floor groove, tongue half
   first, then the groove half.
5. Lower the pack in — **the pack goes in before the covers and comes out through the
   floor.** For service: remove the floor screws and tiles with the box upside down or with the
   bike on a lift.
6. Fit the BMS to the rear main cover standoffs (M3), the fuse block to the middle cover bosses
   (M4). Dress the cables toward the front.
7. Fit the main cover halves (lip into the slab rabbet), then the strips; drive the cover
   screws (M3 × 12 countersunk) and the lap screws (M3 × 8 countersunk).

## Cables (owner drills the holes)

- Drill in the marked zone on the inner face of `cover_front_main` only.
- Every hole gets a rubber grommet or a cable gland; no bare printed edges on a power cable.
- Deburr printed holes; ASA edges are sharp enough to cut insulation under vibration.
- Strain-relieve inside the box. Cables must not rest on or rub the shell, the shoulder
  slab edge, or the partition.
- The balance harness (31 wires) plus two main leads plus the BMS B−/P− split all leave
  through this 80 × 120 mm zone — check the area before committing to connector types.
- Pack terminals face the long walls, 1 mm from the shell. Add an insulating sheet or the
  pack's own cover between busbars and the long walls; do not rely on the air gap.

## MEASURE_ME / TODO before printing the full set

| Parameter | Current placeholder | How to measure |
|-----------|--------------------|----------------|
| `BMS_L, BMS_W, BMS_H` | 127 × 127 × 12.7 | real ANT BMS board incl. heatsink and connectors |
| `BMS_HOLES` | ±55, ±55 | hole pattern on the board |
| `BMS_CONNECTOR_SIDE` | rear | which edge the balance/power connectors leave from |
| `FUSE_L, FUSE_W, FUSE_H` | 125 × 60 × 50 | block with cover on |
| `FUSE_HOLES` | ±50 along length | base mounting holes |
| `FUSE_LUG_CLEARANCE` | 20 | ring-lug length on your cable |
| `MOUNT_POINTS` | [] | original frame mounts on the bike |
| `TERMINAL_CUTOUTS`, `VENTS` | [] | after component positions are final |
| Bay height | 7 in | confirm with the frame; the shoulder footprint above 254 mm wide |
| Pack envelope | 444.5 × 279.4 × 152.4 | with compression hardware, straps, terminal covers |

Things to decide that the model does not know about: where the contactor, precharge
resistor, main terminals and charge port live (not in this box per spec), and how the BMS
MOSFET stage gets airflow (`VENTS` is empty; a sealed ASA box has no heat path).
