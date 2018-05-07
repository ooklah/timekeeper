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

    def test_add_record(self):
        """Test adding a record to a particular task."""
        self.j.add_task(None, "cookies")


if __name__ == '__main__':
    unittest.main()
