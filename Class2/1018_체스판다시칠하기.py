n, m = map(int, input().split())
board = [[] for i in range(n)]
for i in range(n):
    tmp = list(input())
    board[i].extend(tmp)

# B
B_cnt = [[0]*m for i in range(n)]
flag = 1
for i in range(n):
    if(i%2 == 1):
        flag = 1
    else:
        flag = 0
    for j in range(m):
        if(flag):
            if(board[i][j] != 'B'):
                B_cnt[i][j] = 1
            flag = 0
        else:
            if(board[i][j] != 'W'):
                B_cnt[i][j]=1
            flag = 1

# w
W_cnt = [[0]*m for i in range(n)]
for i in range(n):
    if(i%2 == 1):
        flag = 1
    else:
        flag = 0
    for j in range(m):
        if(flag):
            if(board[i][j] != 'W'):
                W_cnt[i][j] = 1
            flag = 0
        else:
            if(board[i][j] != 'B'):
                W_cnt[i][j]=1
            flag = 1

tmp = 0
min = 1000000
for i in range(n-7):
    for j in range(m-7):
        tmp = 0
        for k in range(8):
            tmp += sum(B_cnt[i+k][j:j+8])
        if(min>tmp):
            min = tmp

for i in range(n-7):
    for j in range(m-7):
        tmp = 0
        for k in range(8):
            tmp += sum(W_cnt[i + k][j:j + 8])
        if(min>tmp):
            min = tmp
print(min)
