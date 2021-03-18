n = int(input())
l = []
for i in range(n):
    x,y = map(int, input().split())
    l.append((x,y))
l.sort(key = lambda e : (e[0], e[1]))
for x, y in l:
    print(x, y)
