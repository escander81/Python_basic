# класс
class MyRoad:

    # методы
    def __init__(self, length, width, thickness, weight): #конструктор

        self.length = length
        self.width = width
        self.thickness = thickness
        self.weight = weight
        # self.r = {}
    def getlength(self):
        return self._length

    def getwidth(self):
        return self._width

    def getthickness(self):
        return self._thickness

    def getweight(self):
        return self._weight

    def getcalc(self):
        return self.length * self.width * self.thickness * self.weight // 10

r1 = MyRoad(1000, 1, 0.04, 25.5)
print("length = ", r1.length, "m")
print("width = ", r1.width, "m")
print("thickness = ", r1.thickness, "m")
print("weight = ", r1.weight, "kg")
print("calculation = ", r1.getcalc(), "tonns")


# данные расчета (взяты из интернета)
# Например у нас имеется территория площадью 1000 м2, и нужно выполнить асфальтирование толщиной H=4 см:
# 1) 25,5 кг * 4см = 102 кг — количество м/з плотной асфальтовой смеси тип А м I, для 1 м2 укладки асфальта.
# 2) 0,102 т * 1000 м2 = 102 тонны — кол-во асфальтобетона, необходимое для асфальтирования территории.
# ответ 102 тонны
