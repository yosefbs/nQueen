import random
from models import NodeLocation


class Player:
    def __init__(self, board,printSteps = False):
        self.board=board
        self.queensInds = list(range(board.n))


    def play(self,printSteps = False,locationToIgnore = NodeLocation(-1, -1) ):
        self.printSteps=printSteps
        n=self.board.n
        board=self.board
        queensInds=self.queensInds
        while len(board.freeNodes) > 0:
            node = random.choice(board.freeNodes)
            if node.location == locationToIgnore:
                if len(board.freeNodes)==1:
                    break
                else:
                    continue
            board.moveQueenToNode(queensInds.pop(), node.location.rowId,node.location.colId)
            if self.printSteps:
                board.printMiniBorad()
            if len(queensInds) == 0:
                return True
        queenToMoveInd = max(board.queens.keys(), key=(lambda k: len(board.queens[k].uniqueAttackableNode)))
        queensInds.append(queenToMoveInd)
        queenToMove=board.queens[queenToMoveInd]
        removedLocatin =queenToMove.location
        board.leaveNode(queenToMove.id)
        if board.moveCounter > 30:
            return False
        return self.play(self.printSteps,removedLocatin)