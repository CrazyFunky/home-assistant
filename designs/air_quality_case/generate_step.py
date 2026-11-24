"""Generate STEP files for the ESPHome air quality sensor case."""

from pathlib import Path

import cadquery as cq


OUT_DIR = Path(__file__).resolve().parent

CASE_W = 130
CASE_D = 105
CASE_H = 42
WALL = 2.4
FLOOR_H = 2.4
CORNER_R = 4

LID_H = 16
BASE_H = CASE_H - LID_H

SDS_W = 72
SDS_D = 72
MODULE_CLEARANCE = 1.5

MHZ_W = 36
MHZ_D = 24

DHT_W = 18
DHT_D = 36
SLOT_W = 2.4

MODULE_SDS_X = 58
MODULE_SDS_Y = 48

MODULE_MHZ_X = 27
MODULE_MHZ_Y = 20

MODULE_NODE_X = 93
MODULE_NODE_Y = 32

MODULE_DHT_X = 23
MODULE_DHT_Y = 87


def rounded_box(w, d, h, r):
    return (
        cq.Workplane("XY")
        .box(w, d, h, centered=(False, False, False))
        .edges("|Z")
        .fillet(r)
    )


def cut_box(obj, x, y, z, w, d, h):
    cutter = cq.Workplane("XY").box(w, d, h, centered=(False, False, False)).translate((x, y, z))
    return obj.cut(cutter)


def post(x, y, h=8, outer=5, inner=2.2):
    outer_cyl = cq.Workplane("XY").circle(outer / 2).extrude(h).translate((x, y, FLOOR_H))
    inner_cyl = cq.Workplane("XY").circle(inner / 2).extrude(h + 1).translate((x, y, FLOOR_H - 0.5))
    return outer_cyl.cut(inner_cyl)


def tray(x, y, w, d, h=4):
    outer = cq.Workplane("XY").box(w + 2, d + 2, h, centered=(False, False, False)).translate(
        (x - w / 2 - 1, y - d / 2 - 1, FLOOR_H)
    )
    inner = cq.Workplane("XY").box(w - 2, d - 2, h, centered=(False, False, False)).translate(
        (x - w / 2 + 1, y - d / 2 + 1, FLOOR_H + 1.2)
    )
    return outer.cut(inner)


def cable_anchor(x, y):
    body = cq.Workplane("XY").box(14, 5, 5).translate((x, y, FLOOR_H))
    channel = cq.Workplane("XY").box(8, 6, 3).translate((x, y, FLOOR_H - 0.5))
    return body.cut(channel)


def make_base():
    base = rounded_box(CASE_W, CASE_D, BASE_H, CORNER_R)
    inner = rounded_box(CASE_W - WALL * 2, CASE_D - WALL * 2, BASE_H + 1, CORNER_R - 1).translate(
        (WALL, WALL, FLOOR_H)
    )
    base = base.cut(inner)

    base = cut_box(base, MODULE_NODE_X - 8, CASE_D - WALL - 0.2, 8, 22, WALL + 1, 13)
    base = cut_box(base, -0.2, 75, 10, WALL + 1, 16, 8)
    base = cut_box(base, CASE_W - WALL - 0.2, 55, 10, WALL + 1, 20, 8)

    sds_floor = (
        cq.Workplane("XY")
        .box(SDS_W + MODULE_CLEARANCE * 2, SDS_D + MODULE_CLEARANCE * 2, 1.2, centered=(False, False, False))
        .translate(
            (
                MODULE_SDS_X - SDS_W / 2 - MODULE_CLEARANCE,
                MODULE_SDS_Y - SDS_D / 2 - MODULE_CLEARANCE,
                FLOOR_H,
            )
        )
    )

    parts = [
        base,
        sds_floor,
        post(MODULE_SDS_X - 34, MODULE_SDS_Y - 34, 5),
        post(MODULE_SDS_X + 34, MODULE_SDS_Y - 34, 5),
        post(MODULE_SDS_X - 34, MODULE_SDS_Y + 34, 5),
        post(MODULE_SDS_X + 34, MODULE_SDS_Y + 34, 5),
        post(MODULE_NODE_X - 14, MODULE_NODE_Y - 24, 6, 4.5, 1.8),
        post(MODULE_NODE_X + 14, MODULE_NODE_Y - 24, 6, 4.5, 1.8),
        post(MODULE_NODE_X - 14, MODULE_NODE_Y + 24, 6, 4.5, 1.8),
        post(MODULE_NODE_X + 14, MODULE_NODE_Y + 24, 6, 4.5, 1.8),
        tray(MODULE_MHZ_X, MODULE_MHZ_Y, MHZ_W, MHZ_D),
        tray(MODULE_DHT_X, MODULE_DHT_Y, DHT_W, DHT_D),
        cable_anchor(96, 74),
        cable_anchor(58, 12),
    ]

    result = parts[0]
    for part in parts[1:]:
        result = result.union(part)
    return result


def make_lid():
    lid = rounded_box(CASE_W, CASE_D, LID_H, CORNER_R)
    inner = rounded_box(CASE_W - WALL * 2, CASE_D - WALL * 2, LID_H, CORNER_R - 1).translate(
        (WALL, WALL, -1)
    )
    lid = lid.cut(inner)

    for x in range(MODULE_SDS_X - 24, MODULE_SDS_X + 25, 10):
        for y in range(MODULE_SDS_Y - 24, MODULE_SDS_Y + 25, 10):
            if (x - MODULE_SDS_X) ** 2 + (y - MODULE_SDS_Y) ** 2 < 32**2:
                hole = cq.Workplane("XY").circle(2.3).extrude(LID_H + 2).translate((x, y, -1))
                lid = lid.cut(hole)

    for i in range(6):
        lid = cut_box(lid, MODULE_MHZ_X - 18 + i * 7, 6, 4, SLOT_W, 18, LID_H)

    for i in range(5):
        lid = cut_box(lid, 8, MODULE_DHT_Y - 14 + i * 7, 4, 18, SLOT_W, LID_H)

    for i in range(8):
        lid = cut_box(lid, CASE_W - 58 + i * 7, CASE_D - 13, 4, SLOT_W, 24, LID_H)

    lip_outer = rounded_box(CASE_W - (WALL + 0.8) * 2, CASE_D - (WALL + 0.8) * 2, 5, CORNER_R - 1.5).translate(
        (WALL + 0.8, WALL + 0.8, 0)
    )
    lip_inner = rounded_box(
        CASE_W - (WALL + 0.8) * 2 - WALL * 2,
        CASE_D - (WALL + 0.8) * 2 - WALL * 2,
        7,
        CORNER_R - 2,
    ).translate((WALL * 2 + 0.8, WALL * 2 + 0.8, -1))
    lip = lip_outer.cut(lip_inner)

    return lid.union(lip)


def export_step():
    base = make_base()
    lid = make_lid().translate((0, CASE_D + 12, 0))
    model = cq.Compound.makeCompound([base.val(), lid.val()])

    cq.exporters.export(base, str(OUT_DIR / "air_quality_case_base.stp"), exportType="STEP")
    cq.exporters.export(lid, str(OUT_DIR / "air_quality_case_lid.stp"), exportType="STEP")
    cq.exporters.export(model, str(OUT_DIR / "air_quality_case_assembly.stp"), exportType="STEP")


if __name__ == "__main__":
    export_step()
