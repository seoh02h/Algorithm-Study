n = int(input())
sum = 0
sum += n // 5
n = n%5
sum += n // 3
if( n%3 == 0 ):
    print(sum)
else:
    print(-1)