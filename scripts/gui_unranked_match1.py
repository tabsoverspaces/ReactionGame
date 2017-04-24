from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class unranked_match():

    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        self.quit_enabled = True

        # player1 score labels
        self.p1r1 = QLabel(self.base_widget)
        self.p1r2 = QLabel(self.base_widget)
        self.p1r3 = QLabel(self.base_widget)
        self.p1r4 = QLabel(self.base_widget)
        self.p1r5 = QLabel(self.base_widget)

        

        # player2 score labels
        self.p2r1 = QLabel(self.base_widget)
        self.p2r2 = QLabel(self.base_widget)
        self.p2r3 = QLabel(self.base_widget)
        self.p2r4 = QLabel(self.base_widget)
        self.p2r5 = QLabel(self.base_widget)

        

        

        self.player1name = QLabel(self.base_widget)
        self.player2name = QLabel(self.base_widget)

        self.quit_button = QPushButton("Quit" , self.base_widget)

        self.setup()
        self.base_widget.hide()

    def setup(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800,600)

        self.quit_button.resize(80,30)
        self.quit_button.move(700, 550)

        self.player1name.move(50, 450)
        self.player1name.resize(250, 80)

        self.player2name.move(450 , 450)
        self.player2name.resize(250,80)

        self.player1name.setStyleSheet("font:20pt")
        self.player1name.setText("Player 1")

        self.player2name.setStyleSheet("font:20pt")
        self.player2name.setText("Player 2")


        
        if(self.quit_enabled == True):
            self.quit_button.setEnabled(True)
        else:
            self.quit_button.setEnabled(False)

        self.setup_labels()

    def setup_labels(self):
        # p1
        self.p1rounds = list()
        self.p1rounds.append(self.p1r1)
        self.p1rounds.append(self.p1r2)
        self.p1rounds.append(self.p1r3)
        self.p1rounds.append(self.p1r4)
        self.p1rounds.append(self.p1r5)

        # p2
        self.p2rounds = list()
        self.p2rounds.append(self.p2r1)
        self.p2rounds.append(self.p2r2)
        self.p2rounds.append(self.p2r3)
        self.p2rounds.append(self.p2r4)
        self.p2rounds.append(self.p2r5)


        xl = 30
        yl = 30

        ystart = 300

        p1x = 300
        p2x = 420

        spacing = 10

        count = 0
        for label in self.p1rounds:
            label.resize(xl,yl)

            y = ystart + (count*(spacing+yl))
            label.move(p1x, y)

            count+=1

            label.setStyleSheet("border: 1px solid black")

        count = 0
        for label in self.p2rounds:
            label.resize(xl,yl)

            y = ystart + (count* (spacing+yl))
            label.move(p2x, y)

            count+=1

            label.setStyleSheet("border: 1px solid black")

        
