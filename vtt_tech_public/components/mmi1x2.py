import gdsfactory as gf
from gdsfactory.components import mmi1x2 as _mmi1x2
from gdsfactory import Component
from functools import partial
from vtt_tech_public.xsections import strip
from vtt_tech_public.components import strip_taper


@gf.cell
def mmi1x2() -> Component:
    return partial(
        _mmi1x2,
        width_mmi=6.25,
        length_mmi=43.25,
        width_taper=1.875,
        cross_section=strip,
        gap_mmi=(6.25 - 2 * 1.875) / 2,
        taper=strip_taper,
        length_taper=1.0,
    )()
