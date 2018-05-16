# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ooklah/workspace/everfree/timekeeper/qt\tkMainWindow.ui'
#
# Created: Tue May 15 19:30:10 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TimeKeeperWindow(object):
    def setupUi(self, TimeKeeperWindow):
        TimeKeeperWindow.setObjectName("TimeKeeperWindow")
        TimeKeeperWindow.resize(1023, 600)
        self.centralwidget = QtGui.QWidget(TimeKeeperWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskTree = QtGui.QTreeView(self.centralwidget)
        self.taskTree.setObjectName("taskTree")
        self.horizontalLayout.addWidget(self.taskTree)
        self.recordsTable = QtGui.QTableWidget(self.centralwidget)
        self.recordsTable.setObjectName("recordsTable")
        self.recordsTable.setColumnCount(0)
        self.recordsTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.recordsTable)
        TimeKeeperWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TimeKeeperWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TimeKeeperWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TimeKeeperWindow)
        self.statusbar.setObjectName("statusbar")
        TimeKeeperWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(TimeKeeperWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(TimeKeeperWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(TimeKeeperWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TimeKeeperWindow)
        QtCore.QMetaObject.connectSlotsByName(TimeKeeperWindow)

    def retranslateUi(self, TimeKeeperWindow):
        TimeKeeperWindow.setWindowTitle(QtGui.QApplication.translate("TimeKeeperWindow", "Time Keeper", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("TimeKeeperWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("TimeKeeperWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("TimeKeeperWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("TimeKeeperWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("TimeKeeperWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("TimeKeeperWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("TimeKeeperWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("TimeKeeperWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

