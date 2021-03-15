t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h +1
    if a == 0:
        a = h
        b -= 1
    print(a*100+b)