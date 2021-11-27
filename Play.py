import random 
class Play():

    def __init__(self,BoardObj):
        self.currPlayer= 0
        self.BoardObj = BoardObj

    def move(self):

        if self.BoardObj.end == True:
            return 

        if self.currPlayer not in self.BoardObj.blocked:

            diceNum = random.randint(1,6)
            oldPos = self.BoardObj.positions[self.currPlayer]
            newPos = oldPos + diceNum 

            while newPos in self.BoardObj.snake:
                newPos = self.BoardObj.snake[newPos]
            
            while newPos in self.BoardObj.ladder:
                newPos = self.BoardObj.ladder[newPos]


            self.BoardObj.positions[self.currPlayer] = newPos


            if newPos == self.BoardObj.size:
                print(self.BoardObj.playerDict[self.currPlayer],"wins the game")
                self.BoardObj.end = True
            
            else:
                print(self.BoardObj.playerDict[self.currPlayer],"rolled a",diceNum,"and moved from",oldPos,"to",newPos)

            if newPos >= self.BoardObj.size:
                self.BoardObj.blocked.add(self.currPlayer)

        self.currPlayer = (self.currPlayer+1) % self.BoardObj.numberOfPlayers