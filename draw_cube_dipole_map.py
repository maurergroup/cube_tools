#! /usr/bin/env python
from cube import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
cube = cube()
filename = str(sys.argv[1])
castep2cube_flag=bool(sys.argv[2])
start = time.time()
cube.read(filename,castep2cube_format=castep2cube_flag)
stop = time.time()
print 'runtime of read-in:', stop-start

section, workfunction = cube.dipole_map_xy()
print section.shape

X,Y = np.meshgrid(range(cube.x_len),list(np.linspace(cube.y_len-1,0,cube.y_len)))
X=X*cube.x_vec[0]+Y*cube.y_vec[0]
print X
Y=Y*cube.y_vec[1]

#im = plt.imshow(section, cmap=cm.RdBu, vmin=abs(section).min(), vmax=abs(section).max(), extent=[0, X.max(), 0, Y.max()])
#im.set_interpolation('bilinear')
#im = ax.pcolor(X, Y, section, cmap=cm.RdBu, vmin=section.min(), vmax=section.max())
#im = plt.contourf(X,Y,section)
fig = plt.figure()#figsize=(8,4))
ax = fig.add_subplot(111)
mmin = section.min()
mmax = -mmin
im=ax.pcolormesh(X,Y,section, shading='gouraud', cmap=cm.RdBu, vmin=mmin, vmax=mmax)
print 'maximum x valuey:',X.max()
print 'maximum y valuey:',Y.max()
cb = fig.colorbar(im, ax=ax)
plt.show()
fig = plt.figure()#figsize=(8,4))
ax = fig.add_subplot(111)
mmin = workfunction.min()
mmax = -mmin
im=ax.pcolormesh(X,Y,workfunction, shading='gouraud', cmap=cm.RdBu, vmin=mmin, vmax=mmax)
cb = fig.colorbar(im, ax=ax)
plt.show()

import pickle

output = open('workfunction_map.pkl','wb')
pickle.dump(workfunction, output)
output.close()
