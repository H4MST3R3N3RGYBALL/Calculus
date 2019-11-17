import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
f, ax = plt.subplots()
star = mpath.Path.unit_regular_star(6)
circle = mpath.Path.unit_circle()
# concatenate the circle with an internal cutout of the star
verts = np.concatenate([circle.vertices, star.vertices[::-1, ...]])
codes = np.concatenate([circle.codes, star.codes])
cut_star = mpath.Path(verts, codes)
m3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
z = [61,62,62,63,63,64,63,60,65,62,62,63,63,31,0,17,4]
ax.plot(np.array(m3), np.array(z), '--r', marker=cut_star, markersize=15)
ax.set(xlabel='Time (s)', ylabel='Velocity(MPH)',
       title='Time vs Velocity Graph')
ax.grid()

plt.show()


