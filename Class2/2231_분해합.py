n = int(input())

for i in range(1,n+1):
    res = 0
    a = list(map(int, str(i)))
    res += i +sum(a)
    if res == n:
        print(i)
        break
    if i == n :
        print(0)
