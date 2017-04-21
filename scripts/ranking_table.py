import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import pymysql

class rankingtable():
    def __init__(self, Widget):
        self.base_widget = QWidget(Widget)

        #table
        self.table = QTableWidget(self.base_widget)
        self.conn = pymysql.connect(user='root', password='',
                               host='localhost', database='reaction_game')
        self.a = self.conn.cursor()

        self.setup()
        self.show_best()

        self.base_widget.show()

    def setup(self):
        self.table.setRowCount(10)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(("Name", "Best time", "Average time"))

        self.table.move(50, 50)
        self.table.resize(700, 450)


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

        query = "SELECT * FROM ranking ORDER BY best_time ASC"

        self.fill_table(query)

    def show_average(self):
        query = "SELECT * FROM ranking ORDER BY avg_time ASC"

        self.fill_table(query)
