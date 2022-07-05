import pooch
import os
import pickle


data = pooch.create(
    # Use the default cache folder for the operating system
    path=pooch.os_cache("my-project"),
    # The remote data is on Github
    # base_url is a required param, even though we override this
    # using individual urls in the registry.
    base_url="https://github.com/scipy-datasets/",
    registry={
        "ascent.dat": "e8a84939484463ab8051aedc5b40aa262ab33a91d6458a6cd13c6a1cad5a023d"
    },
    urls = {
        "ascent.dat": "https://raw.githubusercontent.com/scipy-datasets/dataset-ascent/main/ascent.dat"
    }
)


fname = data.fetch("ascent.dat")

with open(fname, 'rb') as f:
    ascent = array(pickle.load(f))

print(ascent)
