from PySide2 import QtCore
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QTabWidget
from pubsub import pub


class EditorTab(QWidget):
    def __init__(self, page_model, tab_widget: QTabWidget):
        QWidget.__init__(self)

        self.tab_widget = tab_widget

        self.page_model = page_model
        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Label"), 0, 0)
        self.label_line_edit = QLineEdit()
        self.label_line_edit.textChanged.connect(self.edit_label)
        layout.addWidget(self.label_line_edit, 0, 1)
        self.label_line_edit.setText(self.page_model["label"])

        layout.addWidget(QLabel("Area"), 1, 0)
        self.area_line_edit = QLineEdit()
        self.area_line_edit.textChanged.connect(self.edit_area)
        layout.addWidget(self.area_line_edit, 1, 1)
        self.area_line_edit.setText(self.page_model["area"])

        text_label = QLabel("Text")
        text_label.setAlignment(QtCore.Qt.AlignTop)
        layout.addWidget(text_label, 2, 0)
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.edit_text)
        layout.addWidget(self.text_edit, 2, 1)
        self.text_edit.setText(self.page_model["text"])

    def get_tab_name(self):
        return self.page_model["label"]

    @Slot()
    def edit_label(self):
        self.page_model["label"] = self.label_line_edit.text()
        pub.sendMessage("model_updated")

    @Slot()
    def edit_area(self):
        self.page_model["area"] = self.area_line_edit.text()
        pub.sendMessage("model_updated")

    @Slot()
    def edit_text(self):
        self.page_model["text"] = self.text_edit.document()
        pub.sendMessage("model_updated")
