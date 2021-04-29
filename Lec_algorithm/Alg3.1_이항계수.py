import time

#from numpy import *
#import numpy as np
def bin(n,k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n-1,k-1)+bin(n-1,k)

def bin2(n,k):
    #shape = (n+1,n+1)
    #b = np.empty(shape)
    #B = [[0]*(k+1) for _ in range(n+1)]
    b = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(n+1):
        small = min(i,k)
        for j in range(small+1):
            if j==0 or j == i:
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j-1]+b[i-1][j]
    return b[n][k]



print(bin(10,5), bin2(10,5))

# 더 오래걸림
start = time.time()
res = bin(30,10)
end = time.time()
print(res, end-start)

start = time.time()
res = bin2(30,10)
end = time.time()
print(res, end-start)


