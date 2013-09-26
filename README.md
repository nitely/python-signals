
python-signals
============

python-signals is a MIT Licensed lib, written in Python, for dispatching events/signals.

Requires Python 2.7.X


Usage, create signal:

    #my_signals.py
    from dispatch import Signal

    quit_app = Signal()  # arg1: str

Connect (a func, method, class, any callable):

    def my_func(arg1):
        print arg1
        sys.exit(0)

    my_signals.quit_app.connect(my_func)

Emit:

    my_signals.quit_app.emit("bye-bye")

Disconnect:

    my_signals.quit_app.disconnect(my_func)

