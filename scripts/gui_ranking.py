

from scripts import ranking_table

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class ranking_panel():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)
        # table widget
        self.table = ranking_table.rankingtable(self.base_widget)

        #best-time button
        self.best_time_button = QPushButton("Best-time", self.base_widget)
        
        #average-time button
        self.average_time_button = QPushButton("Average time", self.base_widget)

        #general stats button
        self.general_button = QPushButton("General stats", self.base_widget)

        #back button
        self.back_button = QPushButton("Back", self.base_widget)

        # ranking button listeners
        self.best_time_button.clicked.connect(self.table.show_best)
        self.average_time_button.clicked.connect(self.table.show_average)





        self.setup()

    def setup(self):
        self.base_widget.move(0, 0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Ranking and stats")

        # top-most portion setup
        # self.title_label.move(300, 10)
        # self.title_label.resize(200, 80)
        # self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        # reset button
        # self.reset_button.move(300, 80)
        # self.reset_button.resize(80, 30)
        # back button
        self.back_button.move(700, 550)
        self.back_button.resize(80, 30)

        # control buttons
        self.best_time_button.move(50, 20)
        self.best_time_button.resize(100, 30)

        self.average_time_button.move(180 , 20)
        self.average_time_button.resize(100, 30)

        self.general_button.move(310, 20)
        self.general_button.resize(100, 30)

        # hide this panel
        self.base_widget.hide()


    def setVisible(self):
        self.base_widget.show()
    def setInvisible(self):
        self.base_widget.hide()
