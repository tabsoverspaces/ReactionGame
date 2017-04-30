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

        self.tournament_mode = self.names_prompt.initialize_tournament(self.bracket)
        self.setup_bracket()
        
        self.bracket.next_match_button.clicked.connect(self.tournament_mode.play_next_match)
        self.bracket.next_match_button.clicked.connect(self.update_bracket)

        self.bracket.base_widget.show()
        self.names_prompt.base_widget.hide()

    def setup_bracket(self):

        i = 0
        for label in self.bracket.players_labels:
            label.setText(self.tournament_mode.quarterfinalsRoster[i].name)
            i+=1

            
        
    def update_bracket(self):
        # update quarterfinals
        i = 0
        while(i<self.tournament_mode.qf_played):
            self.bracket.qf_winners[i].setText(self.tournament_mode.semifinalsRoster[i].name)

            
            self.bracket.players_scores[2*i].setText(str(self.tournament_mode.qf_match_scores[2*i]))
            self.bracket.players_scores[(2*i)+1].setText(str(self.tournament_mode.qf_match_scores[(2*i)+1]))
            
            i+=1
            
        # update semifinals
        i= 0
        while(i<self.tournament_mode.sf_played):
            self.bracket.sf_winners[i].setText(self.tournament_mode.finalRoster[i].name)

            self.bracket.qf_scores[2*i].setText(str(self.tournament_mode.sf_match_scores[2*i]))
            self.bracket.qf_scores[(2*i)+1].setText(str(self.tournament_mode.sf_match_scores[(2*i)+1]))
            
            i+=1
            
        i = 0
        while(i<self.tournament_mode.f_played):
            self.bracket.sf_scores[2*i].setText(str(self.tournament_mode.f_match_scores[2*i]))
            self.bracket.sf_scores[(2*i)+1].setText(str(self.tournament_mode.f_match_scores[(2*i)+1]))

            i+=1
