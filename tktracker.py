"""
Time Tracker Class

Keeps track of an individual timer/log object
"""

import time

from timekeeper.tkcomm import calc_time, str_time

class TrackerStartError(Exception):
    pass

class TrackerStopError(Exception):
    pass


class TKTracker(object):

    def __init__(self, id):
        super(TKTracker, self).__init__()
        self._id = id
        self._lap = []
        self._total_laps = []
        self.results = {}
        self.stop_flag = True

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
        # Get the inital lap value in laps
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
        """Start the tracker."""
        if self.stop_flag:
            self._lap.append(time.time())
            self.stop_flag = False
        else:
            raise TrackerStartError('Already running.')

    def stop(self):
        """Stop the tracker."""
        if not self.stop_flag:
            self._lap.append(time.time())
            self._total_laps.append(self._lap)
            self._lap = []
            self.stop_flag = True
        else:
            raise TrackerStopError("Already stopped.")

    def str_time(self):
        """Return a string of time as D H M S"""
        return str_time(*calc_time(self.elapsed_time))

    def __repr__(self):
        msg = "<Tracker (id:{}) (laps:{}) (time:{})>".format(
            self.id, self.laps, self.elapsed_time
        )

        return msg
