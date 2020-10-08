from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QAction, QApplication


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Adventure")

        # Menu
        self.menu = self.menuBar()
        self.setCentralWidget(widget)

        self.file_menu = self.menu.addMenu("File")

        #new
        exit_action = QAction("New", self)
        exit_action.setShortcut("Ctrl+N")
        exit_action.triggered.connect(self.dummy)
        self.file_menu.addAction(exit_action)

        #new
        exit_action = QAction("Save as...", self)
        exit_action.setShortcut("Ctrl+Shift+S")
        exit_action.triggered.connect(self.dummy)
        self.file_menu.addAction(exit_action)

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

    @Slot()
    def exit_app(self):
        QApplication.quit()

    @Slot()
    def dummy(self, checked):
        print(self, checked)
