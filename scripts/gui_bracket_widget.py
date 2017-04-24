from PyQt5 import QtCore, QtGui, QtWidgets
import tournament

class bracket():
    def __init__(self, Widget):
        self.base_widget = QtWidgets.QWidget(Widget)
        ## FRAMES ##
        
        # label_frames #
        self.QF1 = QtWidgets.QFrame(self.base_widget)
        self.QF2 = QtWidgets.QFrame(self.base_widget)
        self.QF3 = QtWidgets.QFrame(self.base_widget)
        self.QF4 = QtWidgets.QFrame(self.base_widget)
        
        self.SF1 = QtWidgets.QFrame(self.base_widget)
        self.SF2 = QtWidgets.QFrame(self.base_widget)
                
        self.F1 = QtWidgets.QFrame(self.base_widget)
        # label_frames_end #

        # line_frames #
        self.frame_QF1toSF1 = QtWidgets.QFrame(self.base_widget)
        self.frame_QF2toSF1 = QtWidgets.QFrame(self.base_widget)

        self.frame_QF3toSF2 = QtWidgets.QFrame(self.base_widget)
        self.frame_QF4toSF2 = QtWidgets.QFrame(self.base_widget)

        self.frame_SF1toF = QtWidgets.QFrame(self.base_widget)
        self.frame_SF2toF = QtWidgets.QFrame(self.base_widget)
        # line_frames_end
        
        ## FRAMES_END ##
        
        #
        
        ## BUTTONS ##
        self.quit_tournament_button = QtWidgets.QPushButton("Quit", self.base_widget)
        self.next_match_button = QtWidgets.QPushButton("Next match", self.base_widget)
        ### BUTTONS_END ###

        #
        
        ## LABELS ##
        self.p1_score_label = QtWidgets.QLabel(self.QF1)
        self.p1_name_label = QtWidgets.QLabel(self.QF1)
        self.p2_name_label = QtWidgets.QLabel(self.QF1)
        self.p2_score_label = QtWidgets.QLabel(self.QF1)
        
        self.p3_score_label = QtWidgets.QLabel(self.QF2)
        self.p3_name_label = QtWidgets.QLabel(self.QF2)
        self.p4_name_label = QtWidgets.QLabel("John", self.QF2)
        self.p4_score_label = QtWidgets.QLabel("P4 score", self.QF2)
        
        self.p5_score_label = QtWidgets.QLabel(self.QF3)
        self.p5_name_label = QtWidgets.QLabel(self.QF3)
        self.p6_name_label = QtWidgets.QLabel(self.QF3)
        self.p6_score_label = QtWidgets.QLabel(self.QF3)
        
        self.p7_score_label = QtWidgets.QLabel(self.QF4)
        self.p7_name_label = QtWidgets.QLabel(self.QF4)
        self.p8_name_label = QtWidgets.QLabel(self.QF4)
        self.p8_score_label = QtWidgets.QLabel(self.QF4)
        
        ###

        self.qf1_score_label = QtWidgets.QLabel(self.SF1)
        self.qf1_name_label = QtWidgets.QLabel(self.SF1)        
        self.qf2_name_label = QtWidgets.QLabel(self.SF1)
        self.qf2_score_label = QtWidgets.QLabel(self.SF1)
        

        self.qf3_score_label = QtWidgets.QLabel(self.SF2)
        self.qf3_name_label = QtWidgets.QLabel(self.SF2)
        self.qf4_name_label = QtWidgets.QLabel(self.SF2)
        self.qf4_score_label = QtWidgets.QLabel(self.SF2)

        ###
        
        self.sf1_score_label = QtWidgets.QLabel(self.F1)
        self.sf1_name_label = QtWidgets.QLabel(self.F1)
        self.sf2_name_label = QtWidgets.QLabel(self.F1)
        self.sf2_score_label = QtWidgets.QLabel(self.F1)

        ###
        
        self.champion_name_label = QtWidgets.QLabel(self.base_widget)
        self.champion_label = QtWidgets.QLabel(self.base_widget)

        ###
        
        self.playerlist = list()

        self.playerlist.append(self.p1_name_label)
        self.playerlist.append(self.p2_name_label)
        self.playerlist.append(self.p3_name_label)
        self.playerlist.append(self.p4_name_label)
        self.playerlist.append(self.p5_name_label)
        self.playerlist.append(self.p6_name_label)
        self.playerlist.append(self.p7_name_label)
        self.playerlist.append(self.p8_name_label)

        self.playerlist.append(self.p1_score_label)
        self.playerlist.append(self.p2_score_label)
        self.playerlist.append(self.p3_score_label)
        self.playerlist.append(self.p4_score_label)
        self.playerlist.append(self.p5_score_label)
        self.playerlist.append(self.p6_score_label)
        self.playerlist.append(self.p7_score_label)
        self.playerlist.append(self.p8_score_label)
        #
        self.playerlist.append(self.qf1_score_label)
        self.playerlist.append(self.qf2_score_label)
        self.playerlist.append(self.qf3_score_label)
        self.playerlist.append(self.qf4_score_label)

        self.playerlist.append(self.qf1_name_label)
        self.playerlist.append(self.qf2_name_label)
        self.playerlist.append(self.qf3_name_label)
        self.playerlist.append(self.qf4_name_label)
        #
        self.playerlist.append(self.sf1_name_label)
        self.playerlist.append(self.sf2_name_label)

        self.playerlist.append(self.sf1_score_label)
        self.playerlist.append(self.sf2_score_label)
        #
        ### LABELS_END ###
        #####

        ### LINES ###
        self.line = QtWidgets.QFrame(self.frame_QF1toSF1)
        self.line_2 = QtWidgets.QFrame(self.frame_QF3toSF2)
        self.line_3 = QtWidgets.QFrame(self.frame_QF1toSF1)
        self.line_6 = QtWidgets.QFrame(self.frame_QF1toSF1)
        self.line_7 = QtWidgets.QFrame(self.frame_QF3toSF2)
        self.line_8 = QtWidgets.QFrame(self.frame_QF3toSF2)
        self.line_9 = QtWidgets.QFrame(self.frame_QF4toSF2)
        self.line_10 = QtWidgets.QFrame(self.frame_QF4toSF2)
        self.line_11 = QtWidgets.QFrame(self.frame_QF4toSF2)
        self.line_12 = QtWidgets.QFrame(self.frame_QF2toSF1)
        self.line_13 = QtWidgets.QFrame(self.frame_QF2toSF1)
        self.line_14 = QtWidgets.QFrame(self.frame_QF2toSF1)
        self.line_15 = QtWidgets.QFrame(self.frame_SF2toF)
        self.line_16 = QtWidgets.QFrame(self.frame_SF2toF)
        self.line_17 = QtWidgets.QFrame(self.frame_SF2toF)
        self.line_18 = QtWidgets.QFrame(self.frame_SF1toF)
        self.line_19 = QtWidgets.QFrame(self.frame_SF1toF)
        self.line_20 = QtWidgets.QFrame(self.frame_SF1toF)
        
    
        ### LINES_END ###

        ### TOP_LABELS ###
        
        self.top_label = QtWidgets.QLabel(self.base_widget)
        self.qf_label = QtWidgets.QLabel(self.base_widget)
        self.sf_label = QtWidgets.QLabel(self.base_widget)
        self.f_label = QtWidgets.QLabel(self.base_widget)
        
        ### TOP_LABELS_END ###

        self.setupui()

        self.base_widget.show()

    def setupui(self):
        self.base_widget.move(0, 0)
        self.base_widget.resize(800 , 600)

        for label in self.playerlist:
            
            label.setAutoFillBackground(True)
            label.setFrameShape(QtWidgets.QFrame.Box)
            label.setFrameShadow(QtWidgets.QFrame.Sunken)

            label.setText("iii")

        self.quit_tournament_button.setGeometry(QtCore.QRect(675, 555, 101, 23))
        self.next_match_button.setGeometry(QtCore.QRect(570, 555, 101, 23))
        self.p4_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.p4_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.p3_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.p3_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.p2_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.p2_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.p1_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.p1_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.p6_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.p6_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.p5_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.p5_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.p8_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.p8_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.p7_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.p7_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.qf2_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.qf2_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.qf1_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.qf1_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.qf4_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.qf4_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.qf3_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.qf3_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        self.sf2_name_label.setGeometry(QtCore.QRect(0, 31, 125, 31))
        self.sf2_score_label.setGeometry(QtCore.QRect(124, 31, 47, 31))
        self.sf1_score_label.setGeometry(QtCore.QRect(124, 0, 47, 31))
        self.sf1_name_label.setGeometry(QtCore.QRect(0, 0, 125, 31))
        
        self.champion_name_label.setGeometry(QtCore.QRect(0, 30, 170, 31))
        self.champion_label.setGeometry(QtCore.QRect(0, 0, 170, 31))

        self.setup_frames()
        self.setup_lines()
        self.setup_top_label()



    def setup_top_label(self):
        self.top_label.setGeometry(QtCore.QRect(9, 4, 762, 33))
        self.top_label.setAutoFillBackground(True)
        self.top_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_label.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.qf_label.setGeometry(QtCore.QRect(10,5,270,31))
        self.sf_label.setGeometry(QtCore.QRect(270,5,270,31))
        self.f_label.setGeometry(QtCore.QRect(525,5,270,31))

        self.qf_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sf_label.setAlignment(QtCore.Qt.AlignCenter)
        self.f_label.setAlignment(QtCore.Qt.AlignCenter) 

        self.qf_label.setText("Quarter-finals")
        self.sf_label.setText("Semi-finals")
        self.f_label.setText("Final")
        
    def setup_frames(self):
        self.QF1.setGeometry(QtCore.QRect(60, 60, 170, 62))
        self.QF2.setGeometry(QtCore.QRect(60, 181, 170, 62))
        self.QF3.setGeometry(QtCore.QRect(60, 301, 170, 62))
        self.QF4.setGeometry(QtCore.QRect(60, 421, 170, 62))

        self.SF1.setGeometry(QtCore.QRect(331, 120, 170, 62))
        self.SF2.setGeometry(QtCore.QRect(331, 360, 170, 62))

        self.F1.setGeometry(QtCore.QRect(581, 240, 170, 62))

        self.frame_QF1toSF1.setGeometry(QtCore.QRect(230, 70, 101, 81))
        self.frame_QF2toSF1.setGeometry(QtCore.QRect(230, 147, 101, 81))

        self.frame_QF3toSF2.setGeometry(QtCore.QRect(230, 310, 101, 81))
        self.frame_QF4toSF2.setGeometry(QtCore.QRect(230, 387, 101, 81))

        self.frame_SF1toF.setGeometry(QtCore.QRect(501, 132, 81, 136)) 
        self.frame_SF2toF.setGeometry(QtCore.QRect(501, 266, 81, 136))    

    def setup_lines(self):
        self.line.setGeometry(QtCore.QRect(0, 13, 51, 16))
        self.line_3.setGeometry(QtCore.QRect(50, 20, 3, 46))
        self.line_6.setGeometry(QtCore.QRect(51, 56, 52, 20))
        self.line_2.setGeometry(QtCore.QRect(0, 13, 51, 16))
        self.line_7.setGeometry(QtCore.QRect(50, 20, 3, 46))
        self.line_8.setGeometry(QtCore.QRect(51, 56, 52, 20))
        self.line_9.setGeometry(QtCore.QRect(0, 56, 51, 16))
        self.line_10.setGeometry(QtCore.QRect(50, 19, 3, 46))
        self.line_11.setGeometry(QtCore.QRect(51, 10, 52, 20))
        self.line_12.setGeometry(QtCore.QRect(0, 56, 51, 16))
        self.line_13.setGeometry(QtCore.QRect(50, 19, 3, 46))
        self.line_14.setGeometry(QtCore.QRect(51, 10, 52, 20))
        self.line_15.setGeometry(QtCore.QRect(0, 117, 51, 16))
        self.line_16.setGeometry(QtCore.QRect(50, 19, 3, 107))
        self.line_17.setGeometry(QtCore.QRect(51, 10, 33, 20))
        self.line_18.setGeometry(QtCore.QRect(0, 11, 51, 16))
        self.line_19.setGeometry(QtCore.QRect(50, 18, 3, 109))
        self.line_20.setGeometry(QtCore.QRect(51, 116, 33, 20))
        

        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)

        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)

        
    
        
