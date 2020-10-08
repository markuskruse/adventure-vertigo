from PySide2 import QtCore
from PySide2.QtCore import QAbstractListModel


class PagesListModel(QAbstractListModel):
    LabelRole = QtCore.Qt.UserRole + 1000

    def __init__(self, pages, parent=None):
        super(PagesListModel, self).__init__(parent)
        self._pages = pages

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._pages)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._pages[index.row()]
            if role == PagesListModel.LabelRole:
                return item["label"]

    def roleNames(self):
        roles = dict()
        roles[PagesListModel.LabelRole] = b"label"
        return roles

    def appendRow(self, page):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._pages.append(page)
        self.endInsertRows()
