def orangesRotting( grid):
    r1 = [1, -1, 0, 0]
    r2 = [0, 0, 1, -1]
    t = 0

    # Code here
    n = len(grid)
    m = len(grid[0])
    l1 = []
    t = 0


    l2 = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 or grid[i][j] == 1:
                continue
            else:
                l2.append((i, j))

    while len(l2) > 0:
        print("start SET:::::::")
        print("locate start: ",end=" ")
        for i in l2:
            print( i,end=" ")
        print()
        flag = 0
        for p in l2.copy():
            print("2 at ",p[0],p[1])


            print("fresh oranges found at::")
            for k in range(4):
                a = p[0] + r1[k]
                b = p[1] + r2[k]
                if 0 <= a < n and 0 <= b < m and grid[a][b] == 1:
                    flag = 1
                    print("rotting-",a,b)
                    grid[a][b] = 2

                    l2.append((a, b))
            grid[p[0]][p[1]]=0
            l2.remove(l2[0])
        if flag == 1:
            t += 1
            print("t +=1 :, current time: ",t)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1
    return t

grid = [[0,2]]


"""for i in range(3):
    for j in range(3):
        print(grid[i][j],end=" ")
    print()"""
print("____________________________________")
print(orangesRotting( grid))
