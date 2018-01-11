#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Exercise 4: Delineate watershed based on TauDEM functions with PyGeoC

from pygeoc.TauDEM import TauDEMWorkflow


def main():
    """The simplest usage of watershed delineation based on TauDEM."""
    dem = '../tests/data/Jamaica_dem.tif'
    num_proc = 2
    wp = '../tests/data/tmp_results/wtsd_delineation'

    TauDEMWorkflow.watershed_delineation(num_proc, dem, workingdir=wp)


if __name__ == "__main__":
    main()
