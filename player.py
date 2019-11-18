import random
from models import NodeLocation


class Player:
    def __init__(self, board, printSteps=False):
        self.board = board
        self.queensInds = list(range(board.n))
        self.backTrackLogic = BacktrackLogic()

    def play(self, printSteps=False):
        self.printSteps = printSteps
        n = self.board.n
        board = self.board
        queensInds = self.queensInds
        while len(board.freeNodes) > 0:
            freeNodesLocations = list(map(lambda node: node.location, board.freeNodes))
            usableNodes = list(set(freeNodesLocations) - set(self.backTrackLogic.dontUseLocation))
            if len(usableNodes)==0:
                break
            node = random.choice(usableNodes)
            board.moveQueenToNode(queensInds.pop(), node.rowId, node.colId)
            if self.printSteps:
                board.printMiniBorad()
            if len(queensInds) == 0:
                return True
        self.backTrackLogic.doBackTrack(board,queensInds)

        if board.moveCounter > 14:
            return False
        return self.play(self.printSteps)


class BacktrackLogic:
    def __init__(self):
        self.dontUseLocation = []
        # self.inBacktrack = False
        self.dontUsehistory = []

    # def getUseableNode(self,freeNodes):
    #     if (len(self.history) == 5) and (len(list(dict.fromkeys(self.history))) == 2):
    #         return None
    #
    #     freeNodesLocations = list(map(lambda node:node.location,freeNodes))
    #     usableNodes = list(set(freeNodesLocations) - set(self.dontUseLocation))
    #     if len(usableNodes) == 0:
    #         return None
    #     self.dontUseLocation.clear()
    #     if len(self.history)== 5:
    #         self.history.pop()
    #     selectedNode = random.choice(usableNodes)
    #     self.history.insert(0,selectedNode)
    #     return selectedNode

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
                self.doBackTrack(board,queensInds)
        board.leaveNode(queenToRemove.id)
        return self.dontUseLocation
