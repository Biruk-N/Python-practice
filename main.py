# name = input('add your name \n')
      
# print(name + ' first one')

# print(type(2 + 5))
# print(2**2)
# print(8//6)
# print(8//3)
#math functions
print(round(3.2))
print(abs(-39))

# operator precedence
print(12 - 4 * 4)

print(bin(2))
print(int('0b10', 2))

# variables

# expresions vs statement

# augumented assignment operators
x = 10
x += 2
print(x)

# strings and concatination
x = 'this is me' + ' ' +'and you'
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
print (emoji)

# formatted strings

name = 'Jhon'
age = 30
print(f'Hey {name} is {age}')

# imutability | `string` is immutable
# str = '01222'
# str[0] = '9'
# this is type error because string is immutable

# built-in functions
greet = 'hello'
print(greet[0:len(greet)])

qoute = 'to be or not to be'
# methods
print(qoute.capitalize())
print(qoute.upper())
print(qoute.find('be'))
print(qoute.replace('be', 'me'))

#boolean
name = 'Biruk'
is_cool = False

is_cool = True

print(bool(1))

name = 'Jhon'
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
  'singlasses',
  'toys',
  'grapes'
]
# list slicing
amazon_cart[0] = 'pc'
new_cart = amazon_cart
new_cart2 = amazon_cart[:] # amazon_cart.copy()
amazon_cart[0] = 'laptop'
print(new_cart) # this one update every time when amazon_cart updated
print(new_cart2) # only has amazon_cart value that assigned eariler
print(amazon_cart[0::2])
# lists are immutable

# Matrix
matrix = [
  [1, 2, 3], 
  [4, 5, 6],
  [7, 8, 9]
]
print(matrix[0][1])

#list method

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
print(basket) # by index remove like basket.pop(0)

basket.remove(4)# by value remove
print(basket)

new_list = basket.pop(4) # it holds a avalue that removed

# basket.clear()
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d', 2, 4)) # 2 & 4 are start and end of index to searching for d
print('d' in basket) # boolean value
print(basket.count('d'))
# ======
basket.sort()
print(basket)
# or
print(sorted(basket)) # it does't change the original value
basket.reverse()
print(basket)

# common list patterns
# to reverse slicing reverse

print(basket[::-1])
print(basket) # not changed by slicing reverse

print(range(1, 100)) # range(1, 100)
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
print(user.get('age', 44)) # if not exist

user2 = dict(name = 'John')
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
print(new_tuple) # (2,)

new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

#tuple methods are 2 count & index

print(my_tuple.count(4))
print(my_tuple.index(4, 1, 5))
print(len(my_tuple))

# set
# unordered collections of unique objetcs

my_set = {2, 4, 3, 4, 4, 5}
print(my_set) # {2, 3, 4, 5}
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

b =['dh', 'hd']
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

print(bool('hello')) # truthy

print(bool('')) #falsy

print(bool(0)) # falsy



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

print('a' > 'A') # True because
# indentation

is_old = True

is_licenced = True

if is_old and is_licenced:
    print('you\'r')
else:
    print('sorry')

print('okok')

# Truthy and falsy

print(bool('hello')) # truthy

print(bool('')) #falsy

print(bool(0)) # falsy



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

print('a' > 'A') # True because
# ternary operator
is_true = False
test = 'this on is true' if is_true else 'this is incorrect'
print(test)
# loops
# for loop
for item in 'this is a test':
  print(item)
  