import random


class Player:  # Player Logic
    def __init__(self, board, maxMoves):
        self.maxMoves = maxMoves  # after max moves stop try to resolve and return false
        self.board = board  # the game board obj
        self.notOnBoardQueens = list(range(board.n))   # id's of queen that not in board, when start all queen are
        # outside the board
        self.queensOnBoard = 0
        self.backTrackLogic = BacktrackLogic()

#the play logic writen in PlayLogic.docx file
    def play(self, printSteps=False):
        n = self.board.n
        board = self.board
        notOnBoardQueens = self.notOnBoardQueens

        while len(board.freeNodes) >= len(notOnBoardQueens):
            freeNodesLocations = list(map(lambda node: node.location, board.freeNodes))
            usableNodes = list(set(freeNodesLocations) - set(self.backTrackLogic.dontUseLocation))
            if len(usableNodes) == 0:
                break
            node = random.choice(usableNodes)
            board.moveQueenToNode(notOnBoardQueens.pop(), node.rowId, node.colId)
            curQueenOnBoard = board.n - len(notOnBoardQueens)
            if curQueenOnBoard < self.queensOnBoard:
                lastRemoved = self.backTrackLogic.dontUseLocation[-1]
                self.backTrackLogic.dontUseLocation.clear()
                self.backTrackLogic.dontUseLocation.append(lastRemoved)
            self.queensOnBoard = curQueenOnBoard
            if printSteps:
                print('total free nodes:{0} usable free nodes:{1}'.format(len(freeNodesLocations), len(usableNodes)))
                print(board.printMiniBorad())
            if len(notOnBoardQueens) == 0:
                return True

        if board.moveCounter > self.maxMoves:
            return False
        self.backTrackLogic.doBackTrack(board, notOnBoardQueens)
        return self.play(printSteps)


class BacktrackLogic:
    def __init__(self):
        self.dontUseLocation = []
        self.dontUsehistory = []

    def doBackTrack(self, board, queensInds):
        queenToRemoveInd = max(board.queens.keys(), key=(lambda k: len(board.queens[k].uniqueAttackableNode)))
        queensInds.append(queenToRemoveInd)
        queenToRemove = board.queens[queenToRemoveInd]
        removedLocatin = queenToRemove.location
        self.dontUseLocation.append(removedLocatin)

        self.dontUsehistory.insert(0, removedLocatin)
        board.leaveNode(queenToRemove.id)
        if len(self.dontUsehistory) == 6:
            self.dontUsehistory.pop()
            if self.dontUsehistory[0] == self.dontUsehistory[2] == self.dontUsehistory[4]:
                self.dontUsehistory.pop()
                self.doBackTrack(board, queensInds)
        return self.dontUseLocation
