n = int(input())
net = {}
for i in range(1,n+1):
    net[i] = set()
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    net[a].add(b)
    net[b].add(a)

visited = []
def dfs(n):
    for i in net[n]:
        if i not in visited:
            visited.append(i)
            dfs(i)
dfs(1)
print(len(visited)-1)