import unittest

from openpyscad.base import Rotate

class TestBaseObject(unittest.TestCase):

    def test_dump(self):
        pass

    def test_dumps(self):
        pass


class TestRotete(unittest.TestCase):

    def test_dump(self):
        rt = Rotate([0, 0, 0])
        self.assertEqual("", rt._dump())
