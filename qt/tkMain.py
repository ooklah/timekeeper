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


class TKMain(QtWidgets.QMainWindow):

    def __init__(self, model):
        super(TKMain, self).__init__(parent=None)
        self.model = model

        self._setup()

    def _setup(self):
        """Window Setup."""
        self.qt = tkMainWindow.Ui_TimeKeeperWindow()
        self.qt.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tkmain = TKMain()
    tkmain.show()
    sys.exit(app.exec_())
