while(True):
    num = list(map(int, input().split()))
    if(sum(num) ==0):
        break
    else:
        m = max(num)
        num.remove(m)
        if(m**2 == num[0]**2 + num[1]**2):
            print('right')
        else:
            print('wrong')