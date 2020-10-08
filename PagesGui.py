from PySide2.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListView

from gui_util import widget_wrap


class PagesGui(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        area_filter_layout = QHBoxLayout()
        area_filter_layout.setMargin(5)
        area_filter_layout.addWidget(QLabel("Filter on area"))
        area_filter_layout.addWidget(QLineEdit("Some area..."))
        area_filter_clear_button = QPushButton("X")
        area_filter_clear_button.setMaximumWidth(30)
        area_filter_layout.addWidget(area_filter_clear_button)
        layout.addWidget(widget_wrap(area_filter_layout))

        title_search = QHBoxLayout()
        title_search.setMargin(5)
        title_search.addWidget(QLabel("Search for titles"))
        title_search.addWidget(QLineEdit("Some title..."))
        title_search_clear_button = QPushButton("X")
        title_search_clear_button.setMaximumWidth(30)
        title_search.addWidget(title_search_clear_button)
        layout.addWidget(widget_wrap(title_search))

        body_search = QHBoxLayout()
        body_search.setMargin(5)
        body_search.addWidget(QLabel("Search in bodies"))
        body_search.addWidget(QLineEdit("Some text..."))
        body_search_clear_button = QPushButton("X")
        body_search_clear_button.setMaximumWidth(30)
        body_search.addWidget(body_search_clear_button)
        layout.addWidget(widget_wrap(body_search))

        layout.addWidget(QListView())
