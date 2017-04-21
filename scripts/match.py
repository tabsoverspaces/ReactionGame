# project file imports
import random
import threading
import time

import RPi.GPIO as GPIO
import player
# python module imports
import pygame

from scripts import db

# set RPI pin layout to BCM
GPIO.setmode(GPIO.BCM)
# disable RPI warnings
GPIO.setwarnings(0)

# initialize pygame mixer
pygame.mixer.init()
# load sound
pygame.mixer.music.load("beep-02.mp3")  # SOUNDS NEEDS TO BE CHANGED

# number of rounds to be played
numberofrounds = 5  # SHOULD NOT BE CHANGED! BREADBOARD LAYOUT DESIGNED FOR 5 ROUNDS

# PIN_SETUP_START
# DO NOT CHANGE ANY OF THE CODE UNTIL "PIN_SETUP_END"

# ready LED
readylight = 23

# player1 score LEDs
p11 = 21
p12 = 20
p13 = 16

# player2 score LEDs
p21 = 25
p22 = 22
p23 = 27

# players' score LED lists
player1 = [p11, p12, p13]
player2 = [p21, p22, p23]

# round LEDs
r1 = 26
r2 = 19
r3 = 13
r4 = 6
r5 = 5

# round LED list
rounds = [r1, r2, r3, r4, r5]

# player1 button pin
p1button = 24
# player2 button pin
p2button = 18

# reset button pin
resetbutton = 12

# setup output pins(LEDs)
for a in player1:
    GPIO.setup(a, GPIO.OUT)
for a in player2:
    GPIO.setup(a, GPIO.OUT)
for a in rounds:
    GPIO.setup(a, GPIO.OUT)

# setup yellow ready light
GPIO.setup(readylight, GPIO.OUT)

# setup input pins(buttons)
GPIO.setup(resetbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(p1button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# PIN_SETUP_END

#####################
## MAIN MATCH CLASS ##
#####################
class match_class:
    ###
    def __init__(self, player1, player2,
                 ranked):  # constructor . Needs to be modified so that it takes two paramters, Player1 name and Player2 name which will be entered prior to the start of the game
        self.p1 = player.Player(player1);
        self.p2 = player.Player(player2);

        self.roundflag = False
        self.thread = dnf_thread(self)  # create instance of class dnf_thread

        self.roundsPlayed = 0;

        self.ranked = ranked

    ################
    ## RESET GAME ##
    ################
    # sets all values to default/0
    def resetgame(self):

        self.roundsPlayed = 0;
        self.p1.reset();
        self.p2.reset();

        for a in player1:
            GPIO.output(a, GPIO.LOW)
        for a in player2:
            GPIO.output(a, GPIO.LOW)
        for a in rounds:
            GPIO.output(a, GPIO.LOW)

    GPIO.output(readylight, GPIO.LOW)

    ################
    ## START GAME ##
    ################
    def start(self):


self.thread.start()
try:

    while self.p1.roundsWon < 3 and self.p2.roundsWon < 3:
        GPIO.output(rounds[self.roundsPlayed], GPIO.HIGH)
        self.roundstart();

    if self.p1.roundsWon == 3:
        print(self.p1.name, " wins!")
        print("Average reaction time :", self.p1.getAverage())
        print("Best reaction time : ", self.p1.best_time)
        self.p1.printAverages()

        if (self.ranked == 1):
            end_game = end_game_object(self.p1, self.p2)
            end_game.write_ranked_match()
    elif self.p2.roundsWon == 3:
        print(self.p2.name, " wins!")
        print("Average reaction time :", self.p2.getAverage())
        print("Best reaction time : ", self.p2.best_time)
        self.p2.printAverages()

        if (self.ranked == 1):
            end_game = end_game_object(self.p2, self.p1)
            end_game.write_ranked_match()

    time.sleep(3)
finally:
    # GPIO.cleanup();
    self.resetgame();
    self.thread.stop_thread()
GPIO.cleanup();


#################
## START ROUND ##
#################
def roundstart(self):
    self.thread.dnf_flag = False
    self.roundflag = False;

    try:

        GPIO.output(readylight, GPIO.LOW)  # turn ready light off

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
            pygame.mixer.music.play(1, 0.0)  # THERE WILL BE A SEPARATE SOUND THREAD FOR THE BEEP TO BE PLAYED
            # turn ready light ON
            GPIO.output(readylight, GPIO.HIGH)
            # take time stamp from the start of the round
            start = time.time();
            end = 0
        # checker-loop
        # waits for a button to be pressed
        while self.roundflag == False:
            input_p1 = GPIO.input(p1button)
            input_p2 = GPIO.input(p2button)

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


# player1 wins function
def p1win(self):
    self.p1.winRound();
    self.p2.loseRound();
    self.roundsPlayed += 1

    print(self.p1.name, " wins round!")
    # the respective LED gets lit up
    GPIO.output(player1[self.p1.roundsWon - 1], GPIO.HIGH)
    # end-of-round flag
    self.roundflag = True;


# player2 wins function
def p2win(self):
    self.p2.winRound();
    self.p1.loseRound();
    self.roundsPlayed += 1

    print(self.p2.name, " wins round")
    GPIO.output(player2[self.p2.roundsWon - 1], GPIO.HIGH)
    self.roundflag = True


# player1 disqualified function
def p1dnf(self):
    print(self.p1.name, " disqualified!")
    self.p2win()


# player2 disqualified function
def p2dnf(self):
    print(self.p2.name, " disqualified!")
    self.p1win()


# check player1's button
# returns a boolean value
# True if button is not pressed
# False if button is pressed
def check_p1_button():
    input_p1 = GPIO.input(p1button)

    return input_p1


# chcheck player2's button
def check_p2_button():
    input_p2 = GPIO.input(p2button)

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
                    p1_button = check_p1_button()
                    p2_button = check_p2_button()

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
    def __init__(self, winner, player):
        self.winner = winner
        self.player = player

    def writeUnrankedMatch(self):
        db.insertUnranked(self.winner.name, self.winner.getAverage(), self.winner.best_time)

    def write_ranked_match(self):
        db.insertRanked(self.winner.name, self.winner.getAverage(), self.winner.best_time)