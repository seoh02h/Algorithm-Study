t = int(input())
l = list(map(int, input().split()))
l.sort()
sum = 0
for i in range(t):
    sum += l[i]*(t-i)

print(sum)