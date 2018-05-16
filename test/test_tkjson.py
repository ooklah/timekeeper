"""
Unittests for the data.tkjson module
"""

# Python
import unittest
import os
import shutil

# Local
from timekeeper.data import tkjson
from timekeeper.test import vars


class TestTKJson(unittest.TestCase):

    def setUp(self):
        self.p = vars.FYLE_PATH
        self.j = tkjson.TkJson()
        self.j.create_project(vars.PROJECT_NAME, vars.FYLE_PATH)

    def tearDown(self):
        self.j = None
        shutil.rmtree(os.path.join(vars.DEFAULT_PATH, vars.TEST_FOLDER))
        pass

    def test_create_project(self):
        """
        Test to see if the json will properly create the file location.
        This includes directories if they don't pre-exist.
        """
        j = tkjson.TkJson()
        j.create_project(vars.PROJECT_NAME, vars.FYLE_PATH)
        self.assertTrue(os.path.exists(self.p), "Path was not created.")
        self.assertTrue(j.project_name, vars.PROJECT_NAME)
        self.assertTrue(j.api_version, tkjson.API_VERSION)

    def test_add_top_task(self):
        """Test adding in a task at the top level."""
        self.j.add_task(None, "cookies")
        task = self.j.get_task("cookies")
        self.assertEqual(task.get("name"), "cookies")
        self.assertEqual(task.get("id"), 1)

    def test_add_nested_task(self):
        """Test adding a nested task."""
        self.j.add_task(None, "cookies")
        self.j.add_task("cookies", "chocolate")
        self.j.add_task("cookies/chocolate", "chunk")

        task = self.j.get_task("cookies/chocolate/chunk")
        self.assertEqual(task.get("name"), "chunk")
        self.assertEqual(task.get("id"), 3)

    def test_get_task_id(self):
        """Test getting back the task ID."""
        self.j.add_task(None, "cookies")
        tid = self.j.get_task_id("cookies")
        self.assertEqual(tid, 1)

    def test_add_task_return_id(self):
        """Test getting back the task ID."""
        tid = self.j.add_task(None, "cookies")
        self.assertEqual(tid, 1)

    def test_add_record(self):
        """Test adding a record to a particular task."""
        tid = self.j.add_task(None, "cookies")
        r = self.j.add_record(tid, "start", "end", "these are some notes")
        self.assertEqual(r.get('time_start'), "start")
        self.assertEqual(r.get('time_elapsed'), "end")
        self.assertEqual(r.get('notes'), "these are some notes")
        self.assertEqual(len(self.j.records.keys()), 1)

    def test_get_records(self):
        """Test getting the records of a particular task."""
        tida = self.j.add_task(None, "cookies")
        tidb = self.j.add_task(None, "cupcakes")
        self.j.add_record(tida, "sa", "ea", "na")
        self.j.add_record(tidb, "sb", "eb", "nb")
        self.j.add_record(tidb, "sc", "ec", "nc")
        ra = self.j.get_records(tida)
        self.assertEqual(len(ra), 1)
        self.assertEqual(ra[0].get('time_start'), "sa")

        rb = self.j.get_records(tidb)
        self.assertEqual(len(rb), 2)
        self.assertEqual(rb[1].get('time_start'), "sc")


if __name__ == '__main__':
    unittest.main()
