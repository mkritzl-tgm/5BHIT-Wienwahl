from threading import Thread
import os

from PySide import QtGui, QtCore
from datetime import datetime
import time
from command.command import EditCommand, InsertRowsCommand, RemoveRowsCommand, DuplicateRowCommand
from command.delegate import ItemDelegate
from controller.DatabasedialogController import DatabaseDialogController

from csvhandler.CSVHandler import CSVHandler
from database.DatabaseHandler import DatabaseHandler
from model.WienwahlModel import WienwahlModel, TableModel, Accessor, ConnectionType
from gui import WienwahlView

__author__ = 'mkritzl'

import sys
from PySide.QtGui import *


class MyController(QMainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)

        self.form = WienwahlView.Ui_MainWindow()
        self.form.setupUi(self)

        self.dialogWindow = DatabaseDialogController()

        self.model = WienwahlModel()

        self.handler = {}
        self.handler["csvHandler"] = CSVHandler()
        self.handler["databaseHandler"] = DatabaseHandler('mysql+pymysql://wienwahl:wienwahl@localhost/wienwahl?charset=utf8')

        self.databaseStep = None

        self.threads = []


        self.form.newFile.triggered.connect(self.newFile)
        self.form.openFile.triggered.connect(self.openFile)
        self.form.saveFile.triggered.connect(self.saveResourceThread)
        self.form.saveAsFile.triggered.connect(self.saveAsFile)
        self.form.saveAsDatabase.triggered.connect(self.saveAsDatabase)
        self.form.openDatabase.triggered.connect(self.openDatabase)
        self.form.copy.triggered.connect(self.copy)
        self.form.cut.triggered.connect(self.cut)
        self.form.paste.triggered.connect(self.paste)
        self.form.undo.triggered.connect(self.undo)
        self.form.redo.triggered.connect(self.redo)
        self.form.closeWindow.triggered.connect(self.closeWindow)
        self.form.helpWindow.triggered.connect(self.helpWindow)
        self.form.tabs.currentChanged.connect(self.tabChanged)
        self.form.tabs.tabCloseRequested.connect(self.closeTab)
        self.form.addRow.triggered.connect(self.addRow)
        self.form.duplicateRow.triggered.connect(self.duplicateRow)
        self.form.removeRow.triggered.connect(self.removeRows)

        self.form.prediction.triggered.connect(self.prediction)
        self.form.createPrediction.triggered.connect(self.createPrediction)

    def openFileDialog(self):
        """
        Opens a file dialog and sets the label to the chosen path
        """

        path, _ = QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
        return path


    def newFileDialog(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", os.getcwd())
        return path

    def closeDatabaseDialog(self):
        self.dialogWindow.hide()


    def newFile(self):
        self.generateNewTab([["T","WV","WK","BZ","SPR","WBER","ABG","UNG","SPOE","FPOE","OEVP","GRUE","NEOS","WWW","ANDAS","GFW","SLP","WIFF","M","FREIE"]], None)

    def formatTable(self, table):
        # set font
        font = QFont("Courier New", 14)
        table.setFont(font)
        # set column width to fit contents (set font first!)
        table.resizeColumnsToContents()
        # enable sorting
        if self.model.getCurrentTable().getContent():
            table.setSortingEnabled(True)


    def appendTab(self, accessor):
        tab = QtGui.QWidget()
        tab.setObjectName("tab"+str(self.model.getTableCount()))
        if accessor:
            tab.setToolTip(accessor.getAccessString())
            self.form.tabs.addTab(tab, accessor.getName())
        else:
            tab.setToolTip("New")
            self.form.tabs.addTab(tab, "New")
        self.form.tabs.setCurrentIndex(self.form.tabs.count()-1)
        return tab

    def appendTable(self, table_model, parent):
        table_view = QTableView()
        table_view.setObjectName("table"+str(self.model.getTableCount()))
        table_view.setModel(table_model)
        table_view.setItemDelegate(ItemDelegate(table_model.getUndoStack(), self.editedSomething))

        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        parent.setLayout(layout)

        return table_view

    def generateNewTab(self, content, accessor):
            tab = self.appendTab(accessor)

            table_model = TableModel(tab, content, accessor)

            self.model.setCurrentTableAndAdd(table_model)
            table_view = self.appendTable(table_model, tab)
            self.formatTable(table_view)
            self.model.getCurrentTable().setView(table_view)
            self.model.getCurrentTable().setEdited(False)

    def openFile(self):
        path = self.openFileDialog()
        if path is not "":
            accessor = Accessor(path, ConnectionType.csv)
            self.generateNewTab(self.handler["csvHandler"].getContentAsArray(accessor.getAccessString()), accessor)

    def databaseDialog(self):
        self.dialogWindow.setElections(self.handler["databaseHandler"].getElections())
        self.dialogWindow.show()
        if self.dialogWindow.exec_():
            self.dialogWindow.hide()
            return self.dialogWindow.getElection()

    def handleDatabase(self):
        pass

    def openDatabase(self):
        access = self.databaseDialog()
        if access:
            accessor = Accessor(access, ConnectionType.database)
            self.generateNewTab(self.handler["databaseHandler"].getVotesAsArray(accessor.getAccessString()), accessor)

    def saveAsResourceThread(self, type, append=False):
        self.saveAsResource(type, append)

    def saveResourceThread(self, accessor=None, data=None, append=False):
        self.saveResource(accessor, data, append)

    def setSavingStatus(self, saved, currentTable):
        if saved==True:
            self.form.statusbar.showMessage('saved')
            currentTable.setEdited(False)
            # print("Set saving status saved")
        else:
            self.form.statusbar.showMessage('saving...')
            # print("Set saving saving")

    def askForAppending(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Do want to append this content", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return reply == QtGui.QMessageBox.Yes


    def saveResource(self, accessor=None, data=None, append=False):
        if data or self.model.getCurrentTable() and self.model.getCurrentTable().getAccessor():
            saver = Saver(self.handler, self.model.getCurrentTable(), accessor, data, append)
            saver.updateProgress.connect(self.setSavingStatus)
            saver.start()
            self.threads.append(saver)

    def saveAsDatabase(self):
        append = self.askForAppending()
        self.saveAsResourceThread(ConnectionType.database, append)

    def saveAsFile(self):
        self.saveAsResourceThread(ConnectionType.csv)

    def saveAsResource(self, type=ConnectionType.csv, append=False):
        accessor = None
        if self.model.getTableCount()>0:
            if type==ConnectionType.csv:
                accessor = Accessor(self.newFileDialog(), ConnectionType.csv)
            elif type==ConnectionType.database:
                accessor = Accessor(self.databaseDialog(), ConnectionType.database)

            self.model.getCurrentTable().setAccessor(accessor)

            self.saveResourceThread(accessor, None, append)

            self.form.tabs.setTabText(self.model.getCurrentIndex(), accessor.getName())
            self.form.tabs.setTabToolTip(self.model.getCurrentIndex(), accessor.getName())

    def get_selected_rows(self):
        indexes = self.model.getCurrentTable().getView().selectionModel().selectedIndexes()
        if indexes:
            print(str(indexes[0].row()) + "amount:" + str(len(indexes)))
            return indexes[0].row(), len(indexes)
        else:
            return None, None


    def addRow(self):
        table = self.model.getCurrentTable()
        if table:
            start, amount = self.get_selected_rows()
            if amount:
                table.getUndoStack().beginMacro("Added table")
                table.getUndoStack().push(InsertRowsCommand(self.model.getCurrentTable(), start, 1))
                table.getUndoStack().endMacro()
                self.editedSomething()

    def duplicateRow(self):
        table = self.model.getCurrentTable()
        if len(table.getContent()) == 0:
            return
        start, amount = self.get_selected_rows()
        if amount:
            table.getUndoStack().beginMacro("Duplicated row")
            table.getUndoStack().push(DuplicateRowCommand(table, start))
            table.getUndoStack().endMacro()
            self.editedSomething()

    def removeRows(self):
        table = self.model.getCurrentTable()
        if len(table.getContent()) == 0:
            return
        start, amount = self.get_selected_rows()
        if amount:
            table.getUndoStack().beginMacro("Removed row(s)")
            table.getUndoStack().push(RemoveRowsCommand(table, start, amount))
            table.getUndoStack().endMacro()
            self.editedSomething()

    def cut(self):
        table = self.model.getCurrentTable()
        selectedIndexes = self.model.getCurrentTable().getView().selectionModel().selectedIndexes()
        if len(selectedIndexes) == 0:
            return

        sys_clip = QApplication.clipboard()
        selection = selectedIndexes[0]
        selected_text = str(self.model.getCurrentTable().data(selection))
        sys_clip.setText(selected_text)

        cmd = EditCommand(self.model.getCurrentTable(), selection)
        cmd.newValue("")
        table.getUndoStack().beginMacro("Cutted Text")
        table.getUndoStack().push(cmd)
        table.getUndoStack().endMacro()

        self.editedSomething()

    def copy(self):
        selectedIndexes = self.model.getCurrentTable().getView().selectionModel().selectedIndexes()
        if len(selectedIndexes) == 0:
            return

        sys_clip = QApplication.clipboard()
        selection = selectedIndexes[0]
        selected_text = str(self.model.getCurrentTable().data(selection))
        sys_clip.setText(selected_text)


    def paste(self):
        table = self.model.getCurrentTable()
        selectedIndexes = self.model.getCurrentTable().getView().selectionModel().selectedIndexes()
        if len(selectedIndexes) == 0:
            return

        sys_clip = QApplication.clipboard()
        value = str(sys_clip.text())
        index = selectedIndexes[0]
        cmd = EditCommand(self.model.getCurrentTable(), index)
        cmd.newValue(value)
        table.getUndoStack().beginMacro("Pasted Text")
        table.getUndoStack().push(cmd)
        table.getUndoStack().endMacro()
        self.editedSomething()

    def editedSomething(self):
        self.model.getCurrentTable().getView().reset()
        self.model.getCurrentTable().setEdited(True)
        self.setUndoRedoMenu()

    def undo(self):
        self.model.getCurrentTable().getUndoStack().undo()
        self.editedSomething()

    def redo(self):
        self.model.getCurrentTable().getUndoStack().redo()
        self.editedSomething()

    def closeWindow(self):
        pass

    def helpWindow(self):
        pass

    def prediction(self,date=None):
        if not date:
            if self.model.getCurrentTable() and self.model.getCurrentTable().getAccessor() and self.model.getCurrentTable().getAccessor().getConnectionType()==ConnectionType.database:
                date = self.model.getCurrentTable().getAccessor().getAccessString()
            else:
                date = self.databaseDialog()
        if date:
            accessor = Accessor(date, ConnectionType.prediction)
            self.generateNewTab(self.handler["databaseHandler"].getPredictionsAsArray(accessor.getAccessString()), accessor)

    def createPrediction(self):
        if self.model.getCurrentTable() and self.model.getCurrentTable().getAccessor() and self.model.getCurrentTable().getAccessor().getConnectionType()==ConnectionType.database:
            date = self.model.getCurrentTable().getAccessor().getAccessString()
        else:
            date = datetime.now().strftime("%Y-%m-%d")
        self.prediction(self.handler["databaseHandler"].createPrediction(date))

    def tabChanged(self):
        self.model.setCurrentIndex(self.form.tabs.currentIndex())

    def closeTab(self, index):
        if not self.model.getTables()[index].isEdited():
            self.removeTab(index)
        else:
            quit_msg = "The file is not saved. Are you sure you want to close the file?"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Save:
                self.saveResourceThread()
                self.removeTab(index)
            elif reply == QtGui.QMessageBox.Yes:
                self.removeTab(index)

    def removeTab(self, index):
        widget = self.form.tabs.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.form.tabs.removeTab(index)
        self.model.deleteTable(index)


    def setUndoRedoMenu(self):
        undo = "Undo"
        redo = "Redo"
        undoText = self.model.getCurrentTable().getUndoStack().undoText()
        redoText = self.model.getCurrentTable().getUndoStack().redoText()
        if undoText:
            undo+= " (" + undoText + ")"
        if redoText:
            redo+= " (" + redoText + ")"

        self.form.undo.setText(undo)
        self.form.redo.setText(redo)

class Saver(QtCore.QThread):
    updateProgress = QtCore.Signal(bool, TableModel)

    def __init__(self, handler, currentTable, accessor, data, append):
        QtCore.QThread.__init__(self)
        self.handler = handler
        self.currentTable = currentTable
        self.accessor = accessor
        self.data = data
        self.append = append

    def run(self):
        if not self.accessor:
            self.accessor = self.currentTable.getAccessor()
        if not self.data:
            self.data = self.currentTable.getData()

        handler = None
        if self.accessor and self.data:
            if self.accessor.getConnectionType()==ConnectionType.csv:
                handler = self.handler["csvHandler"]
            elif self.accessor.getConnectionType()==ConnectionType.database:
                handler = self.handler["databaseHandler"]

            self.updateProgress.emit(False, self.currentTable)
            handler.setContent(self.accessor.getAccessString(), self.data, self.append)
            self.updateProgress.emit(True, self.currentTable)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())