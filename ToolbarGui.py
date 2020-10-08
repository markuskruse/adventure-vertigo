from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class ToolbarGui(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.content = QHBoxLayout()
        self.content.setMargin(10)

        self.content.addWidget(QPushButton("New"))
        self.content.addWidget(QPushButton("Save as..."))
        self.content.addWidget(QPushButton("Export..."))