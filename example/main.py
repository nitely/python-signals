# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

import sys

import signals


def quiter(my_arg):
    print my_arg
    sys.exit(0)


if __name__ == "__main__":
    signals.quit_app.connect(quiter)  # connect the callback/slot
    my_arg = "goodbye"
    signals.quit_app.emit(my_arg)  # emit the signal

    signals.quit_app.disconnect(quiter)  # disconnect
    signals.quit_app.emit(my_arg)