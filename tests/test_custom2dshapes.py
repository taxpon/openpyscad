import unittest
from openpyscad.custom2dshapes import Custom2dShapes as c2d


class TestCustom2dShapes(unittest.TestCase):

    def test_regular_polygon(self):
        triangle = c2d.regular_polygon(3, 10)
        self.assertTrue(c.dumps().startswith("polygon(points=[[10.0, 0.0], [-4.99"))

    def test_star(self):
        c = c2d.star(20, [6, 10])
        self.assertTrue(c.dumps().startswith("polygon(points=[[6.0, 0.0], [9.5"))

