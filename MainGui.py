from PySide2.QtWidgets import QSplitter, QTabWidget, QVBoxLayout, QWidget

from EditorGui import EditorGui
from EditorTab import EditorTab
from PagesGui import PagesGui
from StatusBar import StatusBar


class MainGui(QWidget):
    def __init__(self, model):
        QWidget.__init__(self)

        self.model = model
        layout = QVBoxLayout()
        layout.setMargin(5)
        self.setLayout(layout)

        splitter = QSplitter()
        layout.addWidget(splitter)

        splitter.setHandleWidth(10)

        self.pages_gui = PagesGui(model, self)
        splitter.addWidget(self.pages_gui)
        splitter.setStretchFactor(0, 0)

        self.editor_gui = EditorGui()
        splitter.addWidget(self.editor_gui)
        splitter.setStretchFactor(1, 1)

        layout.addWidget(StatusBar())

        self.open_pages = ["welcome"]

    def open_page(self, page):
        if page:
            if not page in self.open_pages:
                self.editor_gui.addTab(EditorTab(page, self.editor_gui), page["label"])
                self.open_pages.append(page)
            index = self.open_pages.index(page)
            self.editor_gui.setCurrentIndex(index)