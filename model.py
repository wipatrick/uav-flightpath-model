import matplotlib.path as mpath
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import numpy as np


plt.ylim([0,100])
plt.xlim([0,100])
plt.gca().set_aspect('equal', adjustable='box')

ax = plt.subplot(111)

major_ticks = np.arange(0, 101, 10)
minor_ticks = np.arange(0, 101, 5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.set_xlabel('x')
ax.set_ylabel('y')

# and a corresponding grid
ax.grid(which='both')

# or if you want differnet settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


# add source
#
# [x], [y]: x,y position
# 'ro': red circle
source = plt.plot([35], [25], 'ro', markersize=10)
plt.plot([35, 75], [25, 65], color='red', linewidth=2)
# plt.plot([35, 35], [25, 85], color='r', linewidth=2)

circle1=plt.Circle((35,25),5, color='red', alpha=0.4)
ax.add_artist(circle1)


# add geofence
#
# http://matplotlib.org/api/patches_api.html
#
# facecolor='none': no fill
# lw: line width
# alpha: opacity level
polygon = plt.Polygon([
            [20, 10], [10, 50], [20, 80], [50, 100], [90, 90], [90, 20], [60,10], [20,10]],
            facecolor='none',
            edgecolor='black',
            linewidth=2,
            linestyle='solid',
            alpha=0.9)
ax.add_patch(polygon)

# delta_x_wedge = np.tan(np.radians(15)) * 35
# delta_x = np.cos(np.radians(45)) * delta_x_wedge
# delta_y = np.sin(np.radians(45)) * delta_x_wedge

fov = Wedge((35,25), 40/np.cos(np.radians(45)), 15, 75, color="red", alpha=0.5)
# fov2 = Wedge((35,25), 60, 60, 120, color="r", alpha=0.5)

ax.add_artist(fov)
# ax.add_artist(fov2)

# add wind vector
#
#
Y, X = np.mgrid[5:100:10, 5:100:10]
U = 1
V = 1

ax.quiver(X, Y, U, V,
           angles='xy',
           color='blue',
           width=0.002,
           scale=1/0.015,
           headlength=5)


#plt.saveax('uav.png')
plt.show()
