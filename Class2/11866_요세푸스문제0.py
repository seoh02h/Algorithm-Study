from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(n):
    s.append((i))
