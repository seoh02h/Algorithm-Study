
e = {0: [1, 2, 3], 1: [2, 5], 2: [3, 4, 5, 6], 3: [4, 6], 4: [6, 7]}
n = 8
a = [[0 for j in range(0, n)] for i in range(0, n)]
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1

#utility.printMatrix(a)

visited = n * [0]

global cnt
cnt = 1

def DFS(a, v):
    visited[v] = 1
    global cnt
    print(cnt,v)
    cnt += 1
    for x in range(0, n):
        if a[v][x] == 1 and visited[x] == 0:
            DFS(a, x)

DFS(a, 0)

global cnt2
cnt2 = 0
def promising(i,col):
    k=0
    switch=True
    while(k<i and switch==True):
       if(col[i]==col[k] or abs(col[i]-col[k])==i-k):
          switch=False
       k+=1
    return switch

def queens(n,i,col):
    global cnt2
    if (promising(i, col) == True):
        if (i == n - 1):
            cnt2 += 1
            if(cnt2 == 3):
                print(col)
        else:
            for j in range(0, n):
                col[i + 1] = j
                queens(n, i + 1, col)

n=7
col=n*[0]
queens(n,-1,col)
print('총 해의 개수 : ' +str(cnt2))
