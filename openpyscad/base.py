# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Python 2 and 3:
from six import with_metaclass
import os


from .modifiers import ModifierMixin

__all__ = ['Empty', 'BaseObject', 'Scad', 'Import']
INDENT = '    '


class MetaObject(type):

    object_definition = {
        # Bool
        'union': ('union', (), True),
        'difference': ('difference', (), True),
        'intersection': ('intersection', (), True),
        # Transforms
        'translate': ('translate', ('v', ), True),
        'rotate': ('rotate', ('a', 'v'), True),
        'scale': ('scale', ('v', ), True),
        'resize': ('resize', ('newsize', 'auto'), True),
        'mirror': ('mirror', ('__axis', ), True),
        'color': ('color', ('__color', 'a'), True),
        'offset': ('offset', ('r', 'chamfer'), True),
        'minkowski': ('minkowski', (), True),
        'hull': ('hull', (), True),
        'linear_extrude': ('linear_extrude', ('height', 'center',
                           'convexity', 'twist', 'slices', 'scale'),
                           True),
        'rotate_extrude': ('rotate_extrude', ('angle', 'convexity',
                           '_fn'), True),
        # 2D
        'circle': ('circle', ('r', 'd', '_fn'), False),
        'square': ('square', ('size', 'center'), False),
        'polygon': ('polygon', ('points', 'paths', 'convexity'), False),
        'text': ('text',
                 ('text', 'size', 'font', 'halign', 'valign', 'spacing',
                  'direction', 'language', 'script', '_fn'),
                 False),
        # 3D
        'sphere': ('sphere', ('r', 'd', 'center', '_fa', '_fs', '_fn'), False),
        'cube': ('cube', ('size', 'center'), False),
        'cylinder': ('cylinder',
                     ('h', 'r', 'r1', 'r2', 'd', 'd1', 'd2',
                      'center', '_fa', '_fs', '_fn'),
                     False
                     ),
        'scad': ('scad', ('scadfile', 'version'), False),
        'import': ('import', ('file', 'convexity'), False),
        'surface': ('surface', ('file', 'center', 'invert', 'convexity'), False),
        'polyhedron': ('polyhedron',
                       ('points', 'triangles', 'faces', 'convexity'),
                       False)
    }

    def __new__(mcs, name, bases, attr):
        if name[0] != '_':
            definition = MetaObject.object_definition[name.lower()]
            attr['_name'] = definition[0]
            attr['_properties'] = definition[1]
            for param in definition[1]:
                attr[param] = None
            attr['has_child'] = definition[2]
        return type.__new__(mcs, name, bases, attr)


class _BaseObject(with_metaclass(MetaObject, ModifierMixin, object)):

    def __init__(self, *args, **kwargs):
        super(_BaseObject, self).__init__()
        self.modules = list()
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
        try:
            if isinstance(val, (str, unicode)):
                return '"{}"'.format(val)
        except Exception as e:
            print(e)
            if isinstance(val, str):
                return '"{}"'.format(val)

        return '{}'.format(val)

    def _get_params(self, fp=None):
        valid_keys = list(filter(lambda x: getattr(self, x) is not None, self._properties))

        def is_no_keyword_args(arg_name):
            if arg_name[0] == '_' and arg_name[1] == '_':
                return True
            return False

        def is_keyword_args(arg_name):
            return not is_no_keyword_args(arg_name)

        def convert_special_args(arg_name):
            if arg_name[0] == '_':
                if arg_name[1] != '_':
                    return '$' + arg_name[1:]
            return arg_name

        def _get_attr(self, x, fp):
            if x == 'scadfile':
                scadfile = getattr(self, x)

                def rename_scadfile(scadfile):
                    sf = ''.join(os.path.basename(scadfile).split('.')[:-1])
                    scadfile_renamed = sf.lower().strip('_').strip('-')
                    return(scadfile_renamed)
                with open(scadfile) as f:
                    content = f.readlines()
                    content = ''.join(content).rstrip('\n')
                    sc = rename_scadfile(scadfile)
                    module = 'module {sc}() {{{content};}}\n'.format(**{'content': content, 'sc': sc})
                    module = module.replace(';;', ';')
                    self.modules.append(module)
                    if fp is not None:
                        fp.write(module)
                    content = '{}()'.format(sc)
                    return(content)
            elif x == 'file':
                content = getattr(self, x)
                if not content.startswith('"'):
                    content = '"' + content
                if not content.endswith('"'):
                    content = content + '"'
                return(content)
            else:
                return(getattr(self, x))

        args = ''
        # no-keyword args
        no_kw_args = list(filter(lambda x: is_no_keyword_args(x), valid_keys))
        args += ' '.join(map(lambda x: '{},'.format(self._retrieve_value(x)), no_kw_args))[:-1]

        # keyword args
        kw_args = filter(lambda x: is_keyword_args(x), valid_keys)
        args += ' '.join(map(lambda x: '{}={},'.format(convert_special_args(x), _get_attr(self, x, fp)), kw_args))[:-1]
        args = args.replace('scadfile=', '')
        return args

    def _get_children_content(self, indent_level=0, fp=None):
        _content = ''
        if len(self.children) > 0:
            for child in self.children:
                _content += child.dumps(indent_level, fp)

        return _content

    def _get_content(self, indent_level=0, fp=None):
        if len(self.children) == 0:
            return ''
        else:
            return '{{\n{children}{indent}}}'.format(
                children=self._get_children_content(indent_level + 1, fp=fp),
                indent=INDENT * indent_level
            )

    def _validate_append(self, obj):
        """Override if any validation in append operation is required.
        :param obj:
        """

    def append(self, obj):
        if not self.has_child:
            raise TypeError('This object can not have any children.')
        else:
            self._validate_append(obj)
            if isinstance(obj, (list, tuple, set)):
                for o in obj:
                    self.append(o)
            else:
                self.children.append(obj)
            return self

    def dump(self, fp):
        dumps = self.dumps(fp=fp)
        fp.write(dumps)

    def dumps(self, indent_level=0, fp=None):
        if self._name == 'scad':
            return '{indent}{prefix}{params};\n'.format(
                indent=INDENT * indent_level,
                prefix=self.mod.get_prefix(),
                params=self._get_params(fp).replace('True', 'true')
            )
        else:
            return '{indent}{prefix}{op_name}({params}){content};\n'.format(
                indent=INDENT * indent_level,
                prefix=self.mod.get_prefix(),
                op_name=self._name,
                params=self._get_params(fp).replace('True', 'true'),
                content=self._get_content(indent_level, fp=fp)
            )

    def write(self, filename, with_print=False):
        with open(filename, 'w') as fp:
            self.dump(fp)
        if with_print:
            print(self.dumps())

    def clone(self):
        import copy
        return copy.deepcopy(self)

    def equals(self, other):
        for prop in self._properties:
            if self.__class__.__name__ != other.__class__.__name__:
                return False

            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        return self.dumps()

    def __add__(self, other):
        from .boolean import Union
        if isinstance(self, _Empty):
            return other.clone()

        elif isinstance(self, Union):
            cloned = self.clone()
            cloned.append(other)
            return cloned
        else:
            return Union().append(self).append(other)

    def __sub__(self, other):
        from .boolean import Difference
        if isinstance(self, _Empty):
            return other.clone()

        elif isinstance(self, Difference):
            cloned = self.clone()
            cloned.append(other)
            return cloned
        else:
            return Difference().append(self).append(other)

    def __and__(self, other):
        from .boolean import Intersection
        if isinstance(self, _Empty):
            return other.clone()

        elif isinstance(self, Intersection):
            cloned = self.clone()
            cloned.append(other)
            return cloned
        else:
            return Intersection().append(self).append(other)

    def translate(self, *args, **kwargs):
        from .transformations import Translate
        return Translate(*args, **kwargs).append(self)

    def rotate(self, *args, **kwargs):
        from .transformations import Rotate
        return Rotate(*args, **kwargs).append(self)

    def scale(self, *args, **kwargs):
        from .transformations import Scale
        return Scale(*args, **kwargs).append(self)

    def resize(self, *args, **kwargs):
        from .transformations import Resize
        return Resize(*args, **kwargs).append(self)

    def mirror(self, *args, **kwargs):
        from .transformations import Mirror
        return Mirror(*args, **kwargs).append(self)

    def color(self, *args, **kwargs):
        from .transformations import Color
        return Color(*args, **kwargs).append(self)

    def offset(self, *args, **kwargs):
        from .transformations import Offset
        return Offset(*args, **kwargs).append(self)

    def minkowski(self, *args, **kwargs):
        from .transformations import Minkowski
        return Minkowski(*args, **kwargs).append(self)

    def hull(self, *args, **kwargs):
        from .transformations import Hull
        return Hull(*args, **kwargs).append(self)

    def linear_extrude(self, *args, **kwargs):
        from .transformations import Linear_Extrude
        return Linear_Extrude(*args, **kwargs).append(self)

    def rotate_extrude(self, *args, **kwargs):
        from .transformations import Rotate_Extrude
        return Rotate_Extrude(*args, **kwargs).append(self)


BaseObject = _BaseObject


class _Empty(_BaseObject):
    pass


Empty = _Empty


class Scad(_BaseObject):
    pass


class Import(_BaseObject):
    pass
