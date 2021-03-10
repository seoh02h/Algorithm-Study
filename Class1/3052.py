n = 42
l = list()
cnt = 0
for i in range(10):
    num = int(input())
    l.append(num%n)

l = set(l)
print(len(l))