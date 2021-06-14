def promising(i,weight, total):
    return ((weight+total >= W) and (weight==W or weight+w[i+1] <=W))

def s_s(i, weight, total, include):
    if(promising(i, weight, total)==True):
        if(weight == W):
            print("include",include )
            print('해 :',end=' ')
            for i in range(0,n):
                if include[i]==1:
                    print(str(w[i])+", ", end=' ')
            print('\n')
        else:
            include[i+1]=1
            s_s(i+1, weight+w[i+1],total-w[i+1],include)
            include[i+1]=0
            s_s(i+1,weight,total-w[i+1],include)

n=6
w=[1,2,3,4,5,6]
w.sort()
W=9
print("items =",w, "W =", W)
include = n*[0]
total=0
for k in w:
    total+=k

s_s(-1,0,total,include)


def color(i,vcolor):
    if(promising(i,vcolor)):
        if(i==n-1):
            print(vcolor)
        else:
            for c in range(1,m+1):
                vcolor[i+1]=c
                color(i+1,vcolor)

def promising(i,vcolor):
   switch=True
   j=0
   while(j<i and switch):
        if(W[i][j] and vcolor[i]==vcolor[j]):
           switch = False
        j+=1
   return switch

n=4
W=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
vcolor=n*[0]
m=3
color(-1,vcolor)
