# -*- coding: utf-8 -*-
import base

__all__ = ["Translate", "Rotate", "Scale", "Resize", "Mirror", "Color", "Offset", "Hull", "Minkowski"]


# Transformations
class Translate(base.BaseObject):
    pass


class Rotate(base.BaseObject):
    pass


class Scale(base.BaseObject):
    pass


class Resize(base.BaseObject):
    pass


class Mirror(base.BaseObject):
    pass


class Color(base.BaseObject):
    pass


class Offset(base.BaseObject):

    def _validate_append(self, obj):
        from shapes_2d import Shape2dObject
        if not isinstance(obj, Shape2dObject):
            raise TypeError("Appended object must be a instance of Shape2dObject.")


class Hull(base.BaseObject):
    pass


class Minkowski(base.BaseObject):
    pass
