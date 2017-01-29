import unittest
from openpyscad.custom3dshapes import Custom3dShapes as c3d


class TestCustom3dShapes(unittest.TestCase):

    def test_dice(self):
        dice = c3d.dice(15)
        self.assertTrue(dice.dumps().startswith("mirror("))
