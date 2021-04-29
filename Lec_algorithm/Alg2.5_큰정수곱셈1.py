def prod1(a,b):
    threshold = 4
    n = max((len(str(a))),(len(str(b))))
    if (a == 0 or b == 0):
        return 0
    elif n <= threshold :
        return a*b
    else:
        m = int(n/2)
        x = a // 10**m
        y = a % 10**m
        w = b // 10**m
        z = b % 10**m
        return prod1(x,w)*10**(2*m)+(prod1(x,z)+prod1(w,y))*10**m+prod1(y,z)

a=1234567812345678
b=2345678923456789


print(prod1(a,b))
print(a*b)