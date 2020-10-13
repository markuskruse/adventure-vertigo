from PySide2.QtCore import Slot
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListView, \
    QAbstractItemView
from pubsub import pub

from AdventureModel import AdventureModel


class PagesGui(QWidget):
    def __init__(self, model: AdventureModel, gui):
        QWidget.__init__(self)

        self.gui = gui
        self.model = model

        layout = QVBoxLayout()
        self.setLayout(layout)

        area_filter_layout = QHBoxLayout()
        area_filter_layout.setMargin(5)
        area_filter_layout.addWidget(QLabel("Area search"))
        self.area_search_edit = QLineEdit(placeholderText="Some area...", clearButtonEnabled=True)
        area_filter_layout.addWidget(self.area_search_edit)
        self.area_search_edit.textEdited.connect(self.search)
        layout.addLayout(area_filter_layout)

        label_search = QHBoxLayout()
        label_search.setMargin(5)
        label_search.addWidget(QLabel("Label search"))
        self.label_search_edit = QLineEdit(placeholderText="Some label...", clearButtonEnabled=True)
        label_search.addWidget(self.label_search_edit)
        self.label_search_edit.textEdited.connect(self.search)
        layout.addLayout(label_search)

        body_search = QHBoxLayout()
        body_search.setMargin(5)
        body_search.addWidget(QLabel("Search all"))
        self.search_edit = QLineEdit(placeholderText="Some text...", clearButtonEnabled=True)
        body_search.addWidget(self.search_edit)
        self.search_edit.textEdited.connect(self.search)
        layout.addLayout(body_search)

        add_page_button = QPushButton("Add page")
        layout.addWidget(add_page_button)
        add_page_button.clicked.connect(self.add_page)

        self.page_list_model = QStandardItemModel()
        for page in self.model.pages():
            item = QStandardItem(page["area"] + ": " + page["label"])
            self.page_list_model.appendRow(item)

        self.page_list_view = QListView()
        self.page_list_view.setModel(self.page_list_model)
        self.page_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        layout.addWidget(self.page_list_view)
        self.page_list_view.clicked.connect(self.open_page)

    @Slot()
    def add_page(self):
        page = self.model.add_page()
        self.gui.open_page(page)
        self.search()

    @Slot()
    def open_page(self):
        index = self.page_list_view.currentIndex()
        page_name = self.lookup_page(index).text()
        page = self.model.find_page(page_name)
        self.gui.open_page(page)

    @Slot()
    def search(self):
        self.rebuild_page_list()

    def lookup_page(self, index: int):
        return self.page_list_model.itemFromIndex(index)

    def rebuild_page_list(self):
        self.page_list_model.clear()
        print(self.model.pages()[0]["area"])
        print(self.area_search_edit.text() in self.model.pages()[0]["area"])
        for page in self.model.pages():
            if (not self.area_search_edit.text() or self.area_search_edit.text() in page["area"]) \
                    and (not self.label_search_edit.text() or self.label_search_edit.text() in page["label"])\
                    and (not self.search_edit.text() or self.search_edit.text() in page["text"]):
                item = QStandardItem(page["area"] + ": " + page["label"])
                self.page_list_model.appendRow(item)
            else:
                print(page)

    def model_update_event(self, arg1):
        self.rebuild_page_list()
