#!/usr/bin/env python3

from xbout import open_boutdataset

ds = open_boutdataset("data/BOUT.dmp.*.nc", keep_xboundaries=False).squeeze()

# Select 'saturated turbulent state'
# Warning: values needed for this selection are potentially parameter-dependent...
ds = ds.isel(t=slice(101, None))

# `.values` converts the xarray.DataArray to a numpy array
density_profile = ds["n"].mean(dim=["t", "z"]).values

# save or use the profile here
