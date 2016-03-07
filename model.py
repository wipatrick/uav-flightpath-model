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


# delta_x_wedge = np.tan(np.radians(15)) * 35
# delta_x = np.cos(np.radians(45)) * delta_x_wedge
# delta_y = np.sin(np.radians(45)) * delta_x_wedge

# add geofence
def set_geofence(x):
    polygon = plt.Polygon(
                x,
                facecolor='none',
                edgecolor='black',
                linewidth=2,
                linestyle='solid',
                alpha=0.9)
    ax.add_patch(polygon)

# add wind vectors
def set_wind_vectors(uwind,vwind):
    U = uwind
    V = vwind
    Y,X = np.mgrid[5:100:10, 5:100:10]

    ax.quiver(X,Y,U,V,
            angles='uv',
            color='blue',
            width=0.002,
            headlength=5)

def set_gas_source(x,y,theta):
    radius = 40/np.cos(np.deg2rad(45))
    # add source
    plt.plot([x], [y], 'ro', markersize=10)
    plt.plot([x, x + radius * np.cos(np.deg2rad(theta))], [y, y + radius * np.sin(np.deg2rad(theta))], color='red', linewidth=2)
    # add radius
    circle = plt.Circle((x,y),5, color='red', alpha=0.4)
    # add wedge
    wedge = Wedge((x,y), radius, theta - 30, theta + 30, color="red", alpha=0.4)
    ax.add_artist(circle)
    ax.add_artist(wedge)


theta = 75
windspeed = 1

u = windspeed * np.cos(np.deg2rad(theta))
v = windspeed * np.sin(np.deg2rad(theta))

set_wind_vectors(u,v)
set_gas_source(35,25,theta)

geofence = [[20, 10], [10, 50], [20, 80], [50, 100], [90, 90], [90, 20], [60,10], [20,10]]
set_geofence(geofence)


#plt.saveax('uav.png')
plt.show()
