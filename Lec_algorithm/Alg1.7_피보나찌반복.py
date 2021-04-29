import time

def fib2(n):
    f = [0]*(n+1)
    f[0] = 0
    if n > 0:
        f[1]=1
        for i in range(2,n+1):
            f[i] = f[i-1]+f[i-2]
    return f[n]


#for i in range(10):
#    print( f'{i:2d} {fib2(i): 6d}')

for i in range(30,36):
    stime =  time.time()
    fib2(i)
    etime = time.time()
    print( f'{i:2d}{etime-stime:10.5f}')
