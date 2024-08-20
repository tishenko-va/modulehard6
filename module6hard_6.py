# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# # объекты которых будут обладать методами изменения размеров, цвета и т
import math
class Figure():
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True) :
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [i for i in self.__color]

    # Метод __is_valid_color - служебный, принимает параметры  r, g, b, который
    # проверяет корректность переданных значений перед установкоq нового цвета.Корректным
    # цвет: все значения r, g и b - целые  числа диапазоне  от  0 до 255(включительно).

    def __is_valid_color(self, r, g, b):
        lst = [r, g, b]
        lst.sort()
        if lst[0] < 0 or lst[-1] > 255:
            return False
        else:
            return True

    #     Метод
    #  set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    # предварительно проверив их  на  корректность.Если введены некорректные данные, то  цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    # Метод __is_valid_sides - служебный, принимает
    # неограниченное кол - во  сторон, возвращает True если все стороны целые положительные числа
    # и кол - во  новых  сторон  совпадает  с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, sides):
        res = []
        for i in sides:
            if i > 0:
                res.append(i)
        if len(res) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    # Метод set_sides(self, *new_sides) должен принимать новые стороны,
    # если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
class Circle(Figure):

    sides_count = 1

    def __radius(self):
        return self.__len__ * (2/pi)

    def get_square(self):
        return (self.__len__**2)/(4*pi)


class Triangle(Figure):
    sides_count = 3

    def __height(self):
        sp = self.__len__/2
        h = (2**(sp(sp-self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2]))
        )/2*sp
        return h

    def get_square(self):
        sp = self.__len__/2
        s = sqrt((sp(sp - self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2])))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1*self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# 55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216