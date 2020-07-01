#!/usr/bin/python3

import requests

def get_planet_pos(name):
    url = ("https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1"
         + "&COMMAND='399'"
         + "&CENTER='500@0'"
         + "&MAKE_EPHEM='YES'"
         + "&TABLE_TYPE='VECTORS'"
         + "&START_TIME='2020-07-01'"
         + "&STOP_TIME='2020-07-31'"
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

    # print(url)
    text = requests.get(url).text
    # print(text)
    scsv = text[text.find('$$SOE\n') + 6: text.find('$$EOE')]
    # print(scsv)

    from io import StringIO
    import csv

    reader = list(csv.reader(StringIO(scsv), delimiter=','))
    x, y, z = tuple(([float(row[i]) for row in reader]) for i in range(2,5))
    return x, y, z

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def main():
    x, y, z = get_planet_pos("earth")
    print(x)
    print(y)
    print(z)

    # plot3

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(0, 0, 0, color='r')
    ax.text(0, 0, 0, "SUN", size=10, zorder=1, color='k')

    ax.plot3D(x, y, z, "red", label="earth")
    ax.plot3D(list(map(lambda x: x/2, x)), y, z, "blue", label="earth2")

    plt.legend()
    plt.show()

    # plot3(list(map(lambda x: x/2, x)), y, z, "blue")
    print("")

if __name__ == '__main__':
    main()
