""" Красильников Илья
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return "Ручка рисует"


class Pencil(Stationery):

    def draw(self):
        return "Карандаш начал отрисовку"


class Handle(Stationery):

    def draw(self):
        return "Маркер ярко отрисовывает обЪект"


my_pen = Pen("Ручка")
my_pencil = Pencil("Карандаш")
my_handle = Handle("Маркер")

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())

