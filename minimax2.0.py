


class Node:
    def __init__(self,boardPos,lastTurn):
        self.boardPos = boardPos
        self.lastTurn = lastTurn

        self.key = None
        self.val = None
        self.depth=None
        self.next = []
    def __str__(self):

        print("----------------")
        print(self.boardPos[0])
        print(self.boardPos[1])
        print(self.boardPos[2])
        print("Last Turn:",self.lastTurn)
        if self.key!=None:
            print(self.lastTurn+" at ",self.key)
        print("Val got: ",self.val)
        print("depth: ",self.depth)
        return ""





def result(board,turn):
    w = 0
    o = turn
    for i in range(len(board)):

        for j in range(len(board)):
            # print(i,j)
            if board[i][j] != turn:
                #print("breaking")
                break
            elif j == 2 and board[i][j] == turn:
                #print("return -1")
                return 1
    ##==================
    #print("000000000000",turn)
    for i in range(len(board)):
        for j in range(len(board)):


            #print(j,i,board[j][i])
            if board[j][i] != turn:
                #print("breaking")
                break
            elif j == 2 and board[j][i] == turn:
                return 1
    ##==================
    if board[0][0] == o and board[1][1] == o and board[2][2] == o:
        return 1

    if board[0][2] == o and board[1][1] == o and board[2][0] == o:
        return 1
    return 0



def draw(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=="":
                return False
    return True


rc=0
d={}
noD = {}
def comp(turn):
    s = {"o","x"}
    t = set(turn)
    k = s-t
    k=str(k)[2:3]
    return k


def findGoodMove(board,turn,depth):
    global rc,d,noD
    rc+=1
    maxbest=-1000000000
    maxtup=0
    mintup=0
    optup=0
    minbest=1000000000
    tmp = rc
    h={}
    dlist = []
    r1 = result(board,turn)
    r2 = result(board,comp(turn))
    maxdepth=-1
    #print()


    #for i in board:

        #print(i)
    #print()
    #3print("turn: ",turn)

    if r1 :
        #print("won")

        if turn == "x": return 1,None,-1
        if turn == "o": return -1,None,-1
    elif r2:
        #print("won")
        if turn == "x": return -1,None,-1
        if turn == "o": return 1,None,-1
    if draw(board): return 0,None,-1

    for i in range(len(board)):
        for j in range(len(board)):
            ##print("at location for ",turn,i,j, board[i][j])
            if board[i][j]=="":
                #print(tmp,")empty at ",i,j, " for ",turn,"depth :",depth)
                board[i][j]=turn
                new = Node(board, turn)
                new.key = (i,j)
                #print("pos at i j changed")
                #print("++++++++++++++++++++++++++++")
                v = findGoodMove(board.copy(),comp(turn),depth)
                val = v[0]
                new.val = val

                new.depth = v[2]+1
                dlist.append(new.depth)
                print(new)
                noD[new]=1
                #print(v)
                v=(v[0],(i,j),v[2])
                #print("v: ",v)

                if turn =="x":
                    if v[0] not in h:
                        h[v[0]] = (v[1],new.depth)
                    elif v[0] in h and v[0]==1 and new.depth<h[v[0]][1]:
                        h[v[0]] = (v[1], new.depth)
                    elif v[0] in h and v[0] !=1 and new.depth > h[v[0]][1]:
                        h[v[0]] = (v[1], new.depth)

                if turn =="o":
                    if v[0] not in h:
                        h[v[0]] = (v[1],new.depth)
                    elif v[0] in h and v[0]==-1 and new.depth<h[v[0]][1]:
                        h[v[0]] = (v[1], new.depth)
                    elif v[0] in h and v[0]!=-1 and new.depth>h[v[0]][1]:
                        h[v[0]] = (v[1], new.depth)


                if tmp==1:
                    d[(i,j)] = v[0],new.depth
                #print(tmp," )val got   for turn ",turn, " at ", i,j,"at depth: ",new.depth," is ",val)
                #print("removing: ",turn," at ",i,j)
                #print(h)
                board[i][j]=""

                if val>maxbest and turn=="x":
                    maxbest = val
                    maxtup = (i,j)
                    maxdepth = new.depth
                elif val<minbest and turn=="o":
                    minbest = val
                    mintup = (i,j)
                    maxdepth = new.depth
    if turn=="x":
        return maxbest,h[maxbest][0],h[maxbest][1]
    if turn == "o":
        return minbest, h[minbest][0], h[minbest][1]











    """elif turn=="x" and maxbest==-1:
        minip=-1
        for i in h:
            if h[i][1]>minip:
                print(i,h[i])
                minip=h[i][2]
                maxtup=h[i]
        return maxbest,maxtup,depth+1"""

    """elif turn =="o" and minbest==1:
        minip = -1
        for i in h:
            print(i,h[i])
            if h[i][1] > minip:
                minip = h[i][2]
                mintup = h[i]
        return minbest, mintup,depth+1"""





board=[["x","o",""],
       ["","",""],
        ["","",""]]


turn = "x"


a=findGoodMove(board,turn,0)
print(a)
b=a[1]
board[b[0]][b[1]]=turn
print()
l=[]
m=[]
draw=[]

print(d)
print()









