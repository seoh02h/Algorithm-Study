#pip install numpy
import numpy as np
a = [1,2,3]
print(a)
b = np.array(a)
print(b)

c = [[1,2,3],[5,6,7]]
print(c)
d = np.array(c)
print(d)
print(d[1,2])
print(d[1][2])

# @는 numpy행렬의 곱셈 operator
a = [[1,2],[3,4]]
b = [[1, 0], [2,5]]
c = np.array(a)
d = np.array(b)
f = c @ d
print(f)

# 행렬의 덧셈, 뺄셈 기능
a = [[1,2],[3,4]]
b = [[1, 0], [2,5]]
c = np.array(a)
d = np.array(b)
f = c+d
print(f)
g = c - d
print(g)

# 행렬의 초기화
# j : 열의 인덱스, i : 행의 인덱스
A = [[2 for j in range(3)] for i in range(2)]
print(A)
B = np.array(A)
print(B)

A = np.array([[i+j for j in range(3)]for i in range(2)])
print(A)

# 행렬의 병합
a = [[1,2],[3,4]]
b = [[1, 0], [2,5]]
c = np.array(a)
d = np.array(b)
print(np.hstack([c,d])) # horizontal stack
print()
print(np.vstack([c,d])) # vertical stack
