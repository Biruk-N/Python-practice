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
@@@
( )
  ;
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
new_cart2 = amazon_cart[:]
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