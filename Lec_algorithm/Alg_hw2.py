global flag
global sum

def mergeSort(n, s):
    h = n//2
    m = n-h
    global flag
    global sum
    if n > 1:
        u = s[:h]
        v = s[h:]
        if(flag):
            sum += len(u) + len(v)
            #print(f'A: {len(u)}, B: {len(v)}')
            #print(f'추가공간 = {sum}')
        if(len(u)==1):
            flag = 0
        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)



def merge(h, m, u, v, s):
    i=0
    j=0
    k=0
    while (i < h and j < m):
        if(u[i]<v[j]):
            s[k]=u[i]
            i += 1
        else:
            s[k] = v[j]
            j+=1
        k+= 1
    if i >= h:
        s[k:h+m] = v[j:m]
    else:
        s[k:h+m] = u[i:h]


def mergeSort2(s, low, high):
    if(low < high):
        mid = (low+high)//2
        mergeSort2(s,low,mid)
        mergeSort2(s,mid+1, high)
        merge2(s, low, mid, high)


def merge2(s, low, mid, high):
    i = low
    j = mid+1
    k = low
    u = [0]*(high - low + 1)
    global sum

    if(sum <len(u)):
        sum += (len(u)-sum)
        #print(f'추가공간 : {sum}')
    while(i<=mid and j <= high):
        if s[i]<s[j]:
            u[k-low] = s[i]
            i += 1
        else:
            u[k-low]= s[j]
            j += 1
        k+=1
    if(i>mid):
        u[k-low:high-low+1] = s[j:high+1]
    else:
        u[k-low:high-low+1] = s[i:mid+1]
    s[low:high+1] = u[low-low:high-low+1]



sum = 0
flag = 1
s =  [3, 16, 13, 1, 9, 2, 7, 5, 8, 4, 11, 6, 15, 14, 10, 12]
print("합병정렬 1")
mergeSort(len(s), s)
print(f'필요한 추가 저장공간 : {sum}')
print(f'결과 : {s}')

print()
sum = 0
s =  [3, 16, 13, 1, 9, 2, 7, 5, 8, 4, 11, 6, 15, 14, 10, 12]
print("합병정렬 2")
mergeSort2(s, 0, len(s)-1)
print(f'필요한 추가 저장공간 : {sum}')
print(f'결과 : {s}')