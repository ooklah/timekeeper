"""
Unittests for tktracker module
"""

# Python
import unittest
import time

# Local
from timekeeper.tktracker import TKTracker, TrackerStartError, TrackerStopError


class TestTKTracker(unittest.TestCase):

    def setUp(self):
        self.tk = TKTracker(1)

    def tearDown(self):
        self.tk = None

    def test_double_start_fail(self):
        """
        Test to make sure that the tracker will fail if start()
        is called twice.
        """
        self.tk.start()
        self.assertRaises(TrackerStartError, self.tk.start())

    def test_double_stop_fail(self):
        """
        Test to make sure that stop cannot be called twice in a row.
        """
        self.tk.start()
        self.tk.stop()
        self.assertRaises(TrackerStopError, self.tk.stop())

    def test_stop_without_start(self):
        """Test that the tracker fails if stop is calle before start."""
        self.assertRaises(TrackerStopError, self.tk.stop())

    def test_start_stop(self):
        """Test that starts and stops the tracker without issue."""
        self.tk.start()
        time.sleep(1)
        self.tk.stop()
        self.assertEqual(len(self.tk._total_laps[0]), 2, self.tk._total_laps)


if __name__ == '__main__':
    unittest.main()