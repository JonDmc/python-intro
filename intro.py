# this is a comment -- will not be executed

#multi
#line
#comment

"""
this is a doc string -- we will learn more about this kind of special comment later
-more than one line
"""

# variables use 'snake_case' -- lowercase and spaces get underscores
my_var = 'hello snakes!'

print(my_var)

"""
How to run the file:
-> pyhton3 <filename.py>
"""
# ## ## ## ## ## #

# DATA TYPES

# Bools

None # falsey -- like null and undefined all in one
True # a truthy bool
False # a Falsey bool

# Text type
str # string constructor
# literals
my_string = "double quotes are cool"
my_other_string = 'single quotes are fine too'

# Number types 
# integers -- whole numbers
int
my_int = 30
# floating points or floats -- decimals
float
my_float = 1.0123123
# complex nums
complex
my_complex = 3j
my_other_complex = 2j

# Container Types
# List  (aka an array)
list
my_li = [ 0, 1, 5, 'hello', 'big snakes']

# Dictionary (aka object -- but not in python)
dict
my_dictionary = {
    'animal': 'snakes'
}

# ## # ## # ## # ## 
# Control flow w if/else

# three bools
None
True
False

# logical operators
"""
and # &&
or # ||
not or ! # ! 

 """ 


# comparison operators
"""
== # equality
> # who is bigger \
<
>=
<=

"""

my_bank_account = False
amount_of_money = 100

# conditionals start with 'if' keyword
if my_bank_account and amount_of_money >= 1000:
    print('you are ballin')
elif my_bank_account: # elif = else if
    print('put more money in the bank!')
else:
    print('you should get some money!')

# ## # ## # ## # ## # ##
# Math

# math operators
# +, -, /, *, =, %
# ** to the power of
# // forced integer division
# print( 10 + 10)
# print (2 ** 7) # 2^7
print (15// 2.7) # forced integer division flooes the output

my_complex = 1 +3j + 5j + 2
print(my_complex)

print(1 + int("1")) # pyython will not do automatic conversion of types

# ## # ## # ## #

# String instance methods
my_str = 'spam and eggs'

print(dir(str)) # print the string directory to see all the methods
# dunder methods -> internal private method (do not touch)

spam_list = my_str.split(" ") #split on the whitespace
print(spam_list)

print(my_str.upper())
print(my_str.lower())

# finding the length of the string
print(len(my_str))

# 'in' keyword to find if a string contains a substring
print("eggs" in my_str)
