n = int(input())
t= int(input())
f = {}
for i in range(n):
    f[i+1] = set()
for i in range(t):
    a,b = map(int, input().split())
    f[a].add(b)
    f[b].add(a)
ans = set(f[1])
for i in f[1]:
    ans.update(f[i])

print(len(ans)-1)