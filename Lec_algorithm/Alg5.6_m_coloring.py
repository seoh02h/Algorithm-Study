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
