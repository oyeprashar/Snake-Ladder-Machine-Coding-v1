from trackPlayers import trackPlayers

class Board(trackPlayers):
    def __init__(self,size,):
        self.size = size
        self.end = False
        self.blocked = set()
        self.ladder = {}
        self.snake = {}

        trackPlayers.__init__(self)

    def addLadder(self,fromCell,toCell):
        self.ladder[fromCell] = toCell
    
    def addSnake(self,fromCell,toCell):
        self.snake[fromCell] = toCell