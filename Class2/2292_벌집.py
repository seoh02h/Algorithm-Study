n = int(input())
res = 2
cnt = 1
while(True):
    if(n < res ):
        print(cnt)
        break
    res += cnt * 6
    cnt += 1
