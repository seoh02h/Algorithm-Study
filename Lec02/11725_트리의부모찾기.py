from collections import deque

n = int(input())
node = [0 for _ in range(n+1)]

adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = deque()
q.append(1)
node[1] = 1
while q:
    cur = q.pop()
    for i in adj[cur]:
        if node[i]==0:
            node[i] = cur
            q.append(i)
for i in range(2,n+1):
    print(node[i])