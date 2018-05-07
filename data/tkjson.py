"""
Json Reader and writer class for the Time Keeper Module
"""

import json
import os
import datetime
import time

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
    "api_version": API_VERSION,
    "id_count": 0
}

_TASK = {
    "name": "",
    "id": 0,
    "children": [],
    "status": "open",
    "type": "task",
    "created": None
}

_RECORD = {
    "time_start": 0,
    "time_elapsed": 0,
    "notes": "",
    "type": "record"
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
        self._j[META] = dict(_METADATA)
        self._j[META]['project_name'] = project_name
        self._j[TASK] = []
        self._j[RECORD] = {}

        # Make sure the file exists.
        dir_path = os.path.dirname(save_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        self._lp = save_path
        self._autosave()

    # ----- Metadata Access ---------------------------------------------------
    @property
    def project_name(self):
        """Returns the project name in the json file."""
        return self._j[META]['project_name']

    @property
    def api_version(self):
        """Return the json api version."""
        return self._j[META]['api_version']

    @property
    def id_count(self):
        """Return the current ID count."""
        return self._j[META]['id_count']

    # ----- Task Access -------------------------------------------------------
    def add_task(self, parent, name):
        """Add in a new task from the parent location."""
        t = dict(_TASK)
        t['name'] = name
        t['id'] = self._increment()
        t['created'] = time.time()
        if parent is None:
            self._j[TASK].append(t)
        else:
            self.get_task(parent)["children"].append(t)
        print self._j
        self._autosave()

    def get_task(self, task_path):
        """Return the task dictionary from the task path."""
        task = TaskQuery(self._j[TASK]).get(task_path)
        return task

    def get_task_id(self, task_path):
        """Return the task ID of the selected task"""
        task = self.get_task(task_path)
        return task["id"]

    # ----- Record Access -----------------------------------------------------
    def add_record(self, task_id, time_start, time_elapsed, notes=""):
        """Add a record to a particular task."""
        pass

    # ----- Internal Functions ------------------------------------------------
    def _autosave(self):
        """Save data when it is changed."""
        with open(self._lp, 'w') as writer:
            json.dump(self._j, writer)

    def _increment(self):
        task_id = self.id_count + 1
        self._j[META]['id_count'] = task_id
        return self.id_count


class DepthLimitReached(Exception):
    pass


class TaskQuery:
    def __init__(self, data):
        self.data = data
        self.k = "/"

    def get(self, path, pointer=None, c=0):
        # print "--- {} ---".format(c)
        if c == 10:
            raise DepthLimitReached()

        if pointer is None:
            pointer = self.data

        if path.count(self.k):
            key, next = path.split(self.k, 1)
        else:
            key = path
            next = None

        for item in pointer:
            name = item.get("name", None)
            if name and name == key:
                if next:
                    return self.get(next, item["children"], c+1)
                else:
                    # print "Returning item", item
                    return item
