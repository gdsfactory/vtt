from __future__ import annotations

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.components import straight as straight_function
from gdsfactory.components import taper as taper_function
from gdsfactory.typings import ComponentSpec, CrossSectionSpec

from gvtt.tech import TECH


@gf.cell
def mmi2x2(
    width: float | None = None,
    width_taper: float = TECH.width_strip,
    length_taper: float = 1.0,
    length_mmi: float = 112.0,
    width_mmi: float = 5,
    gap_mmi: float = 1.25,
    taper: ComponentSpec = taper_function,
    straight: ComponentSpec = straight_function,
    cross_section: CrossSectionSpec = "xs_sc",
) -> Component:
    r"""Mmi 2x2.

    Args:
        width: input and output straight width.
        width_taper: interface between input straights and mmi region.
        length_taper: into the mmi region.
        length_mmi: in x direction.
        width_mmi: in y direction.
        gap_mmi: (width_taper + gap between tapered wg)/2.
        taper: taper function.
        straight: straight function.
        cross_section: spec.


    .. code::

                   length_mmi
                    <------>
                    ________
                   |        |
                __/          \__
            o2  __            __  o3
                  \          /_ _ _ _
                  |         | _ _ _ _| gap_mmi
                __/          \__
            o1  __            __  o4
                  \          /
                   |________|

                 <->
            length_taper

    """
    c = gf.Component()
    gap_mmi = gf.snap.snap_to_grid(gap_mmi, grid_factor=2)
    w_taper = width_taper
    x = gf.get_cross_section(cross_section)
    width = width or x.width

    _taper = gf.get_component(
        taper,
        length=length_taper,
        width1=width,
        width2=w_taper,
        cross_section=cross_section,
    )

    a = gap_mmi / 2 + width_taper / 2
    _ = c << gf.get_component(
        straight, length=length_mmi, width=width_mmi, cross_section=cross_section
    )

    temp_component = Component()

    ports = [
        temp_component.add_port(
            "o1", orientation=180, center=(0, -a), width=w_taper, cross_section=x
        ),
        temp_component.add_port(
            "o2", orientation=180, center=(0, +a), width=w_taper, cross_section=x
        ),
        temp_component.add_port(
            "o3",
            orientation=0,
            center=(length_mmi, +a),
            width=w_taper,
            cross_section=x,
        ),
        temp_component.add_port(
            "o4",
            orientation=0,
            center=(length_mmi, -a),
            width=w_taper,
            cross_section=x,
        ),
    ]

    for port in ports:
        taper_ref = c << _taper
        taper_ref.connect(port="o2", other=port, allow_width_mismatch=True)
        c.add_port(name=port.name, port=taper_ref.ports["o1"])

    c.flatten()
    return c


if __name__ == "__main__":
    c = mmi2x2()
    c.show()
