def promising(i,weight, total):
    return ((weight+total >= W) and (weight==W or weight+w[i+1] <=W))

def s_s(i, weight, total, include):
    global cnt_node
    cnt_node += 1
    if(promising(i, weight, total)==True):

        if(weight == W):
            print("sol",include )
        else:
            include[i+1]=1
            s_s(i+1, weight+w[i+1],total-w[i+1],include)
            include[i+1]=0
            s_s(i+1,weight,total-w[i+1],include)

n=4
w=[1, 2, 8, 4]
w.sort()
W=6
global cnt_node
cnt_node = 0
print("items =",w, "W =", W)
include = n*[0]
total=0
for k in w:
    total+=k
s_s(-1,0,total,include)
print("node : ",cnt_node)
