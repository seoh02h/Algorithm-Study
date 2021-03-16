cnt = 1
while(True):
    l, p, v = map(int, input().split())
    if (l+p+v == 0):
        break
    ans = v//p * l
    if(v%p > l):
        ans += l
    else:
        ans += v%p
    print(f'Case {cnt}: {ans}')
    cnt += 1