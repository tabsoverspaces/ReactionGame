import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class tournament:
    ###
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        # self.init_list = [self.base_widget, self.p1 , self.p2, self.p3 , self.p4 , self.p5, self.p6, self.p7, self.p8]
        # self. = QLabel()
        self.tournament_btn = QPushButton("Tournament", self.base_widget)
        self.rankings_btn = QPushButton("Rankings and stats", self.base_widget)
        self.quit_btn = QPushButton("Quit Tournament", self.base_widget)


        #add buttons to a list
        self.list_buttons = [self.tournament_btn, self.rankings_btn, self.quit_btn]

        # self.unranked_match_btn.clicked.connect(self.setInvisible)


        self.setup()

    def setup(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Main")

        #setup up buttons location
        self.set_buttons_location()

        self.base_widget.hide()
    # geo position the buttons
    def set_buttons_location(self):
        # x location FIXED
        xc = 50

        # y location initial
        init_yc = 150
        # button spacing
        spacing = 5
        counter = 0

        #size of buttons
        xl = 200
        yl = 50

        for x in self.list_buttons:
            x.resize(xl, yl)

            # location
            x.move(xc, init_yc + (counter*(spacing+yl)))
            counter += 1

    def setVisible(self):
        self.base_widget.show()
    def setInvisible(self):
        self.base_widget.hide()
    
