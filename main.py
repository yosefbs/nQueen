from models import *
from random import randrange

from board import Board
from player import Player


def main():
    runMultiGames()
    # debug()
    return


def debug():
    b = Board(8)
    p = Player(b)
    win = p.play(True)
    print(win)
    print(b.moveCounter)
    print(*p.freeNodeCntHistory)


def runMultiGames():
    winCounter = 0
    playCounter = 0
    totalMoves = 0
    totalWinGamesMoves = 0
    b = Board(8)
    p = Player(b)

    numOfWinReq = 400
    while winCounter < numOfWinReq:
        b = Board(8)
        p = Player(b)
        playCounter += 1
        win = p.play()
        if win:
            totalWinGamesMoves += b.moveCounter
            winCounter += 1
            b.printBorad()
        totalMoves += b.moveCounter
    print()
    print('wins: ' + str(winCounter) + '/ play: ' + str(playCounter))
    print(totalMoves / numOfWinReq)
    print(totalWinGamesMoves / numOfWinReq)


if __name__ == '__main__':
    main()
