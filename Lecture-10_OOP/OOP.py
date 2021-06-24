# # Создаем класс Car
# class CarMercedez:
#     # создаем атрибуты класса
#     name = "c200" # Все экземпляры этого класса будут иметь атрибут arg, равный "Python"     Но впоследствии мы его можем изменить
#     make = "mercedez"
#     model = 2008

#     # создаем методы класса
#     def start(self):       # self - обязательный аргумент, содержащий в себе экземпляр класса, передающийся при вызове метода, поэтому этот аргумент должен присутствовать во всех методах класса.
#         print("Заводим двигатель")

#     def stop(self):
#         print("Отключаем двигатель")


# # Создаем объект класса Car под названием car_a
# car_a = CarMercedez()
# # Создаем объект класса Car под названием car_b
# car_b = CarMercedez()

# print(type(car_a))
# print(type(car_b))
# # print(dir(car_b))
# # str_ = ''
# # print(type(str_))
# # print(dir(str_))

# # car_a.start()

# # print(car_a.model)
# # car_a.model = 2020
# # print(car_a.model)
# # print(car_b.model)

# def brabus_switch_gear(gear_number):
#     print(f'switched gear - {gear_number}')
# car_b.custom_switch_gear = brabus_switch_gear
# print('Alex car-', type(car_b))
# print(dir(car_b))
# print(dir(car_a))
# car_b.custom_switch_gear(1)
# car_b.custom_switch_gear(2)
# car_b.custom_switch_gear(3)
# # Все пользовательские атрибуты сохраняются в атрибуте __dict__, который является словарем.
# print(car_b.__dict__)


# ==============================
# class Car:
#     # создаем атрибуты класса
#     car_count = 0

#     # создаем методы класса
#     def start(self, name, make, model):
#         print("Двигатель заведен")

#         self.name = name    # атрибуты экземпляра ссылаются при помощи ключевого слова self
#         self.make = make
#         self.model = model
#         Car.car_count += 1  # атрибуты класса ссылаются при помощи названия класса.


# car_a = Car()
# car_a.start("Corrola", "Toyota", 2015)
# print(car_a.name)
# print(car_a.car_count)


# # # создадим еще один объект класса Car и вызываем метод start()
# car_b = Car()
# car_b.start("City", "Honda", 2013)
# print(car_b.name)
# print(car_b.car_count)
# значение атрибута car_count, вы увидите 2 в выдаче. Это связано с тем, что атрибут car_count является атрибутом класса и таким образом он разделяется между экземплярами. Объект car_a увеличил свое значение до 1, в то время как car_b увеличил свое значение еще раз, так что итоговое значение равняется 2.


# #==============================
# # Локальная переменная
# class Car:
#     def start(self):
#         message = "Двигатель заведен"
#         return message


# car_a = Car()
# print(car_a.message)


# #==============================
# # Глобальная переменная
# class Car:
#     message1 = "Двигатель заведен"

#     def start(self):
#         message2 = "Автомобиль заведен"
#         msg = Car.message1
#         print('msg: ', msg)
#         return message2

# car_a = Car()
# print(car_a.message1)
# print(car_a.start)
# print(car_a.start())


# #==============================
# Конструктор
# class Car:
#     # создание атрибутов класса
#     car_count = 0

#     # создание методов класса
#     def __init__(self, name, make, model):
#         Car.car_count +=1
#         print(Car.car_count)
#         self.name = name
#         self.make = make
#         self.model = model

#     def start(self):
#         print(f'Я завел {self.make} {self.name} {self.model} года')

# car_a = Car()
# car_b = Car("corolla", "toyota", 1999)
# car_b.start()
# car_c = Car("crv", "honda", 20202112)
# car_c.car_count = 10
# print('car_c.car_count: ', car_c.car_count)
# car_d = Car("crv", "honda", 2020)
# car_b.start(self)
# car_b.start(self)


# ==============================
# Статический метод
# class Car:
#     name = "c200"
#     make = "mercedez"
#     model = 2008

#     @property
#     def full_name_1(self):
#         return ' '.join([self.make, self.name])

#     def full_name_2(self):
#         print('self: ', self)
#         return  ' '.join([self.make, self.name])

#     @classmethod
#     def hello(cls):
#         print('cls: ', cls)
#         print('Hello, класс {}'.format(cls.__name__))

#     @staticmethod
#     def get_class_details():
#         print (f"Это класс Car")

# sd = Car()
# # sd.get_class_details()
# sd.hello()


# car = Car()
# print(car.name)
# print(car.full_name_1)
# print(car.full_name_2())



# class Square:
#     @staticmethod
#     def get_squares(a, b):
#         return a*a, b*b

# print(Square.get_squares(3, 5))

# class SomeClass(object):
#     pass
# ds = SomeClass()
# print('dir(ds): ', dir(ds))

# Жизненний цикл
# class SomeClass(object):
#     def __new__(cls, *args, **kwargs):
#         print("new")
#         return super(SomeClass, cls).__new__(cls)

#     def __init__(self, name):
#         print("init")
#         self.name = name

#     def __del__(self):
#         print('удаляется объект {} класса SomeClass'.format(self.name))

# obj = SomeClass("john")
# del obj
# obj
#Дефолтное значение
# class TestB():
#     def __init__(self, attr, attr_2):
#         print('attr: ', attr)
#         print('attr_2: ', attr_2)
#         self.attr = attr
#         self.attr_2 = attr_2

# a = TestB()

# class TestB():
#     def __init__(self, attr=None):
#         print('attr: ', attr)
#         self.attr = attr

# a = TestB()
# print(a.attr)
# a.attr = 2
# print(a.attr)


# ==============================
# ПРИНЦИПИ ООП
# Инкапсуляция
# Публичные, приватные и защищенные переменные
# class Car:
#     def __init__(self):
#         print ("Двигатель заведен")
#         self.name = "corolla"
#         self._model = 1999
#         self.__make = "toyota"

#     def get_name(self):
#         print('self.name: ', self.name)

#     def _get_model(self):
#         print('self._model: ', self._model)

#     def __get_make(self):
#         print('self.__make: ', self.__make)


# car_a = Car()
# print('car_a: ', car_a)
# print('dir(car_a): ', dir(car_a))
# print(car_a.name)
# print(car_a._model)
# print(car_a._Car__make)
# print(car_a.get_name())
# print(car_a._get_model())
# print(car_a._Car__get_make())

# #================================================
# Наследование
class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        # super – это ключевое слово, которое используется для обращения к родительскому классу.
        super().__init__(color) #визов  конструктора родительского класса
        self._height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    def set_width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    def height(self):
        return self._height

    def area(self):
        return self.__width * self._height


rect = Rectangle(10, 20, "green")


# print('rect.width: ', rect.width)
# rect.width = 30
# print('rect.width: ', rect.width)
# rect.width = -30
# rect.set_width(50)
# print('rect.width: ', rect.width)


# print('rect.height: ', rect.height())
# rect._height = 40
# print('rect.height: ', rect.height())
# print('rect.height: ', rect._height)


# print('rect.color: ', rect.color)
# rect.color = "red"
# print('rect.color: ', rect.color)


# fig = Figure('arange')
# print('fig.height: ', fig.height())
# fig._height = 40
# print('fig.height: ', fig.height())
# print('fig.height: ', fig._height)


# # #Абстрактный класс
from abc import ABC, abstractmethod
class ChessPiece(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        pass

# a = ChessPiece()

class Queen(ChessPiece):

    def help(self):
        print('help')

    def move(self):
        print("Moved Queen to e2e4")

# Мы можем создать экземпляр класса
q = Queen()
# И нам доступны все методы класса
print(q.draw())
print(q.help())
print(q.move())


# # Множественное наследование
class A:
    # pass
    def hi(self):
        print("A")

class B(A):
    pass
    # def hi(self):
    #     print("B")

class C(A):
    pass
    # def hi(self):
    #     print("C")

class D(B, C):
    pass
    # def hi(self):
    #     print("D")

d = D().hi()
print(d)
print(D.mro())

# class D(B, C):
#     def call_hi(self):
#         C.hi(self)
# d = D()
# print(d.call_hi())

# class A: pass
# class B(A): pass
# class C: pass
# class D(C): pass
# class E(B, D): pass
# print(E.mro())


# #=================================================
# # Полиморфизм

# class Figure:
#     def __init__(self, color):
#         self.__color = color

#     @property
#     def color(self):
#         return self.__color

#     @color.setter
#     def color(self, c):
#         self.__color = c

#     def info(self):
#         print("Figure")
#         print("Color: " + self.__color)


# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError

#     def info(self):
#         print("Rectangle")
#         print("Color: " + self.color)
#         print("Width: " + str(self.width))
#         print("Height: " + str(self.height))
#         print("Area: " + str(self.area()))

#     def area(self):
#         return self.__width * self.__height


# fig = Figure("orange")
# print('fig.info(): ', fig.info())
# print('--------------------------')
# rect = Rectangle(10, 20, "green")
# print('rect.info(): ', rect.info())