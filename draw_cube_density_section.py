#! /usr/bin/env python
from cube import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
cube = cube()
filename = str(sys.argv[1])
height = float(sys.argv[2])
start = time.time()
cube.read(filename)
stop = time.time()
print('runtime of read-in:', stop-start)

height = int(height/cube.bohr2ang/cube.z_vec[2])
print('printing crossection at height equal to:', height*cube.z_vec[2]*cube.bohr2ang)
cube.density.shape=(cube.x_len,cube.y_len,cube.z_len)
section = cube.density[:,:,height]
print(section.shape)

X,Y = np.meshgrid(list(range(cube.x_len)),list(np.linspace(cube.y_len-1,0,cube.y_len)))
X=X*cube.x_vec[0]+Y*cube.y_vec[0]
print(X)
Y=Y*cube.y_vec[1]
fig = plt.figure()#figsize=(8,4))
ax = fig.add_subplot(111)

#im = plt.imshow(section, cmap=cm.RdBu, vmin=abs(section).min(), vmax=abs(section).max(), extent=[0, X.max(), 0, Y.max()])
#im.set_interpolation('bilinear')
#im = ax.pcolor(X, Y, section, cmap=cm.RdBu, vmin=section.min(), vmax=section.max())
#im = plt.contourf(X,Y,section)

###Py3 now requires a transpose()

im=ax.pcolormesh(X,Y,-section.transpose(), shading='gouraud', cmap=cm.RdBu)
print('maximum x valuey:',X.max())
print('maximum y valuey:',Y.max())
cb = fig.colorbar(im, ax=ax)
plt.show()

