

import ranking_table
import stats_widget

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class ranking_panel():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)
        
        # table widget
        self.table = ranking_table.rankingtable(self.base_widget)

        # stats widget
        self.general_stats = stats_widget.statswidget(self.base_widget)

        #best-time button
        self.table_button = QPushButton("Ranking table", self.base_widget)

        #general stats button
        self.general_button = QPushButton("General stats", self.base_widget)

        #back button
        self.back_button = QPushButton("Back", self.base_widget)

        # ranking button listeners
        self.table_button.clicked.connect(self.show_table)
        self.general_button.clicked.connect(self.show_general_stats)


    
        self.setup()

    def setup(self):
        self.base_widget.move(0, 0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Ranking and stats")
        self.back_button.move(700, 550)
        self.back_button.resize(80, 30)

        # control buttons
        self.table_button.move(50, 20)
        self.table_button.resize(100, 30)

        self.general_button.move(170, 20)
        self.general_button.resize(100, 30)

        # hide this panel
        self.base_widget.hide()
        

    def show_general_stats(self):
        self.general_stats.base_widget.show()
        self.table.base_widget.hide()

        #update
        self.general_stats.update()
        
    def show_table(self):
        self.general_stats.base_widget.hide()
        self.table.base_widget.show()
        self.base_widget.show()

    def setVisible(self):
        self.base_widget.show()
    def setInvisible(self):
        self.base_widget.hide()
