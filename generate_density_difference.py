#! /usr/bin/env python

"""
This script takes three cube files and calculates 
cube1 - (cube2+cube3)
and prints it to a file density_difference.cube

"""

from sys import argv
from cube import cube
cube_sys = cube()
cube_part1 = cube()
cube_part2 = cube()

cube_sys.read(argv[1])
cube_part1.read(argv[2])
cube_part2.read(argv[3])


cube_part1+cube_part2
cube_sys-cube_part1

cube_sys.write('density_difference.cube')
