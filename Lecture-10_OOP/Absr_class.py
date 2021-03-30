#Дефолтное значение
class TestB():
    def __init__(self, attr):
        self.attr = attr

a = TestB()
print(a.attr)
a.attr = 2
print(a.attr)
class TestB():
    def __init__(self, attr=1):
        self.attr = attr

a = TestB()
print(a.attr)
a.attr = 2
print(a.attr)




# #Абстрактный класс
# from abc import ABC, abstractmethod
# class ChessPiece(ABC):
#     # общий метод, который будут использовать все наследники этого класса
#     def draw(self):
#         print("Drew a chess piece")
 
#     # абстрактный метод, который будет необходимо переопределять для каждого подкласса
#     @abstractmethod
#     def move(self):
#         pass

# # a = ChessPiece()

# class Queen(ChessPiece):
#     def move(self):
#         print("Moved Queen to e2e4")

# # Мы можем создать экземпляр класса
# q = Queen()
# # И нам доступны все методы класса
# print(q.draw())
# print(q.move())





# # #Множественное наследование
# class A:
#     def hi(self):
#         print("A")

# class B(A):
#     def hi(self):
#         print("B")

# class C(A):
#     def hi(self):
#         print("C")

# class D(B, C):
#     def hi(self):
#         print("D")

# d = D()
# print(d.hi())
# print(D.mro())

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
print(E.mro())
