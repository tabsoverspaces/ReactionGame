from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import player
import tournament

class names_prompt():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        self.p1name = QLineEdit(self.base_widget)
        self.p2name = QLineEdit(self.base_widget)
        self.p3name = QLineEdit(self.base_widget)
        self.p4name = QLineEdit(self.base_widget)
        self.p5name = QLineEdit(self.base_widget)
        self.p6name = QLineEdit(self.base_widget)
        self.p7name = QLineEdit(self.base_widget)
        self.p8name = QLineEdit(self.base_widget)

        self.p1label = QLabel(self.base_widget)
        self.p2label = QLabel(self.base_widget)
        self.p3label = QLabel(self.base_widget)
        self.p4label = QLabel(self.base_widget)
        self.p5label = QLabel(self.base_widget)
        self.p6label = QLabel(self.base_widget)
        self.p7label = QLabel(self.base_widget)
        self.p8label = QLabel(self.base_widget)

        self.start_tournament_button = QPushButton("Start tournament", self.base_widget)
        self.cancel_button = QPushButton("Cancel tournament", self.base_widget)
        self.clear_button = QPushButton("Clear", self.base_widget)


        self.setup()


    def setup(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800,600)

        self.setup_line_edits()
        self.setup_labels()

        self.start_tournament_button.move(450, 250)
        self.start_tournament_button.resize(200, 50)
        self.start_tournament_button.setEnabled(False)
        
        self.cancel_button.move(450, 300)
        self.cancel_button.resize(200,30)

        self.clear_button.move(475, 100)
        self.clear_button.resize(150,30)
        self.clear_button.clicked.connect(self.clear)

        

        self.base_widget.show()

    def setup_labels(self):
        self.labels_list = list()

        self.labels_list.append(self.p1label)
        self.labels_list.append(self.p2label)
        self.labels_list.append(self.p3label)
        self.labels_list.append(self.p4label)
        self.labels_list.append(self.p5label)
        self.labels_list.append(self.p6label)
        self.labels_list.append(self.p7label)
        self.labels_list.append(self.p8label)

        xloc = 30
        yinit = 20

        spacing = 40

        xlength = 200
        ylength = 30

        count=0
        for label in self.labels_list:
            label.resize(xlength,ylength)

            y = yinit + (count*(ylength + spacing))
            label.move(xloc, y)
            count+=1
            
            label.setText("Player %d name :" % count)
            
        
    
    def setup_line_edits(self):
        self.line_edit_list = list()

        self.line_edit_list.append(self.p1name)
        self.line_edit_list.append(self.p2name)
        self.line_edit_list.append(self.p3name)
        self.line_edit_list.append(self.p4name)
        self.line_edit_list.append(self.p5name)
        self.line_edit_list.append(self.p6name)
        self.line_edit_list.append(self.p7name)
        self.line_edit_list.append(self.p8name)

        self.p1name.textChanged.connect(self.checker)
        self.p2name.textChanged.connect(self.checker)
        self.p3name.textChanged.connect(self.checker)
        self.p4name.textChanged.connect(self.checker)
        self.p5name.textChanged.connect(self.checker)
        self.p6name.textChanged.connect(self.checker)
        self.p7name.textChanged.connect(self.checker)
        self.p8name.textChanged.connect(self.checker)

        xloc = 30
        yinit = 50

        spacing = 40

        xlength = 200
        ylength = 30

        count = 0
        for line_edit in self.line_edit_list:
            line_edit.resize(xlength, ylength)
            

            y = yinit + (count*(ylength + spacing))
            line_edit.move(xloc, y)
            count += 1

    def checker(self):
        if(self.p1name.text() == "" or
           self.p2name.text() == "" or
           self.p3name.text() == "" or
           self.p4name.text() == "" or
           self.p5name.text() == "" or
           self.p6name.text() == "" or
           self.p7name.text() == "" or
           self.p8name.text() == ""):
            self.start_tournament_button.setEnabled(False)
        else:
            self.start_tournament_button.setEnabled(True)

    def clear(self):
        self.p1name.setText("")
        self.p2name.setText("")
        self.p3name.setText("")
        self.p4name.setText("")
        self.p5name.setText("")
        self.p6name.setText("")
        self.p7name.setText("")
        self.p8name.setText("")

    def create_players(self):
        self.player_list = list()
        
        for label in self.line_edit_list:
            self.player_list.append(player.Player(label.text()))
        
    
    def initialize_tournament(self, bracket):
        tournament1 = tournament.Tournament(self.player_list, bracket)
        return tournament1
