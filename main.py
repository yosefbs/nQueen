from models import *
from random import randrange

from board import Board
from player import Player


def main():
    winCounter = 0
    playCounter=0
    totalMoves = 0
    totalWinGamesMoves = 0
    b = Board(8)
    p = Player(b)
    playCounter += 1
    win = p.play(True)
    print(win)
    print(b.moveCounter)
    numOfWinReq=1000
    while winCounter < numOfWinReq:

        b = Board(8)
        p = Player(b)
        playCounter += 1
        win = p.play()
        if win:
            totalWinGamesMoves+= b.moveCounter
            winCounter+=1
            b.printBorad()
            print(b.moveCounter)
        totalMoves += b.moveCounter
    print()
    print('wins: '+ str(winCounter) + '/ play: ' + str(playCounter))
    print(totalMoves / numOfWinReq)
    print(totalWinGamesMoves / numOfWinReq)
    # print(len(b.freeNodes))
    # b.moveQueenToNode(0, 1, 2)
    # print(len(b.freeNodes))
    # b.leaveNode(0)
    # print(len(b.freeNodes))
    #
    # b.printBorad()
    # b.moveQueenToNode(0,1,2)
    # b.moveQueenToNode(1, 2, 2)
    # b.moveQueenToNode(2, 3, 3)
    # b.moveQueenToNode(3, 4, 4)
    # b.printBorad()
    # b.queens[3].printQueen()
    #
    # b.moveQueenToNode(3, 2, 7)
    # b.printBorad()
    # b.queens[3].printQueen()
    #
    # print(*b.freeNodes)


if __name__ == '__main__':
    main()
