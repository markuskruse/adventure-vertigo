from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel


class StatusBar(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setMaximumHeight(30)

        layout = QHBoxLayout()
        layout.setMargin(5)
        self.setLayout(layout)

        layout.addWidget(QLabel("Left"))
        layout.addStretch(1)
        layout.addWidget(QLabel("Center"))
        layout.addStretch(1)
        layout.addWidget(QLabel("Right"))