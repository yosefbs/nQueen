from models import *


class Board:
    def __init__(self, n):
        self.freeNodes = []
        self.nodes = {}
        self.queens = {}
        self.n = n
        for r in range(0, n):
            for c in range(0, n):
                key = (r, c)
                newNode = BoardNode(r, c)
                self.nodes[key] = newNode
                self.freeNodes.append(newNode)
            self.queens[r] = Queen(r)

    def moveQueenToNode(self, queenId, rowId, colId):
        self.leaveNode(queenId)
        self.queens[queenId].setLocation(rowId, colId)
        self.setAttackInfo(queenId)

    def setAttackInfo(self, queenId):
        q = self.queens[queenId]
        r = q.location[0]
        c = q.location[1]
        for i in range(0, self.n):
            self.nodes[(r, i)].addAttacker(q)
            if i != r:
                self.nodes[(i, c)].addAttacker(q)

        tempR = r + 1
        tempC = c + 1
        while (tempR < self.n) and (tempC < self.n):
            self.nodes[(tempR, tempC)].addAttacker(q)
            tempR += 1
            tempC += 1

        tempR = r - 1
        tempC = c - 1
        while (tempR > -1) and (tempC > -1):
            self.nodes[(tempR, tempC)].addAttacker(q)
            tempR -= 1
            tempC -= 1

        tempR = r + 1
        tempC = c - 1
        while (tempR < self.n) and (tempC > -1):
            self.nodes[(tempR, tempC)].addAttacker(q)
            tempR += 1
            tempC -= 1

        tempR = r - 1
        tempC = c + 1
        while (tempR > -1) and (tempC < self.n):
            self.nodes[(tempR, tempC)].addAttacker(q)
            tempR -= 1
            tempC += 1

    def leaveNode(self, queenId):
        q = self.queens[queenId]
        if q.location == (-1, -1):
            return

        q.uniqueAttackableNode = []
        r = q.location[0]
        c = q.location[1]
        for i in range(0, self.n):
            self.nodes[(r, i)].removeAttacker(q)
            if i != r:
                self.nodes[(i, c)].removeAttacker(q)

        tempR = r + 1
        tempC = c + 1
        while (tempR < self.n) and (tempC < self.n):
            self.nodes[(tempR, tempC)].removeAttacker(q)
            tempR += 1
            tempC += 1

        tempR = r - 1
        tempC = c - 1
        while (tempR > -1) and (tempC > -1):
            self.nodes[(tempR, tempC)].removeAttacker(q)
            tempR -= 1
            tempC -= 1

        tempR = r + 1
        tempC = c - 1
        while (tempR < self.n) and (tempC > -1):
            self.nodes[(tempR, tempC)].removeAttacker(q)
            tempR += 1
            tempC -= 1

        tempR = r - 1
        tempC = c + 1
        while (tempR > -1) and (tempC < self.n):
            self.nodes[(tempR, tempC)].removeAttacker(q)
            tempR -= 1
            tempC += 1

    #       q.location[]

    def printBorad(self):
        occupiedNodes = {}
        for i in range(0, self.n):
            q = self.queens[i]
            if q.location[0] != -1:
                occupiedNodes[q.location] = q.id
        print('-', end='')
        for i in range(0, self.n):
            print('--' + str(i) + '-', end='')
        print('-')
        for r in range(0, self.n):
            print(str(r) + '|', end='')
            for c in range(0, self.n):
                if (r, c) in occupiedNodes:
                    print(' X |', end='')
                else:
                    print('   |', end='')
            print()