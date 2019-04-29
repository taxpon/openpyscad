from __future__ import absolute_import

from .base import _BaseObject

__all__ = ['Sphere', 'Cube', 'Cylinder', 'Polyhedron', 'Surface']


# 3D
class _Shape3dObject(_BaseObject):
    pass


class Sphere(_Shape3dObject):
    pass


class Cube(_Shape3dObject):
    pass


class Cylinder(_Shape3dObject):
    pass


class Polyhedron(_Shape3dObject):
    pass


class Surface(_Shape3dObject):
    pass
