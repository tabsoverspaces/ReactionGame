# project file imports
import random
import threading
import time

import RPi.GPIO as GPIO
import player
# python module imports
import pygame



import db

class gpio_object():
    
    def __init__(self):
        # PIN_SETUP_START
        # DO NOT CHANGE ANY OF THE CODE UNTIL "PIN_SETUP_END"
        
        # number of rounds to be played
        self.numberofrounds = 5  # SHOULD NOT BE CHANGED! BREADBOARD LAYOUT DESIGNED FOR 5 ROUNDS

        
        
        self.readylight = 23

        # player1 score LEDs
        self.p11 = 21
        self.p12 = 20
        self.p13 = 16

        # player2 score LEDs
        self.p21 = 25
        self.p22 = 22
        self.p23 = 27

        # players' score LED lists
        self.player1 = [self.p11, self.p12, self.p13]
        self.player2 = [self.p21, self.p22, self.p23]

        # round LEDs
        self.r1 = 26
        self.r2 = 19
        self.r3 = 13
        self.r4 = 6
        self.r5 = 5

        # round LED list
        self.rounds = [self.r1, self.r2, self.r3, self.r4, self.r5]

        # player1 button pin
        self.p1button = 24
        # player2 button pin
        self.p2button = 18

        # reset button pin
        self.resetbutton = 12

    def setup(self):

        # set RPI pin layout to BCM
        GPIO.setmode(GPIO.BCM)
        # disable RPI warnings
        GPIO.setwarnings(0)

        # setup yellow ready light
        GPIO.setup(self.readylight, GPIO.OUT)

        # setup input pins(buttons)
        GPIO.setup(self.resetbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.p1button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.p2button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # setup output pins(LEDs)
        for a in self.player1:
            GPIO.setup(a, GPIO.OUT)
        for a in self.player2:
            GPIO.setup(a, GPIO.OUT)
        for a in self.rounds:
            GPIO.setup(a, GPIO.OUT)

        # PIN_SETUP_END ###############################
        ###############################################


        
#####################
## MAIN MATCH CLASS ##
#####################
class match_class:
    ###
    def __init__(self, player1, player2,
                 ranked):  # constructor . Needs to be modified so that it takes two paramters, Player1 name and Player2 name which will be entered prior to the start of the game
        self.p1 = player1
        self.p2 = player2

        self.roundflag = False
        self.thread = dnf_thread(self)  # create instance of class dnf_thread

        self.roundsPlayed = 0;

        self.ranked = ranked

        self.gpio = gpio_object()
        self.gpio.setup()

    ################
    ## RESET GAME ##
    ################
    # sets all values to default/0
    def resetgame(self):

        self.roundsPlayed = 0;
        self.p1.reset();
        self.p2.reset();

        for a in self.gpio.player1:
            GPIO.output(a, GPIO.LOW)
        for a in self.gpio.player2:
            GPIO.output(a, GPIO.LOW)
        for a in self.gpio.rounds:
            GPIO.output(a, GPIO.LOW)

        GPIO.output(self.gpio.readylight, GPIO.LOW)

    


    #################
    ## START ROUND ##
    #################
    def roundstart(self):
        self.thread.dnf_flag = False
        self.roundflag = False

        try:

            GPIO.output(self.gpio.readylight, GPIO.LOW)  # turn ready light off

            ## add listener thread for disqualification
            self.thread.lower_flag()

            time.sleep(3)  # 3 fixed seconds before yellow light turns on
            randomwait = random.uniform(1, 3)  # getting the random value
            time.sleep(randomwait)  # waiting the random value before beeping

            # turn off dnf check
            self.thread.raise_flag()

            # if no one is disqualfied, do this
            if self.thread.dnf_flag == False:
                # the following line plays the sound
                
                # turn ready light ON
                GPIO.output(self.gpio.readylight, GPIO.HIGH)
                # take time stamp from the start of the round
                start = time.time();
                end = 0
            # checker-loop
            # waits for a button to be pressed
            while self.roundflag == False:
                input_p1 = GPIO.input(self.gpio.p1button)
                input_p2 = GPIO.input(self.gpio.p2button)

                if input_p1 == False:
                    end = time.time()
                    reaction = end - start

                    self.p1win()
                    self.p1.addAverage(reaction)
                    self.p1.checkBest(reaction)


                elif input_p2 == False:
                    end = time.time()
                    reaction = end - start

                    self.p2win()
                    self.p2.addAverage(reaction)
                    self.p2.checkBest(reaction)

        finally:
            # stop dnf checking
            self.thread.raise_flag()
            time.sleep(1)
            print("\n")
    ################
    ## START GAME ##
    ################
    def start(self):
        self.gpio.setup()
        self.thread.start()
        try:

            while self.p1.roundsWon < 3 and self.p2.roundsWon < 3:
                GPIO.output(self.gpio.rounds[self.roundsPlayed], GPIO.HIGH)
                self.roundstart()
            
            if self.p1.roundsWon == 3:
                print(self.p1.name, " wins!")
                # print("Average reaction time :", self.p1.getAverage())
                # print("Best reaction time : ", self.p1.best_time)
                # self.p1.printAverages()

                end_game = end_game_object(self.p1, self.p2)
                if (self.ranked == 1):

                    end_game.write_ranked_match()
                else:
                    end_game.write_unranked_matches()

            elif self.p2.roundsWon == 3:
                print(self.p2.name, " wins!")
                # print("Average reaction time :", self.p2.getAverage())
                # print("Best reaction time : ", self.p2.best_time)
                # self.p2.printAverages()

                end_game = end_game_object(self.p2, self.p1)
                if (self.ranked == 1):

                    end_game.write_ranked_match()
                else:
                    end_game.write_unranked_matches()

            time.sleep(1)

            return end_game
        finally:
            # GPIO.cleanup()
            self.resetgame()
            self.thread.stop_thread()
            GPIO.cleanup()


    # player1 wins function
    def p1win(self):
        self.p1.winRound();
        self.p2.loseRound();
        self.roundsPlayed += 1

        print(self.p1.name, " wins round!")
        # the respective LED gets lit up
        GPIO.output(self.gpio.player1[self.p1.roundsWon - 1], GPIO.HIGH)
        # end-of-round flag
        self.roundflag = True;


    # player2 wins function
    def p2win(self):
        self.p2.winRound();
        self.p1.loseRound();
        self.roundsPlayed += 1

        print(self.p2.name, " wins round")
        GPIO.output(self.gpio.player2[self.p2.roundsWon - 1], GPIO.HIGH)
        self.roundflag = True


    # player1 disqualified function
    def p1dnf(self):
        print(self.p1.name, " disqualified!")
        self.p2win()
        self.p2.dnf_won+=1


    # player2 disqualified function
    def p2dnf(self):
        print(self.p2.name, " disqualified!")
        self.p1win()
        self.p1.dnf_won += 1


    # check player1's button
    # returns a boolean value
    # True if button is not pressed
    # False if button is pressed
    def check_p1_button(self):
        input_p1 = GPIO.input(self.gpio.p1button)

        return input_p1


    # chcheck player2's button
    def check_p2_button(self):
        input_p2 = GPIO.input(self.gpio.p2button)

        return input_p2


# thread subclass
# use an instance to check for premature clicks
class dnf_thread(threading.Thread):
    def __init__(self, match):
        threading.Thread.__init__(self)
        self.stop_flag = False  # game flag
        self.check_flag = False  # round flag
        self.match = match
        self.dnf_flag = False;

    # must-have superclass-inherited function
    # defines what the thread will do
    def run(self):
        i = 0;  # debugger. ignore it
        while (self.stop_flag == False):  # this flag keeps the thread running until the very end of the match
            while self.check_flag == False:  # this flag is raised when a player presses the button before the signal
                if (self.check_flag == False):  # unecessary, will be removed
                    print("CHECKERINO %d" % i)  # debugger...ignore it for now pls
                    i += 1  # debugger. ignore it

                    # invokes both of the button-checking functions
                    p1_button = self.match.check_p1_button()
                    p2_button = self.match.check_p2_button()

                    # False value means the button was pressed
                    if p1_button == False:
                        self.match.p1dnf()
                        self.raise_flag()
                        self.dnf_flag = True
                    elif p2_button == False:
                        self.match.p2dnf()
                        self.raise_flag()
                        self.dnf_flag = True

                    time.sleep(0.001)
            time.sleep(0.1)

    # flag raised upon premature button press
    def raise_flag(self):
        self.check_flag = True

    # flag lowered at the start of a round
    def lower_flag(self):
        self.check_flag = False

    # stops the thread at the end of the game
    def stop_thread(self):
        self.raise_flag()
        self.stop_flag = True


class end_game_object():
    def __init__(self, winner, player2):
        self.player1 = winner
        self.player2 = player2
        self.winner = self.player1

        self.p1score = self.player1.roundsWon
        self.p2score = self.player2.roundsWon

        self.winner_best = self.winner.best_time
        self.winner_avg = self.winner.getAverage()
        

    def write_unranked_matches(self):
        db.update_unranked_matches()

    def write_ranked_match(self):
        db.insert_time(self.winner.name, self.winner.getAverage(), self.winner.best_time)
        db.insert_match(self.winner, self.player1, self.player2, self.player1.roundsWon, self.player2.roundsWon)     
