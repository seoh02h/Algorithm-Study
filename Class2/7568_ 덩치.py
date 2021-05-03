n = int(input())
info = []
rank =[0]*n
for i in range(n):
    x,y = map(int, input().split())
    info.append((x,y))

for i in range(n):
    for j in range(n):
        if(info[i][0]<info[j][0] and info[i][1]<info[j][1]):
            rank[i] += 1
for i in rank:
    print(i+1, end=' ')