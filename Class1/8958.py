t = int(input())

for i in range(t):
    cnt = 1
    sum = 0
    str = input()
    for s in str:
        if (s == 'O'):
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
