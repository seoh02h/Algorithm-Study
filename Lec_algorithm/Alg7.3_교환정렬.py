s = [5,4,3,2,1]
n = len(s)
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if (s[j] < s[i]):
            cnt +=1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

print(s)
print(cnt)
