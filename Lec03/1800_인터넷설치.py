import sys
import heapq

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now]< wei:
            continue
        for w, next_node in graph[now]:
            next_wei = w+wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
        print(dp)

n, p, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
inf = 100000000
dp=[inf]*(n+1)
heap = []
for i in range(p):
    a,b,c =  map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

Dijkstra(1)
print(dp)
print(dp[n])