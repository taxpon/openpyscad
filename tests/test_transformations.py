# -*- coding: utf-8 -*-
import unittest
from openpyscad import *


class TestOffset(unittest.TestCase):

    def test_validate_append(self):
        c1 = Circle(10)
        offset = Offset([10, 10, 10])
        offset.append(c1)

        c2 = Cube(10)
        with self.assertRaises(TypeError):
            offset.append(c2)

class TestLinearExtrude(unittest.TestCase):

    def test_validate_append_linear_extrude(self):
        c1 = Circle(10)
        c2 = c1.linear_extrude(height=1.4)
        
        c3 = Cube(10)
        with self.assertRaises(TypeError):
            c3.linear_extrude(height=1.2)

class TestRotateExtrude(unittest.TestCase):

    def test_validate_append_rotate_extrude(self):
        c1 = Circle(10)
        c2 = c1.rotate_extrude(angle=90)
        
        c3 = Cube(10)
        with self.assertRaises(TypeError):
            c3.rotate_extrude(angle=90)

