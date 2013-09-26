# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import weakref

__all__ = ['weak_ref', ]


class BoundMethodWeakref:
    def __init__(self, func):
        self.func_name = func.__name__
        self.wref = weakref.ref(func.__self__)  # __self__ returns the class

    def __call__(self):
        func_cls = self.wref()
        if func_cls is None:  # lost reference
            return None
        else:
            func = getattr(func_cls, self.func_name)
            return func


def weak_ref(callback):
    if getattr(callback, '__self__', None) is not None:  # is a bound method?
        return BoundMethodWeakref(callback)
    else:
        return weakref.ref(callback)