import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import gui_bracket_widget
import names_prompt_tournament

class tournament:
    ###
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)
        
        self.bracket = gui_bracket_widget.bracket(self.base_widget)
        self.names_prompt = names_prompt_tournament.names_prompt(self.base_widget)

        self.names_prompt.start_tournament_button.clicked.connect(self.initialize_tournament)

        

        self.setup()

    def setup(self):
        self.base_widget.move(0,0)
        self.base_widget.resize(800, 600)
        self.base_widget.setWindowTitle("Main")

        self.bracket.base_widget.hide()
        self.names_prompt.base_widget.show()

        

        self.base_widget.hide()
    
    def setVisible(self):
        self.base_widget.show()
    def setInvisible(self):
        self.base_widget.hide()
    
    def show_panel(self):
        self.base_widget.show()
        self.names_prompt.base_widget.show()
        self.bracket.base_widget.hide()
        self.names_prompt.clear()

    def show_bracket(self):
        self.base_widget.show()
        self.names_prompt.base_widget.hide()
        self.bracket.base_widget.show()

    def initialize_tournament(self):
        self.names_prompt.create_players()

        self.tournament_mode = self.names_prompt.initialize_tournament()
        self.setup_bracket()
        
        self.bracket.next_match_button.clicked.connect(self.tournament_mode.play_next_match)

        self.bracket.base_widget.show()
        self.names_prompt.base_widget.hide()

    def setup_bracket(self):
        
        self.bracket.p1_name_label.setText(self.tournament_mode.quarterfinalsRoster[0].name)
        self.bracket.p2_name_label.setText(self.tournament_mode.quarterfinalsRoster[1].name)
        self.bracket.p3_name_label.setText(self.tournament_mode.quarterfinalsRoster[2].name)
        self.bracket.p4_name_label.setText(self.tournament_mode.quarterfinalsRoster[3].name)
        self.bracket.p5_name_label.setText(self.tournament_mode.quarterfinalsRoster[4].name)
        self.bracket.p6_name_label.setText(self.tournament_mode.quarterfinalsRoster[5].name)
        self.bracket.p7_name_label.setText(self.tournament_mode.quarterfinalsRoster[6].name)
        self.bracket.p8_name_label.setText(self.tournament_mode.quarterfinalsRoster[7].name)
        
        
