
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

                #print("pos at i j changed")
                #print("++++++++++++++++++++++++++++")
                v = findGoodMove(board.copy(),comp(turn),depth)
                val = v[0]


                newdepth = v[2]+1


                #print(v)
                v=(v[0],(i,j),v[2])
                #print("v: ",v)

                if turn =="x":
                    if v[0] not in h:
                        h[v[0]] = (v[1],newdepth)
                    elif v[0] in h and v[0]==1 and newdepth<h[v[0]][1]:
                        h[v[0]] = (v[1], newdepth)
                    elif v[0] in h and v[0] !=1 and newdepth > h[v[0]][1]:
                        h[v[0]] = (v[1], newdepth)

                if turn =="o":
                    if v[0] not in h:
                        h[v[0]] = (v[1],newdepth)
                    elif v[0] in h and v[0]==-1 and newdepth<h[v[0]][1]:
                        h[v[0]] = (v[1], newdepth)
                    elif v[0] in h and v[0]!=-1 and newdepth>h[v[0]][1]:
                        h[v[0]] = (v[1], newdepth)



                #print(tmp," )val got   for turn ",turn, " at ", i,j,"at depth: ",new.depth," is ",val)
                #print("removing: ",turn," at ",i,j)
                #print(h)
                board[i][j]=""

                if val>maxbest and turn=="x":
                    maxbest = val

                    maxdepth = newdepth
                elif val<minbest and turn=="o":
                    minbest = val

                    maxdepth = newdepth
    if turn=="x":
        return maxbest,h[maxbest][0],h[maxbest][1]
    if turn == "o":
        return minbest, h[minbest][0], h[minbest][1]



board=[["x","o",""],
       ["","",""],
        ["","",""]]


turn = "x"


a=findGoodMove(board,turn,0)

print(a)

b=a[1]
print(turn," at ",b)

board[b[0]][b[1]]=turn
for i in board:
    print(i)












