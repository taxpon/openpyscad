from __future__ import absolute_import

from .base import _BaseObject

__all__ = ['Circle', 'Square', 'Polygon', 'Text']


class _Shape2dObject(_BaseObject):
    pass


Shape2dObject = _Shape2dObject


class Circle(_Shape2dObject):
    pass


class Square(_Shape2dObject):
    pass


class Polygon(_Shape2dObject):
    pass


class Text(_Shape2dObject):
    pass
