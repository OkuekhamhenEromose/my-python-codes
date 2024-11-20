#  data types

# '''
# 1. string
# 2. int - integer
# 3. float
# 4. bool
# '''

# first_name = "Nathaniel"
# last_name = 'Nosa'
# salary = 4000000 #integer
# height = 5.2 #float
# is_Good = True #Bool

# '''
# print(first_name)
# print(last_name)
# print(salary)
# print(height)
# print(is_Good)
# '''

# first_name,last_name,salary,height,is_Good = ('Nathaniel', "Nosa", 40000000, 5.2, True)
# print(first_name,last_name,salary,height,is_Good)

# HOW TO ACCEPT INPUT==INPUT FUNCTION

# first_name = input('Enter your first name: ')//always gives a string
# last_name = input('Enter your last name: ')
# age = int(input('Enter your age: '))

# print(first_name, last_name, age)


# CHECKING DATA TYPES

# name = "charles"
# age = 25
# print(name)
# print(age)
# print(type(name))
# print(type(age))

# CASTING

# x = 6
# y = str(x)

# print(y)
# print(type(y))

# ======================== CLASS 2 ==========================
# ::::  CONCATENATION
# ex 1
# first_name = 'Eromose'
# last_name = 'Charles'

# full_name = first_name +' '+ last_name
# print(full_name)

#::: concatenation with number
# name = "Eromose"
# age = 26
# result = "Hello" + name + "I heard you are " + str(age) + "years old"
# print(result)

#::: string format
#::: 1. arguement by position
# name = "Eromose"
# age = 26
# print('hello {0} I heard you are {1} years old'.format(name,age))

#::: 2. arguement ny name
#::: 2a
# print('hello {name} I heard you are {age} years old'.format(name='Eromose', age=24))

#::: 2b
# first_name = 'Eromose'
# r_age = 30
# print('hello {name} I heard you are {age} years old'.format(name=first_name, age=r_age))

# 3. f-string
# name = 'Eromose'
# age = 34
# print(f'hello {name} I heard you are {age} years old')

# 4. Strings method and property
# name = "Nathaniel"
# print(name.capitalize())
# print(name.count('a'))
# print(name.endswith('l'))
# print(name.swapcase())
# print(len(name))
# print(name.replace('Nathaniel','Charles'))
# print(name.capitalize().count('a'))

#=======================  CLASSWORK  =======================
# name = 'Charles'
# age  = '45'
# time = 15.55
# casting_1 = int(age)
# print(casting_1)
# casting_2 = float(time)
# print(casting_2)

# # display fullname
# first_name = 'eromose'
# last_name = 'charles'
# fullname = first_name + " " + last_name
# print(fullname)

# # display length
# print(len(fullname))

# # uppercase
# print(fullname.capitalize())

# #count an alphabet
# print(fullname.count('e'))

# #replace your name to your colleagues name
# print(fullname.replace('charles', 'daniel'))



