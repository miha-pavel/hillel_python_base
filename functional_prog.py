def myfun(n):
     return lambda a: a*n

my_d = myfun(2)
my_t = myfun(3)
print(type(my_d))
print(type(my_t))
print(my_d(3))
print(my_t(3))