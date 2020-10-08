from PySide2 import QtCore
from PySide2.QtCore import QObject, Slot

from PagesListModel import PagesListModel


class EditorBinding(QObject):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.pagesListModel = PagesListModel(self.model["pages"])

    @QtCore.Property(QtCore.QObject, constant=True)
    def pages(self):
        return self.pagesListModel

    @Slot(None)
    def addPage(self):
        page = {
            "label": "Unnamed",
            "text": "Empty",
            "choices": []
        }
        self.pagesListModel.appendRow(page)

    @Slot(None)
    def removePage(self):
        print("Remove page")
