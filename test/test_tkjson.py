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

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
