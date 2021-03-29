t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    apt = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        apt[0][i] = i
    for i in range(1,k+1):
        for j in range(1,n+1):
            for p in range(1,j+1):
                apt[i][j] += apt[i-1][p]
    print(apt[k][n])