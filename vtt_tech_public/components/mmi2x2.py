import gdsfactory as gf
from gdsfactory.components import mmi2x2 as _mmi2x2
from gdsfactory import Component
from functools import partial
from vtt_tech_public.xsections import strip
from vtt_tech_public.components import strip_taper


@gf.cell
def mmi2x2() -> Component:
    return partial(
        _mmi2x2,
        width_mmi=5.0,
        length_mmi=112.0,
        width_taper=1.875,
        cross_section=strip,
        gap_mmi=1.25,
        taper=strip_taper,
        length_taper=1.0,
    )()
