s = [3, 2, 5, 7, 1, 9, 4, 6, 8]
n = len(s)
for i in range(n - 1, -1, -1):
    for j in range(1, i + 1):
        if (s[j - 1] > s[j]):
            temp = s[j]
            s[j] = s[j - 1]
            s[j - 1] = temp

print(s)
