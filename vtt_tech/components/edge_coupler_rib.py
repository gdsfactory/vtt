import gdsfactory as gf
from gdsfactory.component import Component
from vtt_tech.xsections import rib


@gf.cell
def edge_coupler_rib(edge_coupling_width : float = 3.0,
                     polishing_length: float = 25.0,
                     side : str = 'W',
                     pos : float = 0.0,
                     die: gf.component_reference.ComponentReference = None) -> Component:

    c = gf.Component()
    side = side.upper()

    if side == 'W':
        ypos = pos
        xpos = die.info['port_x_position_west']
        orientation = 0
    if side == 'E':
        ypos = pos
        xpos = die.info['port_x_position_east']
        orientation = 180
    if side == 'N':
        xpos = pos
        ypos = die.info['port_y_position_north']
        orientation = -90
    if side == 'S':
        xpos = pos
        ypos = die.info['port_y_position_south']
        orientation = 90

    ref = c << gf.components.straight(cross_section=rib(edge_coupling_width), length=polishing_length)
    ref.rotate(orientation)
    ref.move((xpos, ypos))

    c.add_port('o1', port=ref.ports['o2'])
    c.absorb(ref)

    return c