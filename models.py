from collections import Set


class Queen:
    def __init__(self, id):
        self.id = id
        self.uniqueAttackableNode = []
        self.location = (-1, -1)

    def setLocation(self, r, c):
        self.location = (r, c)

    def __str__(self):
        return 'Q {0} at: ({1},{2}).'.format(self.id, self.location[0], self.location[1])

    def printQueen(self):
        print('Queen {0} at: ({1},{2}). unique controlled nodes:'.format(self.id, self.location[0], self.location[1]))
        print(*self.uniqueAttackableNode)





class BoardNode:
    def __init__(self, rowId, colId):
        self.rowId = rowId
        self.colId = colId
        self.attackableBy = []

    def addAttacker(self, queen):
        if len(self.attackableBy) == 0:
            queen.uniqueAttackableNode.append(self)
        if len(self.attackableBy) == 1:
            self.attackableBy[0].uniqueAttackableNode.remove(self)
        self.attackableBy.append(queen)

    def removeAttacker(self, queen):
        self.attackableBy.remove(queen)
        if len(self.attackableBy) == 1:
            self.attackableBy[0].uniqueAttackableNode.append(self)

    def printNode(self):
        print('Node: ({0},{1}) controled by queens:'.format(self.rowId, self.colId))
        print(*self.attackableBy)


    def __str__(self):
        return ('({0},{1}) '.format(self.rowId, self.colId))