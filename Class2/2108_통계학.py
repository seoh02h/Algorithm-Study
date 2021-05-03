import sys
from collections import Counter
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

print(round(sum(num)/n))
num.sort()
print(num[n//2])

cnt  = Counter(num).most_common()

if(n>1):
    if(cnt[0][1] ==cnt[1][1]):
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(num[-1]-num[0])