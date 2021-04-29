def allShortestPath(g,n):
    d=g
    p=[[0 for i in range(n+1)]for i in range(n+1)]
    printMatrix(d)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j]=d[i][k]+d[k][j]
                    p[i][j]=k
    # node number는 1부터 n
    return d, p

def printMatrix(d):
    n=len(d[1])
    for i in range(1,n):
        for j in range(1,n):
            print(d[i][j],end=" ")
        print()

def path(q, r):
    if p[q][r] != 0:
        path(q,p[q][r])
        print(' v'+str(p[q][r]),end=" ")
        path(p[q][r],r)

inf=1000
g=[[],[0,0,1,inf, 1,5],
   [0,9,0,3,2,inf],
   [0,inf,inf,0,4,inf],
   [0,inf,inf,2,0,3],
   [0,3,inf,inf,inf,0]]
d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
print()
path(5,3)


