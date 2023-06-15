from typing import Optional, Tuple, Union

import numpy as np

import gdsfactory as gf
from gdsfactory.components.text import text
from gdsfactory.typings import LayerSpec, ComponentSpec, Float2

import vtt_tech


def box(x0, y0, w, h):
    dw = w / 2.0
    dh = h / 2.0
    retval = [
        [x0 + dw, y0 + dh],
        [x0 + dw, y0 - dh],
        [x0 - dw, y0 - dh],
        [x0 - dw, y0 + dh],
    ]

    return retval


@gf.cell
def die(
    size: Tuple[float, float] = (5000.0, 9500.0),
    street_width: float = 75.0,
    street_length: float = 1000.0,
    die_name: Optional[str] = "chip99",
    text_size: float = 100.0,
    text_location: Union[str, Float2] = "SW",
    layer: LayerSpec = None,  # "FLOORPLAN",
    bbox_layer: Optional[LayerSpec] = None,
    draw_corners: bool = True,
    draw_dicing_lane: bool = True,
    text_component: ComponentSpec = text,
) -> gf.Component:
    c = gf.Component(name="die")
    w, h = size[0], size[1]

    for layer, size in vtt_tech.frame_dimensions.items():
        c.add_polygon(box(w / 2.0 - size / 2.0, 0.0, size, h), layer=layer)
        c.add_polygon(box(-w / 2.0 + size / 2.0, 0.0, size, h), layer=layer)

        c.add_polygon(box(0.0, h / 2.0 - size / 2.0, w, size), layer=layer)
        c.add_polygon(box(0.0, -h / 2.0 + size / 2.0, w, size), layer=layer)

    if bbox_layer:
        c.add_polygon(
            [[w / 2, h / 2], [w / 2, -h / 2], [-w / 2, -h / 2], [-w / 2, h / 2]],
            layer=bbox_layer,
        )

    c.info["port_x_position_west"] = (
        -w / 2.0 + vtt_tech.frame_dimensions[vtt_tech.LAYER.WG_SNGL_ADD] + 1.5
    )
    c.info["port_x_position_east"] = (
        w / 2.0 - vtt_tech.frame_dimensions[vtt_tech.LAYER.WG_SNGL_ADD] - 1.5
    )

    c.info["port_y_position_north"] = (
        h / 2.0 - vtt_tech.frame_dimensions[vtt_tech.LAYER.WG_SNGL_ADD] - 1.5
    )
    c.info["port_y_position_south"] = (
        -h / 2.0 + vtt_tech.frame_dimensions[vtt_tech.LAYER.WG_SNGL_ADD] + 1.5
    )

    return c
