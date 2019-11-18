class Queen:  # represent a queen in board
    def __init__(self, id):
        self.id = id  # queen id
        self.uniqueAttackableNode = []  # list of node that Threatened *only* by this queen
        self.location = NodeLocation(-1, -1)  # queen location on borad (-1, -1) is out of board

    def setLocation(self, r, c):
        self.location = NodeLocation(r, c)  # update queen location

    def __str__(self):
        return 'Q {0} at: ({1},{2}).'.format(self.id, self.location[0], self.location[1])

    def printQueen(self):
        print('Queen {0} at: ({1},{2}). unique controlled nodes:'.format(self.id, self.location[0], self.location[1]))
        print(*self.uniqueAttackableNode)


class BoardNode:  # represent a node in board
    def __init__(self, rowId, colId):
        self.location = NodeLocation(rowId, colId)  # location in board
        self.attackableBy = []  # list of all queens that threading this node

    def addAttacker(self, queen):  # add queen that threaded this node to list
        if len(self.attackableBy) == 0:  # if there is no any other queen that threaded this queen set the new
            # threaded queen as unique attacker of this node
            queen.uniqueAttackableNode.append(self)
        if len(
                self.attackableBy) == 1:  # when adding the second attacker remove unique attacker flag from the first queen
            self.attackableBy[0].uniqueAttackableNode.remove(self)
        self.attackableBy.append(queen)

    def removeAttacker(self, queen):  # remove queen from attacker list (when queen is moved...)
        self.attackableBy.remove(queen)
        if len(self.attackableBy) == 1:  # if after removing a queen there is only one queen that threaded this node set
            # it as unique attacker of this node
            self.attackableBy[0].uniqueAttackableNode.append(self)

    def printNode(self):
        print('Node: ({0},{1}) controled by queens:'.format(self.location.rowId, self.location.colId))
        print(*self.attackableBy)

    def __str__(self):
        return '({0},{1}) '.format(self.rowId, self.colId)


class NodeLocation:  # help class for print and compare locations in board
    def __init__(self, rowId, colId):
        self.rowId = rowId
        self.colId = colId
        a = self.rowId
        b = self.colId
        self.cantorPairing = int((a + b) * (a + b + 1) / 2 + a)  # canto func that create hash from two integers

    def __hash__(self):
        return self.cantorPairing

    def __eq__(self, other):
        """Overrides the default implementation"""
        return (self.colId == other.colId) and (self.rowId == other.rowId)
