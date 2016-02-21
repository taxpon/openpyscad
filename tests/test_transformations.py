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
