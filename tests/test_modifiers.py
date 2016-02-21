# -*- coding: utf-8 -*-
import unittest
from openpyscad.modifiers import Modifier
from openpyscad.modifiers import ModifierMixin


class TestModifier(unittest.TestCase):
    
    def setUp(self):
        self.mod = Modifier()
        
    def test_turn_on_disable(self):
        self.mod.turn_on_disable()
        self.assertTrue(self.mod.is_disable)
        
    def test_turn_off_disable(self):
        self.mod.turn_off_disable()
        self.assertFalse(self.mod.is_disable)
    
    def test_turn_on_show_only(self):
        self.mod.turn_on_show_only()
        self.assertTrue(self.mod.is_show_only)
        
    def test_turn_off_show_only(self):
        self.mod.turn_off_show_only()
        self.assertFalse(self.mod.is_show_only)
    
    def test_turn_on_debug(self):
        self.mod.turn_on_debug()
        self.assertTrue(self.mod.is_debug)
        
    def test_turn_off_debug(self):
        self.mod.turn_off_debug()
        self.assertFalse(self.mod.is_debug)
    
    def test_turn_on_transparent(self):
        self.mod.turn_on_transparent()
        self.assertTrue(self.mod.is_transparent)
        
    def test_turn_off_transparent(self):
        self.mod.turn_off_transparent()
        self.assertFalse(self.mod.is_transparent)

    def test_get_prefix(self):
        mod = Modifier()
        self.assertEqual(mod.get_prefix(), "")

        mod.turn_on_disable()
        self.assertEqual(mod.get_prefix(), "*")

        mod.turn_on_show_only()
        self.assertEqual(mod.get_prefix(), "*!")

        mod.turn_on_debug()
        self.assertEqual(mod.get_prefix(), "*!#")

        mod.turn_on_transparent()
        self.assertEqual(mod.get_prefix(), "*!#%")


class TestModifierMixin(unittest.TestCase):

    def setUp(self):
        self.mm = ModifierMixin()

    def test_init(self):
        self.assertIsNotNone(self.mm.mod)

    def test_turn_on_disable(self):
        self.mm.turn_on_disable()
        self.assertTrue(self.mm.mod.is_disable)

    def test_disable(self):
        self.mm.disable()
        self.assertTrue(self.mm.mod.is_disable)

    def test_turn_off_disable(self):
        self.mm.turn_off_disable()
        self.assertFalse(self.mm.mod.is_disable)

    def test_turn_on_show_only(self):
        self.mm.turn_on_show_only()
        self.assertTrue(self.mm.mod.is_show_only)

    def test_show_only(self):
        self.mm.show_only()
        self.assertTrue(self.mm.mod.is_show_only)

    def test_turn_off_show_only(self):
        self.mm.turn_off_show_only()
        self.assertFalse(self.mm.mod.is_show_only)

    def test_turn_on_debug(self):
        self.mm.turn_on_debug()
        self.assertTrue(self.mm.mod.is_debug)

    def test_turn_off_debug(self):
        self.mm.turn_off_debug()
        self.assertFalse(self.mm.mod.is_debug)

    def test_debug(self):
        self.mm.debug()
        self.assertTrue(self.mm.mod.is_debug)

    def test_turn_on_transparent(self):
        self.mm.turn_on_transparent()
        self.assertTrue(self.mm.mod.is_transparent)

    def test_turn_off_transparent(self):
        self.mm.turn_off_transparent()
        self.assertFalse(self.mm.mod.is_transparent)

    def test_transparent(self):
        self.mm.transparent()
        self.assertTrue(self.mm.mod.is_transparent)
