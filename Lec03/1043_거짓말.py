
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y]=x
    else:
        parent[x]=y

party = []
cnt = 0

N, M = map(int, input().split())
t = list(map(int, input().split()))
t = (t[1:])
parent =[i for i in range(N+1)]

if(len(t) == 0 ):
    print(0)
else:
    t_fix = t[0]
    t = set(t)
    for i in t:
        union(t_fix,i)

    for i in range(M):
        flag = 1
        p = list(map(int, input().split()))
        p = p[1:]
        party.append(p)
        for j in party[i]:
            if j in t:
                t = t.union(set(party[i]))
                flag = 0
                break
        if flag:
            fix = party[i][0]
            for k in party[i]:
                union(fix,k)
        else:
            for k in party[i]:
                union(t_fix, k)

    for i in range(N):
        if find(t_fix)==find(i):
            t.add(i)

    for i in range(M):
        for j in party[i]:
            if j in t:
                break
        else: cnt +=1

    print(cnt)
