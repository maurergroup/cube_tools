#!/bin/python
import numpy as np
import math
import os
import shutil
import sys

#This script takes several .cube files and calculates the 
#overlap integral of their absolute values 
#Their grids have to have the same dimension and everything
n_configs = 0
inputfile = open('input').readlines()
n_configs = len(inputfile)
coeff = []
file1 = []
file2 = []
for i in range(n_configs):
  coeff.append( float(inputfile[i].split()[0]) )
  file1.append( inputfile[i].split()[1])
  file2.append( inputfile[i].split()[2])

Overlap = []
print('Overlap between ', file1 , ' and ', file2)
for nc in range(n_configs):

  startingpoint = []
  n_atoms = None
  voxels_x = None
  voxels_y = None
  voxels_z = None
  incr = None

  wvfn1 = open(file1[nc]).readlines()
  wvfn2 = open(file2[nc]).readlines()

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
  func_product = []
  while (currentline < len(wvfn1) ):
    test1 = wvfn1[currentline].split()
    test2 = wvfn2[currentline].split()
    if len(test1) > 0:
      for j in range(len(test1)):
	func1.append( abs(float(test1[j])) )
	func2.append( abs(float(test2[j])) )
	func_product.append( abs(float(test1[j]) * float(test2[j])) )
    currentline += 1
  #integration
  dV = incr**3
  result = 0.0
  norm1 = 0.0
  norm2 = 0.0
  for ix in range(voxels_x):
    for iy in range(voxels_y):
      for iz in range(voxels_z):
	norm1 += (func1[ix*voxels_x*voxels_y+iy*voxels_y+iz]**2) * dV
	norm2 += (func2[ix*voxels_x*voxels_y+iy*voxels_y+iz]**2) * dV
	result += func_product[ix*voxels_x*voxels_y+iy*voxels_y+iz] * dV

  print('config ', nc)
  print(norm1)
  print(norm2)
  print(result)
  print('---------------------')
  Overlap.append( result/np.sqrt(norm1*norm2) )
  print('Overlap ', Overlap[nc])
  
print('Calculating Lambda')
coeff_sum = 0.0
lamda = 0.0
for nc in range(n_configs):
  coeff_sum += coeff[nc]
for nc in range(n_configs):
  lamda += Overlap[nc] * coeff[nc]
  
lamda /= coeff_sum
print('LAMDA  ', lamda)
