mul = 1
for i in range(3):
    tmp = int(input())
    mul *= tmp
mul = list(str(mul))
for i in range(10):
    print(mul.count(str(i)))