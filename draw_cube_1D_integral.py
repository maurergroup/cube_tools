#! /usr/bin/env python
from cube import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
cube = cube()
filename = str(sys.argv[1])
start = time.time()
cube.read(filename)
stop = time.time()
print 'runtime of read-in:', stop-start

cube.density.shape=(cube.x_len,cube.y_len,cube.z_len)


cube.integrate_xy('Output.txt')

