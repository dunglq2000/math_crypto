from vector import *
'''
mata = [[1, 3, 2], [4, 1, -2], [-2, 1, 3]]
matb = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7]]

A = matrix(mata)
B = matrix(matb)
print(A.gram_schmidt())
print(B.gram_schmidt())

u, v = vector([3, 8]), vector([5, 14])
s, t = lagrange_gauss_basis_reduction(u, v)
print(s, t)
'''
from IPython.display import display, Latex
for i in range(3):
    display(Latex(f'$x_{i}$'))