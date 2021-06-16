def mergeSort(n, s):
    h=int(n/2)
    m=n-h
    u=h*[0]
    v=m*[0]

    if(n>1):
        leftHalf=s[:h]
        rightHalf=s[h:]
        mergeSort(h,leftHalf)
# h=len(leftHalf)
        mergeSort(m,rightHalf)
        merge(h,m,leftHalf,rightHalf,s)

def merge(h,m,u,v,s):
    i=j=k=0
    while(i<=h-1 and j<=m-1):
        if(u[i]<v[j]):
           s[k]=u[i]
           i+=1
        else:
           s[k]=v[j]
           j+=1
        k+=1
    if(i>h-1):
           for ii in range (j,m):
                s[k+ii-j]=v[ii]
    else:
           for ii in range (i,h):
              s[k+ii-i]=u[ii]

s=[3,5,2,9,10,14,4,8]
mergeSort(8,s)
print(s)
