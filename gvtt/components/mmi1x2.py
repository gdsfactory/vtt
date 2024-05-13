from functools import partial

# from gdsfactory.components import mmi1x2 as _mmi1x2

from gvtt.components.transitions import strip_taper
from gvtt.xsections import xs_sc

import gdsfactory as gf

from gdsfactory.component import Component
from gdsfactory.components.taper import taper as taper_function
from gdsfactory.typings import ComponentFactory, CrossSectionSpec


@gf.cell
def _mmi1x2(
    width: float | None = None,
    width_taper: float = 1.0,
    length_taper: float = 1.0,
    length_mmi: float = 5.5,
    width_mmi: float = 2.5,
    gap_mmi: float = 0.25,
    taper: ComponentFactory = taper_function,
    cross_section: CrossSectionSpec = "xs_sc",
    **kwargs,
) -> Component:
    r"""1x2 MultiMode Interferometer (MMI).

    Args:
        width: input and output straight width. Defaults to cross_section width.
        width_taper: interface between input straights and mmi region.
        length_taper: into the mmi region.
        length_mmi: in x direction.
        width_mmi: in y direction.
        gap_mmi:  gap between tapered wg.
        taper: taper function.
        cross_section: specification (CrossSection, string or dict).


    .. code::

               length_mmi
                <------>
                ________
               |        |
               |         \__
               |          __  o2
            __/          /_ _ _ _
         o1 __          | _ _ _ _| gap_mmi
              \          \__
               |          __  o3
               |         /
               |________|

             <->
        length_taper

    """
    c = Component()
    gap_mmi = gf.snap.snap_to_grid(gap_mmi, grid_factor=2)
    x = gf.get_cross_section(cross_section, **kwargs)
    width = width or x.width

    _taper = taper(
        length=length_taper,
        width1=width,
        width2=width_taper,
        cross_section=x,
    )

    delta_width = width_mmi - width
    y = width_mmi / 2
    print(x.layer)
    c.add_polygon([(0, -y), (length_mmi, -y), (length_mmi, y), (0, y)], layer=x.layer)
    for section in x.sections[1:]:
        layer = section.layer
        y = section.width / 2 + delta_width / 2
        c.add_polygon(
            [
                (-0, -y),
                (length_mmi, -y),
                (length_mmi, y),
                (-0, y),
            ],
            layer=layer,
        )
    x.add_bbox(c)

    a = gap_mmi / 2 + width_taper / 2
    ports = [
        gf.Port(
            "o1",
            orientation=180,
            center=(0, 0),
            width=width_taper,
            layer=x.layer,
            cross_section=x,
        ),
        gf.Port(
            "o2",
            orientation=0,
            center=(+length_mmi, +a),
            width=width_taper,
            layer=x.layer,
            cross_section=x,
        ),
        gf.Port(
            "o3",
            orientation=0,
            center=(+length_mmi, -a),
            width=width_taper,
            layer=x.layer,
            cross_section=x,
        ),
    ]

    for port in ports:
        taper_ref = c << _taper
        taper_ref.connect(port="o2", destination=port)
        c.add_port(name=port.name, port=taper_ref.ports["o1"])
        c.absorb(taper_ref)

    return c


mmi1x2 = partial(
    _mmi1x2,
    width_mmi=6.25,
    length_mmi=43.25,
    width=1.875,
    width_taper=1.875,
    cross_section=xs_sc,
    gap_mmi=(6.25 - 2 * 1.875) / 2,
    taper=strip_taper,
    length_taper=1.0,
)

if __name__ == "__main__":
    c = mmi1x2(name="mmi1x2")
    c.show()
