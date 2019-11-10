from models import *


def main():
    print('Hello, world!')
    b=Borad(8)
    b.printBorad()
    b.moveQueenToNode(0,1,2)
    b.moveQueenToNode(1, 2, 2)
    b.moveQueenToNode(2, 3, 3)
    b.moveQueenToNode(3, 4, 4)
    b.printBorad()
    b.nodes[(3,3)].printNode()
    b.queens[0].printQueen()

if __name__ == '__main__':
    main()
