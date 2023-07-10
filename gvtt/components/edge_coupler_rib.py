import gdsfactory as gf
from gdsfactory.component import Component
from gvtt.xsections import rib


@gf.cell
def edge_coupler_rib(
    edge_coupling_width: float = 3.0,
    polishing_length: float = 25.0,
    side: str = "W",
    xpos: float = 0.0,
    ypos: float = 0.0,
) -> Component:
    c = gf.Component()
    side = side.upper()

    if side == "W":
        orientation = 0
    if side == "E":
        orientation = 180
    if side == "N":
        orientation = -90
    if side == "S":
        orientation = 90

    ref = c << gf.components.straight(
        cross_section=rib(edge_coupling_width), length=polishing_length
    )
    ref.rotate(orientation)
    ref.move((xpos, ypos))

    c.add_port("o1", port=ref.ports["o2"])
    c.absorb(ref)
    return c


if __name__ == "__main__":
    c = edge_coupler_rib()
    c.show()
