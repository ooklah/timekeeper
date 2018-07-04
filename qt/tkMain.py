"""
Main Qt Window for the Time Keep Program.
"""
# Standard
import sys

# Third
from PySide import QtGui as QtWidgets
from PySide import QtCore

# Local
from timekeeper.qt import tkMainWindow
from timekeeper.data import tkmodel


class TKMain(QtWidgets.QMainWindow):

    def __init__(self, model):
        super(TKMain, self).__init__(parent=None)
        self.model = model

        self._setup()

    def notsure(self, index):
        print index
        item = index.data(QtCore.Qt.DisplayRole)
        print item
        print index.model()
        item = self.model.itemFromIndex(index)
        print item.parent

    def _setup(self):
        """Window Setup."""
        self.qt = tkMainWindow.Ui_TimeKeeperWindow()
        self.qt.setupUi(self)
        self.qt.taskTree.setModel(self.model)
        self.qt.taskTree.clicked.connect(self.notsure)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    j = "c:/temp/timekeeper/project.json"
    m = tkmodel.TkModel(j)
    tkmain = TKMain(m.get_model())
    tkmain.show()
    sys.exit(app.exec_())
