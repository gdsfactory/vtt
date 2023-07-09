from gdsfactory.components import mmi2x2 as _mmi2x2
from functools import partial
from gvtt.xsections import strip
from gvtt.components import strip_taper


mmi2x2 = partial(
    _mmi2x2,
    width_mmi=5.0,
    length_mmi=112.0,
    width_taper=1.875,
    cross_section=strip,
    gap_mmi=1.25,
    taper=strip_taper,
    length_taper=1.0,
)
