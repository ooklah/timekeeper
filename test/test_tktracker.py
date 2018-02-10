"""
Unittests for tktracker module
"""

# Python
import unittest
import time

# Local
from timekeeper.tktracker import TKTracker, TrackerStartError, TrackerStopError


def s(c=1):
    """Shorthand sleep timer."""
    time.sleep(c)


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
        with self.assertRaises(TrackerStartError):
            self.tk.start()

    def test_double_stop_fail(self):
        """
        Test to make sure that stop cannot be called twice in a row.
        """
        self.tk.start()
        self.tk.stop()
        with self.assertRaises(TrackerStopError):
            self.tk.stop()

    def test_stop_without_start(self):
        """Test that the tracker fails if stop is calle before start."""
        with self.assertRaises(TrackerStopError):
            self.tk.stop()

    # @unittest.SkipTest
    def test_start_stop(self):
        """Test that starts and stops the tracker without issue."""
        self.tk.start()
        s()
        self.tk.stop()
        self.assertEqual(len(self.tk._total_laps[0]), 2, self.tk._total_laps)

    # @unittest.SkipTest
    def test_start_restart(self):
        """Test Starting and then starting the same tracker again."""
        self.tk.start()
        s()
        with self.assertRaises(TrackerStartError):
            self.tk.start()

    # @unittest.SkipTest
    def test_elapsed_time(self):
        """
        Test the elapsed time property to ensure it returns the correct
        value on one cyle.
        """
        self.tk.start()
        s(5)
        self.tk.stop()
        # Round to the nearest whole number for now.
        self.assertEquals(int(self.tk.elapsed_time), 5)

    # @unittest.SkipTest
    def test_elapsed_time_laps(self):
        """
        Test the elapsed time with multiple time lapses.
        """
        for i in range(5):
            self.tk.start()
            s()
            self.tk.stop()
        
        # Round to the nearest whole number.
        self.assertEqual(int(self.tk.elapsed_time), 5)

    # @unittest.SkipTest
    def test_no_lap_elapsed_without_stop(self):
        """
        Test getting the elapsed time before the tracker has been 
        stopped on the first lap."""
        self.tk.start()
        s()
        self.assertEqual(int(self.tk.elapsed_time), 1)
        s()
        self.tk.stop()
        self.assertEqual(int(self.tk.elapsed_time), 2)

    def test_lap_counter_one(self):
        """Test that the lap counter returns one lap on first lap."""
        self.tk.start()
        self.assertEqual(self.tk.laps, 1)

    def test_lap_counter_two(self):
        """Test lap counter on 1.5 laps"""
        self.tk.start()
        s()
        self.tk.stop()
        s()
        self.tk.start()
        s()
        self.assertEqual(self.tk.laps, 2)


if __name__ == '__main__':
    unittest.main()
