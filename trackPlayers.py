class trackPlayers:
    def __init__(self):
        self.positions = []
        self.playerDict = {}
        self.currPos = 0
        self.numberOfPlayers = 0
    
    def scores(self,numOfPlayers):
        self.positions = [0] * numOfPlayers
        self.numberOfPlayers = numOfPlayers

    def addPlayer(self,name):
        self.playerDict[self.currPos] = name 
        self.currPos += 1 