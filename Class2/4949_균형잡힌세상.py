from collections import deque

a = deque()

while(True):
    s = list(input())
    if(s[0]=='.'):
        break
    flag = 0
    a.clear()

    for i in s:
        if i == '[':
            a.append('[')
        elif i == ']':
            if(len(a) == 0 or a[-1]=='('):
                print('no')
                flag = 1
                break
            else:
                a.pop()
        elif i == '(':
            a.append('(')
        elif i ==')':
            if (len(a) == 0 or a[-1] =='['):
                print('no')
                flag = 1
                break
            else:
                a.pop()
    if len(a)== 0 and flag == 0:
        print('yes')
    else:
        if(flag ==0 ):
            print('no')
