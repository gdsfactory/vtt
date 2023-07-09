from gdsfactory.typings import Layer
from pydantic import BaseModel


class LayerMap(BaseModel):
    # waveguide types
    TYPE_RIB: Layer = (89, 0)
    TYPE_STRIP: Layer = (89, 1)

    AX_BBOX: Layer = (63, 10)
    AX_BPIN: Layer = (63, 12)
    AX_BVIZ: Layer = (63, 11)
    AX_INFO: Layer = (63, 63)
    AX_LINE: Layer = (63, 40)
    AX_NOME: Layer = (63, 1)
    AX_NOUS: Layer = (63, 9)
    AX_NOWG: Layer = (63, 2)
    AX_NOXX: Layer = (63, 0)
    AX_TRIP: Layer = (63, 41)
    AX_WARN: Layer = (63, 42)
    ME_ALUM_ADD: Layer = (2, 13)
    ME_ALUM_CPY: Layer = (2, 33)
    ME_ALUM_LF: Layer = (2, 3)
    ME_ALUM_SUB: Layer = (2, 23)
    ME_GOLD_ADD: Layer = (2, 12)
    ME_GOLD_CPY: Layer = (2, 32)
    ME_GOLD_LF_C: Layer = (2, 2)
    ME_GOLD_SUB: Layer = (2, 22)
    ME_HVIA_ADD: Layer = (2, 14)
    ME_HVIA_CPY: Layer = (2, 34)
    ME_HVIA_DF: Layer = (2, 4)
    ME_HVIA_SUB: Layer = (2, 24)
    ME_WIPO_ADD: Layer = (2, 16)
    ME_WIPO_CPY: Layer = (2, 36)
    ME_WIPO_DF_C: Layer = (2, 6)
    ME_WIPO_SUB: Layer = (2, 26)
    ME_WIRE_ADD: Layer = (2, 15)
    ME_WIRE_CPY: Layer = (2, 35)
    ME_WIRE_LF: Layer = (2, 5)
    ME_WIRE_SUB: Layer = (2, 25)
    NP_NIMP_ADD: Layer = (5, 13)
    NP_NIMP_CPY: Layer = (5, 33)
    NP_NIMP_DF: Layer = (5, 3)
    NP_NIMP_SUB: Layer = (5, 23)
    NP_PIMP_ADD: Layer = (5, 12)
    NP_PIMP_CPY: Layer = (5, 32)
    NP_PIMP_DF: Layer = (5, 2)
    NP_PIMP_SUB: Layer = (5, 22)
    WG_ARCO_ADD: Layer = (1, 14)
    WG_ARCO_CPY: Layer = (1, 34)
    WG_ARCO_LF: Layer = (1, 4)
    WG_ARCO_SUB: Layer = (1, 24)
    WG_DEOX_ADD: Layer = (1, 13)
    WG_DEOX_CPY: Layer = (1, 33)
    WG_DEOX_DF: Layer = (1, 3)
    WG_DEOX_SUB: Layer = (1, 23)
    WG_LANE_ADD: Layer = (1, 12)
    WG_LANE_CPY: Layer = (1, 32)
    WG_LANE_DF: Layer = (1, 2)
    WG_LANE_SUB: Layer = (1, 22)
    WG_MOST_ADD: Layer = (1, 11)
    WG_MOST_CPY: Layer = (1, 31)
    WG_MOST_DF: Layer = (1, 1)
    WG_MOST_SUB: Layer = (1, 21)
    WG_PEDE_ADD: Layer = (1, 16)
    WG_PEDE_CPY: Layer = (1, 36)
    WG_PEDE_LF: Layer = (1, 6)
    WG_PEDE_SUB: Layer = (1, 26)
    WG_RIBS_ADD: Layer = (1, 10)
    WG_RIBS_CPY: Layer = (1, 30)
    WG_RIBS_DF: Layer = (1, 0)
    WG_RIBS_SUB: Layer = (1, 20)
    WG_SNGL_ADD: Layer = (1, 15)
    WG_SNGL_CPY: Layer = (1, 35)
    WG_SNGL_DF: Layer = (1, 5)
    WG_SNGL_SUB: Layer = (1, 25)

    # AUX
    FLOORPLAN: Layer = (63, 98)

    # common gdsfactory layers
    LABEL_INSTANCE: Layer = (66, 0)
    DEVREC: Layer = (68, 0)
    PORT: Layer = (99, 10)
    PORTE: Layer = (99, 11)
    TE: Layer = (203, 0)
    TM: Layer = (204, 0)
    TEXT: Layer = (66, 0)

    class Config:
        frozen = True
        extra = "forbid"


LAYER = LayerMap()


if __name__ == "__main__":
    import gdsfactory as gf
    from gdsfactory.technology.klayout_tech import KLayoutTechnology
    from gvtt.config import PATH

    # from gdsfactory.technology import lyp_to_dataclass

    # layers = lyp_to_dataclass(PATH.lyp)
    # print(layers)
    LAYER_VIEWS = gf.technology.LayerViews(filepath=PATH.lyp)
    LAYER_VIEWS.to_yaml(PATH.lyp_yaml)
    t = KLayoutTechnology(
        name="VTT",
        layer_map=dict(LAYER),
        layer_views=LAYER_VIEWS,
        # layer_stack=LAYER_STACK,
        # connectivity=connectivity,
    )
    t.write_tech(tech_dir=PATH.tech_dir)
    # print(LAYER)
