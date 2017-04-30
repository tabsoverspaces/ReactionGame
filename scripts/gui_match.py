from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import os


class unranked_match():

    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        self.quit_enabled = True
        # image label
        self.image_label = QLabel(self.base_widget)
        # text field
        self.text_area = QTextEdit(self.base_widget)


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

        self.player1name.move(83, 450)
        self.player1name.resize(230, 70)

        self.player2name.move(485 , 450)
        self.player2name.resize(230,70)

        self.player1name.setStyleSheet("font:25pt")
        # self.player1name.setStyleSheet("border: 2px solid black")
        self.player1name.setText("Player 1")
        self.player1name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        

        self.player2name.setStyleSheet("font:25pt")
        self.player2name.setText("Player 2")
        # self.player2name.setStyleSheet("border: 2px solid black")
        self.player2name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # text area
        self.text_area.move(440, 30)
        self.text_area.resize(300,150)


        
        if(self.quit_enabled == True):
            self.quit_button.setEnabled(True)
        else:
            self.quit_button.setEnabled(False)

        self.setup_labels()

    def setup_labels(self):

        fileDir = os.path.dirname(os.path.realpath('__file__'))
        image_path = os.path.join(fileDir, '../data/images/match_background')
        image = QtGui.QPixmap(image_path)

        self.image_label.setPixmap(image)
        
        self.image_label.move(0,0)
        self.image_label.resize(800,600)
        self.image_label.show()
        
        
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

        # 'x' image label! - round marker
        image_path1 = os.path.join(fileDir, '../data/images/winroundcross')
        round_marker = QtGui.QPixmap(image_path1)

        # setup location coordinates
        xl = 35
        yl = 37

        ystart = 255

        p1x = 308
        p2x = 456

        spacing = 0

        count = 0
        for label in self.p1rounds:
            label.resize(xl,yl)

            y = ystart + (count*(spacing+yl))
            label.move(p1x, y)

            count+=1

            label.setStyleSheet("border: 1px solid black")
            
            label.setPixmap(round_marker)
            label.hide()

        count = 0
        for label in self.p2rounds:
            label.resize(xl,yl)

            y = ystart + (count* (spacing+yl))
            label.move(p2x, y)

            count+=1

            label.setStyleSheet("border: 1px solid black")
            
            label.setPixmap(round_marker)
            label.hide()
            

        
