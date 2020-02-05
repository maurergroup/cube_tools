#!/usr/bin/python
import numpy as np
import math
import os
import shutil
import sys
from ase.units import Bohr
file1 = sys.argv[1]

#This script takes several .cube files and calculates the 
#overlap integral of their absolute values ve to have the same dimension and everything

#Bohr=1./Bohr

Overlap = []
print(('Integrate ',file1,' in x and y direction'))
for i in range(1):

  startingpoint = []
  n_atoms = None
  voxels_x = None
  voxels_y = None
  voxels_z = None
  incr = None

  wvfn1 = open(file1).readlines()

  n_atoms = int(wvfn1[2].split()[0])
  #forget the first two lines
  currentline = 2
  test = wvfn1[currentline].split()
  for i in range(3) :
    startingpoint.append( float( test[i+1] ) )
  print('n_atoms         startingpoint  ')
  print((n_atoms, '    ', startingpoint))
  currentline += 1
  test = wvfn1[currentline].split()
  voxels_x = int(test[0])
  incr = float(test[1])
  currentline += 1
  test = wvfn1[currentline].split()
  voxels_y = int(test[0])
  currentline += 1
  test = wvfn1[currentline].split()
  voxels_z = int(test[0])
  print(' voxels                increment ')
  print((voxels_x, ' ' , voxels_y, ' ' , voxels_z,'      ', incr))
  currentline +=1
  #forget the coordinates
  currentline += n_atoms
  #generating overlap function
  n_points = voxels_x * voxels_y * voxels_z
  func1 = []
  while (currentline < len(wvfn1) ):
    test1 = wvfn1[currentline].split()
    if len(test1) > 0:
      for j in range(len(test1)):
	      func1.append( abs(float(test1[j])) )
    currentline += 1
  #integration
  dV = incr**3
#  result = np.zeros(voxels_z)
  result = np.zeros(voxels_x)
  norm1 = 0.0
  norm2 = 0.0

  for ix in range(voxels_x):
    for iy in range(voxels_y):
      for iz in range(voxels_z):
        result[ix] += func1[ix*voxels_x*voxels_y+iy*voxels_y+iz] * incr**2
        norm1 += func1[ix*voxels_x*voxels_y+iy*voxels_y+iz] * dV
    norm2 += result[ix] * incr

#  for iz in range(voxels_z):
#    for ix in range(voxels_x):
#      for iy in range(voxels_y):
#        result[iz] += func1[ix*voxels_x*voxels_y+iy*voxels_y+iz] * incr**2
#        norm1 += func1[ix*voxels_x*voxels_y+iy*voxels_y+iz] * dV
#    norm2 += result[iz] * incr

  print(('norm1  : ',norm1*Bohr**3))
  print(('norm2  : ',norm2*Bohr**3))
  out=open('Output.txt',mode='w')
  print(('voxels ', voxels_x))
  for ix in range(voxels_x):
    out.write('{0:16.8f} {1:16.8f} \n'.format((ix*incr+startingpoint[0])*Bohr,result[ix]*Bohr**2))


out.close()
