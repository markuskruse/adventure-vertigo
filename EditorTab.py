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
        self.label_line_edit.editingFinished.connect(self.edit_label)
        layout.addWidget(self.label_line_edit, 0, 1)
        self.label_line_edit.setText(self.page_model["label"])
        layout.addWidget(QLabel("Used only for your organization and linking between pages"), 0, 2)

        layout.addWidget(QLabel("Area"), 1, 0)
        self.area_line_edit = QLineEdit()
        self.area_line_edit.editingFinished.connect(self.edit_area)
        layout.addWidget(self.area_line_edit, 1, 1)
        self.area_line_edit.setText(self.page_model["area"])
        layout.addWidget(QLabel("Used only for you to organize and group pages"), 1, 2)

        text_label = QLabel("Text")
        text_label.setAlignment(QtCore.Qt.AlignTop)
        layout.addWidget(text_label, 2, 0)
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.edit_text)
        layout.addWidget(self.text_edit, 2, 1, 1, 2)
        self.text_edit.setText(self.page_model["text"])

        layout.addWidget(QLabel("State changes"), 3, 0)
        layout.addWidget(QLineEdit("", placeholderText="Variable to set"), 3, 1)
        layout.addWidget(QLineEdit("", placeholderText="Value to set"), 3, 2)

        layout.addWidget(QLabel("State changes"), 4, 0)
        layout.addWidget(QLineEdit("", placeholderText="Variable to set"), 4, 1)
        layout.addWidget(QLineEdit("", placeholderText="Value to set"), 4, 2)

        layout.addWidget(QLabel("State changes"), 5, 0)
        layout.addWidget(QLineEdit("", placeholderText="Variable to set"), 5, 1)
        layout.addWidget(QLineEdit("", placeholderText="Value to set"), 5, 2)

    def get_tab_name(self):
        return self.page_model["label"]

    @Slot()
    def edit_label(self):
        if not self.page_model["label"] == self.label_line_edit.text():
            self.page_model["label"] = self.label_line_edit.text()
            pub.sendMessage("model_updated", arg1={"page": self.page_model, "type": "label"})

    @Slot()
    def edit_area(self):
        if not self.page_model["area"] == self.area_line_edit.text():
            self.page_model["area"] = self.area_line_edit.text()
            pub.sendMessage("model_updated", arg1={"page": self.page_model, "type": "area"})

    @Slot()
    def edit_text(self):
        if not self.page_model["text"] == self.text_edit.document():
            self.page_model["text"] = self.text_edit.document().toRawText()
            pub.sendMessage("model_updated", arg1={"page": self.page_model, "type": "text"})
