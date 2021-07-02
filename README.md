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

UQ
--

Possibly useful input parameters to vary for UQ:
* `mesh:Ly` - sets the 'connection length' used in parallel closures. In reality varies
  across the SOL, so there is uncertainty in the most representative value to use in
  these 'drift plane' simulations. Given in units of `rho_s0`, the default value of 5500
  is around 10 m. JTO suggests reasonable variation maybe +/- 20%.
* `R_c` - 'major radius' used to calculate strength of curvature terms. In reality
  varies across SOL. Given in units of m. JTO suggests reasonable uncertainty is
  probably around the radial box size (`Lx = 150 * rho_s0 ~ 0.193 m), so say 0.2 m.
* `mu_n0` - perpendicular diffusion term in the density equation. Used primarily for
  numerical stabilisation (to provide dissipation before flutuations reach the grid
  scale) - ideally results should be insensitive to the exact value. If results are
  insensitive within increasing or decreasing by an order of magnitude, we would be very
  happy (a factor of 2 would be acceptable), so JTO suggests a (logarithmic) range of
  variation 0.1x - 10x.
* `mu_vort0` - perpendicular diffusion term in the vorticity equation. Same comments as
  `mu_n0`. Could make sense to vary both together, although it would be interesting to
  know the sensitivity to both separately if that is feasible.
* `S:A` - amplitude of the density source term. Expect the radial profiles to be
  sensitive to this (JTO guesses probably roughly proportional to it). Would normally be
  chosen such that the time-average density at some reference location matches a desired
  value. Not sure if it's a good candidate to vary or not - JTO would probably lean
  towards not.
* `S:w` - width of the density source term. Set up in such a way that changing `S:w`
  does not change the total (integrated) particle source. Probably expect results to be
  fairly insensitive to this value - it is usually set arbitrarily (in the best case,
  should be comparable to the penetration depth of neutrals). JTO suggests varying by
  maybe 0.5x - 2x. Don't want to make it too large (or the source term overlaps the
  region where we want to look at turbulence) or too small (or it approaches the grid
  scale and we probably change the actual particle source, since the integral is
  constant for the analytic input expression, but not the discretised input).
