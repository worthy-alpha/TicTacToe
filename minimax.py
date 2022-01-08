





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
def comp(turn):
    s = {"o","x"}
    t = set(turn)
    k = s-t
    k=str(k)[2:3]
    return k


def findGoodMove(board,turn):
    global rc,d
    rc+=1
    maxbest=-1000000000
    maxtup=0
    mintup=0
    minbest=1000000000
    tmp = rc
    r1 = result(board,turn)
    r2 = result(board,comp(turn))
    #print()
    #for i in board:

        #print(i)
    #print()
    #print("turn: ",turn)

    if r1 :
        #print("won")
        if turn == "x": return 1,None
        if turn == "o": return -1,None
    elif r2:
        #print("won")
        if turn == "x": return -1,None
        if turn == "o": return 1,None
    if draw(board): return 0,None

    for i in range(len(board)):
        for j in range(len(board)):
            #print("at location for ",turn,i,j, board[i][j])
            if board[i][j]=="":
                #print(rc,")empty at ",i,j, " for ",turn)
                board[i][j]=turn
                #print("pos at i j changed")
                #print("++++++++++++++++++++++++++++")
                v = findGoodMove(board.copy(),comp(turn))
                val = v[0]
                v=(v[0],(i,j))
                if tmp==1:
                    d[(i,j)] = v[0]
                #print(tmp," )val got for " ,turn, " at ", i,j," : ",v)
                #print("removing: ",turn," at ",i,j)
                board[i][j]=""
                if turn == "x" and val>maxbest:

                    maxbest=val
                    maxtup=(i,j)
                elif turn=="o" and val<minbest:
                    minbest = val
                    mintup = (i,j)
    if turn == "x":
        return maxbest,maxtup
    return minbest,mintup















board=[["","",""],
       ["","",""],
        ["","",""]]


turn = "x"


a=findGoodMove(board,turn)
print(a)
b=a[1]
board[b[0]][b[1]]=turn
print()
l=[]
m=[]
draw=[]
for i in d:
    if d[i]>0 and turn=="x":
        l.append(i)
    elif d[i]<0 and turn=="o":
        m.append(i)
    if d[i]==0:
        draw.append(i)
print()
print(d)
if turn == "o":
    print("x turn:")
    print("number of optimal moves are: ",len(l))
    for i in l:
        print(i)
print()
if turn == "o":
    print("o turn:")
    print("number of optimal moves are: ", len(m))
    for i in m:
        print(i)
print()
print("number of draw moves are: ",len(draw))
for i in draw:
    print(i)
print()
for i in board:
    print(i)
print()








