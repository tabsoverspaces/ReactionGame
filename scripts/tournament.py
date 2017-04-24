import match

# For some reason it tells me match cannot be imported, please confirm it's working properly, it should work in theory
# match.py line 228 returns results

import random


class Tournament():
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

    def __init__(self, roster):  # Constructor; Gets fed a list full of player objects
        self.match_count = 0
        random.seed()
        temp = []
        for x in roster:
            temp.append(x)
        # self.printList(temp)
        while (len(temp) >= 1):
            rnd = random.randint(0, len(temp) - 1)
            self.quarterfinalsRoster.append(temp[rnd])
            temp.remove(temp[rnd])
        # self.matchCreator(self.quarterfinalsRoster, self.quarterfinalsGames)
        self.create_quarter_final_matches()

        self.next_match = self.quarterfinalsGames[0]

    def matchCreator(self, roster, games):
        y = int(len(roster) / 2)
        for x in (range(0, y)):
            games.append(self.createMatch(roster[x * 2], roster[(x * 2) + 1]))
        self.printList(self.quarterfinalsGames)

    def playMatches(self, games, roster):
        for x in range(len(games)):
            roster.append((games[x].start()).winner)

    def play_next_match(self):
        if (self.match_count < 3):
            qfwinner = (self.next_match.start()).winner

            self.semifinalsRoster.append(qfwinner)

            self.match_count += 1
            self.next_match = self.quarterfinalsRoster[self.match_count]

        if (self.match_count == 3):
            qfwinner = (self.next_match.start()).winner
            self.semifinalsRoster.append(qfwinner)

            self.create_semi_final_matches()
            self.next_match = self.semifinalsGames[0]
            self.match_count += 1

        if (self.match_count >= 4 and self.match_match < 5):
            sfwinner = (self.next_match.start()).winner

            self.finalsRoster.append(sfwinner)

            self.match_count += 1
            self.next_match = self.semifinalsRoster[self.match_count - 4]

        if (self.match_count == 5):
            sfwinner = (self.next_match.start()).winner
            self.finalsRoster.append(sfwinner)

            self.create_final_match()
            self.next_match = self.final_match
            self.match_count += 1

        if (match_count == 6):
            winner = (self.next_match.start()).winner

    def createMatch(self, player1, player2):
        # return player1 + ' ' + player2 + ' ||';
        # Comment the previous line and uncomment the next line when the game_class takes two parameters
        return match.match_class(player1, player2, 1)

    def create_quarter_final_matches(self):
        for x in range(0, 8, 2):
            match1 = self.createMatch(self.quarterfinalsRoster[x], self.quarterfinalsRoster[x + 1])
            self.quarterfinalsGames.append(match1)

    def create_semi_final_matches(self):
        for x in range(0, 4, 2):
            match1 = self.createMatch(self.semifinalsRoster[x], self.semifinalsRoster[x + 1])
            self.semifinalsGames.append(match1)

    def create_final_match(self):
        self.final_match = self.createMatch(self.finalsRoster[0], self.finalsRoster[1])

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
