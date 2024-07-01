from __future__ import annotations

from gdsfactory.config import PATH as GPATH
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk, constants
from gdsfactory.technology import LayerViews

from gvtt import components
from gvtt.config import PATH
from gvtt.layers import LAYER
from gvtt.tech import cross_sections

cells = get_cells([components])

frame_dimensions = {
    LAYER.WG_SNGL_ADD: 75.0,
    LAYER.WG_LANE_ADD: 71.5,
    LAYER.WG_DEOX_ADD: 85.0,
    LAYER.WG_ARCO_ADD: 100.0,
}

FRAME_LAYERS = {}

PORT_MARKER_LAYER_TO_TYPE = {
    LAYER.PORT: "optical",
    LAYER.PORTE: "dc",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_LAYER_TO_TYPE = {
    LAYER.TYPE_RIB: "optical",
    LAYER.TYPE_STRIP: "optical",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_TYPE_TO_MARKER_LAYER = {v: k for k, v in PORT_MARKER_LAYER_TO_TYPE.items()}

LAYER_TRANSITIONS = {
    LAYER.TYPE_RIB: "rib_taper",
    LAYER.TYPE_STRIP: "strip_taper",
    (LAYER.TYPE_RIB, LAYER.TYPE_STRIP): "rib_to_strip",
    (LAYER.TYPE_STRIP, LAYER.TYPE_RIB): "strip_to_rib",
}

LAYER_VIEWS = LayerViews(filepath=PATH.lyp_yaml)

PDK = Pdk(
    name="VTT-3umSOI",
    cells=cells,
    cross_sections=cross_sections,
    layers=LAYER,
    layer_stack=None,
    layer_views=LAYER_VIEWS,
    layer_transitions=LAYER_TRANSITIONS,
    constants=constants,
)

GPATH.sparameters = PATH.sparameters

# pdk.register_cells_yaml(dirpath=pathlib.Path(__file__).parent.absolute())

# gdsfactory.routing.all_angle.LOW_LOSS_CROSS_SECTIONS = [
#     {"cross_section": "rib", "settings": {"width": 2.5}},
#     {"cross_section": "xs_sc", "settings": {"width": 6.0}},
#     {"cross_section": "xs_sc", "settings": {"width": 3.0}},
# ]
#
PDK.activate()
__version__ = "0.1.0"

if __name__ == "__main__":
    # layer_views = LayerViews(filepath=PATH.lyp_yaml)
    # layer_views.to_lyp(PATH.lyp)

    print(PDK.name)
