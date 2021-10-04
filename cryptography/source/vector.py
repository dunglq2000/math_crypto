from typing import List
from functools import reduce
from math import sqrt

class vector:
    def __init__(self, v):
        if type(v) == list:
            self.vec = v
        elif type(v) == vector:
            self.vec = [i for i in v.vec]
        self.sqrnorm = None

    def __str__(self):
        return str(self.vec)

    def __mul__(self, other):
        assert len(self.vec) == len(other.vec)
        return sum([x*y for x, y in zip(self.vec, other.vec)])

    def __rmul__(self, n):
        return vector([n * x for x in self.vec])

    def __add__(self, other):
        return vector([x+y for x, y in zip(self.vec, other.vec)])

    def __sub__(self, other):
        return vector([x-y for x, y in zip(self.vec, other.vec)])

    def copy(self, other):
        self.vec = [i for i in other.vec]

    def sqr_norm(self):
        if not self.sqrnorm:
            self.sqrnorm = sum([j *j for j in self.vec])
        return self.sqrnorm
    
    def norm(self):
        return sqrt(self.sqrnorm)


class matrix:
    def __init__(self, vecs: List):
        self.rows = [vector(v) for v in vecs]

    def __str__(self):
        return '\n'.join([str(v) for v in self.rows])

    def gram_schmidt(self) -> List[vector]:
        v = [vector(self.rows[0])]
        for i in range(1, len(self.rows)):
            u = vector(self.rows[i])
            for j in range(i):
                my = (self.rows[i] * v[j]) / (v[j] * v[j])
                u = u - my * v[j]
            v.append(u)
        return matrix(v)

def lagrange_gauss_basis_reduction(b1: vector, b2: vector):
    B1 = b1.sqr_norm()
    my = (b1 * b2) / B1
    b2 = b2 - round(my) * b1
    B2 = b2.sqr_norm()
    while B2 < B1:
        b1, b2 = b2, b1
        B1 = B2
        my = (b1 * b2) / B1
        b2 = b2 - round(my) * b1
        B2 = b2.sqr_norm()
    return b1, b2

