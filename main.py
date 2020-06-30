#!/usr/bin/python3

import requests, json
from math import sqrt

#
#   perhelion sun                 aphelion
#     |<--Rp-->|<--------Ra--------->|
#     |     ___|_-----------_____    |
#     | -^^    |                 ^^- |
#     |/       |                    \|
#     |        |              ,      |
#     X--------S------O------S-------X
#     |        |      |      |       |
#     |<--q--->|<-ea->|<-ea->|       |
#     |               |              |
#     |<------a------>|<------a------>|              |
#
#   e : eccentricity
#   a : semimajorAxis
#
# https://stjarnhimlen.se/comp/tutorial.html
#

class Planet:
    def __init__(self, raw_json):

        self.raw = raw_json
        self.name = raw_json["name"]

        self.semimajorAxis = raw_json["semimajorAxis"]

        self.perihelion = raw_json["perihelion"]
        self.aphelion = raw_json["aphelion"]

        self.eccentricity = raw_json["eccentricity"]
        self.inclination = raw_json["inclination"]
        self.meanRadius = raw_json["meanRadius"]

        # mass [kg]
        self.mass = (raw_json["mass"]["massValue"] *
                    10 ** raw_json["mass"]["massExponent"])
        print("mass", self.mass)

        m = self.mass / 5.02785431e-31 #Solar mass
        a = self.semimajorAxis #km
        e = self.eccentricity # coef
        T = 000
        q = a * (1 - e) # Rp [km]
        Q = a * (1 + e) # Ra [km]
        i = self.inclination # degrees
        P = 365.256898326 * a**1.5/sqrt(1+m) #day
        n = 360 / P # deg/day
        t = 000
        M = n * (t - T) # Mean anomaly
        w = 000
        N = 000
        L = M + w + N # Mean Longitude
        # M = E - e * sin(E) kepler eq
        v = 000 # True anomaly


    def __str__(self):
        return str(self.raw)


def get_planet(name):
    url = "https://api.le-systeme-solaire.net/rest/bodies/{{{}}}".format(name)
    response = requests.get(url)
    data = response.json()
    print(data)
    return Planet(data)



def main():
    print("Hello word");
    planet = get_planet("earth");
    print(planet)


if __name__ == '__main__':
    main()
