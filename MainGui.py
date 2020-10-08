from PySide2.QtWidgets import QSplitter, QTabWidget

from PagesGui import PagesGui


class MainGui(QSplitter):
    def __init__(self):
        QSplitter.__init__(self)

        self.setHandleWidth(10)

        pages_gui = PagesGui()
        self.addWidget(pages_gui)
        self.setStretchFactor(0, 0)

        editor_gui = QTabWidget()
        self.addWidget(editor_gui)
        self.setStretchFactor(1, 1)
