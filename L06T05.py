class Stationery:
    def __init__(self, title = "Канцелярские пренадлежности"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title} ручки")

class Pencil(Stationery):
    def draw(self):
       print(f"Запуск отрисовки с помощью {self.title} карандаша")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title} маркера")

s = Stationery()
s.draw()
pen = Pen("Parker")
pen.draw()

pencil = Pencil("простой")
pencil.draw()

handle = Handle('желтый')
handle.draw()