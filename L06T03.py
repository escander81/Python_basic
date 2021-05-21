class Worker:
    # атрибуты класса

    # конструктор
    # атрибуты объекта
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': w, 'bonus': b}
        # print(n, s, p)

class Position(Worker):
    # методы
    # def __init__(self):super().__init__(n, s, p)

    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return f"{sum(self._income.values())}"

p = Position("Stu", "Johnston", "President", 50000, 200000)

print("Mr.", p.get_full_name())
print(p.position)
print(p.get_total_income(),"$")

