import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

#import match
import player

import imp


class ranked_match():

    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        self.names_prompt = QWidget(self.base_widget)
        self.base_widget_match = QWidget(self.base_widget)

        # top-most portion of the frame
        self.title_label = QLabel("Ranked match", self.base_widget_match)
        self.reset_button = QPushButton("Reset game", self.base_widget_match)
        self.quit_button = QPushButton("Quit game", self.base_widget_match)

        # player1 elements
        self.name_label_1 = QLabel("Player 1", self.base_widget_match)
        self.rounds_player1 = list()

        # player2 elements
        self.name_label_2 = QLabel("Player 2" , self.base_widget_match)
        self.rounds_player2 = list()

        # fill both player's lists with QLabels
        for x in range(0,5):
            self.rounds_player1.append(QLabel(self.base_widget_match))
            self.rounds_player2.append(QLabel(self.base_widget_match))

        # rounds elements
        self.rounds_text = QLabel("Rounds ", self.base_widget_match)
        self.rounds_list = list()
        for x in range(0,5):
            label = QLabel(self.base_widget_match)
            label.setText("1")
            self.rounds_list.append(label)

        # notification text box
        self.textbox = QTextEdit(self.base_widget_match)

        # NAMES PROMPT PANEL
        self.title_label = QLabel("Enter players' names :", self.names_prompt)
        
        self.player1name = QLineEdit(self.names_prompt)
        self.player2name = QLineEdit(self.names_prompt)

        self.start_match = QPushButton("Start match", self.names_prompt)
        self.cancel_button = QPushButton("Cancel" , self.names_prompt)
        self.clear_button = QPushButton("Clear" , self.names_prompt)
        self.check_button = QPushButton("Check", self.names_prompt)


        # setup
        self.setup_match()
        self.setup_names_prompt()

    def setup_match(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Ranked match")

        self.base_widget_match.move(0,0)
        self.base_widget_match.resize(800,600)

        self.names_prompt.move(0,0)
        self.names_prompt.resize(800,600)

        # top-most portion setup
        self.title_label.move(300, 10)
        self.title_label.resize(200, 80)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        # reset button
        self.reset_button.move(300, 80)
        self.reset_button.resize(80,30)
        # quit button
        self.quit_button.move(420 , 80)
        self.quit_button.resize(80,30)

        # rounds setup
        self.rounds_text.move(200, 200)
        # player1 setup
        self.name_label_1.move(50, 50)
        self.name_label_2.move(700, 50)
        # notification textbox
        self.textbox.move(300, 380)
        self.textbox.resize(200, 200)

        # hide this panel
        self.base_widget.hide()

        #setup up buttons location
    # geo position the buttons

    # rounds LED pointers positioning
        self.move_rounds_led_labels()


    def move_rounds_led_labels(self):
        spacing = 25
        initial = 300
        counter = 0

        length = 20
        width = 20

        yc = 340

        for x in self.rounds_list:
            x.resize(length,width)
            x.move(initial + (counter*(length + spacing)), yc)
            x.setAlignment(QtCore.Qt.AlignCenter)

            print("yo rounds led position and size")

            x.setText("1")
            x.setBackgroundRole(QtGui.QPalette.Dark)
            x.setAutoFillBackground(True)
            counter += 1


    def setup_names_prompt(self):
        self.title_label.move(250, 20)
        self.title_label.resize(300, 50)

        self.player1name.move(50, 200)
        self.player2name.move(50, 350)

        self.player1name.resize(200,50)
        self.player2name.resize(200,50)

        self.start_match.move(500, 275)
        self.check_button.move(525, 240)
        self.cancel_button.move(600, 500)
        self.clear_button.move(500, 500)

        self.start_match.resize(180, 50)
        self.check_button.resize(130,30)
        self.cancel_button.resize(80,30)
        self.clear_button.resize(80,30)

        self.check_button.clicked.connect(self.check_names)
        self.clear_button.clicked.connect(self.clear)

        self.start_match.setEnabled(False)
        self.start_match.clicked.connect(self.start_ranked_match)

    def show_names_prompt(self):
        self.names_prompt.show()
        self.base_widget_match.hide()

    def show_match(self):
        self.names_prompt.hide()
        self.base_widget_match.show()

    def clear(self):
        self.player1name.setText("")
        self.player2name.setText("")

        
    def reset(self):
        self.clear()

    def check_names(self):
        if(self.player1name.text() == "" or self.player2name.text() == ""):
            self.start_match.setEnabled(False)
        else:
            self.start_match.setEnabled(True)

    def start_ranked_match(self):
        import match
        
        player1 = player.Player(self.player1name.text())
        player2 = player.Player(self.player2name.text())

        new_match = match.match_class(player1, player2, 1)

        obj = new_match.start()
        print(obj.winner.name)
        

        
        
