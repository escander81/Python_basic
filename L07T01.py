from itertools import zip_longest

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])

m = [[1, 2, 3], [4, 5, 6], [1, 2]]
n = [[9, 8, 7], [7, 6, 5]]
matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print(matr_1 + matr_2)
