
python-signals
============

python-signals is a LGPL Licensed, written in Python, for dispatching events/signals.

Requires Python 2.7.X


Usage, create signal:

    #my_signals.py
    from dispatch import Signal

    quit_app = Signal(name='quit app') #arg1: str

Connect (a func, method, class, any callable):

    def my_func(arg1):
        print arg1
        sys.exit(0)

    my_signals.quit_app.connect(my_func)

Emit:

    my_signals.quit_app.emit("bye-bye")

Disconnect:

    my_signals.quit_app.disconnect(my_func)

Dispatch events:

    from dispatch.idle_queue import idle_loop

    #this should go in your main thread loop if your are using a gui.
    callback = idle_loop.get() #blocks
    callback() #dispatch the event


____________________________________________________________________________


Copyright (C) 2012 Esteban Borsani ochdownloader@gmail.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.