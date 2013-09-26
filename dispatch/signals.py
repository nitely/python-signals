# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import threading

from weak_ref import weak_ref

__all__ = ['Signal', ]


class Signal:
    def __init__(self):
        self.callbacks = []
        self.r_lock = threading.RLock()

    def connect(self, callback):
        with self.r_lock:
            callback = weak_ref(callback)
            self.callbacks.append(callback)

    def disconnect(self, callback):
        with self.r_lock:
            for index, weakref_callback in enumerate(self.callbacks):
                if callback == weakref_callback():
                    del self.callbacks[index]
                    break

    def emit(self, *args, **kwargs):
        with self.r_lock:
            for weakref_callback in self.callbacks[:]:
                callback = weakref_callback()
                if callback is not None:
                    callback(*args, **kwargs)
                else:  # lost reference
                    self.callbacks.remove(weakref_callback)