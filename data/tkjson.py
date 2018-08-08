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
def create_metadata(project_name):
    """Create a new metadata object."""
    t = {
        "created": time.time(),
        "last_updated": time.time(),
        "project_name": project_name,
        "api_version": API_VERSION,
        "id_count": 0
    }
    return t


def create_task(name, task_id):
    """Create a new task object."""
    t = {
        "name": name,
        "id": task_id,
        "children": [],
        "status": "open",
        "type": "task",
        "created": time.time()
    }
    return t


def create_record(time_start, time_elapsed, notes=""):
    t = {
        "time_start": time_start,
        "time_elapsed": time_elapsed,
        "notes": notes,
        "type": "record"
    }
    return t


class TkJson:

    def __init__(self):
        # Internal json data structure.
        self._j = None
        # Load path variable.
        self._lp = None

    def load(self, load_path):
        """Load and validate the json file."""
        with open(load_path) as fp:
            self._j = json.load(fp)
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
        self._j[META] = create_metadata(project_name)
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
    def meta(self):
        """Access to the metadata dictionary."""
        return self._j[META]

    @property
    def project_name(self):
        """Returns the project name in the json file."""
        return self.meta['project_name']

    @property
    def api_version(self):
        """Return the json api version."""
        return self.meta['api_version']

    @property
    def id_count(self):
        """Return the current ID count."""
        return self.meta['id_count']

    # ----- Task Access -------------------------------------------------------
    @property
    def tasks(self):
        """Access to tasks dictionary"""
        return self._j[TASK]

    def add_task(self, parent, name):
        """Add in a new task from the parent location."""
        t = create_task(name, self._increment())

        if parent is None:
            self.tasks.append(t)
        else:
            self.get_task(parent)["children"].append(t)

        self._autosave()
        return t.get('id')

    def get_task(self, task_path):
        """Return the task dictionary from the task path."""
        task = TaskQuery(self.tasks).get(task_path)
        return task

    def get_task_id(self, task_path):
        """Return the task ID of the selected task"""
        task = self.get_task(task_path)
        return task["id"]

    # ----- Record Access -----------------------------------------------------
    @property
    def records(self):
        return self._j[RECORD]

    def add_record(self, task_id, time_start, time_elapsed, notes=""):
        """Add a record to a particular task."""
        record = create_record(time_start, time_elapsed, notes)

        if not self.records.get(task_id, None):
            self.records[task_id] = []
        self.records[task_id].append(record)

        self._autosave()
        return record

    def get_records(self, task_id):
        """
        Get the records for a particular task id. No individual access to
        the records here.
        """

        return self.records.get(task_id, None)

    # ----- Internal Functions ------------------------------------------------
    def _autosave(self):
        """Save data when it is changed."""
        self.meta["last_updated"] = time.time()
        with open(self._lp, 'w') as writer:
            json.dump(self._j, writer)

    def _increment(self):
        """
        Increment the id count. Don't touch this otherwise it could start
        overwriting existing tasks or records. Or things could just
        generally screw up.
        """
        task_id = self.id_count + 1
        self.meta['id_count'] = task_id
        return self.id_count


class DepthLimitReached(Exception):
    pass


class TaskQuery:
    def __init__(self, data):
        self.data = data
        self.k = "/"

    def get(self, path, pointer=None, c=0):
        """Recursive get query. Find the task from the given path."""
        # print "--- {} ---".format(c)
        # Break, should never be this deep.
        if c == 10:
            raise DepthLimitReached()

        # At the top of the tree
        if pointer is None:
            pointer = self.data

        # Split off the first item in the path, save the rest for later.
        if path.count(self.k):
            key, next = path.split(self.k, 1)
        else:
            key = path
            next = None

        # Go through the list of children until we find where the
        # name matches the key. And if we have a next, then continue
        # into those children to keep looking. Otherwise, we've found
        # the item we're looking for.
        for item in pointer:
            name = item.get("name", None)
            if name and name == key:
                if next:
                    return self.get(next, item["children"], c+1)
                else:
                    # print "Returning item", item
                    return item
