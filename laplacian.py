#! /usr/bin/env python

"""
This script takes three cube files and calculates 
cube1 - (cube2+cube3)
and prints it to a file density_difference.cube

"""

from sys import argv
from cube import cube
cube_sys = cube()

cube_sys.read(argv[1])

cube_sys.laplacian()

cube_sys.write('laplacian.cube')
