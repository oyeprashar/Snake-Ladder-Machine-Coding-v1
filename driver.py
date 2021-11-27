from Board import Board 
from Play import Play


currBoard = Board(100)

numOfSnakes = int(input())
for _ in range(numOfSnakes):
    fromCell,toCell = map(int,input().split())
    currBoard.addSnake(fromCell,toCell)

numOfLadder = int(input())
for _ in range(numOfLadder):
    fromCell,toCell = map(int,input().split())
    currBoard.addLadder(fromCell,toCell)

totalPlayer = int(input())
currBoard.scores(totalPlayer)
names = []

for _ in range(totalPlayer):
    currBoard.addPlayer(input())

currBoard.numberOfPlayers = totalPlayer
currBoard.namesArr = names

playing = Play(currBoard)

while True:
    playing.move()
