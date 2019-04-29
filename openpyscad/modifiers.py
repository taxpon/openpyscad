# -*- coding: utf-8 -*-


class Modifier(object):

    def __init__(self):
        self.is_disable = False
        self.is_show_only = False
        self.is_debug = False
        self.is_transparent = False

    def turn_on_disable(self):
        self.is_disable = True

    def turn_off_disable(self):
        self.is_disable = False

    def turn_on_show_only(self):
        self.is_show_only = True

    def turn_off_show_only(self):
        self.is_show_only = False

    def turn_on_debug(self):
        self.is_debug = True

    def turn_off_debug(self):
        self.is_debug = False

    def turn_on_transparent(self):
        self.is_transparent = True

    def turn_off_transparent(self):
        self.is_transparent = False

    def get_prefix(self):
        prefix = ''
        if self.is_disable:
            prefix += '*'
        if self.is_show_only:
            prefix += '!'
        if self.is_debug:
            prefix += '#'
        if self.is_transparent:
            prefix += '%'
        return prefix


class ModifierMixin(object):

    def __init__(self):
        super(ModifierMixin, self).__init__()
        self.mod = Modifier()

    def turn_on_disable(self):
        self.mod.is_disable = True
        return self

    def turn_off_disable(self):
        self.mod.is_disable = False
        return self

    def turn_on_show_only(self):
        self.mod.is_show_only = True
        return self

    def turn_off_show_only(self):
        self.mod.is_show_only = False
        return self

    def turn_on_debug(self):
        self.mod.is_debug = True
        return self

    def turn_off_debug(self):
        self.mod.is_debug = False
        return self

    def turn_on_transparent(self):
        self.mod.is_transparent = True
        return self

    def turn_off_transparent(self):
        self.mod.is_transparent = False
        return self

    # Shorthand
    def disable(self):
        return self.turn_on_disable()

    def show_only(self):
        return self.turn_on_show_only()

    def debug(self):
        return self.turn_on_debug()

    def transparent(self):
        return self.turn_on_transparent()
