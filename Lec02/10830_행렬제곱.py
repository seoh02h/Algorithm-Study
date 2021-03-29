n,b = map(int, input().split())
mat = []
for i in range(n):
    tmp = list(map(int, input().split()))
    mat.append(tmp)

res=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j):
            res[i][j] = 1

while(b>0):
    if(b%2 ==1):
        tmp = [[0] * (n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp[i][j] += res[i][k]*mat[k][j]
        for i in range(n):
            for j in range(n):
                res[i][j] = tmp[i][j]%1000
    b //= 2
    tmp = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += mat[i][k] * mat[k][j]
    for i in range(n):
        for j in range(n):
            mat[i][j] = tmp[i][j]%1000


for i in range(n):
    for j in range(n):
        print(res[i][j], end=" ")
    print()





