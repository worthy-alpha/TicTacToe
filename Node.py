class Node:
    def __init__(self ,boardPos ,nextTurn):
        self.boardPos = boardPos
        self.nextTurn = nextTurn
        self.val = None 
        self.next = []
        self.best = None
        
        
    def __str__(self):
        print("----------------")
        print(self.boardPos[0])
        print(self.boardPos[1])
        print(self.boardPos[2])
        print("Next Turn:" ,self.nextTurn)
        print("moves: ",self.next)
        print("Val got: " ,self.val)
        print("best: ",self.best)
        return ""
