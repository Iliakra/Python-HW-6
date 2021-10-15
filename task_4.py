""" Красильников Илья
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, п
овернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала\n"

    def stop(self):
        return "Машина остановилась\n"

    def turn(self, direction):
        return f"Машина повернула {direction}\n"

    def show_speed(self):
        return f"{self.speed} км/ч"


class TownCar(Car):

    def show_speed(self):
        print(f"{self.speed} км/ч")
        if self.speed > 60:
            return "Скорость превышена!\n"


class WorkCar(Car):

    def show_speed(self):
        print(f"{self.speed} км/ч")
        if self.speed > 40:
            return "Скорость превышена!\n"


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_town_car = TownCar(70, "red", "Hyundai", False)
my_work_car = WorkCar(30, "grey", "Ford", False)
my_sport_car = SportCar(120, "white", "Ferrari", False)
my_police_car = PoliceCar(50, "white", "Ford", True)

print(my_town_car.speed, my_town_car.name, my_town_car.color)
print(my_town_car.show_speed())
print(my_work_car.go())
print(my_work_car.stop())
print(my_sport_car.turn("вправо"))
print(my_sport_car.show_speed())
print(my_police_car.is_police)

