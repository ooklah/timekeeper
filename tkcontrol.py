"""
Time Keeper Controller
"""

import os
import sys
import time
from threading import Thread, Event

f_path = os.path.dirname(__file__)
runfile = os.path.join(f_path, 'runfile')


THREADS = []
DELAY = 10


class Timer(Thread):

    def __init__(self, begin):
        super(Timer, self).__init__()
        self.st = begin
        self.ed = 0
        self.daemon = True
        self.stop_flag = False
        self.exit_flag = Event()

    def run(self):
        while not self.is_done():
            self.exit_flag.wait(timeout=DELAY)
        self.calc_time()

    def stop(self):
        print "stopping"
        self.stop_flag = True
        self.exit_flag.set()

    def is_done(self):
        return self.stop_flag

    def calc_time(self):
        self.ed = time.time()
        delta = self.ed - self.st
        min, sec = divmod(delta, 60)
        hours, min = divmod(min, 60)
        days, hours = divmod(hours, 24)
        print "Elapsed Time: {:.0f}:{:.0f}:{:.0f}:{:.0f}".format(
            days, hours, min, sec)


def start():
    # with open(runfile, 'w') as rf:
    #     rf.write('start time')
    begin = time.time()
    t = Timer(begin)
    THREADS.append(t)
    t.start()


def stop():
    THREADS[0].stop()
