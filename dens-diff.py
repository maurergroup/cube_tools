#!/usr/bin/python
import numpy as np
import math
import os
import shutil
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

#This script takes 2 .cube files and calculates the 
#density or orbital difference
#Their grids have to have the same dimension and everything

print('density difference between ', file1 , ' and ', file2)
if True:
  startingpoint = []
  n_atoms = None
  voxels_x = None
  voxels_y = None
  voxels_z = None
  incr = None

  wvfn1 = open(file1).readlines()
  wvfn2 = open(file2).readlines()

  n_atoms = int(wvfn1[2].split()[0])
  #forget the first two lines
  currentline = 2
  test = wvfn1[currentline].split()
  for i in range(3) :
    startingpoint.append( float( test[i+1] ) )
  print('n_atoms         startingpoint  ')
  print(n_atoms, '    ', startingpoint)
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
  print(voxels_x, ' ' , voxels_y, ' ' , voxels_z,'      ', incr)
  currentline +=1
  #forget the coordinates
  currentline += n_atoms
  #generating overlap function
  n_points = voxels_x * voxels_y * voxels_z
  func1 = []
  func2 = []
  func_difference = []
  while (currentline < len(wvfn1) ):
    test1 = wvfn1[currentline].split()
    test2 = wvfn2[currentline].split()
    if len(test1) > 0:
      for j in range(len(test1)):
	func1.append( float(test1[j]) )
	func2.append( float(test2[j]) )
	func_difference.append( float(test1[j]) - float(test2[j]) )
    currentline += 1

  #now writing out the density difference
f=open('dens_diff.cube','w')
for i in range(6):
  f.write(wvfn1[i]) 
for i in range(n_atoms):
  f.write(wvfn1[i+6])
for i in range(voxels_x*voxels_y*voxels_z): 
  f.write(str(func_difference[i])+' \n')

f.close()




