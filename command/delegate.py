from PySide.QtGui import QStyledItemDelegate, QUndoStack, QTextEdit, QLineEdit
from command.command import EditCommand


class ItemDelegate(QStyledItemDelegate):

    def __init__(self, undoStack, editedFunction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.undoStack = undoStack
        self.editedFunction = editedFunction
        self.edit = None

    def setModelData(self, editor, model, index):
        newValue = editor.text()
        self.edit.newValue(newValue)
        self.undoStack.beginMacro("Edited table")
        self.undoStack.push(self.edit)
        self.undoStack.endMacro()
        self.editedFunction()

    def editorEvent(self, event, model, option, index):
        self.edit = EditCommand(model, index)

    def createEditor(self, parent, option, index):
        return QLineEdit(parent)

