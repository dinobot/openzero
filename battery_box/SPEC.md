Create a parametric, 3D-printable enclosure for a LiFePO4 power pack using
build123d (Python; pip install if needed). Work in mm internally. This is for
a motorcycle (Zero FX chassis), so the shell must be rigid and crash-tolerant.

=== INPUT DIMENSIONS (put ALL in one parameters block at top of script) ===
Power pack (includes compression system), lies on its widest face:
  length 17.5 in (444.5 mm), depth 11 in (279.4 mm), height 6 in (152.4 mm)
Battery bay envelope in the chassis: 18 x 10 x 7 in (457.2 x 254.0 x 177.8 mm)
  = max length, max depth, max height of the enclosure's NARROW upper section.
Components in the upper zone (placeholder solids, all dimensions are
parameters, flagged MEASURE_ME):
  ANT BMS: plate 5 x 5 x 0.5 in (127 x 127 x 12.7 mm). Add parameter
    BMS_CONNECTOR_CLEARANCE = 25 mm on the side where its cables/connectors
    attach (side TBD, default: toward the rear).
  FUSE_BLOCK: ZOOKOTO 150 VDC Class T 100 A block, with its own ABS cover
    kept on. Placeholder 125 x 60 x 50 mm (L x W x H), MEASURE_ME. Include
    two stud terminals and wire-lug clearance of 20 mm beyond each end of the
    block (parameter FUSE_LUG_CLEARANCE).

=== GEOMETRY ===
Two-zone stepped shell, symmetric in depth:
1. LOWER ZONE (houses the pack): inner depth = pack depth + 2*CLEARANCE.
   It intentionally sticks out of the bay by ~0.5 in per side plus wall
   thickness; this is allowed and acts as crash protection.
2. UPPER ZONE (above the pack height): narrows to OUTER depth 10 in (254 mm).
   This narrow part mounts to the frame via the original mounts.
   It holds the fuse block and the ANT BMS.
3. Transition: a 45-degree chamfered shoulder (no horizontal overhang) so the
   parts print without supports, located above the pack top plane + clearance.
Hard constraints:
- Total outer LENGTH <= 457.2 mm. With the 444.5 mm pack this leaves 6.35 mm
  per end for clearance + wall. Use CLEARANCE = 1.0 mm, end wall 4.0 mm;
  ASSERT it fits.
- Outer height <= 177.8 mm (parameter MAX_OUTER_HEIGHT, default 177.8).
- Wall thickness: long (depth-direction) walls of the lower zone 5.0 mm
  (crash zone); end walls and everything else 4.0 mm; floor 5.0 mm. All wall
  thicknesses are multiples of 0.4 mm.
- Include "ghost" solids of the pack, BMS and FUSE_BLOCK in the assembly.
  Verify by boolean intersection that nothing intrudes into the pack volume
  and that the pack does not touch the shell (min clearance >= CLEARANCE).

=== UPPER ZONE LAYOUT AND HEIGHT CHECK (important) ===
- Layout in the upper zone, along the length: BMS plate lying flat, fuse block
  next to it, with the cable exit at the top FRONT. Keep >= 10 mm air gap
  between the BMS plate and any fuse terminal or lug, and add a printed
  insulating partition wall (2.0 mm, full height of the zone) between them.
- Compute and print: free inner height of the upper zone (outer height minus
  pack height minus clearance minus floor/roof thickness), versus the REQUIRED
  height for the BMS (plate + 3 mm standoff) and for the fuse block (its
  height + 3 mm). If the fuse block does not fit under MAX_OUTER_HEIGHT, DO NOT
  silently increase the height. Instead:
    a) print a clear WARNING with the numbers, and
    b) support an optional local raised pocket in the top cover over the fuse
       block (parameters FUSE_POCKET_ENABLE=False, FUSE_POCKET_EXTRA_HEIGHT),
       with 45-degree sloped walls (no supports), so I can enable it if the
       chassis allows more room in that spot.
- Mounting inside: the BMS plate sits on 4 printed standoffs (insulating,
  M3 heat-set insert holes) and the fuse block on 2-4 M4/M5 bosses, positions
  derived from placeholder mounting-hole parameters (BMS_HOLES, FUSE_HOLES,
  TODO: replace with measured hole patterns). Bosses must be thickened pads
  that do not intrude into the pack volume.

=== WIRE EXIT (top, front, narrow section) ===
- I will drill the wire holes myself in the printed cover, so do NOT cut
  holes. Instead make the top cover locally thickened (to 6.0 mm) in a
  marked flat rectangular zone (parameters CABLE_ZONE_X, CABLE_ZONE_Y,
  CABLE_ZONE_W, CABLE_ZONE_L; default: front 120 mm of the top cover, centered
  in depth, 80 mm wide) with a shallow 0.4 mm engraved outline on the INNER
  face so I can see the area. Keep the zone free of screw bosses and ribs.
- Add a note in the README: cable grommets/strain relief required, no sharp
  edges on drilled holes, and wires must not rub on the shell.

=== EXTERIOR AND JOINTS ===
- The OUTSIDE surfaces must be flat and flush: no external flanges, ribs,
  brackets or protruding screw heads. Panel-to-panel joints (lap/rabbet or
  tongue-and-groove) must be hidden inside the wall thickness, with fasteners
  on the inner side. Use local thickening only outside the pack envelope
  (upper zone, shoulder) and in the thick long walls.
- Fasteners: M3 or M4 screws into heat-set inserts (insert hole 4.0 mm for M3,
  5.6 mm for M4, depth 6-8 mm, parameters). Max screw spacing 80 mm along
  every joint, at least 2 screws per joint.
- Removable access: the pack cannot leave through the top (the upper zone is
  narrower than the pack). Make the FLOOR removable as a set of panels, held
  by countersunk screws that sit flush with the outer surface into inserts in
  the bottom edge of the walls. Make the top plate of the upper zone a
  separate removable service cover (fuse/BMS access), flush, countersunk.
  If you find a better access scheme under these constraints, propose it
  but do not silently change the requirements.
- Printed-fit clearance for mating joints: 0.25 mm per side (parameter).

=== PRINTABILITY (printer: Bambu Lab P2S, enclosed, bed 256 x 256 mm) ===
- No printed part larger than 240 x 240 x 240 mm. Split long walls, floor
  and covers into sections (the floor needs a grid of tiles); keep joint lines
  away from the highest-stress areas and stagger them between adjacent panels.
- Orient every part so its OUTER face is on the build plate (flat, smooth
  exterior) with no supports. Layer lines parallel to panel faces.
- Avoid overhangs steeper than 45 degrees and bridges longer than 20 mm.
- Min feature size 0.8 mm. 2 mm fillet or chamfer on outer edges, except
  where it would break the flush joints.
- Frame mounts: MOUNT_POINTS = [] (x, y, hole diameter, boss diameter, on the
  upper zone) with a TODO. The model must build without them and print a clear
  WARNING that mounts are not defined. Do NOT invent mount positions.
- Other placeholders (empty, TODO): TERMINAL_CUTOUTS, VENTS.

=== OUTPUT ===
1. enclosure.py (single parametric script, readable, commented).
2. ./output/ with one STL per unique part in print orientation (quantity in
   the file name, e.g. floor_tile_a_x2.stl).
3. assembly.step (full assembly incl. ghost pack, BMS and fuse block in a
   different color/layer).
4. test_coupons.stl: ~60 mm sections with one corner joint, one lap joint,
   one countersunk insert hole and one heat-set boss, to verify tolerances
   before printing full parts.
5. After running, print a table: part name, quantity, bounding box (mm),
   estimated volume; confirm each part fits within 240 x 240 mm. Print all
   assertion and warning results (length fit, pack clearance, upper zone
   height check for BMS and fuse). Fix any failures yourself and re-run,
   except the height conflict, which you must only report.
6. README.md: assembly order, recommended material (ASA or PETG-FR), slicer
   settings (walls, infill), print order starting with the test coupon, and
   a list of MEASURE_ME values I still need to confirm.
