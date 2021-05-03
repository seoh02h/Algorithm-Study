import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    x,y = map(int, input().split())
    num.append((x,y))
num.sort(key=lambda x:(x[1],x[0]))
for x,y in num:
    print(x,y)