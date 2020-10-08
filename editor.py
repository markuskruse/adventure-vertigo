import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, QWidget, QTableWidget, QHeaderView, \
    QHBoxLayout, QTableWidgetItem, QLineEdit, QVBoxLayout, QLabel
from PySide2.QtCore import Slot, Qt


# Greetings
from MainGui import MainGui
from MainWindow import MainWindow


if __name__ == "__main__":

    #file = open("test.adv", 'r')
    #adventure_model = json.load(file)
    #binding = EditorBinding(adventure_model)

    app = QApplication(sys.argv)

    main_gui = MainGui()

    window = MainWindow(main_gui)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())
