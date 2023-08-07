""" technology definitions."""
import sys

import gdsfactory as gf
from gdsfactory.cross_section import (
    CrossSection,
    LayerSpec,
    Section,
    get_cross_section_factories,
    xsection,
)

from gvtt.layers import LAYER


@xsection
def rib(
    width: float = 2.5,
    width_trench: float = 10.0,
    wg_marking_layer: LayerSpec = LAYER.TYPE_RIB,
    **kwargs,
) -> CrossSection:
    """Return CrossSection of rib waveguide defined by trenches."""

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

    return CrossSection(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


@xsection
def strip(
    width: float = 1.875,
    width_trench: float = 10.0,
    wg_marking_layer: LayerSpec = LAYER.TYPE_STRIP,
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

    return CrossSection(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


@xsection
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

    return CrossSection(
        width=width,
        layer=wg_marking_layer,
        sections=tuple(sections),
        port_names=("o1", "o2"),
        **kwargs,
    )


sm_rib = rib(width=2.5)
euler_strip = strip(width=1.875)
cross_sections = get_cross_section_factories(sys.modules[__name__])

if __name__ == "__main__":
    print(cross_sections.keys())
    c = gf.components.straight(cross_section=rib)
    c.show()
