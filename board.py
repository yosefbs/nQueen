from models import *

class Board:
    def __init__(self, n):
        self.freeNodes = [] #nodes that not Threatened by any Queen
        self.nodes = {} # all nodes in board
        self.queens = {}# all queen
        self.n = n
        self.moveCounter=0
        for r in range(0, n):
            for c in range(0, n):
                key = (r, c)
                newNode = BoardNode(r, c)
                self.nodes[key] = newNode
                self.freeNodes.append(newNode)
            self.queens[r] = Queen(r)



    def moveQueenToNode(self, queenId, rowId, colId):
        self.leaveNode(queenId)  # remove queen from old node and update threaded nodes
        self.queens[queenId].setLocation(rowId, colId) # set new location for queen
        self.moveCounter += 1  # count a move
        self.updateBoardAttackMap(queenId)  # update all nodes that Threatened by this queen

    def updateBoardAttackMap(self, queenId):  # update all nodes that Threatened by this queen
        q = self.queens[queenId]
        r = q.location.rowId
        c = q.location.colId
        for i in range(0, self.n):
            self.setNodeAttacker(r, i, q)
            if i != r:
                self.setNodeAttacker(i, c, q)

        tempR = r + 1
        tempC = c + 1
        while (tempR < self.n) and (tempC < self.n):
            self.setNodeAttacker(tempR, tempC, q)
            tempR += 1
            tempC += 1

        tempR = r - 1
        tempC = c - 1
        while (tempR > -1) and (tempC > -1):
            self.setNodeAttacker(tempR, tempC, q)
            tempR -= 1
            tempC -= 1

        tempR = r + 1
        tempC = c - 1
        while (tempR < self.n) and (tempC > -1):
            self.setNodeAttacker(tempR, tempC, q)
            tempR += 1
            tempC -= 1

        tempR = r - 1
        tempC = c + 1
        while (tempR > -1) and (tempC < self.n):
            self.setNodeAttacker(tempR, tempC, q)
            tempR -= 1
            tempC += 1


    def setNodeAttacker(self, row, col, queen):
        node = self.nodes[(row, col)]
        node.addAttacker(queen)
        if node in self.freeNodes:
            self.freeNodes.remove(node)


    def leaveNode(self, queenId):
        q = self.queens[queenId]
        if q.location == NodeLocation(-1, -1):
            return
        self.moveCounter+= 1
        for node in q.uniqueAttackableNode:
            self.freeNodes.append(node)
        q.uniqueAttackableNode = []
        r = q.location.rowId
        c = q.location.colId
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
        q.setLocation(-1, -1)

    def printMiniBorad(self):
        res = ''
        occupiedNodes = {}
        for i in range(0, self.n):
            q = self.queens[i]
            if q.location.rowId != -1:
                occupiedNodes[q.location.rowId] = q.location.colId
        for i in range(0,self.n):
            if i in occupiedNodes:
                res+=(str(occupiedNodes[i])+',')
            else:
                res += ('-,')
        res += ('\n')
        return res

    def printBorad(self):
        occupiedNodes = {}
        for i in range(0, self.n):
            q = self.queens[i]
            if q.location.colId != -1:
                occupiedNodes[(q.location.rowId,q.location.colId)] = q.id
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

