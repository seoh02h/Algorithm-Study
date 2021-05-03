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


def path(q, r):
    if p[q][r] != 0:
        sum.append()
        path(q,p[q][r])
        print(' v'+str(p[q][r]),end=" ")
        path(p[q][r],r)

def printMatrix(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()

inf=1000
n, p, k = map(int, input().split())
g=[[inf]*(n+1) for _ in range(n+1)]
for i in range(p):
    a,b,c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c

sum = []

d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
print()

path(1,n)


