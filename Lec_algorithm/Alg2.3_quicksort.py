def quickSort(s, low, high):
    if(high>low):
        pivotpoint = partition(s, low, high)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high)

def partition(s, low, high):
    pivotitem = s[low]
    j = low
    for i in range(low, high+1):
        if s[i]<pivotitem:
            j += 1
            s[i], s[j] = s[j], s[i]
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

s = [3, 4, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)