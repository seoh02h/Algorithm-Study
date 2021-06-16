s = [5,4,3,2,1]
n = len(s)
for i in range(0, n - 1):
    smallest = i
    for j in range(i + 1, n):
        if (s[j] < s[smallest]):
            smallest = j
    temp = s[i]
    s[i] = s[smallest]
    s[smallest] = temp

print(s)
