import gdsfactory as gf
from gdsfactory.components import text
from gdsfactory.typings import ComponentSpec, Coordinate, Float2, LayerSpec

import gvtt
from gvtt.layers import LAYER


def box(x0: float, y0: float, w: float, h: float) -> list[Coordinate]:
    dw = w / 2.0
    dh = h / 2.0
    return [
        (x0 + dw, y0 + dh),
        (x0 + dw, y0 - dh),
        (x0 - dw, y0 - dh),
        (x0 - dw, y0 + dh),
    ]


@gf.cell
def die(
    size: tuple[float, float] = (5000.0, 9500.0),
    street_width: float = 75.0,
    street_length: float = 1000.0,
    die_name: str | None = "chip99",
    text_size: float = 100.0,
    text_location: str | Float2 = "SW",
    layer: LayerSpec | None = None,  # "FLOORPLAN",
    bbox_layer: LayerSpec | None = None,
    draw_corners: bool = True,
    draw_dicing_lane: bool = True,
    text_component: ComponentSpec = text,
) -> gf.Component:
    c = gf.Component(name="die")
    w, h = size[0], size[1]

    for layer_, size_ in gvtt.frame_dimensions.items():
        c.add_polygon(box(w / 2.0 - size_ / 2.0, 0.0, size_, h), layer=layer_)
        c.add_polygon(box(-w / 2.0 + size_ / 2.0, 0.0, size_, h), layer=layer_)

        c.add_polygon(box(0.0, h / 2.0 - size_ / 2.0, w, size_), layer=layer_)
        c.add_polygon(box(0.0, -h / 2.0 + size_ / 2.0, w, size_), layer=layer_)

    if bbox_layer:
        c.add_polygon(
            [(w / 2, h / 2), (w / 2, -h / 2), (-w / 2, -h / 2), (-w / 2, h / 2)],
            layer=bbox_layer,
        )

    c.info["frame_margin"] = gvtt.frame_dimensions[LAYER.WG_SNGL_ADD] + 1.5

    # c.info["port_x_position_west"] = (
    #     -w / 2.0 + gvtt.frame_dimensions[gvtt.LAYER.WG_SNGL_ADD] + 1.5
    # )
    # c.info["port_x_position_east"] = (
    #     w / 2.0 - gvtt.frame_dimensions[gvtt.LAYER.WG_SNGL_ADD] - 1.5
    # )

    # c.info["port_y_position_north"] = (
    #     h / 2.0 - gvtt.frame_dimensions[gvtt.LAYER.WG_SNGL_ADD] - 1.5
    # )
    # c.info["port_y_position_south"] = (
    #     -h / 2.0 + gvtt.frame_dimensions[gvtt.LAYER.WG_SNGL_ADD] + 1.5
    # )

    return c


if __name__ == "__main__":
    c = die()
    c.show()
