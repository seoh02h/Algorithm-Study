'''
(1) 실습동영상 p6_dp_OBStree_alignment.pptx 10쪽: [실습프로그램] 최적이진검색트리 구축 알고리즘을 python으로 완성하라.

데이터는 A, B, C, D, E 이고 p1=4/15, p2=5/15, p3=1/15, p4=3/15, p5=2/15 문제의 답을 구하시오.
- 행렬 출력을 위해 포함되어 있는 utility를 사용하여도 되고, 별도로 필요한 프로그램을 작성하여도 됨. 단순히 출력형식을 지정하여 출력하여도 무방.

입력 데이터는 프로그램 내에 직접 넣어도 됨. 단, 입력 후 처리 프로그램은 데이터의 개수에 무관하게 작동하여야 함.


(2) 실습동영상 p6_dp_OBStree_alignment.pptx 29쪽: [실습프로그램] DNA 서열 맞춤 알고리즘 python으로 완성하라. 아래의 데이터를 이용한다.

a=['A','A','C','A','G','T','A','C','C']

b=['T','A','C','G','T','T','C','A']
'''


def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0, m):
        for j in range(0, n):
            print("%4d" % d[i][j], end=" ")
        print()


# print float matrix
def printMatrixF(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print("%5.2f" % d[i][j], end=" ")
        print()


def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)


def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p


key = [" ", "A", "B", "C", "D", "E"]
p = [0, 0.267, 0.333, 0.067, 0.2, 0.133]
n = len(p) - 1

a = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
r = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]

for i in range(1, n + 1):
    a[i][i - 1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i - 1] = 0
a[n + 1][n] = 0
r[n + 1][n] = 0

for d in range(1,n):
    for i in range(1, n-d+1):
        j = i+d
        tmp_min = 100000
        for k in range(i,j+1):
            tmp_val = a[i][k-1]+a[k+1][j]
            if(tmp_min > tmp_val):
                tmp_min = tmp_val
                min_k = k
        sum = 0
        for k in range(i,j+1):
            sum += p[k]
        a[i][j] = tmp_min + sum
        r[i][j] = min_k

printMatrixF(a)
print()
printMatrix(r)

root=tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)
print()

a=['A','A','C','A','G','T','A','C','C']

b=['T','A','C','G','T','T','C','A']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        penalty = 0
        if a[i] != b[j]:
            penalty = 1
        tmp_min = table[i+1][j+1]+penalty
        minindex[i][j] = (i+1, j+1)
        if tmp_min > table[i + 1][j] + 2:
            tmp_min = table[i + 1][j] + 2
            minindex[i][j] = (i + 1, j)
        if tmp_min > table[i][j + 1] + 2:
            tmp_min = table[i][j + 1] + 2
            minindex[i][j] = (i, j + 1)
        table[i][j] = tmp_min

printMatrix(table)
x = 0
y= 0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")


