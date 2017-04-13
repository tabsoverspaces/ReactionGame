import sys
#project file imports
import player
import match
import stats

import time

############################
## asks for input of names #
## returns created match ###
############################
def prompt_names():
      print("Initiating new ranked match...")
      time.sleep(.5)
      print("Connecting to database...")
      time.sleep(.5)

      print("Connected")
      time.sleep(.25)
      
      print("Enter players' names :")
      player1 = raw_input("Player 1 : ")
      print("\n")
      player2 = raw_input("Player 2 : ")
      print("\n")

      match_c = match.match_class(player1, player2, 1)
      return match_c


###########################################################
## main below #############################################
###########################################################
choice = -1
while(choice != 1):
      print("1.Unranked match\n2.Ranked match\n3.Stats\n4.Exit");

      choice = (int(raw_input()))

      if choice==1:
            match = match.match_class("Player1" , "Player 2", 0)
            #start game
            match.start();
            
      elif choice == 2:
            match = prompt_names()
            #start game
            match.start();
            
      elif choice == 3:
            stats.print_stats()
      elif choice == 4:
            sys.exit()








      
