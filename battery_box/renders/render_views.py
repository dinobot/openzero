"""Review renders for the battery box: cross-sections, top/bottom/iso views and a few parts
as SVG line drawings (hidden lines removed). Usage: python renders/render_views.py [out_dir]
Rasterise on macOS with:  qlmanage -t -s 1700 -o . *.svg
"""
import io, contextlib, os, sys, time
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # battery_box/
out = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(root, "enclosure.py")).read().replace("sys.exit(1 if FAILS else 0)", "pass")
ns = {"__file__": os.path.join(root, "enclosure.py"), "__name__": "render"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src, ns)
from build123d import *
shell = ns["shell_parts"]; ghosts = ns["ghosts"]
HX, Y_OUT_LOW, Z_TOP = ns["HX"], ns["Y_OUT_LOW"], ns["Z_TOP"]

def write(name, groups, origin, up=(0, 0, 1), look_at=None, scale=4.0):
    t = time.time()
    exp = ExportSVG(scale=scale, line_weight=0.35)
    exp.add_layer("shell", line_color=(0.0, 0.0, 0.0), line_weight=0.5)
    exp.add_layer("ghost", line_color=(0.85, 0.0, 0.0), line_weight=0.4)
    exp.add_layer("hidden", line_color=(0.6, 0.6, 0.6), line_weight=0.2, line_type=LineType.DASHED)
    for layer, shapes, with_hidden in groups:
        if not shapes:
            continue
        comp = Compound(children=shapes)
        vis, hid = comp.project_to_viewport(viewport_origin=origin, viewport_up=up, look_at=look_at)
        exp.add_shape(vis, layer=layer)
        if with_hidden and hid:
            exp.add_shape(hid, layer="hidden")
    exp.write(os.path.join(out, name + ".svg"))
    squarify(os.path.join(out, name + ".svg"))
    print(f"{name}: {time.time()-t:.1f}s")


def squarify(path, W=1700):
    import re
    s = open(path).read()
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', s)
    x, y, w, h = map(float, m.groups())
    side = max(w, h) * 1.04
    nx = x - (side - w) / 2; ny = y - (side - h) / 2
    s = s.replace(m.group(0), f'viewBox="{nx} {ny} {side} {side}"', 1)
    s = re.sub(r'width="[^"]+" height="[^"]+"', f'width="{W}px" height="{W}px"', s, count=1)
    s = s.replace('<g transform="scale(1,-1)"', f'<rect x="{nx}" y="{ny}" width="{side}" height="{side}" fill="white"/><g transform="scale(1,-1)"', 1)
    open(path, "w").write(s)

def slab(parts, axis, v, t=0.3):
    if axis == "x":
        cut = ns["box"](v - t/2, v + t/2, -400, 400, -50, 400)
    else:
        cut = ns["box"](-400, 400, v - t/2, v + t/2, -50, 400)
    res = []
    for p in parts:
        s = p & cut
        if s.volume > 1e-6:
            res.append(s)
    return res

far = 5000
# YZ sections (look along -X from +X)
for xv, nm in ((-130, "sec_x-130_bms"), (26, "sec_x26_fuse"), (161, "sec_x161_cable"), (-25, "sec_x-25_partition"), (217.25, "sec_x217_endpad")):
    write(nm, [("shell", slab(shell, "x", xv), False), ("ghost", slab(ghosts, "x", xv), False)],
          origin=(far, 0, 100), look_at=(0, 0, 100))
# XZ sections (look along -Y from +Y)
for yv, nm in ((0, "sec_y0_long"), (ns["COVER_LAP_Y"], "sec_y91_coverlap"), (ns["WALL_SCREW_Y"], "sec_y144_wallscrews"), (ns["COVER_SCREW_Y"], "sec_y113_coverscrews")):
    write(nm, [("shell", slab(shell, "y", yv), False), ("ghost", slab(ghosts, "y", yv), False)],
          origin=(0, far, 100), look_at=(0, 0, 100))
# top view (with hidden lines for the ghosts) and bottom view
write("view_top", [("shell", shell, False), ("ghost", ghosts, True)], origin=(0, 0, far), up=(1, 0, 0), look_at=(0, 0, 0))
write("view_bottom", [("shell", shell, False)], origin=(0, 0, -far), up=(1, 0, 0), look_at=(0, 0, 0))
# isometric
write("view_iso", [("shell", shell, False), ("ghost", ghosts, False)], origin=(far, -far * 0.8, far * 0.7), look_at=(0, 0, 100), scale=3.0)
# single parts in print orientation
up_parts = ns["unique_parts"]
for stem, qty, shp, note in up_parts:
    if stem in ("long_wall_tongue", "cover_middle_main", "end_wall_half_tongue", "floor_tile_mid_left", "cover_rear_main"):
        write("part_" + stem, [("shell", [shp], True)], origin=(far, -far * 0.8, far * 0.9), look_at=(0, 0, 0), scale=3.0)
