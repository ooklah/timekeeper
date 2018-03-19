"""
Time Control Loop
"""

import time
from threading import Thread, Event


class Signal(object):

    def __init__(self):
        self._handles = []
        self._block = False

    def connect(self, func):
        self._handles.append(func)

    def emit(self):
        if self._block:
            return

        for handle in self._handles:
            handle()

    def block(self):
        """Blocks the signals from firing."""
        self._block = True

    def unblock(self):
        """
        Unblocks the signals so they will fire next time they are
        called.
        """
        self._block = False


class TKClock(Thread):

    tick = Signal()

    def __init__(self, delay=1):
        super(TKClock, self).__init__()
        self.daemon = True
        self._delay = delay

        self.stop_flag = False
        self.exit_flag = Event()

    def run(self):
        while not self.is_stopped():
            self.tick.emit()
            time.sleep(self._delay)

    def stop(self):
        """Stop the timer."""
        self.stop_flag = True
        self.exit_flag.set()

    def is_stopped(self):
        return self.stop_flag
        