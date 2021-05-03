n = int(input())

num = 666
res = 0
while(True):
    if "666" in str(num):
        res += 1
        if(res == n):
            print(num)
            break
    num +=1
