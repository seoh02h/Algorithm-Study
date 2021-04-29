import time
def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1)+fib1(n-2)

#for i in range(10):
#    print( f'{i:2d} {fib1(i): 6d}')
for i in range(30,36):
    stime =  time.time()
    fib1(i)
    etime = time.time()
    print( f'{i:2d}{etime-stime:10.5f}')