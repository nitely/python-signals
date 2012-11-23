# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import threading
#import logging
#logger = logging.getLogger(__name__)

import idle_queue
from weak_ref import weak_ref


class Signal:
    def __init__(self, name):
        self.name = name
        self.callbacks = []
        self.lock = threading.Lock()

    def connect(self, callback):
        with self.lock:
            callback = weak_ref(callback)
            self.callbacks.append(callback)

    def disconnect(self, callback):
        with self.lock:
            for index, weakref_callback in enumerate(self.callbacks):
                if callback == weakref_callback():
                    del self.callbacks[index]
                    break

    def emit(self, *args, **kwargs):
        with self.lock:
            #connected_methods = [callback.__name__ for callback in self.callbacks]
            #logger.debug("Event emitted: {}".format(self.name))
            for weakref_callback in self.callbacks[:]:
                callback = weakref_callback()
                if callback is not None:
                    idle_queue.idle_add(callback, *args, **kwargs)
                else: #lost reference
                    self.callbacks.remove(weakref_callback)
            #if not self.callbacks:
                #logger.debug("No signals assosiated to: {}".format(self.name))