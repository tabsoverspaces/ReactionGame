#player class
#two instances are created per game
#the tournament mode will have 8 players(2^n) created and put into a list
class Player:
    def __init__(self, name): #constructor
        self.name = name;
        self.roundsWon = 0;
        self.roundsPlayed = 0;
        self.best_time = 999
        self.reactions = []

        self.dnf_won = 0

    def reset(self): #reset player stats
        self.roundsPlayed = 0;
        self.roundsWon = 0;
        self.reactions[:] = []
        self.dnf_won = 0

    def winRound(self):
        self.roundsWon += 1;
        self.playRound();

    def loseRound(self):
        self.playRound();

    def playRound(self):
        self.roundsPlayed += 1;
        
    def addAverage(self, time):
        self.reactions.append(time)

    def getAverage(self):
        sum = 0
        for x in self.reactions:
            sum+=x

        dividor = 1
        if self.roundsWon == self.dnf_won:
            dividor = 1
        else:
            dividor = self.roundsWon-self.dnf_won
            
        return sum/dividor
       
    def checkBest(self, time):
        if(time < self.best_time):
            self.best_time = time

    def printAverages(self):
        i= 0;
        for x in self.reactions:
            print("Average n.", i , " : ",x)
            i+=1;
            
