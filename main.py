from models import *
from random import randrange



def main():
    print('Hello, world!')
    b=Borad(8)

    rnd=randrange(len(b.freeNodes))
    print(len(b.freeNodes))
    b.moveQueenToNode(0, 1, 2)
    print(len(b.freeNodes))
    b.leaveNode(0)
    print(len(b.freeNodes))

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

if __name__ == '__main__':
    main()
