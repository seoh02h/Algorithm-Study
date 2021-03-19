n = int(input())
num = list(map(int, input().split()))

def Isprime(x):
    n = 2
    flag =1
    if(x == 1 ):
        return False
    elif(x == 2):
        return True

    while(n<x):
        if x % n == 0:
            return False
        else:
            n += 1
    return True
cnt = 0
for e in num:
    if(Isprime(e)):
        cnt += 1
print(cnt)