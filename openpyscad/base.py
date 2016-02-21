# -*- coding: utf-8 -*-

from modifiers import ModifierMixin

__all__ = ["Empty", "BaseObject", "set_value"]


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
        "mirror": ("mirror", ("__axis", ), True),
        "color": ("color", ("__color", "a"), True),
        "offset": ("offset", ("r", "chamfer"), True),
        "minkowski": ("minkowski", (), True),
        "hull": ("hull", (), True),
        # 2D
        "circle": ("circle", ("r", "d"), False),
        "square": ("square", ("size", "center"), False),
        "polygon": ("polygon", ("points", "paths", "convexity"), False),
        "text": ("text",
                 ("text", "size", "font", "halign", "valign", "spacing",
                  "direction", "language", "script", "_fn"),
                 False),
        # 3D
        "sphere": ("sphere", ("r", "d", "_fa", "_fs", "_fn"), False),
        "cube": ("cube", ("size", "center"), False),
        "cylinder": ("cylinder",
                     ("h", "r", "r1", "r2", "d", "d1", "d2",
                      "center", "_fa", "_fs", "_fn"),
                     False
                     ),
        "polyhedron": ("polyhedron",
                       ("points", "triangles", "faces", "convexity"),
                       False)
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

    def _retrieve_value(self, name):
        val = getattr(self, name)
        if val is None:
            return None
        if isinstance(val, (str, unicode)):
            return "\"{}\"".format(val)
        return "{}".format(val)

    def _get_params(self):
        valid_keys = filter(lambda x: getattr(self, x) is not None, self._properties)

        def is_no_keyword_args(arg_name):
            if arg_name[0] == "_" and arg_name[1] == "_":
                return True
            return False

        def is_keyword_args(arg_name):
            return not is_no_keyword_args(arg_name)

        def convert_special_args(arg_name):
            if arg_name[0] == "_":
                if arg_name[1] != "_":
                    return "$" + arg_name[1:]
            return arg_name

        args = ""
        # no-keyword args
        no_kw_args = filter(lambda x: is_no_keyword_args(x), valid_keys)
        args += " ".join(map(lambda x: "{},".format(self._retrieve_value(x)), no_kw_args))[:-1]

        # keyword args
        kw_args = filter(lambda x: is_keyword_args(x), valid_keys)
        args += " ".join(map(lambda x: "{}={},".format(convert_special_args(x), getattr(self, x)), kw_args))[:-1]
        return args

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
            if isinstance(obj, (list, tuple, set)):
                for o in obj:
                    self.append(o)
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

    def write(self, filename, with_print=False):
        with open(filename, "w") as fp:
            self.dump(fp)
        if with_print:
            print(self.dumps())

    def clone(self):
        import copy
        return copy.copy(self)

    def __str__(self):
        return self.dumps()

    def __add__(self, other):
        from boolean import Union
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Union):
            self.append(other)
            return self
        else:
            return Union().append(self).append(other)

    def __sub__(self, other):
        from boolean import Difference
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Difference):
            self.append(other)
            return self
        else:
            return Difference().append(self).append(other)

    def __and__(self, other):
        from boolean import Intersection
        if isinstance(self, _Empty):
            return other

        elif isinstance(self, Intersection):
            self.append(other)
            return self
        else:
            return Intersection().append(self).append(other)

    def translate(self, *args, **kwargs):
        from transformations import Translate
        return Translate(*args, **kwargs).append(self)

    def rotate(self, *args, **kwargs):
        from transformations import Rotate
        return Rotate(*args, **kwargs).append(self)

    def scale(self, *args, **kwargs):
        from transformations import Scale
        return Scale(*args, **kwargs).append(self)

    def resize(self, *args, **kwargs):
        from transformations import Resize
        return Resize(*args, **kwargs).append(self)

    def color(self, *args, **kwargs):
        from transformations import Color
        return Color(*args, **kwargs).append(self)

BaseObject = _BaseObject


class _Empty(_BaseObject):
    pass

Empty = _Empty


def set_value(name, value):

    if isinstance(value, (str, unicode)):
        _value = "\"{}\"".format(value)
    else:
        _value = "{}".format(value)

    return "{name}={value};".format(name=name, value=_value)
