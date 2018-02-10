"""
Time Manager Class

Creates and manages the individual time trackers.
"""

class TimeManager(object):

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
        t = Tracker()
        self._trackers.append(t)
        t.start()
        return len(self._trackers)

    def stop(self, tid):
        self._trackers[tid - 1].stop()
        self._trackers[tid - 1].join()
        return self._trackers[tid - 1].results

    def pause(self, tid):
        self._trackers[tid - 1].pause()