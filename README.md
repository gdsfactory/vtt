# gdsfactory-vtt-public-pdk

A public [gdsfactory](https://gdsfactory.github.io/gdsfactory/index.html#) process design kit (PDK) for VTT's 3 um SOI
platform.

&copy; VTT 2023

## Installation

Easiest way to install is by using the [Anaconda](https://www.anaconda.com/download) Python distribution. Download
the `environment.yml` file in the inder folder and then run in an Anaconda prompt:

    conda env create --file environment.yml

This will create a new Python environment labeled `gf` with all the required packages installed.
You will need to point your editor Python interpreter to this environment, how to do this depends on the editor.

In addition you should install [Klayout](http://www.klayout.de) and the Klive package from the integrated pacakge
manager.

## Testing the PDK without installation

If you want to test the PDK you can run it in browser by clicking the link below.
This will open up a new page with a preconfigured Jupyter notebook running on [mybinder.org](https://mybinder.org).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fgitlab.vtt.fi%2Fttemth%2Fgdsfactory-vtt-public-pdk/HEAD)
