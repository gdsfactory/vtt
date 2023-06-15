import gdsfactory as gf
from gdsfactory.components import mmi1x2 as _mmi1x2
from gdsfactory import Component
from functools import partial
from vtt_tech.xsections import strip
from vtt_tech.components import strip_taper

@gf.cell
def mmi1x2() -> Component:
    return partial(_mmi1x2, width_mmi=5.0, length_mmi=112.0, width_taper=1.875, cross_section=strip, gap_mmi=0.6, taper=strip_taper)()