from functools import partial

from gdsfactory.components import mmi2x2 as _mmi2x2

from gvtt.components.transitions import strip_taper
from gvtt.xsections import xs_sc

mmi2x2 = partial(
    _mmi2x2,
    width_mmi=5.0,
    length_mmi=112.0,
    width_taper=1.875,
    cross_section=xs_sc,
    gap_mmi=1.25,
    taper=strip_taper,
    length_taper=1.0,
)


if __name__ == "__main__":
    c = mmi2x2()
    c.show()
