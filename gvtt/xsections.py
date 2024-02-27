""" technology definitions."""
import sys
from functools import partial

import gdsfactory as gf
from gdsfactory.cross_section import (
    CrossSection,
    LayerSpec,
    Section,
    cross_section,
    get_cross_sections,
)

from gvtt.layers import LAYER


def rib(
    width: float = 2.5,
    width_trench: float = 10.0,
    wg_marking_layer: LayerSpec = LAYER.TYPE_RIB,
    **kwargs,
) -> CrossSection:
    """Return CrossSection of rib waveguide defined by trenches.

    Args:
        width: waveguide width.
        width_trench: trench width.
        wg_marking_layer: layer for waveguide marking.
        kwargs: cross_section arguments.
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
    ]

    return cross_section(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


def strip(
    width: float = 1.875,
    width_trench: float = 10.0,
    wg_marking_layer: LayerSpec = LAYER.TYPE_STRIP,
    **kwargs,
) -> CrossSection:
    """Return CrossSection of strip waveguide defined by trenches.

    Args:
        width: waveguide width.
        width_trench: trench width.
        wg_marking_layer: layer for waveguide marking.
        kwargs: cross_section arguments.
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
            width=2.0 * width_trench + width + 1,
            layer="WG_MOST_ADD",
            name="trench_2",
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


def vttstrip(
    width: float = 1.875,
    width_trench: float = 10.0,
    wg_marking_layer: LayerSpec | None = LAYER.TYPE_STRIP,
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
            width=2.0 * width_trench + width + 1,
            layer="WG_MOST_ADD",
            name="trench_2",
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


sm_rib = rib(width=2.5)
xs_sc = euler_strip = strip(width=1.875)

straight_sc = partial(gf.components.straight, cross_section=xs_sc)
straight_rib = partial(gf.components.straight, cross_section=sm_rib)
straight = straight_sc

cross_sections = get_cross_sections(sys.modules[__name__])

if __name__ == "__main__":
    print(cross_sections.keys())
    c = gf.components.straight(cross_section=rib)
    c.show()
