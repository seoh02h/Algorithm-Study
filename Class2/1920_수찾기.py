n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
num = list(map(int,input().split()))
for e in num:
    low = 0
    high = n-1
    flag = 1
    while(low<=high):
        mid = (low+high)//2
        if(e == A[mid]):
            print(1)
            flag = 0
            break
        elif (e > A[mid]):
            low = mid + 1
        else:
            high = mid -1
    if(flag):
        print(0)