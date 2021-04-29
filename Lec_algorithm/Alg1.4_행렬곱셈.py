def matrix_multiplication(a,b):
    n = len(a)
    c = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c

a=[ [1,2],[3,4]]
b=[ [4,1],[1,0]]

print(matrix_multiplication(a,b))