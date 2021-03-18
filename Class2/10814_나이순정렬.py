n = int(input())
mem = list()
for i in range(n):
    age, name = input().split()
    mem.append((int(age),name))
mem.sort(key = lambda member:(member[0]))
for age,  name in mem:
    print(age, name)