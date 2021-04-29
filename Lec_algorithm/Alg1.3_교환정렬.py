s = [3, 2, 5, 7, 1, 9, 4, 6, 8]
n = len(s)
for i in range(0, n - 1):
    for j in range(i+1, n):
        if s[j]<s[i]:
            s[i], s[j] = s[j], s[i]
print(s)
