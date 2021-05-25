class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) +  '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("sum of cell is: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('subtraction of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'impossible.'

    def __mul__(self, other):
        print('multiply of cell is: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("truediv of cell is: ")
        return Cell(self.nums // nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)


