import random
import time

def exchange_sort(n):
    s = list()
    for i in range(n):
        s.append(random.randrange(1, 101))
    start_time = time.time()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[j] < s[i]:
                s[i], s[j] = s[j], s[i]
    end_time = time.time()
    print(f'exchange sort : {n:7d} {end_time-start_time:10f}')


def mergeSort(n, s):
    h = n//2
    m = n-h
    if n > 1:
        u = s[:h]
        v = s[h:]
        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)

def merge(h, m, u, v, s):
    i=0
    j=0
    k=0

    while (i < h and j < m):
        if(u[i]<v[j]):
            s[k]=u[i]
            i += 1
        else:
            s[k] = v[j]
            j+=1
        k+= 1
    if i >= h:
        s[k:h+m] = v[j:m]
    else:
        s[k:h+m] = u[i:h]

def merge_sort(n):
    s = list()
    for i in range(n):
        s.append(random.randrange(1, 101))
    start_time = time.time()
    mergeSort(n, s)
    end_time = time.time()
    print(f'merge sort : {n:10d} {end_time - start_time:10f}')

exchange_sort(2000)
exchange_sort(4000)
exchange_sort(12000)
print()
merge_sort(2000)
merge_sort(4000)
merge_sort(12000)

