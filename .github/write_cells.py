from typing import Tuple
import inspect
from gvtt.config import PATH
from gvtt import cells


filepath = PATH.repo / "docs" / "cells.rst"

skip = {}

skip_plot: Tuple[str, ...] = ("add_fiber_array_siepic",)
skip_settings: Tuple[str, ...] = ("flatten", "safe_cell_names")


with open(filepath, "w+") as f:
    f.write(
        """

Here are the components available in the PDK


Cells
=============================
"""
    )

    for name in sorted(cells.keys()):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, (int, float, str, tuple))
                and p not in skip_settings
            ]
        )
        if name in skip_plot:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: gvtt.components.{name}

"""
            )
        else:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: gvtt.components.{name}

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.{name}({kwargs})
  c.plot_matplotlib()

"""
            )
