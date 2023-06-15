import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.components.taper_cross_section import taper_cross_section
import vtt_tech_public
from typing import Optional
from gdsfactory.cross_section import Section, CrossSection, LayerSpec


@gf.xsection
def xs_rib_strip(
    width: float = 3.0,
    width_trench: float = 10.0,
    width_deep: float = 10.75,
    dist_deep: float = 3.0,
    wg_marking_layer: Optional[LayerSpec] = None,
    **kwargs,
) -> CrossSection:
    """Return CrossSection of strip waveguide defined by trenches."""

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

    return CrossSection(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


@gf.cell
def rib_to_strip(
    length=200.0,
    width1=3.0,
    width2=3.0,
    **kwargs,
) -> Component:
    """
    Standard rib-to-strip waveguide converter.
    """
    c = gf.Component()

    rib_strip_1 = xs_rib_strip(width=3.0, width_deep=0.5)  # rib end
    rib_strip_2 = xs_rib_strip(width=3.0, dist_deep=-0.25)  # strip end

    cn = c << gf.components.taper_cross_section.taper_cross_section(
        cross_section1=rib_strip_1,
        cross_section2=rib_strip_2,
        linear=True,
        length=length,
    )

    c.absorb(cn)
    c.info["length"] = length

    if width1 != 3.0:
        t1 = c << rib_taper(width1, 3.0)
        t1.connect("o2", cn.ports["o1"])
        c.add_port("o1", port=t1.ports["o1"])
        c.info["length"] += t1.info["length"]
        c.absorb(t1)
    else:
        c.add_port("o1", port=cn.ports["o1"])

    if width2 != 3.0:
        t2 = c << strip_taper(3.0, width2)
        t2.connect("o1", cn.ports["o2"])
        c.add_port("o2", port=t2.ports["o2"])
        c.info["length"] += t2.info["length"]
        c.absorb(t2)
    else:
        c.add_port("o2", port=cn.ports["o2"])

    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)

    return c


@gf.cell
def strip_to_rib(
    length=200.0,
    width1=3.0,
    width2=3.0,
    **kwargs,
) -> Component:
    """
    Standard rib-to-strip waveguide converter.
    """

    c = rib_to_strip(width1=width2, width2=width1)
    c.ports["o1"].name = "o2"
    c.ports["o2"].name = "o1"
    return c


@gf.cell
def strip_taper(
    width1=1,
    width2=1,
    taper_ratio=25.0,
    **kwargs,
) -> Component:
    """
    Standard rib-to-strip waveguide converter.
    """
    if "length" not in kwargs.keys():
        kwargs["length"] = abs(width1 - width2) * taper_ratio

    if "cross_section" in kwargs.keys():
        del kwargs["cross_section"]

    c = taper_cross_section(
        cross_section1=vtt_tech_public.xsections.strip(width1),
        cross_section2=vtt_tech_public.xsections.strip(width2),
        linear=True,
        npoints=2,
        **kwargs,
    )
    c.info["length"] = kwargs["length"]
    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)

    return c


@gf.cell
def rib_taper(
    width1=1,
    width2=1,
    taper_ratio=50.0,
    **kwargs,
) -> Component:
    """
    Standard rib-to-strip waveguide converter.
    """
    length = abs(width1 - width2) * taper_ratio
    c = taper_cross_section(
        cross_section1=vtt_tech_public.xsections.rib(width1),
        cross_section2=vtt_tech_public.xsections.rib(width2),
        length=length,
        linear=True,
        npoints=2,
        **kwargs,
    )
    c.info["length"] = length
    c.info["width1"] = float(width1)
    c.info["width2"] = float(width2)
    return c
