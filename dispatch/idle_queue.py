# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import Queue

idle_loop = Queue.Queue()


def idle_add(func, *args, **kwargs):
    def idle():
        func(*args, **kwargs)
        return False
    idle_loop.put(idle)
