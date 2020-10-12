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

        self.page_list_view = QListView()
        self.page_list_view.setModel(model.pages())
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
        page_name = self.model.lookup_page(index).text()
        page = self.model.find_page(page_name)
        self.gui.open_page(page)

    @Slot()
    def search(self):
        query = {"area": self.area_search_edit.text(),
         "label": self.label_search_edit.text(),
         "text":self.search_edit.text()}
        pub.sendMessage("page_search_event", arg1=query)
