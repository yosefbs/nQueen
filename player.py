import random
from models import NodeLocation


class Player:
    def __init__(self, board):
        self.board = board
        self.queensInds = list(range(board.n))
        self.queensOnBoard = 0
        self.backTrackLogic = BacktrackLogic()
        self.freeNodeCntHistory = []
        self.freeNodeDictCntHistory = {}

    def play(self, printSteps=False):
        n = self.board.n
        board = self.board
        queensInds = self.queensInds

        while len(board.freeNodes) >= len(queensInds):
            freeNodesLocations = list(map(lambda node: node.location, board.freeNodes))
            cntFreeNode = len(freeNodesLocations)
            if cntFreeNode not in self.freeNodeDictCntHistory:
                self.freeNodeDictCntHistory[cntFreeNode] = 0
            self.freeNodeDictCntHistory[cntFreeNode] += 1
            self.freeNodeCntHistory.append(len(freeNodesLocations))
            usableNodes = list(set(freeNodesLocations) - set(self.backTrackLogic.dontUseLocation))
            if len(usableNodes) == 0:
                break
            node = random.choice(usableNodes)
            board.moveQueenToNode(queensInds.pop(), node.rowId, node.colId)
            curQueenOnBoard = board.n - len(queensInds)
            if (curQueenOnBoard < self.queensOnBoard):
                lastRemoved = self.backTrackLogic.dontUseLocation[-1]
                self.backTrackLogic.dontUseLocation.clear()
                self.backTrackLogic.dontUseLocation.append(lastRemoved)
            self.queensOnBoard = curQueenOnBoard
            if printSteps:
                print('total free nodes:{0} usable free nodes:{1}'.format(len(freeNodesLocations), len(usableNodes)))
                print(board.printMiniBorad())
            if len(queensInds) == 0:
                return True

        if board.moveCounter > 14:
            return False
        self.backTrackLogic.doBackTrack(board, queensInds)
        return self.play(printSteps)


class BacktrackLogic:
    def __init__(self):
        self.dontUseLocation = []
        # self.inBacktrack = False
        self.dontUsehistory = []

    def doBackTrack(self, board, queensInds):
        queenToRemoveInd = max(board.queens.keys(), key=(lambda k: len(board.queens[k].uniqueAttackableNode)))
        queensInds.append(queenToRemoveInd)
        queenToRemove = board.queens[queenToRemoveInd]
        removedLocatin = queenToRemove.location
        self.dontUseLocation.append(removedLocatin)

        self.dontUsehistory.insert(0, removedLocatin)
        if len(self.dontUsehistory) == 6:
            self.dontUsehistory.pop()
            if self.dontUsehistory[0] == self.dontUsehistory[2] == self.dontUsehistory[4]:
                self.dontUsehistory.pop()
                self.doBackTrack(board, queensInds)
        board.leaveNode(queenToRemove.id)
        return self.dontUseLocation

    def noLogicBackTrack(self, board, queensInds):
        queenOnBoard = list(set(board.queens.keys()) - set(queensInds))
        queenToRemoveInds = random.choices(queenOnBoard, k=int(len(queenOnBoard) / 3))
        for qInd in queenToRemoveInds:
            queensInds.append(qInd)
            board.leaveNode(qInd)
        self.dontUseLocation.clear()
