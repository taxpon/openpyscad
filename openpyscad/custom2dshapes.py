from math import cos, sin, pi

from openpyscad.shapes_2d import *


class Custom2dShapes(object):

    @staticmethod
    def regular_polygon(num, r):
        points = list()
        for i in range(num):
            a_deg = i * 360 / num
            a_rad = a_deg * 2 * pi / 360
            points += [[r * cos(a_rad), r * sin(a_rad)]]
        regular_poly = Polygon(points)
        return(regular_poly)

    def star(num, radii):
        points = list()
        for i in range(num):
            a_deg = i * 360 / num
            a_rad = a_deg * 2 * pi / 360
            r = radii[i % len(radii)]
            points += [[r * cos(a_rad), r * sin(a_rad)]]
            star_object = Polygon(points)
        return(star_object)
