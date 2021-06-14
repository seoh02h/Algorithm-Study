def kp(i, profit, weight):
    global bestset
    global maxp

    if (weight <= W and profit > maxp):
        maxp = profit
        bestset = include[:]
    # best = include는 best를 include의 reference로 만든다.
    # 한 번 동일한 값을 가진 후 그 이후는 계속 동일함.
    if (promising(i, weight, profit)):
        include[i + 1] = 1
        kp(i + 1, profit + p[i + 1], weight + w[i + 1])
        include[i + 1] = 0
        kp(i + 1, profit, weight)


def promising(i, weight, profit):
    global maxp

    if (weight >= W):
        return False
    else:
        bound = profit
        totweight = weight
        j = i + 1
        while (j <= n - 1 and totweight + w[j] <= W):
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if (k <= n - 1):
            bound += (W - totweight) * p[k] / w[k]
        return bound > maxp

print('\n(1)')
n = 4
W = 8
p = [48, 55, 16, 16]
w = [4, 5, 4, 8]
maxp = 0
include = [0, 0, 0, 0]
bestset = [0, 0, 0, 0]
kp(-1, 0, 0)
print(maxp)
print(bestset)


import queue

class Node:
        def __init__(self,level,weight, profit, bound, include):
                self.level = level
                self.weight = weight
                self.profit = profit
                self.bound = bound
                self.include = include
        def __cmp__(self, other):
               return cmp(self.bound, other.bound)


def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n * [0]
    v = Node(-1, 0, 0, 0.0, temp)
    q = queue.PriorityQueue()
    v.bound = compBound(v)
    q.put((v.bound, v))
    while not q.empty():
        v.bound, v = q.get()
        if (v.bound < maxProfit):
            u = Node(0, 0, 0, 0.0, temp)
            u.level = v.level + 1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            u.include = v.include[:]
            u.include[u.level] = 1
            u.bound = compBound(u)
            if u.weight <= W and u.profit > maxProfit:
                maxProfit = -u.profit
                bestset = u.include[:]

            if u.bound < maxProfit:
                q.put((u.bound, u))
            u = Node(0, 0, 0, 0.0, temp)
            u.weight = v.weight
            u.profit = v.profit
            u.include = v.include[:]
            u.level = v.level + 1
            u.bound = compBound(u)
            if u.bound < maxProfit:
                q.put((u.bound, u))

def compBound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while (j <= n - 1 and totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if (k <= n - 1):
            result += (W - totweight) * p[k] / w[k]
        return -result


print('\n(2)')
n = 4
W = 8
p = [48, 55, 16, 16]
w = [4, 5, 4, 8]
include = [0] * n
maxProfit = 0
bestset = n * [0]
kp_Best_FS()
print(bestset)
print(maxProfit)

