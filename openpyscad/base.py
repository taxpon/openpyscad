# -*- coding: utf-8 -*-

from modifier import ModifierMixin

__all__ = ["_Empty", "Union", "Difference", "Intersection",
           "Translate", "Rotate", "Scale", "Resize",
           "Sphere", "Cube", "Cylinder", "Polyhedron"]


class MetaObject(type):

    object_definition = {
        # Bool
        "union": ("union", (), True),
        "difference": ("difference", (), True),
        "intersection": ("intersection", (), True),
        # Transforms
        "translate": ("translate", ("v", ), True),
        "rotate": ("rotate", ("a", "v"), True),
        "scale": ("scale", ("v", ), True),
        "resize": ("resize", ("newsize", "auto"), True),
        # 3D
        "sphere": ("sphere", ("r", "d", "_fa", "_fs", "_fn"), False),
        "cube": ("cube", ("size", "center"), False),
        "cylinder": ("cylinder",
                     ("h", "r", "r1", "r2", "d", "d1", "d2", "center", "_fa", "_fs", "_fn"),
                     False
                     ),
        "polyhedron": ("polyhedron", ("points", "triangles", "faces", "convexity"), False)
    }

    def __new__(mcs, name, bases, attr):

        if name[0] != "_":
            definition = MetaObject.object_definition[name.lower()]
            attr['_name'] = definition[0]
            attr['_properties'] = definition[1]
            for param in definition[1]:
                attr[param] = None
            attr["has_child"] = definition[2]
        return type.__new__(mcs, name, bases, attr)


class _BaseObject(ModifierMixin, object):

    __metaclass__ = MetaObject

    def __init__(self, *args, **kwargs):
        super(_BaseObject, self).__init__()
        for k, v in kwargs.items():
            if hasattr(self.__class__, k):
                setattr(self, k, v)

        if len(args) > 0:
            for i, k in enumerate(args):
                setattr(self, self._properties[i], args[i])

        self.children = []

    def _get_params(self):
        valid_keys = filter(lambda x: getattr(self, x) is not None, self._properties)

        def convert_special_args(arg_name):
            if arg_name[0] == "_":
                return "$" + arg_name[1:]
            return arg_name

        return " ".join(map(lambda x: "{}={},".format(convert_special_args(x), getattr(self, x)), valid_keys))[:-1]

    def _get_children_content(self, indent_level=0):
        _content = ""
        if len(self.children) > 0:
            for child in self.children:
                _content += child.dumps(indent_level)

        return _content

    def _get_content(self, indent_level=0):
        if len(self.children) == 0:
            return ""
        else:
            return "{{\n{children}{indent}}}".format(
                children=self._get_children_content(indent_level+1),
                indent="    " * indent_level
            )

    def append(self, obj):
        if not self.has_child:
            raise TypeError("This object can not have any children.")
        else:
            self.children.append(obj)
            return self

    def dump(self, fp):
        fp.write(self.dumps())

    def dumps(self, indent_level=0):
        return "{indent}{prefix}{op_name}({params}){content};\n".format(
            indent="    " * indent_level,
            prefix=self.mod.get_prefix(),
            op_name=self._name,
            params=self._get_params(),
            content=self._get_content(indent_level)
        )

    def write(self, filename):
        with open(filename, "w") as fp:
            self.dump(fp)

    def clone(self):
        import copy
        return copy.copy(self)

    def __str__(self):
        return self.dumps()

    def __add__(self, other):
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Union):
            self.append(other)
            return self
        else:
            return Union().append(self).append(other)

    def __sub__(self, other):
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Difference):
            self.append(other)
            return self
        else:
            return Difference().append(self).append(other)

    def __and__(self, other):
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Intersection):
            self.append(other)
            return self
        else:
            return Intersection().append(self).append(other)

    def translate(self, *args, **kwargs):
        return Translate(*args, **kwargs).append(self)

    def rotate(self, *args, **kwargs):
        return Rotate(*args, **kwargs).append(self)

    def scale(self, *args, **kwargs):
        return Scale(*args, **kwargs).append(self)

    def resize(self, *args, **kwargs):
        return Resize(*args, **kwargs).append(self)


class _Empty(_BaseObject):
    pass


# Boolean
class Union(_BaseObject):
    pass


class Difference(_BaseObject):
    pass


class Intersection(_BaseObject):
    pass


# Transformations
class Translate(_BaseObject):
    pass


class Rotate(_BaseObject):
    pass


class Scale(_BaseObject):
    pass


class Resize(_BaseObject):
    pass


# 3D
class _ShapeObject(_BaseObject):
    pass


class Sphere(_ShapeObject):
    pass


class Cube(_ShapeObject):
    pass


class Cylinder(_ShapeObject):
    pass


class Polyhedron(_ShapeObject):
    pass

if __name__ == "__main__":

    i = Intersection()
    i.append(Cube([20, 20, 15]))
    i.append(Sphere(10, _fn=40))

    i2 = Cube([20, 20, 15]) & Sphere(10, _fn=40)
    # base = Cube([20, 20, 15]) + Sphere(10, _fn=40)
    # print base
    # base.write('test.scad')
    print i2
    i2.write("test.scad")
