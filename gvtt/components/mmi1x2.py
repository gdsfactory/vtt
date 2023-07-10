from gdsfactory.components import mmi1x2 as _mmi1x2
from functools import partial
from gvtt.xsections import strip
from gvtt.components.transitions import strip_taper


mmi1x2 = partial(
    _mmi1x2,
    width_mmi=6.25,
    length_mmi=43.25,
    width_taper=1.875,
    cross_section=strip,
    gap_mmi=(6.25 - 2 * 1.875) / 2,
    taper=strip_taper,
    length_taper=1.0,
)
