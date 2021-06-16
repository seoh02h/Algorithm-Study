s=[5,4,3,2,1]
n = len(s)
total_cnt = 0
for i in range (1,n):
    print("---cnt :",i,"---")
    x = s[i]
    j=i-1
    while j>=0 and s[j] > x:
        s[j+1]=s[j]
        print(s)
        j -= 1
        total_cnt+=1
    print("x :",x)
    s[j+1]=x
    print("fin :",s)
print(s)

##comparisions
# worst : n(n-1)/2
# avg : n^2 / 4
print(total_cnt)
