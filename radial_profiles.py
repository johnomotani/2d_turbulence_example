#!/usr/bin/env python3

from matplotlib import pyplot as plt
from xbout import open_boutdataset
from sys import argv

if len(argv) > 1:
    directory = argv[1]
else:
    directory = "data"

ds = open_boutdataset(f"{directory}/BOUT.dmp.*.nc", keep_xboundaries=False).squeeze()

# Drop t=0 point just so that chunk sizes line up nicely with the number of outputs
ds = ds.isel(t=slice(1, None))

nt = ds.sizes["t"]
chunk_length = 20
n_chunks = (nt + chunk_length - 1) // chunk_length

for var in ["n", "vort", "phi"]:
    plt.figure()
    for i in range(n_chunks):
        print(f"processing chunk {i}/{n_chunks}", flush=True)
        subset = ds.isel(t=slice(i * chunk_length, (i + 1) * chunk_length))
        profile = subset[var].mean(dim=["t", "z"])

        profile.plot(label=i)
    plt.legend()

    plt.savefig(f"profiles{var}.pdf")
plt.show()
