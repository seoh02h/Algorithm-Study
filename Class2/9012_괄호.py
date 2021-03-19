import sys
n = int(input())
for i in range(n):
    str = list(input())
    cnt = 0
    for s in str:
        if( s == '('):
            cnt += 1
        else :
            cnt -=1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')