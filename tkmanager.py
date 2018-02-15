"""
Time Manager Class

Creates and manages the individual time trackers.
"""

from timekeeper import tktracker

class TKManager(object):

    def __init__(self):
        """Tracker Manager."""
        self._trackers = []
    
    def start(self, tid=None):
        """
        Start a new tracker or restart an existing tracker.
        If an id is passed in, the manager will restart the existing 
        tracker. If just called, it will create and start a new
        tracker.
        """
        if tid:
            self._trackers[tid - 1].restart()
            return tid
        count = len(self)
        t = tktracker.TKTracker(count) + 1
        self._trackers.append(t)
        t.start()
        return len(self)

    def stop(self, tid):
        """Stop a tracker by the id value."""
        self._trackers[tid - 1].stop()
        return self._trackers[tid - 1].results

    def __len__(self):
        return len(self._trackers)