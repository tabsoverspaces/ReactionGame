import sys


from PyQt5 import QtCore, QtWidgets
import gui_ranked_match, gui_match, gui_tournament_main, gui_home, gui_ranking


# import gui_tournament
# import gui_rankings

import player
import match

class gui():
    def __init__(self, MainWindow):

        MainWindow.setObjectName("Main")
        MainWindow.resize(800,600)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central widget")
        MainWindow.setCentralWidget(self.central_widget)

        # home page
        self.home_gui = gui_home.home_page(self.central_widget)
        
        self.home_gui.unranked_match_btn.clicked.connect(self.start_new_match)
        self.home_gui.ranked_match_btn.clicked.connect(self.show_ranked_match)
        self.home_gui.tournament_btn.clicked.connect(self.show_tournament)
        self.home_gui.rankings_btn.clicked.connect(self.show_rankings)

        # unranked page
        # self.unranked_gui = gui_match.unranked_match(self.central_widget)

        #ranked page
        self.ranked_gui = gui_ranked_match.ranked_match(self.central_widget)

        #tournament page
        self.tournament_gui = gui_tournament_main.tournament(self.central_widget)

        #rankings page
        self.ranking_gui = gui_ranking.ranking_panel(self.central_widget)

        # button listeners
        #self.unranked_gui.quit_button.clicked.connect(self.show_home_gui)
        self.ranked_gui.quit_button.clicked.connect(self.show_home_gui)
        self.ranked_gui.cancel_button.clicked.connect(self.show_home_gui)
        self.tournament_gui.bracket.quit_tournament_button.clicked.connect(self.show_home_gui)
        self.tournament_gui.names_prompt.cancel_button.clicked.connect(self.show_home_gui)
        self.ranking_gui.back_button.clicked.connect(self.show_home_gui)

        # quit
        # self.quit_gui_main = quit_gui.home_page(self.central_widget)
        # self.quit_gui_main.quit_btn.clicked.connect(self.close_app)

        self.re_translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_new_match(self):
        p1 = player.Player("Dragan")
        p2 = player.Player("Natalija")

        match1 = match.match_class(p1,p2,0, self.central_widget)
        match1.setup_gui()
        
        match1.show_gui()
        self.home_gui.base_widget.hide()
        self.central_widget.repaint()
        
        match1.start()

        self.home_gui.base_widget.show()

    def re_translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Main", "Main"))


    def setup(self):
        self.central_widget.move(400, 200)
        self.central_widget.resize(800, 600)
        self.central_widget.setWindowTitle("Main")



        self.central_widget.show()
        self.a.exec_()

   

    def show_home_gui(self):
        self.home_gui.base_widget.show()
        #
        #self.unranked_gui.base_widget.hide()
        self.ranked_gui.base_widget.hide()
        self.tournament_gui.base_widget.hide()
        self.ranking_gui.base_widget.hide()

    def show_ranked_match(self):
        self.home_gui.base_widget.hide()
        #self.unranked_gui.base_widget.hide()
        #
        self.ranked_gui.reset()
        self.ranked_gui.base_widget.show()
        self.ranked_gui.show_names_prompt()
        #
        self.tournament_gui.base_widget.hide()
        self.ranking_gui.base_widget.hide()

    def show_tournament(self):
        self.home_gui.base_widget.hide()
        #self.unranked_gui.base_widget.hide()
        self.ranked_gui.base_widget.hide()
        #
        self.tournament_gui.show_panel()
        #
        self.ranking_gui.base_widget.hide()

    def show_rankings(self):
        self.home_gui.base_widget.hide()
        #self.unranked_gui.base_widget.hide()
        self.ranked_gui.base_widget.hide()
        self.tournament_gui.base_widget.hide()
        #
        self.ranking_gui.show_table()

    def close_app(self):
        self.home_gui.base_widget.hide()
        sys.exit(0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui(MainWindow)

    ui.home_gui.quit_btn.clicked.connect(app.quit)

    MainWindow.show()
    sys.exit(app.exec_())

main()

# OTHER CLASSES BELOW
