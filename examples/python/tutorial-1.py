import gdsfactory as gf

if __name__ == "__main__":
    c = gf.Component(
        "training-1"
    )  # Component can be though to be a canvas to draw on. It maps to GDS cells.

    # define components using standard gdsfactory functions
    straight = gf.components.straight(length=10)
    bend = gf.get_component(
        "bend_euler", angle=90, decorator=gf.add_pins.add_pins_triangle
    )

    # Insert the above components into the Component. You can use the same element multiple times.
    # Each insertion creates a reference which can be stored into a variable and used later for making
    # connections.

    s1 = c << straight
    b1 = c << bend
    b2 = c << bend
    b3 = c << bend
    b4 = c << bend
    s2 = c << straight

    # Reverse the direction of two of the bends.
    b2.mirror()
    b3.mirror()

    # Each component has ports defined. Connecting moves the component so the ports are matching.
    b1.connect("o1", s1.ports["o2"])
    b2.connect("o1", b1.ports["o2"])
    b3.connect("o1", b2.ports["o2"])
    b4.connect("o1", b3.ports["o2"])
    s2.connect("o1", b4.ports["o2"])

    c.show()
