def BS(A,n):
    low = 0
    high = len(A)-1
    find = 0
    while(low<= high):
        mid = (low + high)//2
        if A[mid]> n:
            high = mid -1
        elif A[mid]< n:
            low = mid + 1
        else:
            find = 1
            break
    if(find):
        print(1)
    else:
        print(0)

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))

for i in B:
    BS(A,i)