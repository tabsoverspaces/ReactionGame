import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import mysql.connector

class rankingtable():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        #table
        self.table = QTableWidget(self.base_widget)

        self.best = QPushButton("Best time", self.table)
        self.avg = QPushButton("Average time", self.table)

        self.best.clicked.connect(self.show_best)
        self.avg.clicked.connect(self.show_average)
        
        

        self.setup()
        self.show_best()

        self.base_widget.show()

    def setup(self):
        self.table.setRowCount(10)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(("Name", "Best time", "Average time"))

        self.table.move(50, 50)
        self.table.resize(500, 450)

        self.best.move(365, 80)
        self.best.resize(100,30)

        self.avg.move(365, 130)
        self.avg.resize(100,30)

        


    def fill_table(self, query):

        self.a.execute(query)

        self.table.setRowCount(0)
        self.table.setRowCount(10)

        self.table.setHorizontalHeaderLabels(("Name", "Best time", "Average time"))
        self.table.repaint()

        i = 0 ;

        for row in self.a:
            name = row[3]
            best = str(row[1])
            avg = str(row[2])

            self.table.setItem(i,0,QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(best))
            self.table.setItem(i, 2, QTableWidgetItem(avg))
            i+=1

    def show_best(self):

        self.update_connection()

        query = "SELECT * FROM ranking ORDER BY best_time ASC"

        self.fill_table(query)

    def show_average(self):
        self.update_connection()
        
        query = "SELECT * FROM ranking ORDER BY avg_time ASC"

        self.fill_table(query)


    def update_connection(self):
        self.conn = mysql.connector.connect(user='root', password='cT$82!sE',
                               host='localhost', database='reaction_game')
        self.a = self.conn.cursor()
