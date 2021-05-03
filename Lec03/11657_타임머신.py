import sys

input = sys.stdin.readline


def bellmanFord():
    global isPossible

    for repeat in range(N):
        for i in range(1, N + 1):
            for wei, vec in adjList[i]:
                if dist[i] != INF and dist[vec] > dist[i] + wei:
                    dist[vec] = dist[i] + wei
                    if repeat == N - 1:
                        isPossible = False


N, M = map(int, input().split())
adjList = [[] for _ in range(N + 1)]
INF = 2147483647
dist = [INF] * (N + 1)
dist[1] = 0
isPossible = True

for _ in range(M):
    a, b, c = map(int, input().split())

    adjList[a].append((c, b))

bellmanFord()

if not isPossible:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d != INF else -1)