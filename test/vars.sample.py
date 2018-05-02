"""
Vars file for importing and using data that is not kept in the repo.
Will need a vars.py.sample when done checked into the git instead.
"""
import os

# This will serve as the project file name where we save the file out to
# while testing.
FYLE_NAME = ""
# The extension for the file, in case it needs to be separated for some reason.
FYLE_EXT = ""
# Name of the project that will be created for testing.
PROJECT_NAME = ""

# The default starting path where the test data will reside, this folder is not
# expected to be deleted.
DEFAULT_PATH = ""
# Folder to store the test data into. This folder can expect to be deleted,
# along with everything underneath it when the tests are done.
TEST_FOLDER = ""

# A pre-built file path
FYLE_PATH = os.path.join(DEFAULT_PATH, TEST_FOLDER,
                         "{}.{}".format(FYLE_NAME, FYLE_EXT))