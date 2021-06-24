import unittest
from openpyscad import *


class TestCube(unittest.TestCase):

    def test_cube(self):
        c = Cube(10)
        self.assertEqual(c.dumps(), "cube(size=10);\n")

    def test_is_2d(self):
        c = Cube(10)

        self.assertFalse(c._is_2d())
