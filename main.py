# name = input('add your name \n')

# print(name + ' first one')

# print(type(2 + 5))
# print(2**2)
# print(8//6)
# print(8//3)
# math functions
from functools import reduce

print(round(3.2))
print(abs(-39))

# operator precedence
print(12 - 4 * 4)

print(bin(2))
print(int('0b10', 2))

# variables

# expressions vs statement

# augmented assignment operators
x = 10
x += 2
print(x)

# strings and concatenation
x = 'this is me' + ' ' + 'and you'
print(x)

# type conversion
number = 10

print(type(str(number)))

# escape sequence

emoji = """
      WOW
      O O
      ___
"""
print(emoji)

# formatted strings

name = 'John'
age = 30
print(f'Hey {name} is {age}')

# immutability | `string` is immutable
# str = '01222'
# str[0] = '9'
# this is type error because string is immutable

# built-in functions
greet = 'hello'
print(greet[0:len(greet)])

quote = 'to be or not to be'
# methods
print(quote.capitalize())
print(quote.upper())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# boolean
name = 'Biruk'
# is_cool = False

# is_cool = True

print(bool(1))

# name = 'John'
age = 22
relationship_status = 'single'
relationship_status = 'it\'s complicated'

print(relationship_status)

birth_year = input('what year were you born ? ')

age = 2022 - int(birth_year)

print(f'your age is: {age}')

# password checker
username = input('what is your username ?')
password = input('what is your password ?')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, you password is, {hidden_password}, {password_length} letters long')

# list is a datatype that holds collection of item like arrays

# Data Structure 

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = ['notebooks', 'sunglass']
print(amazon_cart[1])

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# list slicing
amazon_cart[0] = 'pc'
new_cart = amazon_cart
new_cart2 = amazon_cart[:]  # amazon_cart.copy()
amazon_cart[0] = 'laptop'
print(new_cart)  # this one update every time when amazon_cart updated
print(new_cart2)  # only has amazon_cart value that assigned earlier
print(amazon_cart[0::2])
# lists are immutable

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

# list method

basket = [1, 2, 3, 4]
new_list = basket.append(100)

print(new_list)
print(basket)

basket.insert(4, 50)
new_list = basket
print(new_list)

basket.extend([10, 90, 80])
new_list = basket
print(new_list)

basket.pop()
print(basket)  # by index remove like basket.pop(0)

basket.remove(4)  # by value remove
print(basket)

new_list = basket.pop(4)  # it holds a value that removed

# basket.clear()
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d', 2, 4))  # 2 & 4 are start and end of index to searching for d
print('d' in basket)  # boolean value
print(basket.count('d'))
# ======
basket.sort()
print(basket)
# or
print(sorted(basket))  # it does't change the original value
basket.reverse()
print(basket)

# common list patterns
# to reverse slicing reverse

print(basket[::-1])
print(basket)  # not changed by slicing reverse

print(range(1, 100))  # range(1, 100)
print(list(range(1, 100)))
# or
print(list(range(101)))

# join
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is'])
print(sentence)
print(new_sentence)

# or
new_sentence = ' '.join(['hi', 'my', 'name', 'is'])
print(new_sentence)

# list unpacking
a, c, b, *other, d = [1, 3, 4, 5, 6, 6, 8, 4]
print(a)
print(b)
print(c)
print(other)
print(d)
# None 
#  Dictionary
dictionary = {
    'a': [1, 2, 4],
    'b': 'hello',
    'c': True
}
print(dictionary)
print(dictionary['b'])
print(dictionary['a'][1])

mylist = [
    {
        'a': [1, 2, 4],
        'b': 'hello',
        'c': True
    },
    {
        'a': [4, 2, 4],
        'b': 'hello',
        'c': True
    }
]
print(mylist[0]['a'])

#  dictionary methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('hello' in user.values())
print(user.items())

print(user.get('age'))
print(user.get('age', 44))  # if not exist

user2 = dict(name='John')
print(user2)
user2.clear()
print(user2)

user2 = user.copy()
print(user2)
user.pop('age')
print(user)

print(user.update({'age': 30}))
print(user)

# Tuples 
my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)  # (2,)

new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

# tuple methods are 2 count & index

print(my_tuple.count(4))
print(my_tuple.index(4, 1, 5))
print(len(my_tuple))

# set
# unordered collections of unique objetcs

my_set = {2, 4, 3, 4, 4, 5}
print(my_set)  # {2, 3, 4, 5}
my_set.add(100)
my_set.add(2)

print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

my_set = {1, 2, 3, 4, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)
print(my_set.intersection(your_set))
# or
print(my_set & your_set)
print(my_set.isdisjoint(your_set))
# issubset()
# isuperset()
print(my_set.union(your_set))
# or
print(my_set | your_set)
my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))

b = ['dh', 'hd']
print('j' in b)

# indentation

is_old = True

is_licenced = True

if is_old and is_licenced:
    print('you\'r')
else:
    print('sorry')

print('okok')

# Truthy and falsy

print(bool('hello'))  # truthy

print(bool(''))  # falsy

print(bool(0))  # falsy

password = '123'

username = 'johnny'

if password and username:
    print('go on')
else:
    print('please fill the form')

# Ternary operators

# condition_is_true if condition else condition_if_false

is_friend = False

can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)

# Short Ciruciting

is_Friend = True

is_User = True

if is_Friend and is_User:
    print('bff')

# Logical operators

# and, or, >, <, ==, >=, <=, !=, not

print('a' > 'A')  # True because
# indentation

is_old = True

is_licenced = True

if is_old and is_licenced:
    print('you\'r')
else:
    print('sorry')

print('ok ok')

# Truthy and falsy

print(bool('hello'))  # truthy

print(bool(''))  # falsy

print(bool(0))  # falsy

password = '123'

username = 'johnny'

if password and username:
    print('go on')
else:
    print('please fill the form')

# Ternary operators

# condition_is_true if condition else condition_if_false

is_friend = False

can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)

# Short Circuiting

is_Friend = True

is_User = True

if is_Friend and is_User:
    print('bff')

# Logical operators

# and, or, >, <, ==, >=, <=, !=, not

print('a' > 'A')  # True because
# ternary operator
is_true = False
test = 'this on is true' if is_true else 'this is incorrect'
print(test)
# loops
# for loop
for item in 'this is a test':
    print(item)
# iterable
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user:
    print(item)
    # only keys
for item in user.items():
    print(item)
    # ('name', 'Golem')
    # ('age', 5006)
    # ('can_swim', False)

for item in user.values():
    print(item)
    # Golem
    # 5006
    # False

for item in user.keys():
    print(item)
    # only keys

for item in user.items():
    key, value = item
    print(key, value)
    # name Golem
    # age 5006
    # can_swim False
# or
for key, value in user.items():
    print(key, value)
    # name Golem
    # age 5006
    # can_swim False
# exercise tricky counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for item in my_list:
    counter = counter + item
print(counter)
# range in for loop
print(range(100))
# range(0, 100)
# print(list(range(101))) to list all of...
for _ in range(0, 101, 50):
    print(_)
# list in loop

# for _ in range(101, 0, -1):
#     print(_)
# reverse
# list in loop
# enumerate
for i, char in enumerate('hello'):
    print(i, char)
# locate 50's index in list
for i, char in enumerate(list(range(101))):
    if char == 50:
        print(f'index of 50 is {i}')
# while loop
i = 0

while i < 5:
    print('this is ')
    i += 1
    break
else:
    print('done')
    # not executed because of break

while True:
    response = input('say something')

    if response == 'bye':
        break

# continue
my_list = [1, 2, 3]
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

my_list = [1, 2, 3]
while i < len(my_list):
    print(my_list[i])
    continue
    i += 1
#     prints nothing
# pass
while i < len(my_list):
    print(my_list[i])
    pass
    i += 1

# GUI
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*')
        elif pixel == 0:
            print(' ')
#  it prints all value in new line because by default print() has new line
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*', end='')
        elif pixel == 0:
            print(' ', end='')
    print('')
# Exercise find the duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


# functions
def show_tree():
    for image in picture:
        for pixel in image:
            if pixel == 1:
                print('*', end='')
            elif pixel == 0:
                print(' ', end='')
        print('')


show_tree()
show_tree()


# Parameter vs Arguments
def register(name='sally', emoji='😊'):
    # parameter is 'name'
    print(f'hello {name} {emoji}')


# arguments
register('biruk', '😊')

# keyword arguments
register(emoji='😊', name='Bibi')


# # return
# def sum(num11, num22):
#     def another_function(n1, n2):
#         return n1 + n2
#
#     return another_function(num11, num22)
#     print('hello')  # not executed after return the function will exit.
#
#
# total = sum(10, 20)
# print(total)


# Question on tesla
# 1. Wrap the above code in a function called checkDriverAge().
# Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function
# everytime?


def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()


# 2 Instead of using the input().
# Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

def checkdriverage(age=0):
    if int(age) < 18:
        print("Sorry, you are too your to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkdriverage()


# methods vs functions
# create methods in class
# custom function


# Docstrings
def test(a):
    '''
    @param a: is a variable
    @return:
    '''


help(test)
print(test.__doc__)


# clean code


def is_even_number(num):
    if num % 2 == 0:
        return True
    return False


#     this helps to minimize the code instead of using else this can also improve


def is_even(num):
    return num % 2 == 0


print(is_even_number(51))
print(is_even(50))


# args amd kwargs
def super_func(*args):
    print(*args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


def super_funcs(*args, **kwargs):
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args, total)


print(super_funcs(1, 2, 3, num1=5, num3=6))


# Exercise Function
def highest_even(li):
    evens = []
    for number in li:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
# scope
# 1 - start with local
# 2 - parent local ?
# 3 - global
# 4 - built in python

# global key word
total = 0


def count():
    # global total +=1 not work
    global total
    total += 1
    return total


count()

# or

print(total)


def count2(total):
    # global total +=1 not work
    total += 1
    return total


print(count2(count2(count2(total))))


# nonlocal keyword


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner: ", x)

    inner()
    print('outer', x)


outer()
# inner:  nonlocal
# outer nonlocal
# walrus operator
a = 'helloooooo'

if (n := len(a)) > 10:
    print(f'too long {n} elements')
'''

 ----------------------------------------------------------------
|                                                                |
|                           OOP                                  |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
 ----------------------------------------------------------------
'''


# OOP
class PlayerCharacter:
    def __init__(self, name):
        self.name = name
        # print('hey')

    def run(self):
        print(f'you\'r name is {self.name}')


player1 = PlayerCharacter('biruk')
print(player1.run())


# print(player1.name) shows the name


# class object attribute
class PlayerCharacter:
    membership = True

    # static can not be changed

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age
        # print('hey')

    def run(self):
        print(f'you\'r name is {self.name}')


player1 = PlayerCharacter('biruk', 22)
print(player1.membership)


# class object attribute can be accessed directly in a class

# @classmethod
class PlayerCharacter2:
    membership = True

    # static can not be changed

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    # only differ with class method by, static we don't access to cls
    def subtracting_things(cls, num11, num22):
        return num11 - num22


print(PlayerCharacter2.adding_things(23, 22))
print(PlayerCharacter2.adding_things(2, 3))


# can access directly, without object instantiate


# abstraction
class TestClass:
    def __init__(self, name):
        self.__name = name

    # not real private just address for developer don't change it by __

    def speak(self):
        print(f'my name is {self.name}')


Test = TestClass('and')
Test.speak = 'booo'
print(Test.speak)


# inheritance
class User:

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with, {self.power}')


class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'attacking with arrows : arrows left - {self.num_arrow}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(wizard1.attack())
print(archer1.attack())
print(isinstance(archer1, User))
# True
print(isinstance(archer1, object))


# True b/c all python code is an object

# Polymorphism
# same methods different calling of an object
def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

# print(archer1.attack())
for char in [wizard1, archer1]:
    char.attack()


# super()

class User2(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard2(User2):
    def __init__(self, name, power, email):
        # User2.__init__(self, email)
        # or
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with, {self.power}')


class Archer2(User2):

    def attack(self):
        print(f'attacking with arrows : arrows left - {self.num_arrow}')


wizard1 = Wizard2('Merlin', 50, 'merlin@gmail.com')
# archer1 = Archer2('Robin', 100)
print(wizard1.email)
# make an error because of parameter without passing email to Wizard2
# prints => merlin@gmail.com

# introspection is the ability to determine the type of object at runtime

print(dir(wizard1))


# list all dunder methods that we have access to
# dunder
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.mydict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return f'yes'

    def __getitem__(self, i):
        return self.mydict[i]


action_figure = Toy('red', 0)
print(str(action_figure))
# or same as dunder method
print(action_figure.__str__())
# prints <__main__.Toy object at 0x7f35e3df3d60>
# also allow customization
# after modify returns red
print(len(action_figure))
# prints 5

print(action_figure())
# refers call
del action_figure

# after this action_figure is not known

# deleted!
action_figure = Toy('red', 9)
print(action_figure['name'])


class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")


# Instance created
e = Example()

# __call__ method will be called
print(e())


# Instance Created
# Instance is called via special method
# Exercise on extending list
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1)
print(super_list1[0])
print(issubclass(list, object))


# Multiple inheritance

class User3():

    def sign_in(self):
        print('logged in')


class Wizard3(User3):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with, {self.power}')


class Archer3(User3):

    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'attacking with arrows : arrows left - {self.num_arrow}')

    def run(self):
        print('ran really fast ')

    def check_arrows(self):
        print(f'{self.num_arrow} remaining')


class HybridBorg(Wizard3, Archer3):
    def __init__(self, name, power, num_arrow):
        Archer3.__init__(self, name, num_arrow)
        Wizard3.__init__(self, name, power)


# hb1 = HybridBorg('borgie', 50)
# but this could lead to error due to argument that pass
# to solve this we need to pass all available variables from instance classes
# print(hb1.run())
hb1 = HybridBorg('borgie', 50, 90)
print(hb1.attack())


# MRO - Method Resolution Order
class A:
    num = 10


class B:
    pass


class C:
    num = 1


class D(B, C):
    pass


dd = D()
print(dd.num)

# 1
print(D.mro())
# D.__mro__()

# Functional Programming
# Pure Function
# Map(), Filter(), zip(),  Reduce()
my_list = [1, 2, 3]


def number_list(item):
    return item * 2


print(list(map(number_list, my_list)))


# filter


def is_odd(num):
    return num % 2 != 0


print(list(filter(is_odd, my_list)))

# zip()
your_list = [10, 20, 30]
# def
print(list(zip(my_list, your_list)))


# [(1, 10), (2, 20), (3, 30)]

# reduce()
# from functools import reduce
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
# 6

# lambda expressions
print(list(map(lambda numbers: numbers * 2, my_list)))
print(reduce(lambda acc, num: acc + num, my_list, 0))

# exercise to square a list

my_list = [5, 4, 3]

print(list(map(lambda square: square ** 2, my_list)))

# 2 List soring
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda num: num[1])
print(a)

# List Comprehensions or set or dictionary comprehensions
# a quick way to create list
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)
# instead of these in comprehension

# my_list = [param for param in iterable]
my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(0, 100)]
# print(my_list2) list down 0 - 99

my_list3 = [num * 2 for num in range(0, 100)]
# print(my_list3) 0, 2, 4, ...., 198
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
# print(my_list4) 0, 4, 16, 9467

# set, dictionary comprehension
my_list = {char for char in 'hello'}
print(my_list)

my_list2 = {num for num in range(0, 100)}
# print(my_list2) list down 0 - 99

simple_dict = {
    'a': 1,
    'b': 2
}
# my_dict = {key:value}
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
# print(my_dict) {'a': 1, 'b': 4}

my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)

# exercise comprehension
some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)

# python decorators
from time import time


def my_decorator(func):
    def wrap_function():
        t1 = time()
        print(t1)
        func()
        t2 = time
        print(t2())

    return wrap_function


@my_decorator
def hello():
    print('hello')


hello()


def performance(fn):
    def wrap_function(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}')
        return result

    return wrap_function


@performance
def long_time():
    for i in range(100000):
        i * 5


long_time()


def my_decorator(func):
    def wrap_function():
        print('********')
        func()
        print('********')

    return wrap_function


@my_decorator
def hello():
    print('hello')


hello()


def my_decorator(func):
    def wrap_function(x, y):
        func(x, y)

    return wrap_function


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)
    pass


a = my_decorator(hello)
a('Hey', ':) \n\n\n')


def my_decorator(func):
    def wrap_function(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_function


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
    pass


hello('Hey')
# error handling
try:
    x = 2
except Exception:
    print(Exception)
