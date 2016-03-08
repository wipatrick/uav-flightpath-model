import matplotlib.path as mpath
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import numpy as np
import sys

# add geofence
def addGeofence(x):
    polygon = plt.Polygon(x, facecolor='lightgreen', edgecolor='green', linewidth=1.5, linestyle='solid', alpha=0.3)
    ax.add_patch(polygon)

# add wind vectors
def addWindVectors(wdeg, wspeed):
    U = deg2uspeed(wdeg, wspeed)
    V = deg2vspeed(wdeg, wspeed)
    Y,X = np.mgrid[5:100:10, 5:100:10]

    ax.quiver(X, Y, U, V, angles='uv', color='blue', width=0.002, headlength=5)

# add gas leakage
def addGasLeakage(x, y, wdeg):
    radius = 50/np.cos(np.deg2rad(45))
    deltax = np.cos(np.deg2rad(wdeg))
    deltay = np.sin(np.deg2rad(wdeg))
    # add source
    plt.plot([x], [y], 'ro', markersize=10)
    plt.plot([x, x + radius * deltax], [y, y + radius * deltay], color='red', linewidth=2)
    # add radius
    circle = plt.Circle((x,y),5, color='red', alpha=0.4)
    # add wedge
    wedge = Wedge((x,y), radius, wdeg - 35, wdeg + 35, color="red", alpha=0.3)
    ax.add_artist(circle)
    ax.add_artist(wedge)

# helpers

# x-component of wind
# positive: west to east
# negative: east to west
def deg2uspeed(wdeg, wspeed):
    rad = np.deg2rad(wdeg)
    return wspeed * np.cos(rad)

# y-component of wind (south to north)
# positive: south to north
# negative: north to south
def deg2vspeed(wdeg, wspeed):
    rad = np.deg2rad(wdeg)
    return wspeed * np.sin(rad)

def usage():
    return "Usage: main.py <wdeg> <wspeed> <x-pos> <y-pos>\
    \nValid wdeg: wind direction according to u and v components in degrees (0deg - 360deg)\
    \nValid wspeed: wind speed (use: 1)\
    \nValid x-pos: x-value of gas leakage (0 - 100)\
    \nValid y-pos: y-value of gas leakage (0 - 100)"

if __name__ == "__main__":
    len_sys_argv = len(sys.argv[1:])

    if len_sys_argv < 4:
        print usage()

    elif len_sys_argv >= 4:
        commandlineargs = sys.argv[1:]
        wdeg = int(commandlineargs[0])
        wspeed = int(commandlineargs[1])
        x = int(commandlineargs[2])
        y = int(commandlineargs[3])

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


        addWindVectors(wdeg, wspeed)
        addGasLeakage(x, y, wdeg)

        polygon = [[20, 10], [10, 50], [20, 80], [50, 100], [90, 90], [90, 20], [60,10], [20,10]]
        addGeofence(polygon)

        #plt.saveax('uav.png')
        plt.show()
