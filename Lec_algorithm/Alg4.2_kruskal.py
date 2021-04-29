parent = dict()
rank = dict()

def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

def find(v):
    if parent[v] != v:
        parent[v]=find(parent[v])
    return parent[v]

def union(r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += rank[r1]

def kruskal(graph):
    for v in graph['vertices']:
        make_singleton_set(v)
    mst = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, v1, v2 = edge
        r1 = find(v1)
        r2 = find(v2)
        if r1 != r2:
            union(r1, r2)
            mst.add(edge)
    return mst



graph = {
        'vertices' : ['A', 'B', 'C', 'D', 'E'],
        'edges' : set([(1, 'A', 'B'),
                       (3, 'A', 'C'),
                       (3, 'B', 'C'),
                       (6, 'B', 'D'),
                       (4, 'C', 'D'),
                       (2, 'C', 'E'),
                       (5, 'D', 'E'),
                       ])
        }
mst = kruskal(graph)
print(mst)
