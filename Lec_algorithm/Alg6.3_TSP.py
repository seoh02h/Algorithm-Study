#Traveling Salesman(person) Problem
#외판원 문제


import queue


class Node:
    def __init__(self, bound, path):
        self.bound = bound
        self.path = path


#        def __cmp__(self, other):
#               return cmp(self.bound, other.bound)

def TSP_Best_FS():
    global minLength
    global optTour
    path = [start]
    v = Node(0, path)

    v.bound = compBound(v)
    q = queue.PriorityQueue()
    q.put((v.bound, v.path))
    while not q.empty():
        v.bound, v.path = q.get()
        if (v.bound < minLength):
            if len(v.path) == n - 1:
                A = v.path[:]
                B = [x for x in V if x not in A]
                C = [x for x in B if x != start]
                if compLength(v.path) + W[v.path[n - 2]][C[0]] + W[C[0]][start] < minLength:
                    minLength = compLength(v.path) + W[v.path[n - 2]][C[0]] + W[C[0]][start]
                    optTour = v.path[:] + [C[0]]
            else:
                C = [x for x in V if x not in v.path]
                for x in C:
                    u = Node(0, v.path + [x])
                    u.bound = compBound(u)
                    print("path bound ", u.path, u.bound)
                    if u.bound < minLength:
                        q.put((u.bound, u.path))

def compBound(u):
    global start
#  if len(u.path)==n-1:
#      print(" uPP ", u.path, u.path[n-2],compLength(u.path), W[u.path[n-2]][start])
#      return compLength(u.path)+W[u.path[n-2]][start]
#  else:
    tbound = 0
    A = u.path[:]
    B = [x for x in A if x != start]
    C= [x for x in V if x not in A]
    temp1=0
    tMin=10000
    for y in C:
        if W[u.path [ len(u.path)-1]][y] < tMin:
          tMin = W[u.path [ len(u.path)-1]][y]
    tbound += tMin
    for y in C:
       tMin = 10000
       D = [ x for x in C if x != y]
       D.append(start)
       for z in D:
         if W[y][z]<tMin:
           tMin=W[y][z]
       tbound += tMin
    return tbound+compLength(u.path)


def compLength(a):
  length =0
  for x in range (0,len(a)-1):
    length += W[a[x]][a[x+1]]
  return length

start =0
n=5
W=[[0,14,4,10,20],[14,0,7,8,7],[4,5,0,7,16],
  [11,7,9,0,2],[18,7,17,4,0]]
V=list()
for x in range(0,n):
  V.append(x)
optTour=list()
print(V)
minLength=10000
TSP_Best_FS()
print(minLength)
print(optTour)
