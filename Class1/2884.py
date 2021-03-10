h, m = map(int, input().split())
if(m-45 <0):
    h -= 1
    if(h<0):
        h = 23
    m = 60+(m-45)
else:
    m -= 45
print(str(h)+" "+str(m))