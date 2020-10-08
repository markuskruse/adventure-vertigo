from PySide2.QtWidgets import QWidget


def widget_wrap(layout):
    widget = QWidget()
    widget.setLayout(layout)
    return widget