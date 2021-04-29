
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
    u = [0]*(high+1)

    while(i<=mid and j <= high):
        if s[i]<s[j]:
            u[k] = s[i]
            i += 1
        else:
            u[k]= s[j]
            j += 1
        k+=1
    if(i>mid):
        u[k:high+1] = s[j:high+1]
    else:
        u[k:high+1] = s[i:mid+1]
    s[low:high+1] = u[low:high+1]




s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSort2(s, 0, 7)
print(s)