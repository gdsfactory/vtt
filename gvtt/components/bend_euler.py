from __future__ import annotations

from typing import Any

import gdsfactory as gf
import numpy as np
from gdsfactory.add_padding import get_padding_points
from gdsfactory.component import Component
from gdsfactory.path import euler
from gdsfactory.typings import Coordinate, CrossSectionSpec

from gvtt.tech import xs_sc


def _eulerR_1550(angle: float) -> float:
    if angle == 0:
        return 0.0
    p, v, a0 = 0.79, 2093.0, 18.75  # for 1550 nm, TE, 1.875 um
    return float((v / max(abs(angle), a0)) ** (1.0 / p))


@gf.cell
def bend_euler(
    angle: float = 90.0,
    p: float = 1.0,
    with_arc_floorplan: bool = False,
    npoints: int | None = None,
    direction: str = "ccw",
    with_bbox: bool = True,
    cross_section: CrossSectionSpec = xs_sc,
    **kwargs: Any,
) -> Component:
    """Returns an euler bend that transitions from straight to curved.

    By default, `radius` corresponds to the minimum radius of curvature of the bend.
    However, if `with_arc_floorplan` is True, `radius` corresponds to the effective
    radius of curvature (making the curve a drop-in replacement for an arc). If
    p < 1.0, will create a "partial euler" curve as described in Vogelbacher et.
    al. https://dx.doi.org/10.1364/oe.27.031394

    default p = 0.5 based on this paper
    https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-25-8-9150&id=362937

    Args:
        angle: total angle of the curve.
        p: Proportion of the curve that is an Euler curve.
        with_arc_floorplan: If False: `radius` is the minimum radius of curvature
          If True: The curve scales such that the endpoints match a bend_circular
          with parameters `radius` and `angle`.
        npoints: Number of points used per 360 degrees.
        direction: cw (clock-wise) or ccw (counter clock-wise).
        with_bbox: add bbox_layers and bbox_offsets to avoid DRC sharp edges.
        cross_section: specification (CrossSection, string, CrossSectionFactory dict).
        kwargs: cross_section settings.

    .. code::

                  o2
                  |
                 /
                /
               /
       o1_____/
    """

    dx = gf.get_cross_section(cross_section, **kwargs)
    radius = _eulerR_1550(abs(angle))

    c = Component()

    path = euler(
        radius=radius, angle=angle, p=p, use_eff=with_arc_floorplan, npoints=npoints
    )

    ref = c << path.extrude(dx)
    c.info["length"] = float(np.round(path.length(), 3))
    c.info["dy"] = float(
        np.round(abs(float(path.points[0][0] - path.points[-1][0])), 3)
    )
    c.info["radius_min"] = float(np.round(path.info["Rmin"], 3))
    c.info["radius"] = float(path.dxmax)
    c.info["width"] = float(dx.width)

    if with_bbox and dx.bbox_layers:
        padding: list[list[Coordinate]] = []
        angle = int(angle)
        for offset in dx.bbox_offsets or []:
            top = offset if angle in {180, -180, -90} else 0
            bottom = 0 if angle in {-90} else offset
            points = get_padding_points(
                component=c,
                default=0,
                bottom=bottom,
                right=offset,
                top=top,
            )
            padding.append(points)

        for layer, points in zip(dx.bbox_layers, padding):
            c.add_polygon(points, layer=layer)

    if direction == "cw":
        ref.dmirror(p1=(0, 0), p2=(1, 0))

    c.add_ports(ref.ports)
    return c


if __name__ == "__main__":
    c = bend_euler()
    c.show()
