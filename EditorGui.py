from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QTabWidget, QLabel, QVBoxLayout
from pubsub import pub


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

    def model_update_event(self, arg1):
        for index in range(0, self.count()):
            page_tab = self.widget(index)
            # ignore the welcome tab
            function = getattr(page_tab, "get_tab_name", None)
            if callable(function):
                name = page_tab.get_tab_name()
                self.setTabText(index, name)