import sys

import gui_home
import gui_unranked_match
from PyQt5 import QtCore, QtWidgets

from scripts import gui_ranked_match


# import gui_tournament
# import gui_rankings


class gui():
    def __init__(self, MainWindow):

        MainWindow.setObjectName("Main")
        MainWindow.resize(800,600)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central widget")
        MainWindow.setCentralWidget(self.central_widget)

        # home page
        self.home_gui = gui_home.home_page(self.central_widget)
        self.home_gui.unranked_match_btn.clicked.connect(self.show_unranked_match)
        self.home_gui.ranked_match_btn.clicked.connect(self.show_ranked_match)

        # unranked page
        self.unranked_gui = gui_unranked_match.unranked_match(self.central_widget)
        self.unranked_gui.quit_button.clicked.connect(self.show_home_gui)

        #ranked page
        self.ranked_gui = gui_ranked_match.ranked_match(self.central_widget)
        self.ranked_gui.quit_button.clicked.connect(self.show_home_gui_ranked)

        #tournament page

        #rankings page


        # quit

        self.re_translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def re_translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Main", "Main"))


    def setup(self):
        self.central_widget.move(400, 200)
        self.central_widget.resize(800, 600)
        self.central_widget.setWindowTitle("Main")



        self.central_widget.show()
        self.a.exec_()

    def show_unranked_match(self):
        self.home_gui.base_widget.hide()
        self.unranked_gui.base_widget.show()
    def show_home_gui(self):
        self.home_gui.base_widget.show()
        self.unranked_gui.base_widget.hide()

    def show_ranked_match(self):
        self.home_gui.base_widget.hide()
        self.ranked_gui.base_widget.show()
    def show_home_gui_ranked(self):
        self.home_gui.base_widget.show()
        self.ranked_gui.base_widget.hide()



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

main()

# OTHER CLASSES BELOW
