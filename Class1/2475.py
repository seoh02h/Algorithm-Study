num = list(map(int, input().split()))
res = 0
for n in num:
    res += n*n
print(res%10)