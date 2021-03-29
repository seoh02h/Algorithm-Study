d, n = map(int, input().split())
oven = list(map(int, input().split()))
dough = list(map(int, input().split()))


for i in range(1, d):
    oven[i] = min(oven[i], oven[i-1])

idx = 0
res = d-1
for i in reversed(range(d)):
    if idx >= len(dough):
        print(res + 1)
        exit()
    if(oven[i]>= dough[idx]):
        idx += 1
        res = i
print(0)

