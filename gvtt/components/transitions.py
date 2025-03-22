from typing import Any

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.components import taper_cross_section
from gdsfactory.cross_section import (
    CrossSection,
    Section,
    cross_section,
)
from gdsfactory.typings import LayerSpec

from gvtt.layers import LAYER
from gvtt.tech import rib, strip


def xs_rib_strip(
    width: float = 3.0,
    width_trench: float = 10.0,
    width_deep: float = 10.75,
    dist_deep: float = 3.0,
    wg_marking_layer: LayerSpec = LAYER.TYPE_STRIP,
    **kwargs: Any,
) -> CrossSection:
    """Return CrossSection of strip waveguide defined by trenches.

    Args:
        width: waveguide width.
        width_trench: trench width.
        width_deep: deep trench width.
        dist_deep: deep trench distance.
        wg_marking_layer: waveguide marking layer.
        **kwargs: additional arguments.
    """

    sections = kwargs.pop("sections", [])
    sections += [
        Section(width=width, layer="WG_RIBS_SUB", name="WG", simplify=None),
        Section(
            width=2.0 * width_trench + width,
            layer="WG_RIBS_ADD",
            name="trench",
            simplify=None,
        ),
        Section(
            width=width + 2.0 * (dist_deep + width_deep),
            layer="WG_MOST_ADD",
            name="trench_deep",
            simplify=None,
        ),
        Section(
            width=width + 2.0 * dist_deep,
            layer="WG_MOST_SUB",
            name="trench_cut",
            simplify=None,
        ),
    ]

    return cross_section(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


@gf.cell
def rib_to_strip(
    length: float = 200.0,
    width1: float = 3.0,
    width2: float = 3.0,
) -> Component:
    """Standard rib-to-strip waveguide converter.

    Args:
        length: taper length.
        width1: initial width.
        width2: final width.

    """
    c = gf.Component()

    rib_strip_1 = xs_rib_strip(
        width=3.0, width_deep=0.5, wg_marking_layer=LAYER.TYPE_RIB
    )  # rib end
    rib_strip_2 = xs_rib_strip(
        width=3.0, dist_deep=-0.25, wg_marking_layer=LAYER.TYPE_STRIP
    )  # strip end

    cn = c << gf.components.taper_cross_section(
        cross_section1=rib_strip_1,
        cross_section2=rib_strip_2,
        linear=True,
        length=length,
    )

    c.info["length"] = length

    if width1 != 3.0:
        t1 = c << rib_taper(width1, 3.0)
        t1.connect("o2", cn.ports["o1"])
        c.add_port("o1", port=t1.ports["o1"])
        c.info["length"] += t1.info["length"]
    else:
        c.add_port("o1", port=cn.ports["o1"])

    if width2 != 3.0:
        t2 = c << strip_taper(3.0, width2)
        t2.connect("o1", cn.ports["o2"])
        c.add_port("o2", port=t2.ports["o2"])
        c.info["length"] += t2.info["length"]
    else:
        c.add_port("o2", port=cn.ports["o2"])

    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)

    return c


@gf.cell
def strip_to_rib(
    length: float = 200.0,
    width1: float = 3.0,
    width2: float = 3.0,
) -> Component:
    """Returns strip to rib transition.

    Args:
        length: in um.

    """
    return rib_to_strip(length=length, width1=width2, width2=width1)


@gf.cell
def strip_taper(
    width1: float = 1,
    width2: float = 1,
    taper_ratio: float = 25.0,
    length: float | None = None,
    **kwargs: Any,
) -> Component:
    """Standard rib-to-strip waveguide converter.

    Args:
        width1: initial width.
        width2: final width.
        taper_ratio: taper ratio.
        length: taper length.
        **kwargs: additional arguments.
    """

    if "taper_length" in kwargs:
        length = kwargs.pop("taper_length")

    length = length or abs(width1 - width2) * taper_ratio or 10e-3
    kwargs.pop("cross_section", None)
    c = gf.Component()

    ref = c << taper_cross_section(
        cross_section1=strip(width1),
        cross_section2=strip(width2),
        length=length,
        linear=True,
        npoints=2,
    )
    c.info["length"] = length
    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)
    c.add_ports(ref.ports)
    return c


@gf.cell
def rib_taper(
    width1: float = 1,
    width2: float = 1,
    taper_ratio: float = 50.0,
    length: float | None = None,
    **kwargs: Any,
) -> Component:
    """Standard rib-to-strip waveguide converter.

    Args:
        width1: initial width.
        width2: final width.
        taper_ratio: taper ratio.
        length: taper length.
        **kwargs: additional arguments.
    """
    length = length or abs(width1 - width2) * taper_ratio or 10e-3
    c = gf.Component()
    ref = c << taper_cross_section(
        cross_section1=rib(width1),
        cross_section2=rib(width2),
        length=length,
        linear=True,
        npoints=2,
        **kwargs,
    )
    c.info["length"] = length
    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)
    c.add_ports(ref.ports)
    return c


if __name__ == "__main__":
    c = strip_to_rib()
    # c = strip_taper()
    # c.pprint_ports()
    c.show()
