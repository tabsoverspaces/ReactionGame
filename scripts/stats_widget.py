from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import db
import os

class statswidget():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        # labels
        self.unranked_matches_label = QLabel("", self.base_widget)
        self.ranked_matches_label = QLabel("", self.base_widget)
        self.tournaments_label = QLabel("", self.base_widget)

        self.setup()

    def setup(self):
        self.base_widget.move(50,50)
        self.base_widget.resize(500,450)

        self.unranked_matches_label.move(0, 30)
        self.ranked_matches_label.move(0, 80)
        self.tournaments_label.move(0,130)

        self.unranked_matches_label.resize(400, 30)
        self.ranked_matches_label.resize(400,30)
        self.tournaments_label.resize(400,30)

    def update(self):
        um = self.get_unranked()
        rm = self.get_ranked()
        t = self.get_tournaments()

        self.unranked_matches_label.setText("Unranked matches played : %d" % um)
        self.ranked_matches_label.setText("Ranked matches played : %d" % rm[0])
        self.tournaments_label.setText("Tournaments played : %d" % t[0])

        

    def get_unranked(self):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, '../data/unranked_matches_played.txt')

        file = open(filename, 'a+')
        file.seek(0)
        
        line = file.readline()
        number = int(line)

        file.close()

        return number
        

    def get_ranked(self):
        ranked = 0
        
        conn = db.connect_matches()
        cursor = conn.cursor()

        query = "SELECT COUNT(ID) FROM ranked_matches;"

        cursor.execute(query)

        ranked = cursor.fetchall()

        return ranked

    def get_tournaments(self):
        tournaments = 0

        conn = db.connect_matches()
        cursor = conn.cursor()

        query = "SELECT COUNT(ID) FROM tournaments;"

        cursor.execute(query)

        tournaments = cursor.fetchall()

        return tournaments
        

        
