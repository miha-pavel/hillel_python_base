# # Создаем класс Car
# class Car:
#     # создаем атрибуты класса
#     name = "c200" # Все экземпляры этого класса будут иметь атрибут arg, равный "Python"     Но впоследствии мы его можем изменить
#     make = "mercedez"
#     model = 2008

#     # создаем методы класса
#     def start(self):       # self - обязательный аргумент, содержащий в себе экземпляр класса, передающийся при вызове метода, поэтому этот аргумент должен присутствовать во всех методах класса.
#         print ("Заводим двигатель")

#     def stop(self):
#         print ("Отключаем двигатель")


# # Создаем объект класса Car под названием car_a
# car_a = Car()
# # Создаем объект класса Car под названием car_b
# car_b = Car()

# print(type(car_b))
# print(type(car_b))
# print(dir(car_b))

# car_b.start()

# print(car_b.model)
# car_b.model = 2020
# print(car_b.model)

# def switch_gear(gear_number):
#     print(f'switched gear - {gear_number}')
# car_b.new_gear = switch_gear
# car_b.new_gear(1)
# car_b.new_gear(2)
# car_b.new_gear(3)
# # Все пользовательские атрибуты сохраняются в атрибуте __dict__, который является словарем.
# print(car_b.__dict__)


#==============================
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


# # создадим еще один объект класса Car и вызываем метод start()
# car_b = Car()
# car_b.start("City", "Honda", 2013)
# print(car_b.name)
# print(car_b.car_count)
# # значение атрибута car_count, вы увидите 2 в выдаче. Это связано с тем, что атрибут car_count является атрибутом класса и таким образом он разделяется между экземплярами. Объект car_a увеличил свое значение до 1, в то время как car_b увеличил свое значение еще раз, так что итоговое значение равняется 2.


# #==============================
# Локальная переменная
# class Car:
#     def start(self):
#         message = "Двигатель заведен"
#         return message


# car_a = Car()
# print(car_a.message)


# #==============================
# Глобальная переменная
# class Car:
#     message1 = "Двигатель заведен"

#     def start(self):
#         message2 = "Автомобиль заведен"
#         return message2

# car_a = Car()
# print(car_a.message1)


# # #==============================
# # Конструктор
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

# # car_a = Car()
# car_b = Car("corolla", "toyota", 1999)
# car_c = Car("crv", "honda", 2020)




# #==============================
# Публичные, приватные и защищенные переменные
# class Car:
#     def __init__(self):
#         print ("Двигатель заведен")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999

# car_a = Car()
# print(car_a.name)
# print(car_a.make)


# #==============================
# Статический метод
# class Car:
#     name = "c200"
#     make = "mercedez"
#     model = 2008

#     @property
#     def full_name_1(self):
#         return ' '.join([self.make, self.name])

#     def full_name_2(self):
#         return  ' '.join([self.make, self.name])

#     @classmethod
#     def hello(cls):
#         print('Hello, класс {}'.format(cls.__name__))

#     @staticmethod
#     def get_class_details():
#         print ("Это класс Car")

# Car.get_class_details()
# Car.hello()

# car = Car()
# print(car.full_name_1)
# print(car.full_name_2())


# class Square:
#     @staticmethod
#     def get_squares(a, b):
#         return a*a, b*b

# print(Square.get_squares(3, 5))