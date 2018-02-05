"""
Time Tracker Class

Keeps track of an individual timer/log object
"""

import time

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
        self.stop_flag = False

    @property
    def id(self):
        return self._id

    def start(self):
        """Start the tracker."""
        if not self.stop_flag:
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
        else:
            raise TrackerStopError("Already stopped.")