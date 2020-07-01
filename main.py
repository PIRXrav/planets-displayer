#!/usr/bin/python3


# https://ssd.jpl.nasa.gov/horizons.cgi?s_time=1#top

import requests
from io import StringIO
import csv

planet_id = {"mercury": 199,
             "venus": 299,
             "earth": 399,
             "mars": 499,
             "jupiter": 599,
             "saturn": 699,
             "uranus": 799,
             "nepture": 899}

planet_cl = {"mercury": "black",
             "venus": "yellow",
             "earth": "blue",
             "mars": "orange",
             "jupiter": "red",
             "saturn": "gold",
             "uranus": "gray",
             "nepture": "lightblue"}


def get_planet_pos(name):
    url = ("https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1"
           + "&COMMAND='{}'".format(planet_id[name])
           + "&CENTER='500@0'"
           + "&MAKE_EPHEM='YES'"
           + "&TABLE_TYPE='VECTORS'"
           + "&START_TIME='2010-07-01'"
           + "&STOP_TIME='2020-07-01'"
           + "&STEP_SIZE='1 d'"
           + "&OUT_UNITS='AU-D'"
           + "&REF_PLANE='ECLIPTIC'"
           + "&REF_SYSTEM='J2000'"
           + "&VECT_CORR='NONE'"
           + "&VEC_LABELS='NO'"
           + "&VEC_DELTA_T='NO'"
           + "&CSV_FORMAT='YES'"
           + "&OBJ_DATA='NO'"
           + "&VEC_TABLE='1'")

    print(url)
    text = requests.get(url).text
    # print(text)
    scsv = text[text.find('$$SOE\n') + 6: text.find('$$EOE')]
    # print(scsv)

    reader = list(csv.reader(StringIO(scsv), delimiter=','))
    x, y, z = tuple(([float(row[i]) for row in reader]) for i in range(2, 5))
    print("done")
    return x, y, z


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from math import log

import numpy as np
from ai import cs


def logmod(x, y, z):
    # cartesian to spherical
    r, theta, phi = cs.cart2sp(x=x, y=y, z=z)
    # r = log(r)
    # spherical to cartesian
    x, y, z = cs.sp2cart(r=z, theta=theta, phi=phi)
    return x, y, z


def main():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(0, 0, 0, color='r')
    ax.text(0, 0, 0, "SUN", size=10, zorder=1, color='k')

    for planet in planet_id.keys():
        ax.plot3D(*get_planet_pos(planet), planet_cl[planet], label=planet)

    plt.legend()
    plt.show()

    # plot3(list(map(lambda x: x/2, x)), y, z, "blue")
    print("")


if __name__ == '__main__':
    main()
