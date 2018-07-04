"""
Tree Widget Data.
"""

from PySide import QtGui as QtWidgets
import tkjson


def recursive_lookup(task, parent):
    t = TKItem(task.get('name', None), parent)
    children = task.get('children', [])
    if children:
        for ch in children:
            t.appendRow(recursive_lookup(ch, "{}/{}".format(parent, t.name)))
    return t


class TKItem(QtWidgets.QStandardItem):
    def __init__(self, name, parent):
        super(TKItem, self).__init__(name)
        self.name = name
        self.path = parent


class TkModel:
    def __init__(self, load_path):
        """Stuff will happen."""
        self.js = tkjson.TkJson()
        self.js.load(load_path)
        self.model = QtWidgets.QStandardItemModel()

    def get_model(self):
        """build the inital model data and return it."""
        parent = TKItem(self.js.project_name, None)

        for task in self.js.tasks:
            parent.appendRow(recursive_lookup(task, None))
        self.model.appendRow(parent)
        return self.model
