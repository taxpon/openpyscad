# -*- coding: utf-8 -*-

from modifier import ModifierMixin


class KindError(Exception):
    pass


class MetaObject(type):

    object_definition = {
        "union": ("union", (), True),
        "difference": ("difference", (), True),
        "rotate": ("rotate", ("a", "v"), True),
        "translate": ("translate", ("v", ), True),
        "cube": ("cube", ("size", "center"), False)
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
        return " ".join(map(lambda x: "{}={},".format(x, getattr(self, x)), valid_keys))[:-1]

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

    def dumps(self, indent_level=0):
        return "{indent}{prefix}{op_name}({params}){content};\n".format(
            indent="    " * indent_level,
            prefix=self.mod.get_prefix(),
            op_name=self._name,
            params=self._get_params(),
            content=self._get_content(indent_level)
        )

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
            new_union = Union()
            new_union.append(self).append(other)
            return new_union

    def __sub__(self, other):
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Difference):
            self.append(other)
            return self
        else:
            new_diff = Difference()
            new_diff.append(self).append(other)
            return new_diff


class _Empty(_BaseObject):
    pass


class Union(_BaseObject):
    pass


class Difference(_BaseObject):
    pass


# Affine transform
class Translate(_BaseObject):
    pass


class Rotate(_BaseObject):
    pass


# Shape Objects
class _ShapeObject(_BaseObject):

    def translate(self, *args, **kwargs):
        _t = Translate(*args, **kwargs)
        _t.append(self)
        return _t

    def rotate(self, *args, **kwargs):
        _r = Rotate(*args, **kwargs)
        _r.append(self)
        return _r


class Cube(_ShapeObject):
    size = None
    center = None

if __name__ == "__main__":
    c1 = Cube([20, 20, 20])
    c2 = c1.clone()

    base = Cube([20, 20, 20])
    sum = reduce(lambda t, x: t + base.rotate([0, 0, x * 36]), range(10), _Empty())
    # sum = None
    # for i in range(10):
    #     _rot = base.rotate([0, 0, i * 36])
    #
    #     if sum is None:
    #         sum = _rot
    #     else:
    #         sum += _rot

    print sum
    #
    # print c1.rotate([10, 10, 10])