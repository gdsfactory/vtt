import gdsfactory as gf

c = gf.Component("training-3")


@gf.cell
def arm(angle: float = 90.0) -> gf.Component:
    c = gf.Component(name="arm")

    str = gf.components.straight(length=10)
    bend = gf.get_component("bend_euler", angle=angle)

    s1 = c << str
    b1 = c << bend
    b2 = c << bend
    b3 = c << bend
    b4 = c << bend
    s2 = c << str

    s1.connect("o2", b1.ports["o1"])

    b2.mirror()
    b3.mirror()

    b2.connect("o1", b1.ports["o2"])
    b3.connect("o1", b2.ports["o2"])
    b4.connect("o1", b3.ports["o2"])

    s2.connect("o1", b4.ports["o2"])

    c.add_port("o1", port=s1.ports['o1'])
    c.add_port("o2", port=s2.ports['o2'])

    return c


a1 = c << arm()
a2 = c << arm()
a2.mirror()

mmi = gf.get_component("mmi1x2")

mmi1 = c << mmi
mmi2 = c << mmi

a1.connect('o1', mmi1.ports['o2'])
a2.connect('o1', mmi1.ports['o3'])

mmi2.connect('o3', a1.ports['o2'])

c.show()
