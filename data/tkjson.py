"""
Json Reader and writer class for the Time Keeper Module
"""

import json
import os

API_VERSION = 1

# Top level keys
META = "metadata"
TASK = "tasks"
RECORD = "records"

# Default templates for the major data structures
_METADATA = {
    "created": 0,
    "last_updated": 0,
    "project_name": "",
    "api_version": API_VERSION
}

_TASK = {
    "name": "",
    "id": 0,
    "children": [],
    "status": open,
    "type": "task"
}

_RECORD = {
    "time_start": 0,
    "time_elapsed": 0,
    "notes": ""
}


class TkJson:

    def __init__(self, load_path=None):
        self._j = None
        self._lp = None

        if load_path:
            if os.path.exists(load_path):
                self.load(load_path)
            else:
                self.create_project(load_path)

    def load(self, load_path):
        """Load and validate the json file."""
        self._j = json.load(load_path)
        self._lp = load_path

    def create_project(self, project_name, save_path):
        """
        Create the basic template structure of the file and save it to the
        location provided.
        :param project_name: (str) name of the project, can be different then
            the save path, but probably shouldn't be.
        :param save_path: (str) file path to save to.
        :return:
        """
        # Create the initial structure
        self._j = dict()
        self._j[META] = _METADATA
        self._j[META]['project_name'] = project_name
        self._j[TASK] = []
        self._j[RECORD] = {}

        # Make sure the file exists.
        dir_path = os.path.dirname(save_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        self._lp = save_path
        self._autosave()

    @property
    def project_name(self):
        """Returns the project name in the json file."""
        return self._j[META]['project_name']

    @property
    def api_version(self):
        """Return the json api version."""
        return self._j[META]['api_version']

    def _autosave(self):
        """Save data when it is changed."""
        with open(self._lp, 'w') as writer:
            json.dump(self._j, writer)
