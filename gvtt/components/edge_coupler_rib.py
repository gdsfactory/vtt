import gdsfactory as gf
from gdsfactory.component import Component

from gvtt.tech import rib


@gf.cell
def edge_coupler_rib(
    edge_coupling_width: float = 3.0,
    polishing_length: float = 25.0,
    side: str = "W",
    xpos: float = 0.0,
    ypos: float = 0.0,
) -> Component:
    """Returns a rib waveguide edge coupler.

    Args:
        edge_coupling_width: width of the edge coupling waveguide.
        polishing_length: length of the edge coupling waveguide.
        side: side of the edge coupler (W, E, N, S).
        xpos: dx position of the edge coupler.
        ypos: dy position of the edge coupler.
    """
    c = gf.Component()
    side = side.upper()

    if side == "E":
        orientation = 180
    elif side == "N":
        orientation = -90
    elif side == "S":
        orientation = 90

    elif side == "W":
        orientation = 0
    ref = c << gf.components.straight(
        cross_section=rib(edge_coupling_width), length=polishing_length
    )
    ref.drotate(orientation)
    ref.dmove((xpos, ypos))

    c.add_port("o1", port=ref.ports["o2"])
    return c


if __name__ == "__main__":
    c = edge_coupler_rib()
    c.show()
