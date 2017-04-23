# project file imports

import match

# other imports

import random




class Tournament:
    'Initialisation of all needed lists'

    bo8Roster = []
    bo8Games = []
    bo4Roster = []
    bo4Games = []
    bo2Roster = []
    bo2Games = []
    winner = []

    # In order for the init method to work, you need to pass a whole list as argument like ['Test', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7', 'Test8']

    def __init__(self, roster): # Constructor; Gets fed a list full of player objects
        random.seed()
        temp = []
        for x in range(len(roster)):
            temp.append(roster[x])
        self.printList(temp)
        while (len(temp) >= 1):
            rnd = random.randint(0, len(temp)-1)
            self.bo8Roster.append(temp[rnd])
            temp.remove(temp[rnd])
        self.matchCreator(self.bo8Roster, self.bo8Games)


    def matchCreator(self, roster, games):
        y = int(len(roster)/2)
        for x in (range(0, y)):
            games.append(self.createMatch(roster[x*2], roster[(x*2)+1]))
        self.printList(self.bo8Games)

    # createMatch is a placeholder, it will be replaced by the actual object used to create a match

    def createMatch(self, player1, player2):
        # return player1 + ' ' + player2 + ' ||';
        # Comment the previous line and uncomment the next line when the game_class takes two parameters
        return match.match_class(player1, player2, 1);

    def printList(self, list):
        for x in range(len(list)):
            print(list[x].name, end= ' ')
        print()

    def printListx2(self, list):
        y = int(len(list)/2)
        for x in (range(y)):
            print(list[x*2], end= ' ')
        print()


# kek = ['Mike', 'Dragan', 'Filippo', 'Gilles', 'Jack', 'Sam', 'Yves', 'Patrick']
# tournament1 = Tournament(kek)
# tournament1.printList(tournament1.bo8Roster)
# tournament1.printListx2(tournament1.bo8Roster)
# tournament1.matchCreator(tournament1.bo8Roster, tournament1.bo8Games)







