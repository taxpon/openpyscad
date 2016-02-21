# -*- coding: utf-8 -*-
import unittest
from openpyscad import *


class TestBaseObject(unittest.TestCase):

    def test_init(self):
        c = Cube(size=[10, 10, 10])
        self.assertEqual(c.dumps(), "cube(size=[10, 10, 10]);\n")

    def test_retrieve_value(self):
        o = BaseObject()
        setattr(o, "test", None)
        self.assertIsNone(o._retrieve_value("test"))

        setattr(o, "test", "value")
        self.assertEqual(o._retrieve_value("test"), "\"value\"")

        setattr(o, "test", 123)
        self.assertEqual(o._retrieve_value("test"), "123")

    def test_get_params(self):
        o = Cylinder(r=10, _fn=10)
        self.assertEqual(o._get_params(), "r=10, $fn=10")

        o = Color("Red")
        self.assertEqual(o._get_params(), "\"Red\"")

    def test_get_children_content(self):
        o = Union()
        self.assertEqual(o._get_children_content(), "")

        o = Union().append(Cube(10))
        self.assertEqual(o._get_children_content(), "cube(size=10);\n")
        self.assertEqual(o._get_children_content(1), "    cube(size=10);\n")

    def test_get_content(self):
        o = Union()
        self.assertEqual(o._get_content(), "")

        o = Union().append(Cube(10))
        self.assertEqual(o._get_content(), "{\n    cube(size=10);\n}")
        self.assertEqual(o._get_content(1), "{\n        cube(size=10);\n    }")

    def test_append(self):
        o = Cube(size=10)
        with self.assertRaises(TypeError):
            o.append(Cube(size=10))

        c1 = Cube(size=10)
        c2 = Cube(size=20)
        o = Union()
        o.append((c1, c2))
        self.assertEqual(o.children, [c1, c2])

        o = Union()
        o.append(c1)
        self.assertEqual(o.children, [c1])

    def test_dump(self):
        import StringIO
        sio = StringIO.StringIO()
        c1 = Cube(size=10)
        c1.dump(sio)
        self.assertEqual(sio.getvalue(), "cube(size=10);\n")

    def test_dumps(self):
        c1 = Cube(size=10)
        self.assertEqual(c1.dumps(), "cube(size=10);\n")

    def test_write(self):
        from mock import mock_open, patch
        c1 = Cube(size=10)
        m_open = mock_open()
        with patch("__builtin__.open", m_open):
            c1.write("sample", with_print=True)

        m_open.assert_called_once_with("sample", "w")
        handle = m_open()
        handle.write.assert_called_once_with("cube(size=10);\n")

    def test_clone(self):
        c1 = Cube(size=10)
        c2 = c1.clone()

        self.assertEqual(c1.size, c2.size)

    def test_str(self):
        c1 = Cube(size=10)
        self.assertEqual(str(c1), "cube(size=10);\n")

    def test_add(self):
        o = Empty()
        c1 = Cube(10)
        self.assertEqual(o + c1, c1)
        
        u = Union()
        u1 = u + c1
        self.assertEqual(u1.children, [c1])
        
        c2 = Cube(20)
        u2 = c1 + c2
        self.assertEqual(u2.children, [c1, c2])

    def test_sub(self):
        o = Empty()
        c1 = Cube(10)
        self.assertEqual(o - c1, c1)

        d = Difference()
        d1 = d - c1
        self.assertEqual(d1.children, [c1])

        c2 = Cube(20)
        d2 = c1 - c2
        self.assertEqual(d2.children, [c1, c2])

    def test_and(self):
        o = Empty()
        c1 = Cube(10)
        self.assertEqual(o & c1, c1)

        i = Intersection()
        i1 = i & c1
        self.assertEqual(i1.children, [c1])

        c2 = Cube(20)
        i2 = c1 & c2
        self.assertEqual(i2.children, [c1, c2])

    def test_translate(self):
        o = Cube(10)
        o1 = o.translate([10, 10, 10])
        self.assertTrue(isinstance(o1, Translate))
        self.assertEqual(o1.children, [o])
        self.assertEqual(o1.v, [10, 10, 10])
        
    def test_rotate(self):
        o = Cube(10)
        o1 = o.rotate([10, 10, 10])
        self.assertTrue(isinstance(o1, Rotate))
        self.assertEqual(o1.children, [o])
        self.assertEqual(o1.a, [10, 10, 10])
        
    def test_scale(self):
        o = Cube(10)
        o1 = o.scale([10, 10, 10])
        self.assertTrue(isinstance(o1, Scale))
        self.assertEqual(o1.children, [o])
        self.assertEqual(o1.v, [10, 10, 10])

    def test_resize(self):
        o = Cube(10)
        o1 = o.resize([10, 10, 10])
        self.assertTrue(isinstance(o1, Resize))
        self.assertEqual(o1.children, [o])

    def test_mirror(self):
        o = Cube(10)
        o1 = o.mirror([1, 1, 1])
        self.assertTrue(isinstance(o1, Mirror))
        self.assertEqual(o1.children, [o])
        
    def test_color(self):
        o = Cube(10)
        o1 = o.color("Red")
        self.assertTrue(isinstance(o1, Color))
        self.assertEqual(o1.children, [o])

    def test_offset(self):
        o = Circle(10)
        o1 = o.offset([10, 10, 10])
        self.assertTrue(isinstance(o1, Offset))
        self.assertEqual(o1.children, [o])

        o = Cube(10)
        with self.assertRaises(TypeError):
            o.offset([10, 10, 10])
