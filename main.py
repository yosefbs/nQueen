from models import *
from  board import Board


def main():
    print('Hello, world!')
    b=Board(8)
    b.printBorad()
    b.moveQueenToNode(0,1,2)
    b.moveQueenToNode(1, 2, 2)
    b.moveQueenToNode(2, 3, 3)
    b.moveQueenToNode(3, 4, 4)
    b.printBorad()
    b.queens[3].printQueen()

    b.moveQueenToNode(3, 2, 7)
    b.printBorad()
    b.queens[3].printQueen()

    print(*b.freeNodes)

if __name__ == '__main__':
    main()
