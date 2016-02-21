import unittest
from openpyscad import *


class TestCube(unittest.TestCase):

    def test_cube(self):
        c = Cube(10)
        self.assertEqual(c.dumps(), "cube(size=10);\n")
