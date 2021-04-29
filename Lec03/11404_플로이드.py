import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 100000000
g = [[inf]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    g[a][b] = min(c, g[a][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if j == k:
                g[j][k]=0
            else:
                g[j][k] = min(g[j][k],g[j][i]+g[i][k])

for i in range(1, n+1):
    for j in range(1,n+1):
        if g[i][j] == inf:
            print(0,end=' ')
        else:
            print(g[i][j], end=' ')
    print()