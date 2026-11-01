#!/usr/bin/env python3
"""
OpenZero battery box enclosure - parametric build123d model.

Two-zone stepped shell for the 30s1p LiFePO4 pack of the 2014 Zero FX conversion.
Read SPEC.md (requirements) and README.md (assembly, deviations, MEASURE_ME list)
before changing anything here.

Coordinate system (all mm):
    X = length of the bike / pack  (+X = FRONT of the bike)
    Y = depth (left / right)        (symmetric about Y = 0)
    Z = height                      (Z = 0 is the OUTER bottom face of the floor)

Run:  python enclosure.py
Writes ./output/*.stl (one per unique part, print orientation, quantity in name),
./assembly.step (full assembly incl. ghost pack / BMS / fuse), ./test_coupons.stl,
and prints the part table plus every assertion / warning result.
"""
import math
import os
import sys

from build123d import *  # noqa: F401,F403

# =============================================================================
# PARAMETERS  (everything the design depends on lives in this block)
# =============================================================================
IN = 25.4

# --- Power pack (includes compression system), lies on its widest face --------
PACK_L = 17.5 * IN          # 444.5  along X
PACK_D = 11.0 * IN          # 279.4  along Y
PACK_H = 6.0 * IN           # 152.4  along Z

# --- Chassis battery bay --------------------------------------------------------
BAY_L = 18.0 * IN           # 457.2  max outer length of the enclosure
BAY_D = 10.0 * IN           # 254.0  max OUTER depth of the narrow upper section
MAX_INNER_HEIGHT = 7.0 * IN  # 177.8 INNER cavity height (pack 6 in + 1 in upper section).
#   NOTE: the spec text says "Outer height <= 177.8 (MAX_OUTER_HEIGHT)". The owner
#   clarified that the 7 in is the cavity and does NOT include floor and roof
#   thickness, so floor and roof sit outside the 7 in frame window.

# --- Clearances / fits ----------------------------------------------------------
CLEARANCE = 1.0             # pack to shell, every side except the floor it rests on
FIT = 0.25                  # printed-fit clearance per side for mating joints

# --- Wall thicknesses (multiples of 0.4) ---------------------------------------
# VARIANT "spec"  = thicknesses exactly as written in SPEC.md (owner's choice, default).
# VARIANT "thick" = the heavier set proposed on 2026-10-14 so every heat-set insert has
#                   >= 2 mm of plastic around it (long walls 8, shoulder 6, floor 12, roof 6).
# The joint dimensions below are derived from these, so both variants build; the script
# WARNS wherever an insert or countersink has less than MIN_FEATURE of material around it.
VARIANT = "spec"
if VARIANT == "spec":
    WALL_LONG = 5.0         # lower-zone long walls (depth direction, crash zone)
    WALL_END = 4.0          # end walls
    WALL_UPPER = 4.0        # 45 deg shoulder slab and narrow upper walls
    FLOOR_T = 5.0           # floor tiles
    ROOF_T = 4.0            # service cover plate
elif VARIANT == "thick":
    WALL_LONG, WALL_END, WALL_UPPER, FLOOR_T, ROOF_T = 8.0, 4.0, 6.0, 12.0, 6.0
else:
    raise ValueError(VARIANT)
FLOOR_RABBET = 1.0          # long walls sit this deep in a recess in the floor tiles

# --- Fasteners ------------------------------------------------------------------
M3_INSERT_D = 4.0
M3_INSERT_DEPTH = 6.0
INSERT_SKIN = 1.0           # plastic left under a blind insert hole
M3_CLEAR_D = 3.4
M3_CSK_D = 6.0              # DIN 7991 head dia
M4_INSERT_D = 5.6
M4_INSERT_DEPTH = 8.0
MAX_SCREW_SPACING = 80.0

# --- Floor tile grid ------------------------------------------------------------
TILE_SPLIT_X = 75.75        # X joints at +/- this (3 columns, each <= 240)
TILE_SPLIT_Y = 20.0         # single Y joint, offset from 0 to stagger vs end-wall split
LAP_W = 12.0                # half-lap overlap width
TONGUE_FRAC = 0.42          # lower (tongue) half of a lap = this fraction of the thickness

# --- Panel splits (all staggered against each other) ---------------------------
WALL_SPLIT_X = 0.0          # long walls: 2 panels per side
COVER_SPLITS_X = (-45.0, 97.25)  # service cover: 3 segments (rear / middle / front)
COVER_SPLIT_Y = 85.0             # each segment split again into a 212 mm main half (-Y)
#                                  and a 42 mm strip (+Y); half-lap with screw bosses
COVER_LAP_W = 12.0
COVER_LAP_BOSS_D = 8.0
COVER_LAP_BOSS_H = 5.0
COVER_LAP_SCREW_X = ((-200.0, -130.0, -60.0), (-5.0, 65.0), (125.0, 195.0))  # per segment
# end walls split at Y = 0 (2 halves each)

# --- Long-wall / floor screws (X positions on the +X panel; mirrored for -X) ---
FLOOR_SCREW_X = (18.0, 50.0, 105.0, 160.0, 212.0)

# --- Cover screws (X positions, symmetric about 0; Y position derived) ---------
COVER_SCREW_X = (35.0, 80.0, 117.0, 172.0)   # +/- each, into long-wall shoulder pads
COVER_END_SCREW_YS = (60.0, 105.0)           # +/- each, into end-wall top pads
PAD_LEN_X = 12.0                             # shoulder pad length along X
PAD_INNER_Y = 108.0                          # shoulder pad inner face |Y|
PAD_Z0_ABOVE_SHOULDER = 6.6                  # pad bottom above shoulder start
LIP_W = 3.0                                  # cover lip rabbet width in slab top edge
LIP_H = 4.0                                  # cover lip depth

# --- Components in the upper zone (placeholders) -------------------------------
BMS_L, BMS_W, BMS_H = 127.0, 127.0, 12.7     # MEASURE_ME  (ANT BMS plate, lies flat)
BMS_STANDOFF_MIN = 3.0
BMS_CONNECTOR_CLEARANCE = 25.0               # on BMS_CONNECTOR_SIDE
BMS_CONNECTOR_SIDE = "rear"                  # "rear" (-X) or "front" (+X)   TBD
BMS_HOLES = [(-55.0, -55.0), (-55.0, 55.0), (55.0, -55.0), (55.0, 55.0)]  # TODO measure
BMS_BOSS_D = 8.0

FUSE_L, FUSE_W, FUSE_H = 125.0, 60.0, 50.0   # MEASURE_ME (ZOOKOTO Class T 100 A, cover on)
FUSE_ROT = 90.0                              # 90 = block length along Y (depth)
FUSE_STANDOFF_MIN = 3.0
FUSE_LUG_CLEARANCE = 20.0                    # beyond each end of the block
FUSE_HOLES = [(-50.0, 0.0), (50.0, 0.0)]     # TODO measure (along block length)
FUSE_BOSS_D = 10.0
FUSE_POCKET_ENABLE = False
FUSE_POCKET_EXTRA_HEIGHT = 31.0              # only used when FUSE_POCKET_ENABLE

BMS_FUSE_AIR_GAP = 10.0
PARTITION_T = 2.0

# --- Layout along X in the upper zone (component centres) -----------------------
BMS_CENTER_X = None          # None = as far rear as the connector clearance allows
FUSE_CENTER_X = 26.0
PARTITION_X = -25.0          # centre of the 2 mm insulating partition

# --- Cable zone (top cover, front, no holes cut - owner drills) ----------------
CABLE_ZONE_W = 80.0          # across Y
CABLE_ZONE_L = 120.0         # along X
CABLE_ZONE_X = None          # None = front 120 mm of the cover, inside the skirt
CABLE_ZONE_Y = 0.0
CABLE_ZONE_T = 6.0           # local cover thickness in the zone (no-op if ROOF_T already >= this)
CABLE_ZONE_ENGRAVE = 0.4     # outline depth on the inner face
CABLE_ZONE_ENGRAVE_W = 0.8

# --- Exterior ---------------------------------------------------------------------
OUTER_CHAMFER = 2.0
FLOOR_EDGE_CHAMFER = 1.0     # tile bottom edges (screw countersinks sit close to the edge)

# --- Placeholders (TODO) ---------------------------------------------------------
MOUNT_POINTS = []            # [(x, y, hole_d, boss_d)] on the upper zone - DO NOT INVENT
TERMINAL_CUTOUTS = []        # TODO
VENTS = []                   # TODO

# --- Printer ------------------------------------------------------------------------
MAX_PART = 240.0
MIN_FEATURE = 0.8
ASA_DENSITY = 1.07           # g/cm3, for a solid-mass upper bound

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# DERIVED GEOMETRY
# =============================================================================
IN_L = PACK_L + 2 * CLEARANCE                 # 446.5
IN_D = PACK_D + 2 * CLEARANCE                 # 281.4
OUT_L = IN_L + 2 * WALL_END                   # 454.5
OUT_D_LOW = IN_D + 2 * WALL_LONG              # 297.4
OUT_D_UP = BAY_D                              # 254.0
HX = OUT_L / 2                                # 227.25 outer half length
HXI = IN_L / 2                                # 223.25 inner half length
Y_OUT_LOW = OUT_D_LOW / 2                     # 148.7
Y_IN_LOW = IN_D / 2                           # 140.7
Y_OUT_UP = OUT_D_UP / 2                       # 127.0
Y_IN_UP = Y_OUT_UP - WALL_UPPER               # 121.0

Z_FLOOR = FLOOR_T                             # inner floor plane (pack rests here)
Z_WALL_BOT = FLOOR_T - FLOOR_RABBET           # long walls sit in a 1 mm recess
Z_PACK_TOP = Z_FLOOR + PACK_H
Z_SH0 = Z_PACK_TOP + CLEARANCE                # shoulder starts here (outer and inner)
SH_RUN = Y_OUT_LOW - Y_OUT_UP                 # 21.7 horizontal run of the 45 deg shoulder
Z_SH1 = Z_SH0 + SH_RUN                        # top of the sloped outer surface
Z_ROOF_IN = Z_FLOOR + MAX_INNER_HEIGHT        # underside of the cover plate
Z_TOP = Z_ROOF_IN + ROOF_T                    # outer top
C_OUT = Y_OUT_LOW + Z_SH0                     # outer slope line: y + z = C_OUT
C_IN = C_OUT - WALL_UPPER * math.sqrt(2)      # inner slope line: y + z = C_IN
Y_SLAB_TOP_IN = C_IN - Z_SH1                  # inner edge of the slab top face
Z_LIP_BOT = Z_SH1 - LIP_H                     # bottom of the lip rabbet
FREE_H_UPPER = MAX_INNER_HEIGHT - PACK_H - CLEARANCE   # 24.4 free above pack
TONGUE_T = round(FLOOR_T * TONGUE_FRAC / 0.2) * 0.2          # floor lap tongue thickness
COVER_LAP_T = round(ROOF_T * TONGUE_FRAC / 0.2) * 0.2         # cover lap lower-half thickness
TONGUE_WALL_T = round(WALL_LONG / 3.0 / 0.2) * 0.2            # long-wall X-joint tongue
# blind insert depth available in a tile rabbet (above the tongue, keep a skin)
TILE_INSERT_DEPTH = min(M3_INSERT_DEPTH, FLOOR_T - TONGUE_T - FIT - INSERT_SKIN)
TILE_SCREWS_FEASIBLE = TILE_INSERT_DEPTH >= 3.0
# standoffs grow only if the plate is too thin to hold the insert with a skin
BMS_STANDOFF = max(BMS_STANDOFF_MIN, M3_INSERT_DEPTH + INSERT_SKIN - ROOF_T)
FUSE_STANDOFF = max(FUSE_STANDOFF_MIN, M4_INSERT_DEPTH + INSERT_SKIN - ROOF_T)
PAD_Z0 = Z_SH0 + PAD_Z0_ABOVE_SHOULDER
COVER_SCREW_Y = (PAD_INNER_Y + Y_SLAB_TOP_IN) / 2.0    # centred in the pad column
END_PAD_X0 = HXI - 10.0                       # end-wall top pad, 10 mm thick in X
END_PAD_Z0 = Z_ROOF_IN - 14.8
END_PAD_W = 14.0
COVER_END_SCREW_X = (END_PAD_X0 + HXI) / 2.0
SKIRT_W = WALL_UPPER
Z_LAP = Z_ROOF_IN + COVER_LAP_T               # top of the cover's lower lap
COVER_LAP_Y = COVER_SPLIT_Y + COVER_LAP_W / 2 # lap screw line

if CABLE_ZONE_X is None:
    CABLE_ZONE_X = HX - SKIRT_W - CABLE_ZONE_L / 2.0

if BMS_CONNECTOR_SIDE == "rear":
    BMS_X0 = -HXI + BMS_CONNECTOR_CLEARANCE
    BMS_X1 = BMS_X0 + BMS_L
else:
    BMS_X1 = PARTITION_X - PARTITION_T / 2 - BMS_FUSE_AIR_GAP - BMS_CONNECTOR_CLEARANCE
    BMS_X0 = BMS_X1 - BMS_L
if BMS_CENTER_X is not None:
    BMS_X0 = BMS_CENTER_X - BMS_L / 2
    BMS_X1 = BMS_X0 + BMS_L
BMS_CX = (BMS_X0 + BMS_X1) / 2
BMS_Z1 = Z_ROOF_IN - BMS_STANDOFF
BMS_Z0 = BMS_Z1 - BMS_H

FUSE_FX = FUSE_W if FUSE_ROT == 90 else FUSE_L   # footprint along X
FUSE_FY = FUSE_L if FUSE_ROT == 90 else FUSE_W   # footprint along Y
FUSE_ROOF_Z = Z_ROOF_IN + (FUSE_POCKET_EXTRA_HEIGHT if FUSE_POCKET_ENABLE else 0.0)
FUSE_Z1 = FUSE_ROOF_Z - FUSE_STANDOFF
FUSE_Z0 = FUSE_Z1 - FUSE_H

WARNINGS = []
FAILS = []


def warn(msg):
    WARNINGS.append(msg)
    print("WARNING: " + msg)


def fail(msg):
    FAILS.append(msg)
    print("FAIL:    " + msg)


def ok(msg):
    print("OK:      " + msg)


# =============================================================================
# HELPERS
# =============================================================================
MIN3 = (Align.MIN, Align.MIN, Align.MIN)
CCMIN = (Align.CENTER, Align.CENTER, Align.MIN)


def box(x0, x1, y0, y1, z0, z1):
    """Axis-aligned box spanning the given ranges."""
    if x1 <= x0 or y1 <= y0 or z1 <= z0:
        raise ValueError(f"empty box {x0,x1,y0,y1,z0,z1}")
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=MIN3)


def cyl(x, y, z0, z1, d):
    return Pos(x, y, z0) * Cylinder(d / 2, z1 - z0, align=CCMIN)


def csk_cutter(x, y, z_face, outward, through, d_hole=M3_CLEAR_D, d_head=M3_CSK_D):
    """Countersunk through hole. z_face = outer face; outward = +1 if the outer face
    normal is +Z, -1 if -Z. `through` = material thickness along the screw."""
    depth = (d_head - d_hole) / 2.0  # 90 deg countersink
    if outward > 0:
        shank = cyl(x, y, z_face - through - 1, z_face + 1, d_hole)
        cone = Pos(x, y, z_face - depth) * Cone(d_hole / 2, d_head / 2, depth, align=CCMIN)
        cap = cyl(x, y, z_face - 0.01, z_face + 1, d_head)
    else:
        shank = cyl(x, y, z_face - 1, z_face + through + 1, d_hole)
        cone = Pos(x, y, z_face) * Cone(d_head / 2, d_hole / 2, depth, align=CCMIN)
        cap = cyl(x, y, z_face - 1, z_face + 0.01, d_head)
    return shank + cone + cap


def insert_hole(x, y, z_face, direction, d, depth):
    """Blind heat-set insert hole starting at z_face going `direction` (+1 up, -1 down)."""
    if direction > 0:
        return cyl(x, y, z_face - 0.5, z_face + depth, d)
    return cyl(x, y, z_face - depth, z_face + 0.5, d)


def prism_yz(pts, x0, x1):
    """Extrude a (y, z) polygon along X from x0 to x1."""
    face = Plane.YZ * Polygon(*pts, align=None)
    return Pos(x0, 0, 0) * extrude(face, x1 - x0)


def union(shapes):
    out = None
    for s in shapes:
        out = s if out is None else out + s
    return out


def try_chamfer(part, edges, size, what):
    if not edges:
        warn(f"{what}: no edges selected for chamfer")
        return part
    try:
        return chamfer(edges, size)
    except Exception as e:  # pragma: no cover - OCC dependent
        warn(f"{what}: chamfer {size} mm failed ({type(e).__name__}); left square")
        return part


def try_fillet(part, edges, size, what):
    if not edges:
        warn(f"{what}: no edges selected for fillet")
        return part
    try:
        return fillet(edges, size)
    except Exception as e:  # pragma: no cover
        warn(f"{what}: fillet {size} mm failed ({type(e).__name__}); left square")
        return part


def edges_where(part, pred, axis=None):
    es = part.edges() if axis is None else part.edges().filter_by(axis)
    return ShapeList([e for e in es if pred(e)])


def place_flat(part, rot):
    """Rotate so the outer face is on the bed, then move bbox min to the origin."""
    p = rot * part if rot is not None else part
    bb = p.bounding_box()
    return Pos(-bb.min.X, -bb.min.Y, -bb.min.Z) * p


def rot_z180(part):
    return Rot(0, 0, 180) * part


def near(a, b, tol=0.05):
    return abs(a - b) < tol


# =============================================================================
# GHOST SOLIDS
# =============================================================================
pack = box(-PACK_L / 2, PACK_L / 2, -PACK_D / 2, PACK_D / 2, Z_FLOOR, Z_PACK_TOP)
pack.label = "GHOST_pack"
pack.color = Color(0.2, 0.6, 1.0, 0.35)

bms = box(BMS_X0, BMS_X1, -BMS_W / 2, BMS_W / 2, BMS_Z0, BMS_Z1)
bms.label = "GHOST_bms"
bms.color = Color(0.2, 0.9, 0.3, 0.45)

fuse = box(FUSE_CENTER_X - FUSE_FX / 2, FUSE_CENTER_X + FUSE_FX / 2,
           -FUSE_FY / 2, FUSE_FY / 2, FUSE_Z0, FUSE_Z1)
fuse.label = "GHOST_fuse_block"
fuse.color = Color(1.0, 0.5, 0.1, 0.45)

# pack grown by (CLEARANCE - eps) sideways and upward: nothing may enter it
EPS = 0.01
pack_keepout = box(-PACK_L / 2 - CLEARANCE + EPS, PACK_L / 2 + CLEARANCE - EPS,
                   -PACK_D / 2 - CLEARANCE + EPS, PACK_D / 2 + CLEARANCE - EPS,
                   Z_FLOOR + EPS, Z_PACK_TOP + CLEARANCE - EPS)

# =============================================================================
# FLOOR TILES  (3 columns x 2 rows, half-lap joints, countersunk screws from below)
# =============================================================================
# Lower (tongue) half owners and upper (rabbet) half owners are defined so that
# every point of the floor has exactly one lower and one upper owner.
XS = [-HX, -TILE_SPLIT_X, TILE_SPLIT_X, HX]
YS = [-Y_OUT_LOW, TILE_SPLIT_Y, Y_OUT_LOW]
tile_names = {(0, 0): "rear_left", (1, 0): "mid_left", (2, 0): "front_left",
              (0, 1): "rear_right", (1, 1): "mid_right", (2, 1): "front_right"}
# (left = -Y, right = +Y, rear = -X, front = +X)


def tile_lower_range(i, j):
    """Lower half (z 0..TONGUE_T) footprint. Centre column has tongues on both X
    edges; -Y row has the tongue on its +Y edge."""
    x0, x1 = XS[i], XS[i + 1]
    if i == 0:
        x1 = x1 - LAP_W
    elif i == 1:
        x0, x1 = x0 - LAP_W + FIT, x1 + LAP_W - FIT
    else:
        x0 = x0 + LAP_W
    y0, y1 = YS[j], YS[j + 1]
    if j == 0:
        y1 = y1 + LAP_W - FIT
    else:
        y0 = y0 + LAP_W
    return x0, x1, y0, y1


def tile_upper_range(i, j):
    """Upper half (z TONGUE_T+FIT..FLOOR_T) footprint: plain grid cell."""
    x0, x1 = XS[i], XS[i + 1]
    y0, y1 = YS[j], YS[j + 1]
    # shrink the rabbet-side edges by FIT so adjacent tiles do not touch
    if i == 0:
        x1 -= FIT
    elif i == 1:
        x0 += FIT
        x1 -= FIT
    else:
        x0 += FIT
    if j == 0:
        y1 -= FIT
    else:
        y0 += FIT
    return x0, x1, y0, y1


tiles = {}
for (i, j), name in tile_names.items():
    lx0, lx1, ly0, ly1 = tile_lower_range(i, j)
    ux0, ux1, uy0, uy1 = tile_upper_range(i, j)
    t = box(lx0, lx1, ly0, ly1, 0, TONGUE_T) + box(ux0, ux1, uy0, uy1, TONGUE_T + FIT, FLOOR_T)
    # the two halves must be one solid: add the overlap region (full thickness
    # where both footprints coincide) so there is no FIT-thick gap inside a tile
    ox0, ox1 = max(lx0, ux0), min(lx1, ux1)
    oy0, oy1 = max(ly0, uy0), min(ly1, uy1)
    t = t + box(ox0, ox1, oy0, oy1, 0, FLOOR_T)
    tiles[name] = t

# recess for the long walls (both sides, full length)
wall_recess = (box(-HX - 1, HX + 1, Y_IN_LOW, Y_OUT_LOW + 1, Z_WALL_BOT, FLOOR_T + 1)
               + box(-HX - 1, HX + 1, -Y_OUT_LOW - 1, -Y_IN_LOW, Z_WALL_BOT, FLOOR_T + 1))
# groove for the end-wall bottom tongue
EW_X0, EW_X1 = HXI, HX                     # end wall occupies this X band (front)
EW_TONGUE_T, EW_TONGUE_H = 2.0, 3.0
ew_groove_cx = (EW_X0 + EW_X1) / 2
end_grooves = union([
    box(sx * ew_groove_cx - (EW_TONGUE_T / 2 + FIT), sx * ew_groove_cx + (EW_TONGUE_T / 2 + FIT),
        -(Y_OUT_LOW - WALL_LONG + FIT), (Y_OUT_LOW - WALL_LONG + FIT),
        FLOOR_T - EW_TONGUE_H, FLOOR_T + 1) for sx in (1, -1)])

# --- floor screw cutters ------------------------------------------------------------
tile_cutters = []
# (a) long wall screws: through tile (csk from below) into wall bottom edge inserts
WALL_SCREW_Y = (Y_IN_LOW + Y_OUT_LOW) / 2.0
wall_floor_screws = []
for sx in (1, -1):
    for x in FLOOR_SCREW_X:
        for sy in (1, -1):
            wall_floor_screws.append((sx * x, sy * WALL_SCREW_Y))
for (x, y) in wall_floor_screws:
    tile_cutters.append(csk_cutter(x, y, 0.0, -1, Z_WALL_BOT))


def spread(a, b, max_sp, margin):
    """Evenly spaced positions between a+margin and b-margin, spacing <= max_sp."""
    a2, b2 = a + margin, b - margin
    n = max(2, int(math.ceil((b2 - a2) / max_sp)) + 1)
    return [a2 + (b2 - a2) * k / (n - 1) for k in range(n)]


# (b) tile-to-tile screws: through the tongue (csk from below) into the rabbet insert
tile_tile_screws = []   # (x, y) ; tongue tile is pierced, rabbet tile gets the insert
for sx in (1, -1):
    xj = sx * (TILE_SPLIT_X + LAP_W / 2)           # X joints: centre column has tongue
    for j in range(2):
        y0, y1 = YS[j], YS[j + 1]
        if j == 0:
            y1 = y1 - LAP_W / 2                     # stay clear of the Y lap zone
        else:
            y0 = y0 + LAP_W + 4
        for y in spread(y0, y1, MAX_SCREW_SPACING, 18.0):
            tile_tile_screws.append((xj, y))
yj = TILE_SPLIT_Y + LAP_W / 2                       # Y joint: -Y row has the tongue
for i in range(3):
    x0, x1 = XS[i], XS[i + 1]
    if i == 0:
        x1 = x1 - LAP_W - 4
    elif i == 1:
        x0, x1 = x0 + LAP_W + 4, x1 - LAP_W - 4
    else:
        x0 = x0 + LAP_W + 4
    for x in spread(x0, x1, MAX_SCREW_SPACING, 18.0):
        tile_tile_screws.append((x, yj))
for (x, y) in tile_tile_screws:
    if not TILE_SCREWS_FEASIBLE:
        break
    tile_cutters.append(csk_cutter(x, y, 0.0, -1, TONGUE_T))
    if TILE_SCREWS_FEASIBLE:
        tile_cutters.append(insert_hole(x, y, TONGUE_T + FIT, +1, M3_INSERT_D, TILE_INSERT_DEPTH))

tile_cut = union(tile_cutters) + wall_recess + end_grooves

for name in tiles:
    t = tiles[name]
    # outer bottom edge chamfer (box perimeter only)
    es = edges_where(
        t, lambda e: near(e.center().Z, 0) and (near(abs(e.center().X), HX) or near(abs(e.center().Y), Y_OUT_LOW))
        and e.length > 30)
    t = try_chamfer(t, es, FLOOR_EDGE_CHAMFER, f"tile {name}")
    t = t - tile_cut
    t.label = f"floor_tile_{name}"
    t.color = Color(0.55, 0.55, 0.6)
    tiles[name] = t

# =============================================================================
# LONG WALL PANELS (+Y side built; -Y side = 180 deg rotation about Z)
# =============================================================================
# cross-section (y, z) of the wall + shoulder slab, +Y side
wall_profile = [
    (Y_OUT_LOW, Z_WALL_BOT), (Y_OUT_LOW, Z_SH0), (Y_OUT_UP, Z_SH1),
    (Y_SLAB_TOP_IN, Z_SH1), (C_IN - Z_SH0, Z_SH0), (Y_IN_LOW, Z_SH0), (Y_IN_LOW, Z_WALL_BOT),
]
outer_profile = [  # solid region inside the outer skin (for clipping pads)
    (0, Z_WALL_BOT), (Y_OUT_LOW, Z_WALL_BOT), (Y_OUT_LOW, Z_SH0), (Y_OUT_UP, Z_SH1),
    (Y_OUT_UP, Z_TOP + 1), (0, Z_TOP + 1),
]
assert abs((Y_SLAB_TOP_IN - (C_IN - Z_SH0)) - (Z_SH0 - Z_SH1)) < 1e-6  # 45 deg inner slope



def make_long_wall(x0, x1, joint="tongue"):
    """Panel from x0 to x1 on the +Y side. The X joint with the neighbour panel is at
    WALL_SPLIT_X; `joint` says whether this panel carries the tongue or the groove."""
    p = prism_yz(wall_profile, x0, x1)
    # outer edge chamfers FIRST, on the clean prism: vertical end corner(s) + shoulder edge
    es_end = edges_where(p, lambda e: near(abs(e.center().X), HX) and near(e.center().Y, Y_OUT_LOW)
                         and e.length > 50, Axis.Z)
    es_sh = edges_where(p, lambda e: near(e.center().Y, Y_OUT_LOW) and near(e.center().Z, Z_SH0)
                        and e.length > 50, Axis.X)
    try:
        p = chamfer(ShapeList(list(es_end) + list(es_sh)), OUTER_CHAMFER)
    except Exception:
        p = try_chamfer(p, es_sh, OUTER_CHAMFER, "long wall shoulder edge")
        warn("long wall end edge: chamfer skipped (would not chain with shoulder chamfer)")
    outer = prism_yz(outer_profile, x0 - 5, x1 + 5)
    # end rabbet for the end wall: remove inner half of the wall beyond HXI, and the
    # whole slab beyond HXI (end wall covers the slab end)
    for sx in (1, -1):
        xa, xb = sorted((sx * HXI, sx * (HX + 1)))
        if xb > x0 and xa < x1:
            p = p - box(xa, xb, Y_IN_LOW - 1, Y_IN_LOW + WALL_END + FIT, Z_WALL_BOT - 1, Z_SH0 + 0.0)
            p = p - box(xa, xb, 0, Y_OUT_LOW + 2, Z_SH0, Z_TOP + 2)
    # shoulder pads for the cover screws (inside the slope, above the pack)
    pads = []
    for sx in (1, -1):
        for x in COVER_SCREW_X:
            cx = sx * x
            if x0 + 1 < cx < x1 - 1:
                pad = box(cx - PAD_LEN_X / 2, cx + PAD_LEN_X / 2, PAD_INNER_Y, Y_OUT_LOW, PAD_Z0, Z_ROOF_IN)
                pads.append(pad & outer)
    if pads:
        p = p + union(pads)
    # lip rabbet along the slab top edge (inner side), full panel length
    p = p - box(x0 - 1, x1 + 1, Y_SLAB_TOP_IN - 0.5, Y_SLAB_TOP_IN + LIP_W, Z_LIP_BOT, Z_TOP + 2)
    # nothing may stand in the skirt seat
    p = p - box(x0 - 1, x1 + 1, Y_SLAB_TOP_IN + LIP_W, Y_OUT_LOW + 2, Z_SH1, Z_TOP + 2)
    # X joint tongue / groove with the neighbouring panel
    xj = WALL_SPLIT_X
    if x0 < xj < x1:
        raise ValueError("panel spans its own split")
    if near(x0, xj) or near(x1, xj):
        sign = -1 if near(x0, xj) else 1          # tongue sticks out past this end
        yc = WALL_SCREW_Y
        if joint == "tongue":
            tongue = box(min(xj, xj + sign * (3.0 - FIT)), max(xj, xj + sign * (3.0 - FIT)),
                         yc - TONGUE_WALL_T / 2, yc + TONGUE_WALL_T / 2, Z_WALL_BOT + FIT, Z_SH0 - FIT)
            p = p + tongue
        else:
            groove = box(min(xj, xj - sign * 3.0) - (0 if sign > 0 else 0), max(xj, xj - sign * 3.0),
                         yc - TONGUE_WALL_T / 2 - FIT, yc + TONGUE_WALL_T / 2 + FIT, Z_WALL_BOT - 1, Z_SH0)
            # groove is cut INTO this panel (which lies on the other side of xj)
            p = p - groove
    # floor screw inserts in the bottom edge
    cut = []
    for sx in (1, -1):
        for x in FLOOR_SCREW_X:
            cx = sx * x
            if x0 + 2 < cx < x1 - 2:
                cut.append(insert_hole(cx, WALL_SCREW_Y, Z_WALL_BOT, +1, M3_INSERT_D, M3_INSERT_DEPTH))
    # cover screw inserts in the pads (from the top)
    for sx in (1, -1):
        for x in COVER_SCREW_X:
            cx = sx * x
            if x0 + 1 < cx < x1 - 1:
                cut.append(insert_hole(cx, COVER_SCREW_Y, Z_ROOF_IN, -1, M3_INSERT_D, M3_INSERT_DEPTH))
    p = p - union(cut)
    return p


lw_front_R = make_long_wall(WALL_SPLIT_X, HX, "tongue")     # +Y, +X : tongue at x=0
lw_rear_R = make_long_wall(-HX, WALL_SPLIT_X, "groove")     # +Y, -X : groove at x=0
lw_rear_L = rot_z180(lw_front_R)                            # -Y, -X : tongue
lw_front_L = rot_z180(lw_rear_R)                            # -Y, +X : groove
for p, n in ((lw_front_R, "long_wall_tongue (right front)"), (lw_rear_R, "long_wall_groove (right rear)"),
             (lw_rear_L, "long_wall_tongue (left rear)"), (lw_front_L, "long_wall_groove (left front)")):
    p.label = n
    p.color = Color(0.75, 0.75, 0.78)

# =============================================================================
# END WALLS (front built, split at Y = 0; rear = 180 deg rotation about Z)
# =============================================================================
EW_HALF_W = Y_OUT_LOW - WALL_LONG - FIT          # tucked inside the long-wall skins
end_profile = [
    (-EW_HALF_W, Z_FLOOR), (EW_HALF_W, Z_FLOOR), (EW_HALF_W, Z_SH0), (Y_OUT_LOW, Z_SH0),
    (Y_OUT_UP, Z_SH1), (-Y_OUT_UP, Z_SH1), (-Y_OUT_LOW, Z_SH0), (-EW_HALF_W, Z_SH0),
]


def make_end_wall_half(side):
    """Front end wall, `side` = -1 (y<0, carries the Y=0 tongue) or +1 (y>0, groove)."""
    full = prism_yz(end_profile, EW_X0, EW_X1)
    # bottom tongue into the floor groove
    tongue_b = box(ew_groove_cx - EW_TONGUE_T / 2, ew_groove_cx + EW_TONGUE_T / 2,
                   -EW_HALF_W, EW_HALF_W, FLOOR_T - EW_TONGUE_H + FIT, FLOOR_T + 0.01)
    full = full + tongue_b
    # top pads (inside, above the pack) for the cover end screws
    for py in COVER_END_SCREW_YS:
        pad = box(END_PAD_X0, EW_X0 + 0.01, side * py - END_PAD_W / 2,
                  side * py + END_PAD_W / 2, END_PAD_Z0, Z_ROOF_IN)
        pad = pad - box(EW_X1 - SKIRT_W, EW_X1 + 1, -200, 200, Z_SH1, Z_TOP + 1)   # skirt seat
        full = full + pad
    # halve it
    if side < 0:
        half = full & box(EW_X0 - 20, EW_X1 + 20, -400, 0.0, -10, Z_TOP + 10)
        t = box(ew_groove_cx - 0.75, ew_groove_cx + 0.75, 0.0, 3.0 - FIT, Z_FLOOR + FIT, Z_SH1 - FIT)
        half = half + t
    else:
        half = full & box(EW_X0 - 20, EW_X1 + 20, FIT, 400, -10, Z_TOP + 10)
        g = box(ew_groove_cx - 0.75 - FIT, ew_groove_cx + 0.75 + FIT, FIT - 0.01, 3.0 + FIT, Z_FLOOR - 1, Z_SH1 + 1)
        half = half - g
    # outer chamfer along the sloped edge (outer face x = EW_X1)
    es = edges_where(half, lambda e: near(e.center().X, EW_X1) and e.length > 20
                     and abs(abs(e.center().Y) - (Y_OUT_LOW + Y_OUT_UP) / 2) < 1.0)
    half = try_chamfer(half, es, OUTER_CHAMFER, "end wall shoulder edge")
    # cover end screw inserts
    for py in COVER_END_SCREW_YS:
        half = half - insert_hole(COVER_END_SCREW_X, side * py, Z_ROOF_IN, -1,
                                  M3_INSERT_D, M3_INSERT_DEPTH)
    return half


ew_front_L = make_end_wall_half(-1)
ew_front_R = make_end_wall_half(+1)
ew_rear_R = rot_z180(ew_front_L)
ew_rear_L = rot_z180(ew_front_R)
for p, n in ((ew_front_L, "end_wall_half_tongue (front left)"), (ew_front_R, "end_wall_half_groove (front right)"),
             (ew_rear_R, "end_wall_half_tongue (rear right)"), (ew_rear_L, "end_wall_half_groove (rear left)")):
    p.label = n
    p.color = Color(0.7, 0.72, 0.8)

# =============================================================================
# SERVICE COVER (3 segments) with hanging component mounts
# =============================================================================
COVER_X_EDGES = [-HX, COVER_SPLITS_X[0], COVER_SPLITS_X[1], HX]
cover_names = ["cover_rear", "cover_middle", "cover_front"]


def make_cover(k):
    x0, x1 = COVER_X_EDGES[k], COVER_X_EDGES[k + 1]
    if k > 0:
        x0 += FIT / 2
    if k < 2:
        x1 -= FIT / 2
    c = box(x0, x1, -Y_OUT_UP, Y_OUT_UP, Z_ROOF_IN, Z_TOP)
    # long-side skirt + lip
    lip_x1 = min(x1, HXI - FIT)
    lip_x0 = max(x0, -HXI + FIT)
    for sy in (1, -1):
        ya, yb = sorted((sy * (Y_SLAB_TOP_IN + FIT), sy * Y_OUT_UP))
        c = c + box(x0, x1, ya, yb, Z_SH1, Z_ROOF_IN + 0.01)                    # skirt
        la, lb = sorted((sy * (Y_SLAB_TOP_IN + FIT), sy * (Y_SLAB_TOP_IN + LIP_W - FIT)))
        c = c + box(lip_x0, lip_x1, la, lb, Z_LIP_BOT + FIT, Z_ROOF_IN + 0.01)   # lip
    # end skirt
    if k == 2:
        c = c + box(HX - SKIRT_W, HX, -Y_OUT_UP, Y_OUT_UP, Z_SH1, Z_ROOF_IN + 0.01)
    if k == 0:
        c = c + box(-HX, -HX + SKIRT_W, -Y_OUT_UP, Y_OUT_UP, Z_SH1, Z_ROOF_IN + 0.01)
    cut = []
    # cover screws into long-wall pads
    for sx in (1, -1):
        for x in COVER_SCREW_X:
            cx = sx * x
            if x0 + 1 < cx < x1 - 1:
                for sy in (1, -1):
                    cut.append(csk_cutter(cx, sy * COVER_SCREW_Y, Z_TOP, +1, ROOF_T))
    # cover screws into end-wall pads
    if k in (0, 2):
        sx = 1 if k == 2 else -1
        for sy in (1, -1):
            for py in COVER_END_SCREW_YS:
                cut.append(csk_cutter(sx * COVER_END_SCREW_X, sy * py, Z_TOP, +1, ROOF_T))
    # ---- front: cable zone (local thickening + engraved outline, NO holes) ----
    if k == 2:
        zx0, zx1 = CABLE_ZONE_X - CABLE_ZONE_L / 2, CABLE_ZONE_X + CABLE_ZONE_L / 2
        zy0, zy1 = CABLE_ZONE_Y - CABLE_ZONE_W / 2, CABLE_ZONE_Y + CABLE_ZONE_W / 2
        assert x0 < zx0 and zx1 <= HX - SKIRT_W + 0.01, "cable zone outside front cover"
        assert zy1 < COVER_SPLIT_Y - 1, "cable zone must lie entirely on the main cover half"
        zone_t = max(CABLE_ZONE_T, ROOF_T)
        if zone_t > ROOF_T:
            c = c + box(zx0, zx1, zy0, zy1, Z_TOP - zone_t, Z_ROOF_IN + 0.01)
        zi = Z_TOP - zone_t
        w = CABLE_ZONE_ENGRAVE_W
        ring = (box(zx0, zx1, zy0, zy1, zi - 0.01, zi + CABLE_ZONE_ENGRAVE)
                - box(zx0 + w, zx1 - w, zy0 + w, zy1 - w, zi - 1, zi + 1))
        cut.append(ring)
    # ---- rear: BMS standoffs (hang from the cover) ----
    if k == 0:
        for (hx, hy) in BMS_HOLES:
            bx, by = BMS_CX + hx, hy
            assert x0 + BMS_BOSS_D / 2 < bx < x1 - BMS_BOSS_D / 2, "BMS boss outside rear cover"
            c = c + cyl(bx, by, Z_ROOF_IN - BMS_STANDOFF, Z_ROOF_IN + 0.01, BMS_BOSS_D)
            cut.append(insert_hole(bx, by, Z_ROOF_IN - BMS_STANDOFF, +1, M3_INSERT_D, M3_INSERT_DEPTH))
    # ---- middle: fuse bosses, partition, optional pocket ----
    if k == 1:
        roof_z = Z_ROOF_IN
        if FUSE_POCKET_ENABLE:
            E = FUSE_POCKET_EXTRA_HEIGHT
            hx_t, hy_t = FUSE_FX / 2 + 5 + WALL_UPPER - 2, FUSE_FY / 2 + 5 + WALL_UPPER - 2
            outer = loft([Plane.XY.offset(Z_TOP) * Pos(FUSE_CENTER_X, 0) * Rectangle(2 * (hx_t + E), 2 * (hy_t + E)),
                          Plane.XY.offset(Z_TOP + E) * Pos(FUSE_CENTER_X, 0) * Rectangle(2 * hx_t, 2 * hy_t)])
            ihx, ihy = hx_t - ROOF_T, hy_t - ROOF_T
            inner = loft([Plane.XY.offset(Z_ROOF_IN - 0.01) * Pos(FUSE_CENTER_X, 0) * Rectangle(2 * (ihx + E + ROOF_T), 2 * (ihy + E + ROOF_T)),
                          Plane.XY.offset(Z_TOP + E - ROOF_T) * Pos(FUSE_CENTER_X, 0) * Rectangle(2 * ihx, 2 * ihy)])
            bb = outer.bounding_box()
            if bb.min.X < x0 or bb.max.X > x1 or bb.max.Y > Y_OUT_UP - 2:
                warn(f"fuse pocket base {bb.size.X:.1f} x {bb.size.Y:.1f} mm does not fit on the middle cover")
            if bb.max.Y > COVER_SPLIT_Y - 2:
                warn(f"fuse pocket reaches y={bb.max.Y:.1f}, crossing the cover split at y={COVER_SPLIT_Y}; "
                     f"rotate the block (FUSE_ROT=0) or move the split before enabling the pocket for real")
            c = c + outer - inner
            roof_z = Z_TOP + E - ROOF_T
        for (hx, hy) in FUSE_HOLES:
            # holes are given along the block length; rotate with the block
            if FUSE_ROT == 90:
                fx, fy = FUSE_CENTER_X + hy, hx
            else:
                fx, fy = FUSE_CENTER_X + hx, hy
            assert x0 + FUSE_BOSS_D / 2 < fx < x1 - FUSE_BOSS_D / 2, "fuse boss outside middle cover"
            c = c + cyl(fx, fy, roof_z - FUSE_STANDOFF, roof_z + 0.01, FUSE_BOSS_D)
            cut.append(insert_hole(fx, fy, roof_z - FUSE_STANDOFF, +1, M4_INSERT_D, M4_INSERT_DEPTH))
        # insulating partition between fuse and BMS, hangs to 1 mm above pack clearance
        c = c + box(PARTITION_X - PARTITION_T / 2, PARTITION_X + PARTITION_T / 2,
                    -(Y_IN_UP - 1.0), (Y_IN_UP - 1.0), Z_SH0 + 1.0, Z_ROOF_IN + 0.01)
    # top perimeter chamfer
    es = edges_where(c, lambda e: near(e.center().Z, Z_TOP) and e.length > 30
                     and (near(abs(e.center().Y), Y_OUT_UP) or near(abs(e.center().X), HX)))
    c = try_chamfer(c, es, OUTER_CHAMFER, cover_names[k])
    c = c - union(cut)
    # ---- split lengthwise: main half (-Y, 212 mm) and strip (+Y, 42 mm), half-lap ----
    ys = COVER_SPLIT_Y
    main = c & box(x0 - 1, x1 + 1, -400, ys, -10, Z_TOP + 80)
    strip = c & box(x0 - 1, x1 + 1, ys + FIT, 400, -10, Z_TOP + 80)
    main = main + box(x0, x1, ys - 0.01, ys + COVER_LAP_W - FIT, Z_ROOF_IN, Z_LAP)      # lower lap
    if k == 1:   # partition continues under the lap
        main = main + box(PARTITION_X - PARTITION_T / 2, PARTITION_X + PARTITION_T / 2,
                          ys - 0.01, ys + COVER_LAP_W - FIT, Z_SH0 + 1.0, Z_ROOF_IN + 0.01)
    strip = strip - box(x0 - 1, x1 + 1, ys - 1, ys + COVER_LAP_W + FIT, Z_ROOF_IN - 60, Z_LAP + FIT)
    lap_cut_main, lap_cut_strip = [], []
    for lx in COVER_LAP_SCREW_X[k]:
        assert x0 + 5 < lx < x1 - 5, f"lap screw {lx} outside cover segment {k}"
        main = main + cyl(lx, COVER_LAP_Y, Z_ROOF_IN - COVER_LAP_BOSS_H, Z_ROOF_IN + 0.01, COVER_LAP_BOSS_D)
        lap_cut_main.append(insert_hole(lx, COVER_LAP_Y, Z_LAP, -1, M3_INSERT_D, M3_INSERT_DEPTH))
        lap_cut_strip.append(csk_cutter(lx, COVER_LAP_Y, Z_TOP, +1, ROOF_T - COVER_LAP_T))
    main = main - union(lap_cut_main)
    strip = strip - union(lap_cut_strip)
    main.label = cover_names[k] + "_main"
    strip.label = cover_names[k] + "_strip"
    for s in (main, strip):
        s.color = Color(0.85, 0.85, 0.9)
    return [main, strip]


covers = [c for k in range(3) for c in make_cover(k)]

# =============================================================================
# ASSEMBLY
# =============================================================================
shell_parts = (list(tiles.values()) + [lw_front_R, lw_rear_R, lw_rear_L, lw_front_L,
                                       ew_front_L, ew_front_R, ew_rear_R, ew_rear_L] + covers)
ghosts = [pack, bms, fuse]

print("=" * 78)
print("OpenZero battery box  -  geometry report")
print("=" * 78)
print(f"Outer envelope:  L {OUT_L:.1f}  x  D(lower) {OUT_D_LOW:.1f} / D(upper) {OUT_D_UP:.1f}"
      f"  x  H {Z_TOP:.1f} mm   (cavity height {MAX_INNER_HEIGHT:.1f})")
print(f"Shoulder: outer slope from z={Z_SH0:.1f} to z={Z_SH1:.1f} (run {SH_RUN:.1f} mm, 45 deg);"
      f" flat narrow section {Z_ROOF_IN - Z_SH1:.1f} mm + roof {ROOF_T:.1f}")

# ---- assertions required by the spec -------------------------------------------------
print("-" * 78)
if OUT_L <= BAY_L + 1e-6:
    ok(f"length fit: outer {OUT_L:.2f} <= bay {BAY_L:.2f} (spare {BAY_L - OUT_L:.2f} mm total)")
else:
    fail(f"length: outer {OUT_L:.2f} > bay {BAY_L:.2f}")
assert OUT_L <= BAY_L, "enclosure too long for the bay"

per_end = (BAY_L - PACK_L) / 2
print(f"         per end available {per_end:.2f} mm; used clearance {CLEARANCE} + end wall {WALL_END} = {CLEARANCE + WALL_END}")

if OUT_D_UP <= BAY_D + 1e-6:
    ok(f"upper zone outer depth {OUT_D_UP:.1f} <= bay {BAY_D:.1f}")
else:
    fail("upper zone wider than bay")
warn(f"lower zone outer depth {OUT_D_LOW:.1f} mm overhangs the {BAY_D:.1f} mm bay by "
     f"{(OUT_D_LOW - BAY_D) / 2:.1f} mm per side (intentional crash zone, spec).")
warn(f"shoulder is wider than {BAY_D:.0f} mm between z={Z_SH0:.1f} and z={Z_SH1:.1f}, i.e. the first "
     f"{SH_RUN:.1f} mm of the {FREE_H_UPPER + CLEARANCE:.1f} mm upper section. Verify the frame allows this.")

# ---- upper zone height check -------------------------------------------------------
print("-" * 78)
print(f"Upper zone free inner height above pack: {FREE_H_UPPER:.1f} mm "
      f"(= {MAX_INNER_HEIGHT:.1f} - pack {PACK_H:.1f} - clearance {CLEARANCE})")
req_bms = BMS_H + BMS_STANDOFF
req_fuse = FUSE_H + FUSE_STANDOFF
if req_bms <= FREE_H_UPPER:
    ok(f"BMS needs {req_bms:.1f} mm (plate {BMS_H} + standoff {BMS_STANDOFF}) -> fits, {FREE_H_UPPER - req_bms:.1f} mm spare")
else:
    warn(f"BMS needs {req_bms:.1f} mm but only {FREE_H_UPPER:.1f} available")
avail_fuse = FREE_H_UPPER + (FUSE_POCKET_EXTRA_HEIGHT if FUSE_POCKET_ENABLE else 0.0)
if req_fuse <= avail_fuse:
    ok(f"fuse block needs {req_fuse:.1f} mm -> fits (pocket {'on' if FUSE_POCKET_ENABLE else 'off'})")
else:
    warn(f"FUSE BLOCK DOES NOT FIT: needs {req_fuse:.1f} mm (block {FUSE_H} + standoff {FUSE_STANDOFF}), "
         f"available {avail_fuse:.1f} mm. Short by {req_fuse - avail_fuse:.1f} mm. Height NOT increased. "
         f"Either measure the real block (placeholder is MEASURE_ME) or set FUSE_POCKET_ENABLE=True "
         f"with FUSE_POCKET_EXTRA_HEIGHT >= {req_fuse - FREE_H_UPPER:.1f}.")
if not MOUNT_POINTS:
    warn("MOUNT_POINTS is empty - frame mounts are NOT defined. The model builds without them. "
         "Measure the original mount positions on the bike and fill MOUNT_POINTS.")
if not TERMINAL_CUTOUTS:
    print("NOTE:    TERMINAL_CUTOUTS empty (TODO)")
if not VENTS:
    print("NOTE:    VENTS empty (TODO) - the BMS MOSFET stage has no airflow path yet")

# ---- fastener feasibility (material around inserts / under countersinks) ----------------
print("-" * 78)
print(f"Variant '{VARIANT}': long wall {WALL_LONG}, end wall {WALL_END}, shoulder {WALL_UPPER}, floor {FLOOR_T}, roof {ROOF_T} mm")


def meat(label, value, need=MIN_FEATURE):
    if value + 1e-9 >= need:
        ok(f"{label}: {value:.2f} mm (>= {need})")
    else:
        warn(f"{label}: only {value:.2f} mm (< {need} min feature) - weak or unprintable at this thickness")


meat("long wall around floor-screw insert (per side)", (WALL_LONG - M3_INSERT_D) / 2)
meat("long wall around X-joint groove (per side)", (WALL_LONG - TONGUE_WALL_T - 2 * FIT) / 2)
meat("floor tile under wall screw countersink", Z_WALL_BOT - (M3_CSK_D - M3_CLEAR_D) / 2)
meat("floor tile skin above tile-lap insert", FLOOR_T - TONGUE_T - FIT - TILE_INSERT_DEPTH)
if TILE_SCREWS_FEASIBLE:
    ok(f"tile-to-tile lap screws modelled, insert depth {TILE_INSERT_DEPTH:.1f} mm")
else:
    warn(f"tile-to-tile lap screws NOT modelled: floor {FLOOR_T} mm leaves {FLOOR_T - TONGUE_T - FIT - INSERT_SKIN:.1f} mm "
         f"for an insert (need >= 3). Tile joints are plain half-laps held only by the wall screws.")
meat("floor lap tongue thickness", TONGUE_T)
meat("cover strip lap under countersunk head", ROOF_T - COVER_LAP_T - FIT - (M3_CSK_D - M3_CLEAR_D) / 2)
meat("cover lap lower half thickness", COVER_LAP_T)
meat("shoulder slab top edge left beside lip rabbet", WALL_UPPER * math.sqrt(2) - LIP_W)
meat("end wall beside Y=0 groove (per side)", (WALL_END - 1.5 - 2 * FIT) / 2)
meat("floor tile under end-wall groove", FLOOR_T - EW_TONGUE_H)
print(f"         BMS standoff {BMS_STANDOFF:.1f} mm, fuse standoff {FUSE_STANDOFF:.1f} mm (grow when the roof is too thin for the insert)")

# ---- layout checks ---------------------------------------------------------------------
print("-" * 78)
gap_bms_part = (PARTITION_X - PARTITION_T / 2) - BMS_X1
gap_part_fuse = (FUSE_CENTER_X - FUSE_FX / 2) - (PARTITION_X + PARTITION_T / 2)
print(f"BMS x [{BMS_X0:.1f}, {BMS_X1:.1f}], connector side {BMS_CONNECTOR_SIDE}, "
      f"clearance to rear wall {BMS_X0 + HXI:.1f} mm (need {BMS_CONNECTOR_CLEARANCE})")
print(f"Partition at x={PARTITION_X}, fuse x [{FUSE_CENTER_X - FUSE_FX / 2:.1f}, {FUSE_CENTER_X + FUSE_FX / 2:.1f}]"
      f" (block length along {'Y' if FUSE_ROT == 90 else 'X'})")
(ok if gap_bms_part >= BMS_FUSE_AIR_GAP else fail)(f"BMS to partition gap {gap_bms_part:.1f} mm (>= {BMS_FUSE_AIR_GAP})")
(ok if gap_part_fuse >= BMS_FUSE_AIR_GAP else fail)(f"partition to fuse gap {gap_part_fuse:.1f} mm (>= {BMS_FUSE_AIR_GAP})")
lug_y = FUSE_FY / 2 + FUSE_LUG_CLEARANCE
(ok if lug_y <= Y_IN_UP else fail)(f"fuse lug clearance reaches |y|={lug_y:.1f} (inner upper half-width {Y_IN_UP:.1f})")
if BMS_CONNECTOR_SIDE == "rear":
    (ok if BMS_X0 + HXI >= BMS_CONNECTOR_CLEARANCE - 1e-6 else fail)("BMS connector clearance to rear wall")
(ok if BMS_X1 <= COVER_SPLITS_X[0] - 1 else warn)(f"BMS entirely under the rear cover segment (ends x={BMS_X1:.1f}, segment ends {COVER_SPLITS_X[0]})")

# ---- boolean checks -----------------------------------------------------------------------
print("-" * 78)
tot_intr = 0.0
tot_clear = 0.0
for p in shell_parts:
    v1 = (p & pack).volume
    v2 = (p & pack_keepout).volume
    if v1 > 1e-6:
        fail(f"{p.label} intrudes into the pack volume by {v1:.2f} mm3")
    if v2 > 1e-6:
        fail(f"{p.label} is closer than CLEARANCE to the pack (overlap with keep-out {v2:.2f} mm3)")
    tot_intr += v1
    tot_clear += v2
if tot_intr < 1e-6:
    ok("no shell part intrudes into the pack volume")
if tot_clear < 1e-6:
    ok(f"pack keeps >= {CLEARANCE} mm to every shell part (sides and top; it rests on the floor)")

ghost_hits = []
for g in (bms, fuse):
    vp = (g & pack).volume
    if vp > 1e-6:
        ghost_hits.append(f"{g.label} overlaps the pack ghost ({vp / 1000:.1f} cm3) - it does not fit")
    for p in shell_parts:
        v = (g & p).volume
        if v > 1e-6:
            ghost_hits.append(f"{g.label} overlaps {p.label} ({v / 1000:.2f} cm3)")
if ghost_hits:
    for h in ghost_hits:
        warn(h)
else:
    ok("BMS and fuse ghosts clear the pack and the shell")

# pairwise part overlap (joints are designed with FIT clearance, so any overlap is a bug)
overlaps = 0
for i in range(len(shell_parts)):
    for j in range(i + 1, len(shell_parts)):
        a, b = shell_parts[i], shell_parts[j]
        ba, bb_ = a.bounding_box(), b.bounding_box()
        if (ba.max.X < bb_.min.X - 0.01 or bb_.max.X < ba.min.X - 0.01 or
                ba.max.Y < bb_.min.Y - 0.01 or bb_.max.Y < ba.min.Y - 0.01 or
                ba.max.Z < bb_.min.Z - 0.01 or bb_.max.Z < ba.min.Z - 0.01):
            continue
        v = (a & b).volume
        if v > 1e-3:
            overlaps += 1
            fail(f"parts overlap: {a.label} & {b.label} = {v:.2f} mm3")
if overlaps == 0:
    ok("no two shell parts overlap (all joints have clearance)")

# =============================================================================
# EXPORT: unique parts in print orientation
# =============================================================================
os.makedirs(OUT_DIR, exist_ok=True)
for _f in os.listdir(OUT_DIR):           # drop stale exports from earlier runs
    if _f.lower().endswith(".stl"):
        os.remove(os.path.join(OUT_DIR, _f))
ROT_Y_OUT = Rot(-90, 0, 0)    # +Y outer face -> -Z
ROT_X_OUT = Rot(0, 90, 0)     # +X outer face -> -Z
ROT_Z_OUT = Rot(180, 0, 0)    # +Z outer face -> -Z
unique_parts = []   # (file stem, qty, print-oriented shape, note)
for name, t in tiles.items():
    unique_parts.append((f"floor_tile_{name}", 1, place_flat(t, None), "bottom face on bed"))
unique_parts.append(("long_wall_tongue", 2, place_flat(lw_front_R, ROT_Y_OUT), "outer face on bed; 45 deg shoulder rises"))
unique_parts.append(("long_wall_groove", 2, place_flat(lw_rear_R, ROT_Y_OUT), "outer face on bed; 45 deg shoulder rises"))
unique_parts.append(("end_wall_half_tongue", 2, place_flat(ew_front_L, ROT_X_OUT), "outer face on bed"))
unique_parts.append(("end_wall_half_groove", 2, place_flat(ew_front_R, ROT_X_OUT), "outer face on bed"))
for c in covers:
    note = "top face on bed; skirt/lip/bosses rise"
    if c.label == "cover_middle_main" and FUSE_POCKET_ENABLE:
        note = "POCKET ENABLED: cannot lie flat on its outer face - needs supports or a different split"
    unique_parts.append((c.label, 1, place_flat(c, ROT_Z_OUT), note))

print("-" * 78)
print(f"{'part':<28}{'qty':>4}  {'bbox X x Y x Z (mm)':<28}{'vol cm3':>9}{'solid g':>9}  fits 240?")
all_fit = True
for stem, qty, shp, note in unique_parts:
    bb = shp.bounding_box()
    sx, sy, sz = bb.size.X, bb.size.Y, bb.size.Z
    vol = shp.volume / 1000.0
    fits = sx <= MAX_PART + 1e-6 and sy <= MAX_PART + 1e-6 and sz <= MAX_PART + 1e-6
    all_fit &= fits
    print(f"{stem:<28}{qty:>4}  {sx:7.1f} x {sy:7.1f} x {sz:6.1f}   {vol:8.1f}{vol * ASA_DENSITY:9.0f}  {'yes' if fits else 'NO'}")
    fn = os.path.join(OUT_DIR, f"{stem}_x{qty}.stl")
    export_stl(shp, fn, tolerance=0.02, angular_tolerance=0.2)
if all_fit:
    ok(f"every part fits within {MAX_PART:.0f} x {MAX_PART:.0f} x {MAX_PART:.0f} mm")
else:
    fail("some parts exceed the printer volume")
total_vol = sum(s.volume for _, q, s, _ in unique_parts for _ in range(q)) / 1000.0
print(f"Total shell volume {total_vol:.0f} cm3  (~{total_vol * ASA_DENSITY / 1000:.1f} kg if printed solid)")

# =============================================================================
# TEST COUPONS  (~60 mm sections, printed flat, one STL)
# =============================================================================
coupons = []
# 1. floor half-lap: tongue block + rabbet block, one csk screw + insert
cA = (box(0, 48 - FIT, 0, 60, 0, TONGUE_T) + box(0, 36, 0, 60, TONGUE_T + FIT, FLOOR_T)
      + box(0, 36, 0, 60, 0, FLOOR_T))
cA = cA - csk_cutter(42, 30, 0.0, -1, TONGUE_T)
cA.label = "coupon_lap_tongue"
cB = box(0, 36, 0, 60, 0, FLOOR_T) + box(-LAP_W, 36, 0, 60, TONGUE_T + FIT, FLOOR_T)
cB = cB - insert_hole(-LAP_W / 2, 30, TONGUE_T + FIT, +1, M3_INSERT_D, max(TILE_INSERT_DEPTH, 1.0))
cB = Pos(LAP_W, 0, 0) * cB
cB.label = "coupon_lap_rabbet"
# 2. corner joint: 60 mm tall section of long wall end (rabbet) + end wall strip (fits in rabbet)
cW = box(0, 40, 0, WALL_LONG, 0, 60) - box(40 - WALL_END - FIT, 41, -1, WALL_LONG / 2, -1, 61)
cW = cW - insert_hole(20, WALL_LONG / 2, 0, +1, M3_INSERT_D, M3_INSERT_DEPTH)   # floor screw insert
cW.label = "coupon_corner_long_wall"
cE = box(0, WALL_END, 0, 40, 0, 60)
cE.label = "coupon_corner_end_wall"
# 3. countersunk hole + inserts in a 12 mm block (M3 csk through, M3 insert, M4 insert)
cH = box(0, 60, 0, 30, 0, FLOOR_T)
cH = cH - csk_cutter(12, 15, 0.0, -1, FLOOR_T)
cH = cH - insert_hole(30, 15, FLOOR_T, -1, M3_INSERT_D, M3_INSERT_DEPTH)
cH = cH - insert_hole(48, 15, FLOOR_T, -1, M4_INSERT_D, M4_INSERT_DEPTH)
cH.label = "coupon_holes"
# 4. heat-set boss on a 4 mm plate (BMS standoff) and an M4 fuse boss
cP = (box(0, 60, 0, 30, 0, ROOF_T) + cyl(15, 15, ROOF_T, ROOF_T + BMS_STANDOFF, BMS_BOSS_D)
      + cyl(45, 15, ROOF_T, ROOF_T + FUSE_STANDOFF, FUSE_BOSS_D))
cP = cP - insert_hole(15, 15, ROOF_T + BMS_STANDOFF, -1, M3_INSERT_D, M3_INSERT_DEPTH)
cP = cP - insert_hole(45, 15, ROOF_T + FUSE_STANDOFF, -1, M4_INSERT_D, M4_INSERT_DEPTH)
cP.label = "coupon_bosses"
# 5. cover lip rabbet sample: 60 mm of slab top edge + matching lip strip
cL = box(0, 60, 0, 20, 0, 12) - box(-1, 61, 8, 8 + LIP_W, 12 - LIP_H, 13)
cL.label = "coupon_lip_rabbet"
cLip = box(0, 60, 0, 10, 0, ROOF_T) + box(0, 60, 8 + FIT, 8 + LIP_W - FIT, 0, ROOF_T + LIP_H - FIT)
cLip.label = "coupon_lip"
# lay out flat (outer face down), wrapping rows inside the 240 mm bed limit
pieces = [(cA, None), (cB, None), (cW, Rot(-90, 0, 0)), (cE, Rot(0, 90, 0)),
          (cH, None), (cP, None), (cL, None), (cLip, None)]
layout = []
cur_x, cur_y, row_h = 0.0, 0.0, 0.0
for cp, rot in pieces:
    flat = place_flat(cp, rot)
    sz = flat.bounding_box().size
    if cur_x + sz.X > MAX_PART:
        cur_x, cur_y, row_h = 0.0, cur_y + row_h + 10.0, 0.0
    flat = Pos(cur_x, cur_y, 0) * flat
    flat.label = cp.label
    layout.append(flat)
    cur_x += sz.X + 10.0
    row_h = max(row_h, sz.Y)
coupon_comp = Compound(children=layout)
export_stl(coupon_comp, os.path.join(BASE_DIR, "test_coupons.stl"), tolerance=0.02, angular_tolerance=0.2)
bbc = coupon_comp.bounding_box()
print(f"test_coupons.stl: {len(layout)} pieces, footprint {bbc.size.X:.0f} x {bbc.size.Y:.0f} x {bbc.size.Z:.0f} mm")

# =============================================================================
# ASSEMBLY STEP
# =============================================================================
assembly = Compound(children=shell_parts + ghosts, label="openzero_battery_box")
export_step(assembly, os.path.join(BASE_DIR, "assembly.step"))
print("assembly.step written (ghost pack / BMS / fuse are separate coloured, translucent bodies)")

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 78)
print(f"{len(WARNINGS)} warning(s), {len(FAILS)} failure(s)")
for w in WARNINGS:
    print("  WARN  " + w)
for f in FAILS:
    print("  FAIL  " + f)
print("=" * 78)
sys.exit(1 if FAILS else 0)
