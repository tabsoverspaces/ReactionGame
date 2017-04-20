import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class ranked_match():

    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        # top-most portion of the frame
        self.title_label = QLabel("Ranked match", self.base_widget)
        self.reset_button = QPushButton("Reset game", self.base_widget)
        self.quit_button = QPushButton("Quit game", self.base_widget)

        # player1 elements
        self.name_label_1 = QLabel("Player 1", self.base_widget)
        self.rounds_player1 = list()

        # player2 elements
        self.name_label_2 = QLabel("Player 2" , self.base_widget)
        self.rounds_player2 = list()

        # fill both player's lists with QLabels
        for x in range(0,5):
            self.rounds_player1.append(QLabel(self.base_widget))
            self.rounds_player2.append(QLabel(self.base_widget))

        # rounds elements
        self.rounds_text = QLabel("Rounds ", self.base_widget)
        self.rounds_list = list()
        for x in range(0,5):
            label = QLabel(self.base_widget)
            label.setText("1")
            self.rounds_list.append(label)

        # notificcation text box
        self.textbox = QTextEdit(self.base_widget)

        self.setup()

    def setup(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Ranked match")

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


    def setVisible(self):
        self.base_widget.show()
    def setInvisible(self):
        self.base_widget.hide()
