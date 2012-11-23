# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import sys

import signals
from dispatch.idle_queue import idle_loop


def quit(my_arg):
    print my_arg
    sys.exit(0)


if __name__ == "__main__":
    signals.quit_app.connect(quit) #connect the callback/slot
    #signals.quit_app.disconnect(quit) #disconnect
    my_arg = "goodbye"
    signals.quit_app.emit(my_arg) #emit the signal

    #this should go in your main thread loop if your are using a gui.
    #example: http://code.activestate.com/recipes/578299-pyqt-pyside-thread-safe-global-queue-main-loop-int/
    callback = idle_loop.get() #blocks
    callback() #dispatch the event