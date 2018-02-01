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

    def __init__(self):
        super(Timer, self).__init__()
        self._lap = []
        self._laps = []
        self.results = {}
        self.daemon = True
        self.stop_flag = False
        self.pause_flag = False
        self.exit_flag = Event()

    def run(self):
        """Thread run point, start a timed lap."""
        self._set_lap_start()
        while not self.is_done():
            self.exit_flag.wait(timeout=DELAY)
        print "finishing"
        self.finish()

    def stop(self):
        """Stop the timer and finish the current lap. Then stop the thread."""
        # Check to make sure we're not already paused so we don't add a second
        # stop time.
        print "stopping"
        if not self.is_paused():
            self._set_lap_end()
        self.stop_flag = True
        self.exit_flag.set()

    def pause(self):
        """Pause the timer and mark the current lap."""
        print "pausing"
        if self.is_paused():
            print "Timer is already paused."
            return
        self.pause_flag = True
        self._set_lap_end()

    def restart(self):
        """Restart the timer after a pause."""
        print "restarting"
        if self.is_paused():
            self.pause_flag = False
            self._set_lap_start()
        else:
            print "Timer is not paused."

    def _set_lap_start(self):
        """Set the start time of a lap."""
        self._lap.append(time.time())

    def _set_lap_end(self):
        """Set end of a lap. Setup for a new lap and append the current lap."""
        self._lap.append(time.time())
        self._laps.append(self._lap)
        self._lap = []

    def is_done(self):
        return self.stop_flag

    def is_paused(self):
        return self.pause_flag

    def delta(self, start, end):
        """Calculate the delta of the laps"""
        return end - start

    def calc_time(self, tv):
        """Calculate the time into hours, minutes seconds."""
        mins, secs = divmod(tv, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        return [days, hours, mins, secs]

    def finish(self):
        print "Finish"
        t = 0.0
        tdic = {}
        for count, lap in enumerate(self._laps):
            delta = self.delta(*lap)
            t = t + delta
            tdic[count] = delta
            d, h, m, s = self.calc_time(delta)
            self._print_time("Lap {}".format(count), d, h, m, s)

        flarp = self.calc_time(t)
        self._print_time("Total Time:", *flarp)
        self.results = tdic

    def _print_time(self, msg, d, h, m, s):
        print "{}: {:.0f}:{:.0f}:{:.0f}:{:.0f}".format(msg, d, h, m, s)



    # def calc_time(self):
    #     delta = self.delta()
    #     min, sec = divmod(delta, 60)
    #     hours, min = divmod(min, 60)
    #     days, hours = divmod(hours, 24)
    #     print "Elapsed Time: {:.0f}:{:.0f}:{:.0f}:{:.0f}".format(
    #         days, hours, min, sec)


class TimeManager(object):

    def __init__(self):
        self._threads = []

    def start(self, tid=None):
        if tid:
            self._threads[tid - 1].restart()
            return tid

        t = Timer()
        self._threads.append(t)
        t.start()
        return len(self._threads)

    def stop(self, tid):
        self._threads[tid - 1].stop()
        self._threads[tid - 1].join()
        return self._threads[tid - 1].results

    def pause(self, tid):
        self._threads[tid - 1].pause()


# def start():)
#     # with open(runfile, 'w') as rf:
#     #     rf.write('start time')
#     begin = time.time()
#     t = Timer(begin)
#     THREADS.append(t)
#     t.start()
#
#
# def stop():
#     THREADS[0].stop()
#     THREADS.pop()
