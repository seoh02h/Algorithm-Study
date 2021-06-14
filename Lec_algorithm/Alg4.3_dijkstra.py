inf=1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],
   [inf,2,0,5,inf], [inf,3,inf,0,inf], [inf,inf,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]

save_length=n*[0]

NoC = 0 #총 아크 수 = 출발점에 연결된 아크 수

for i in range(1,n):
    length[i]=w[0][i]

for k in range(n-1):
    min = inf
    for i in range(1,n):
        if( 0 <= length[i] and length[i]<min):
            min = length[i]
            vnear=i
    print(vnear+1)

    save_length[vnear] = length[vnear]

    e = (touch[vnear],vnear)
    f.add(e)

    for i in range(1,n):
        if w[vnear][i]>0 and w[vnear][i]<inf: #vnear에서 i로 연결 아크가 있는지
            NoC = NoC+1
        if length[vnear]+w[vnear][i] < length[i]: # 이 부분을 수행하는 횟수는 length[]를 update하는 최대 횟수
            length[i] = length[vnear] + w[vnear][i]
            touch[i] = vnear
    length[vnear] = -1

print(f)
print(save_length)
print(NoC)