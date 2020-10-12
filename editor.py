import json
import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, QWidget, QTableWidget, QHeaderView, \
    QHBoxLayout, QTableWidgetItem, QLineEdit, QVBoxLayout, QLabel
from PySide2.QtCore import Slot, Qt, QFile, QTextStream
import sys
from pubsub import pub

from AdventureModel import AdventureModel
from MainGui import MainGui
from MainWindow import MainWindow


if __name__ == "__main__":

    file = open("test.adv", 'r')
    json_model = json.load(file)
    model = AdventureModel(json_model)

    app = QApplication(sys.argv)

    # file = QFile("dark.qss")
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())

    main_gui = MainGui(model)

    window = MainWindow(main_gui)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())
