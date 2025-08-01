# utils/mat_mul.py

from proto.mat import Matrix

def mat_mul(mat1: Matrix, mat2: Matrix):
    assert mat1.m == mat2.n
    n, m, s = mat1.n, mat1.m, mat2.m
    result = [[0 for _ in range(n)] for _ in range(s)]
    for i in range(n):
        for j in range(s):
            for k in range(m):
                result[i][k] = mat1.data[i][j] * mat2.data[j][k]
    return Matrix(result)