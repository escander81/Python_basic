from random import randint

class Car:

    def __init__(self, s, c, n, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p
        print(f"Car is {self.name}, with {self.color} and {self.is_police}, police ")

    def show_speed(self):
        print(f"Car {self.name} goes with speed {self.speed}")

    def go(self):
        print(f"{self.name} car is moving")
    def stop(self):
        print(f"STOP")
    def turn(self, direction):
        print(f"{self.name} car turned {'left' if direction == 0 else 'right'}")
        return random.randint(1,2)
class TownCar(Car):
    def show_speed(self):
        return f'{self.name} speed is {self.speed} SPEEDING!' \
            if self.speed > 60 else f"{self.name} speed is {self.speed}"
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} speed is {self.speed} SPEEDING!' \
            if self.speed > 40 else f"{self.name} speed is {self.speed}"
class PoliceCar(Car):
    def __init__(self, s, c, n, p=True):
        super().__init__(s, c, n, p)

police = PoliceCar ("Police", "uniform", 120)
police.go()
print(police.show_speed())
# police.turn(randint)
police.stop()
print()

town_car = TownCar("towncar", "black", 80)
town_car.go()
town_car.turn(0)
town_car.turn(1)
print(town_car.show_speed())
town_car.stop()

print(f"\n vehicle {town_car.name} (color{town_car.color}")
print(f" vehicle {police.name} (color {police.color}")
car_1 = Car()
car_1.show_speed()
car_1.go()
car_1.turn()
car_1.stop()