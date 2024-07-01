

Here are the components available in the PDK


Cells
=============================


bend_euler
----------------------------------------------------

.. autofunction:: gvtt.components.bend_euler

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.bend_euler(angle=90.0, p=1.0, with_arc_floorplan=False, direction='ccw', with_bbox=True)
  c.plot()



die
----------------------------------------------------

.. autofunction:: gvtt.components.die

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.die(size=(5000.0, 9500.0), street_width=75.0, street_length=1000.0, die_name='chip99', text_size=100.0, text_location='SW', draw_corners=True, draw_dicing_lane=True)
  c.plot()



edge_coupler_rib
----------------------------------------------------

.. autofunction:: gvtt.components.edge_coupler_rib

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.edge_coupler_rib(edge_coupling_width=3.0, polishing_length=25.0, side='W', xpos=0.0, ypos=0.0)
  c.plot()



mmi1x2
----------------------------------------------------

.. autofunction:: gvtt.components.mmi1x2

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.mmi1x2(width=1.874, width_taper=1.874, length_taper=1.0, length_mmi=43.25, width_mmi=6.25, gap_mmi=1.251, cross_section='xs_sc')
  c.plot()



mmi2x2
----------------------------------------------------

.. autofunction:: gvtt.components.mmi2x2

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.mmi2x2(width_taper=1.874, length_taper=1.0, length_mmi=112.0, width_mmi=5, gap_mmi=1.25, cross_section='xs_sc')
  c.plot()



rib_taper
----------------------------------------------------

.. autofunction:: gvtt.components.rib_taper

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.rib_taper(width1=1, width2=1, taper_ratio=50.0)
  c.plot()



rib_to_strip
----------------------------------------------------

.. autofunction:: gvtt.components.rib_to_strip

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.rib_to_strip(length=200.0, width1=3.0, width2=3.0)
  c.plot()



straight
----------------------------------------------------

.. autofunction:: gvtt.components.straight

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.straight(length=10.0, npoints=2)
  c.plot()



straight_rib
----------------------------------------------------

.. autofunction:: gvtt.components.straight_rib

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.straight_rib(length=10.0, npoints=2)
  c.plot()



straight_sc
----------------------------------------------------

.. autofunction:: gvtt.components.straight_sc

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.straight_sc(length=10.0, npoints=2)
  c.plot()



strip_taper
----------------------------------------------------

.. autofunction:: gvtt.components.strip_taper

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.strip_taper(width1=1, width2=1, taper_ratio=25.0)
  c.plot()



strip_to_rib
----------------------------------------------------

.. autofunction:: gvtt.components.strip_to_rib

.. plot::
  :include-source:

  import gvtt

  c = gvtt.components.strip_to_rib(length=200.0, width1=3.0, width2=3.0)
  c.plot()
