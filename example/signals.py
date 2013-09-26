# -*- coding: utf-8 -*-
__author__ = 'Esteban Castro Borsani'

from dispatch import Signal


# This are globals, you get the same object on import, from anywhere.
# do_something = Event('do something') #args: my_arg1, my_arg_list2, my_arg_str3
quit_app = Signal() #args: some_arg