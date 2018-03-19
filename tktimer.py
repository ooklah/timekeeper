"""
Time Tracker Class

This is a single Event tracking class. It has no concept of project, department,
or task or what have you. It will just keep track of a start time and an end
time.
"""

import time

from timekeeper.tkcomm import calc_time, str_time


class TimerStartError(Exception):
    pass


class TimerStopError(Exception):
    pass


class TKTimer(object):

    def __init__(self, id):
        """
        init for TKTimer.
        :param id: (any) accepts something that can be used to identify this
            particular even again when asked.
        """
        super(TKTimer, self).__init__()
        self._id = id
        self._lap = []
        self._total_laps = []
        self.results = {}
        self.stop_flag = True
        self.pause_flag = False

    @property
    def id(self):
        return self._id

    @property
    def elapsed_time(self):
        """Return the total amount of time that has elapsed so far."""
        total_time = 0
        # Get the total time from previous laps
        for lap in self._total_laps:
            if len(lap) == 2:
                total_time = total_time + (lap[1] - lap[0])
            # I don't think this should ever be a case.
            if len(lap) == 1:
                tmp = list(lap)
                tmp.append(time.time())
                total_time = total_time + (tmp[1] - tmp[0])

        # Get the time from the current lap if we're in one.
        if len(self._lap):
            total_time = total_time + (time.time() - self._lap[0])

        return total_time

    @property
    def start_time(self):
        """Return the start time if there is one."""
        # Get the initial lap value in laps
        if len(self._total_laps):
            return self._total_laps[0][0]
        
        # Unless we're in the first lap, get that value
        if len(self._lap):
            return self._lap[0]
        
        # This tracker has not been started yet.
        return None

    @property
    def laps(self):
        """
        Return the number of laps, including the current lap running.
        """
        # Get previous laps
        count = len(self._total_laps)
        # Get the current lap
        if len(self._lap) == 1:
            count += 1
        return count

    def start(self):
        """Start the timer."""
        if self.stop_flag:
            self._lap.append(time.time())
            self.stop_flag = False
        else:
            raise TimerStartError('Already running.')

    def stop(self):
        """Stop the timer."""
        if not self.stop_flag:
            self._lap.append(time.time())
            self._total_laps.append(self._lap)
            self._lap = []
            self.stop_flag = True
        else:
            raise TimerStopError("Already stopped.")

    def pause(self):
        """Will pause the current timer without setting a new 'lap.'"""
        raise NotImplemented("This has not been created yet.")

    def str_time(self):
        """Return a string of time as D H M S"""
        return str_time(*calc_time(self.elapsed_time))

    def __repr__(self):
        msg = "<Timer (id:{}) (laps:{}) (time:{})>".format(
            self.id, self.laps, self.elapsed_time
        )

        return msg
