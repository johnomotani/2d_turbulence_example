2D turbulence simulations
-------------------------

This STORM2D simulation has been set up as a starting point for uncertainty
quantification (UQ) of turbulence simulations.

The simulation is intended to be run with the public version of STORM2D available from
https://github.com/boutproject/STORM (in the `storm2d/` subdirectory). A submission
script for the Marconi supercomputer (called `jobscript`) is included, which shows how
to call storm2d (the path may need updating depending on where you compiled storm2d).

The script `radial_profiles.py` provides a quick check of the average (binned in 20
output step chunks) radial profiles of the density over time. Based on the output, it
looks like after the first 100 steps (corresponding to 1 ms) of the simulation, it is
probably in a saturated state. The time after 1ms is therefore to be analysed.

`generate_output.py` is intended to be a basis for passing output to a UQ framework. It
calculates an averaged (over time and binormal direction) radial profile of density, and
puts it in a numpy array - this then either needs to be saved somehow, or the code
copied into another script to do something with the output. The script uses xBOUT (and
xarray), but could easily be re-written to use boutdata.collect (and numpy) instead.
