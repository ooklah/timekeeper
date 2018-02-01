import unittest
import time

from timekeeper import tkcontrol as tk


class TestTKControl(unittest.TestCase):

    def test_pausing(self):
        tm = tk.TimeManager()
        t = tm.start()
        time.sleep(5)
        tm.pause(t)
        self.assertEquals(tm._threads[t - 1].is_paused(), True)
        time.sleep(5)
        tm.start(t)
        self.assertEquals(tm._threads[t - 1].is_paused(), False)
        time.sleep(5)
        results = tm.stop(t)
        # For simplicity because the gillianth decimal is never the same.
        results[0] = int(results[0])
        results[1] = int(results[1])
        self.assertEquals(results, {0: 5, 1: 5})


if __name__ == '__main__':
    unittest.main()

