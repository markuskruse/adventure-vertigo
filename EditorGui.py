from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QTabWidget, QLabel, QVBoxLayout
from pubsub import pub

from EditorTab import EditorTab


class EditorGui(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self)

        self.setTabsClosable(True)

        welcome_tab = QWidget()
        welcome_layout = QVBoxLayout()
        welcome_tab.setLayout(welcome_layout)
        welcome_label = QLabel(text="<h1>Welcome to Adventure Vertigo</h1><p>This is the quick start page</p>")
        welcome_label.setAlignment(QtCore.Qt.AlignTop)
        welcome_layout.addWidget(welcome_label)
        self.addTab(welcome_label, "Quick start")

        pub.subscribe(self.model_update_event, "model_updated")

    def model_update_event(self):
        pass