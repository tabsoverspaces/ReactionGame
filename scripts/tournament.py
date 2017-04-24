import match

# For some reason it tells me match cannot be imported, please confirm it's working properly, it should work in theory
# match.py line 228 returns results

import random

class Tournament:

    # Initialisation of all needed lists

    # The 'Roster' lists are for the participating players, whereas the 'Games' lists are for the corresponding matches

    # Quarter-Finals
    quarterfinalsRoster = []
    quarterfinalsGames = []

    # Semi-Finals
    semifinalsRoster = []
    semifinalsGames = []

    # Final
    finalRoster = []
    finalGame = []

    # The Winner
    winner = []

    # Next Match variable
    nextMatch = 0;

    def __init__(self, roster): # Constructor; Gets fed a list full of player objects
        random.seed()
        temp = []
        for x in range(len(roster)):
            temp.append(roster[x])
        # self.printList(temp)
        while (len(temp) >= 1):
            rnd = random.randint(0, len(temp)-1)
            self.quarterfinalsRoster.append(temp[rnd])
            temp.remove(temp[rnd])
        # self.matchCreator(self.quarterfinalsRoster, self.quarterfinalsGames)


    def matchCreator(self, roster, games):
        y = int(len(roster)/2)
        for x in (range(0, y)):
            games.append(self.createMatch(roster[x*2], roster[(x*2)+1]))
        # self.printList(self.quarterfinalsGames)

    def playMatches(self, games, roster):
        for x in range(len(games)):
            self.nextMatch = 0;
            roster.append(games[x].start().winner)
            while (self.nextMatch == 0):


    def tournament_start(self):
        # testTournament = self.Tournament(players)
        # self.printList(self.quarterfinalsRoster)
        self.matchCreator(self.quarterfinalsRoster, self.quarterfinalsGames)
        self.playMatches(self.quarterfinalsGames, self.semifinalsRoster)
        self.matchCreator(self.semifinalsRoster, self.semifinalsGames)
        self.playMatches(self.semifinalsGames, self.finalRoster)
        self.matchCreator(self.finalRoster, self.finalGame)
        self.playMatches(self.finalGame, self.winner)

    def createMatch(self, player1, player2):
        # return player1 + ' ' + player2 + ' ||';
        # Comment the previous line and uncomment the next line when the game_class takes two parameters
        return match.match_class(player1, player2, 1);


    # Debug functions

    # def printList(self, list):
    #     for x in range(len(list)):
    #         print(list[x].name, end= ' ')
    #         #print(list[x], end=' ')
    #     print()
    #
    # def printListx2(self, list):
    #     y = int(len(list)/2)
    #     for x in (range(y)):
    #         print(list[x*2], end= ' ')
    #     print()


# Debug code

# The next three lines are how I imagine the whole thing is launched
# First, you generate a list with all the players, in this case strings are used but I expect player objects to be used
# Then you call the constructor to initialise the tournament and finally you start it with tournament_start

# players = ['Mike', 'Dragan', 'Filippo', 'Gilles', 'Jack', 'Sam', 'Yves', 'Patrick']
# testTournament = Tournament(players)
# testTournament.tournament_start()

# --------------------------------------------------------------------------------------------------------------------

# Tournament.tournament_start(players)
# testTournament.printList(tournament1.bo8Roster)
# testTournament.printListx2(tournament1.bo8Roster)
# testTournament.matchCreator(tournament1.bo8Roster, tournament1.bo8Games)
