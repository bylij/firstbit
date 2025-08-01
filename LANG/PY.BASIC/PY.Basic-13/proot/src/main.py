# src/main.py

from proto.mat import Matrix
from utils.mat_mul import mat_mul

mat1 = Matrix([[1, 2], [3, 4]])
mat2 = Matrix([[5, 6], [7, 8]])

print(mat_mul(mat1, mat2).data)