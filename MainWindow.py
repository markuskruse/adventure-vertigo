import json

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QAction, QApplication

from AdventureModel import AdventureModel


class MainWindow(QMainWindow):
    def __init__(self, widget, model: AdventureModel):
        QMainWindow.__init__(self)
        self.setWindowTitle("Adventure")

        self.model = model

        # Menu
        self.menu = self.menuBar()
        self.setCentralWidget(widget)

        self.file_menu = self.menu.addMenu("File")

        #new
        action = QAction("New", self)
        action.setShortcut("Ctrl+N")
        action.triggered.connect(self.dummy)
        self.file_menu.addAction(action)

        #Save
        action = QAction("Save", self)
        action.setShortcut("Ctrl+S")
        action.triggered.connect(self.save)
        self.file_menu.addAction(action)

        #Save as
        action = QAction("Save as...", self)
        action.setShortcut("Ctrl+Shift+S")
        action.triggered.connect(self.dummy)
        self.file_menu.addAction(action)

        # Exit QAction
        action = QAction("Exit", self)
        action.setShortcut("Ctrl+Q")
        action.triggered.connect(self.exit_app)
        self.file_menu.addAction(action)

    @Slot()
    def exit_app(self):
        QApplication.quit()

    @Slot()
    def dummy(self, checked):
        print(self, checked)

    @Slot()
    def save(self):
        with open('testout.json', 'w') as outfile:
            json.dump(self.model.data(), outfile)
