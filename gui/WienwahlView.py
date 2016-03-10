# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Overview.ui'
#
# Created: Thu Mar 10 13:04:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 599)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setObjectName("tabs")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setAcceptDrops(False)
        self.menuWindows.setObjectName("menuWindows")
        self.helpWindow = QtGui.QMenu(self.menubar)
        self.helpWindow.setAcceptDrops(False)
        self.helpWindow.setObjectName("helpWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openFile = QtGui.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.saveFile = QtGui.QAction(MainWindow)
        self.saveFile.setObjectName("saveFile")
        self.saveAsFile = QtGui.QAction(MainWindow)
        self.saveAsFile.setObjectName("saveAsFile")
        self.newFile = QtGui.QAction(MainWindow)
        self.newFile.setObjectName("newFile")
        self.closeWindow = QtGui.QAction(MainWindow)
        self.closeWindow.setObjectName("closeWindow")
        self.copy = QtGui.QAction(MainWindow)
        self.copy.setObjectName("copy")
        self.addRow = QtGui.QAction(MainWindow)
        self.addRow.setObjectName("addRow")
        self.openDatabase = QtGui.QAction(MainWindow)
        self.openDatabase.setObjectName("openDatabase")
        self.saveAsDatabase = QtGui.QAction(MainWindow)
        self.saveAsDatabase.setObjectName("saveAsDatabase")
        self.paste = QtGui.QAction(MainWindow)
        self.paste.setObjectName("paste")
        self.undo = QtGui.QAction(MainWindow)
        self.undo.setObjectName("undo")
        self.redo = QtGui.QAction(MainWindow)
        self.redo.setObjectName("redo")
        self.removeRow = QtGui.QAction(MainWindow)
        self.removeRow.setObjectName("removeRow")
        self.duplicateRow = QtGui.QAction(MainWindow)
        self.duplicateRow.setObjectName("duplicateRow")
        self.menuFile.addAction(self.openFile)
        self.menuFile.addAction(self.saveFile)
        self.menuFile.addAction(self.saveAsFile)
        self.menuFile.addAction(self.newFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.openDatabase)
        self.menuFile.addAction(self.saveAsDatabase)
        self.menuEdit.addAction(self.copy)
        self.menuEdit.addAction(self.paste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.addRow)
        self.menuEdit.addAction(self.duplicateRow)
        self.menuEdit.addAction(self.removeRow)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.undo)
        self.menuEdit.addAction(self.redo)
        self.menuWindows.addAction(self.closeWindow)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.helpWindow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.closeWindow, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("MainWindow", "Handle files", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Edit content", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setStatusTip(QtGui.QApplication.translate("MainWindow", "Handle the window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("MainWindow", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.helpWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.openFile.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.openFile.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open a file", None, QtGui.QApplication.UnicodeUTF8))
        self.openFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFile.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFile.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save the actual file", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFile.setText(QtGui.QApplication.translate("MainWindow", "Save As File", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFile.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save the actual file again", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.newFile.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.newFile.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new file", None, QtGui.QApplication.UnicodeUTF8))
        self.newFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.closeWindow.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close the window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeWindow.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.copy.setStatusTip(QtGui.QApplication.translate("MainWindow", "Copy the displayed content", None, QtGui.QApplication.UnicodeUTF8))
        self.copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.addRow.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.addRow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a new Row to the Table", None, QtGui.QApplication.UnicodeUTF8))
        self.addRow.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+Return", None, QtGui.QApplication.UnicodeUTF8))
        self.openDatabase.setText(QtGui.QApplication.translate("MainWindow", "Open Database", None, QtGui.QApplication.UnicodeUTF8))
        self.openDatabase.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+O", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsDatabase.setText(QtGui.QApplication.translate("MainWindow", "Save As Database", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsDatabase.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.paste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.undo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.undo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.redo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.redo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRow.setText(QtGui.QApplication.translate("MainWindow", "Delte Row", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRow.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateRow.setText(QtGui.QApplication.translate("MainWindow", "Duplicate Row", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateRow.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))

