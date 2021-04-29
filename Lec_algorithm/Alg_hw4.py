"""
실습 p5_dp_bin_floyd_chainMatrix.mp4 21쪽 [실습프로그램] Floyd 알고리즘, 25쪽 최단경로를 출력하는 프로그램을 python으로 완성하라

별도의 입력 기능을 작성하지 않아도 됨.
오류 확인 기능은 없어도 됨.
필요한 출력기능 함수를 별도로 만들거나 numpy를 이용해도 됨
하나의 프로그램으로 작성

"""
#from utility import *
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0, m):
        for j in range(0, n):
            print("%4d" % d[i][j], end=" ")
        print()


def allShortestPath(g,n):
    d=g
    p=[[0 for i in range(n)]for i in range(n)]
    printMatrix(d)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j]=d[i][k]+d[k][j]
                    p[i][j]=k+1
    return d, p



def path(p, q, r):
    if p[q-1][r-1] != 0:
        path(p, q,p[q-1][r-1])
        print(' v'+str(p[q-1][r-1]),end=" ")
        path(p, p[q-1][r-1],r)

inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]
d, p = allShortestPath(g, 5)
print()
printMatrix(d)
print()
printMatrix(p)

path(p, 5, 3)



