a = [[0,0,2,0,0,0,0,2,0],
     [0,0,0,0,2,2,2,0,0],
     [2,0,2,0,2,2,0,2,2],
     [0,0,0,0,0,0,0,0,0],
     [2,0,2,2,0,2,2,2,0],
     [2,0,0,2,2,0,0,0,0],
     [0,0,2,2,2,2,0,2,0],
     [0,2,0,2,0,2,2,2,2],
     [0,0,0,0,0,0,0,0,0]]

N= 9

start = (0,0)
stack = [start]
import matplotlib.pyplot as plt


m = a[:]
for i in range(len(m)):
    m[i] = a[i].copy()

def DFS(m,start):

    r,c = start[0],start[1]
    #plt.imshow(mat)
    #plt.show()
    m[r][c] = 3

    if r < N-1 and m[r+1][c] == 0:
        if (r+1,c) not in stack:
            stack.append((r+1,c))
            DFS(m,(r+1,c))

    if r > 0 and m[r-1][c] == 0:
        if (r-1,c) not in stack:
            stack.append((r-1,c))
            DFS(m,(r-1,c))

    if c < N-1 and m[r][c+1] == 0:
        if (r,c+1) not in stack:
            stack.append((r,c+1))
            DFS(m,(r,c+1))

    if c > 0 and m[r][c-1] == 0:
        if (r,c-1) not in stack:
            stack.append((r,c-1))
            DFS(m,(r,c-1))



#DFS(m,start)


a = [[0,0,2,0,0,0,0,2,0],
     [0,0,0,0,2,2,2,0,0],
     [2,0,2,0,2,2,0,2,2],
     [0,0,0,0,0,0,0,0,0],
     [2,0,2,2,0,2,2,2,0],
     [2,0,0,2,2,0,0,0,0],
     [0,0,2,2,2,2,0,2,0],
     [0,2,0,2,0,2,2,2,2],
     [0,0,0,0,0,0,0,0,0]]

N= 9

start = (0,0)
stack = [start]

def BFS(mat,start):
    level = {start:0}
    Adj = [start]
    r,c = start[0],start[1]
    # 반시계방향
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    L = 1
    while Adj:
        Next = []
        for v in Adj:
            for i in range(4):
                if 0<= v[0]+dx[i] < N and 0<= v[1]+dy[i] < N and (v[0]+dx[i] , v[1]+dy[i]) not in level:
                    x,y = v[0]+dx[i] , v[1]+dy[i]
                else:
                    continue
                
                if m[x][y] == 0:
                    mat[x][y] = 3
                        
                    plt.imshow(mat)
                    plt.show()
                    if (x,y) not in level:
                        level[(x,y)] = L
                        Next.append((x,y))
        

        print(Next)
        L+=1
        Adj = Next
    
BFS(m,start)
