# The dict() Constructor
# print('='*100)
# print('The dict() Constructor:')
# print('-'*50)
# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# print('thisdict: ', thisdict)
# note that keywords are not string literals
# # note the use of equals rather than colon for the assignment
# some_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print('some_dict: ', some_dict)
# empty_dict = {}
# empty_dict['asdf'] = 'some string'
# empty_dict['asdfe'] = None
# print('empty_dict: ', empty_dict)
# print('empty_dict: ',type(empty_dict))



# # List of the tuples
# print('.'*25)
# print('List of the tuples:')
# tuple_list = [('brand', "Ford"), ("model",  "Mustang"), ("year",1964)]
# print('tuple_list: ', tuple_list)
# # print(dict(tuple_list))
# # print('.'*25)
# list_keys = ['brand', 'model', "year", 'brand']
# list_values = ["Ford",  'Mustang', 1964, 'Pavlo']
# sd = zip(list_keys, list_values)
# print('sd: ', sd)
# print('sd: ', list(sd))
# print(dict(zip(list_keys, list_values)))


# # Dict generation with the fromkeys() methods (Built-in)
# print('='*100)
# print('Dict generation with the fromkeys() methods:')
# print('-'*50)
# # x = ('key1', 'key2', 'key3')
# x = ['key1', 'key2', 'key3']
# thisdict = dict.fromkeys(x, '')
# print(thisdict)
# thisdict['key1'] = "asdf"
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)


# Dict generator (dict comprehension)
# thisdict = {a: a ** 2 for a in range(7)}
# print(thisdict)

# print('.'*25)
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_product": False,
    "max_speed": 125.5,
    "options": ["conditionar", "elctric window", "hard ceiling"],
    "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
    # "gear": "asgdjh"
}
# print(car)

# print(dir({}))
# # 1. Dictionary Length
# print('='*100)
# print('Dictionary Length:')
# print('-'*50)
# print(len(car))


# 2. Dictionary is empty
# print('='*100)
# print('Check if dictionary empty:')
# print('-'*50)
# car_1 = {}
# if car_1:
#     print('Yes')
# else:
#     print('No')
# if len(car_1)>0:
#     print('Yes, car_1 dictionary has items')
# else:
#     print('No, car_1 dictionary has not items')


#3. Accessing Items
# print('.'*25)
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_product": False,
    "max_speed": 125.5,
    "options": ["conditionar", "elctric window", "hard ceiling"],
    "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
}
# cars = [{"brand": "ford", "model": "MusTAng Gt500", "year": 1964}, {"brand": "ZAZ", "model": "Fortza", "year": 2001}, {"brand": "VW", "model": "Golf GTI", "year": 1999}]
# print(car)

# print('='*100)
# print('Accessing Items:')
# print('-'*50)
# brand = car["brand"]
# print('brand: ', brand)

# # custom = car["custom"]
# # print('custom: ', custom)

# print('.'*25)
# # The get() method (Built-in)
# brand = car.get("brand")
# print('brand: ', brand)

# custom = car.get("custom", "asdf")
# print('custom: ', custom)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_product": False,
    "max_speed": 125.5,
    "options": ["conditionar", "elctric window", "hard ceiling"],
    "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
}

# company = car["company"]
# print('company: ', company)

# company = car.get("company")
# print('company: ', company)

# company = car.get("company", "Ford Motor Company")
# print('company: ', company)


# 4. Change Values
# print('='*100)
# print('Change Values:')
# print('-'*50)
# car["year"] = 2018
# print(car)


# # 5. Loop Through a Dictionary
# print('='*100)
# print('Loop Through a Dictionary:')
# print('-'*50)
# print('Print all keys:')
# for item in car:
#     print(item)

# print('-'*50)
# print('Print all values:')
# for item in car:
#     print(car[item])
# print('.'*25)
# for value in car.values():
#     print(value)
# print('.'*25)
# print('car.items(): ', list(car.items()))
# for key, value in car.items():
#     print(value)

# for _, value in car.items():
#     print(_, value)


#6. Check if Key Exists
# print('='*100)
# print('Check if Key Exists:')
# print('-'*50)
# cheked_key = "model"
# if cheked_key in car:
#     print(f"Yes, {cheked_key} is one of the keys in the car dictionary")

# dict_key = "company"
# if dict_key in car:
#     print(f"Yes, {dict_key} is one of the keys in the car dictionary")
# else:
#     print(f"No, {dict_key} key does not exists in the car dictionary")

# opt_list = ['model', 'year', 'custom', 'company', 'country']
# for cheked_key in opt_list:
#     if cheked_key in car:
#         print(f"Yes, {cheked_key} is one of the keys in the car dictionary")


# #7. Adding Items
# print('='*100)
# print('Adding Items:')
# print('-'*50)
# car["color"] = "red"
# print(car)
# print(len(car))


# #8. Removing Items
# print('='*100)
# print('Removing Items:')
# print('-'*50)
# #Python Dictionary pop() Method (Built-in)
# model = car.pop("model")
# print('model: ', model)
# print(car)
# print(len(car))

# print('.'*25)
# #Python Dictionary popitem() Method (Built-in)
# print('Removing the last item:')
# last_item = car.popitem()
# print('last_item: ', last_item)
# print(car)
# print(len(car))

# print('.'*25)
# print('Using "del" method:')
# del car["max_speed"]
# print(car)
# print(len(car))


# print('.'*25)
# print('Using "del" method:')
# max_speed = car.get("max_speed")
# del max_speed
# print(car)
# print(len(car))


# print('.'*25)
# print('Attention! The "del" method can delete whole dictionary:')
# del car
# print(car)


# # 9.Clear a dictionary (Built-in)
# print('='*100)
# print('Clear a dictionary:')
# print('-'*50)
# car.clear()
# print(car)
# print(len(car))
# if car:
#     print(f"Yes, car dictionary has items")
# else:
#     print(f"No, car dictionary has not items")


# # 10. Copy a Dictionary (Built-in)
# print('='*100)
# print('Copy a Dictionary:')
# print('-'*50)
# new_car = car
# print(new_car)
# gear_1 = new_car['gear'][1]
# print('gear_1: ', gear_1)
# new_car['color'] = "blue"
# print('new_car: ', new_car)
# print('car: ', car)
# print('id(new_car): ', id(new_car))
# print('id(car): ', id(car))

# print('.'*25)
# new_car = car.copy()
# print(new_car)
# gear_1 = new_car['gear'][1]
# print('gear_1: ', gear_1)
# new_car['color'] = "blue"
# print('new_car: ', new_car)
# print('car: ', car)
# print('id(new_car): ', id(new_car))
# print('id(car): ', id(car))

# print('.'*25)
# new_car_2 = dict(car)
# print(new_car_2)
# new_car_2['color'] = "blue"
# print('new_car_2: ', new_car_2)
# print('car: ', car)
# print('id(new_car_2): ', id(new_car_2))
# print('id(car): ', id(car))

# print('.'*25)
# new_car_2 ={**car}
# print(new_car_2)
# new_car_2['color'] = "blue"
# print('new_car_2: ', new_car_2)
# print('car: ', car)
# print('id(new_car_2): ', id(new_car_2))
# print('id(car): ', id(car))


# BUILT-IN METHODS THAT YOU CAN USE ON DICTIONARIES
# 1. Python Dictionary items() Method
# print('='*100)
# print('Python Dictionary items() Method:')
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# print('-'*50)
# x = car.items()
# print('x: ', x)
# x = list(car.items())
# print('x: ', x)
# x = dict(car.items())
# print('x: ', x)


# # 2. Python Dictionary keys() Method
# print('='*100)
# print('Python Dictionary keys() Method:')
# print('-'*50)
# x = car.keys()
# print(x)


# #3. Python Dictionary values() Method
# print('='*100)
# print('Python Dictionary values() Method:')
# print('-'*50)
# x = car.values()
# print(x)


# #4. Python Dictionary setdefault() Method
# print('='*100)
# print('Python Dictionary setdefault() Method:')
# # The setdefault() method returns the value of the item with the specified key.
# # If the key does not exist, insert the key, with the specified value, see example below
# print('-'*50)
# x = car.setdefault("color", "White")
# print(x)
# print(car)


# #5. Python Dictionary update() Method
# print('='*100)
# print('Python Dictionary update() Method:')
# print('-'*50)
# car.update({"color": "White"})
# print(car)
