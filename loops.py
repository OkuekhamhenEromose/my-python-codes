# FOR LOOPS
#//to print students
# students = ["Zainab","Daniel","Charles"]
# for student in students:
#     print(student)


# fruits = ["apple","orange","mango","cashew","pineapple"]
# for fruit in fruits:
#     print(fruit)

#Range
# stop //0-9
# for i in range(10):
#     print(i)
# # stop //0-10
# for i in range(10+1):
#     print(i)
# # with start //1-9
# for i in range(1,10):
#     print(i)
# # with step //1,3,5,7,9
# for i in range(1,10,3):
#     print(i)

# fruits = ["apple","orange","mango","cashew","pineapple"]
# ex: 1
# for i in range(len(fruits)):
#     print(i)
#     print(fruits[i])
# ex: 2

# for i in range(1,len(fruits),2):
    # print(i)
    # print(fruits[i])

# while
# number = 0// 0-9
# while number < 10:
#     print(number)
#     number += 1

#Break and Continue
# fruits = ["apple","mango","orange","cashew","pawpaw"]
# for fruit in fruits:
#     if fruit == "cashew":
#         break
#     print(fruit)

#ex 2
# fruits = ["apple","mango","orange","cashew","pawpaw"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "cashew":
#         break

# #ex 3
# numbers = [1,2,3,4,5,6,7,8]
# for number in numbers:
#     if number == 4:
#         continue
#     print(number)
# #ex 4
# numbers = [1,2,3,4,5,6,7,8]
# for number in numbers:
#     print(number)
#     if number == 4:
#         continue

#:::::::::::::::   CLASSWORK  :::::::::::::::::

#  QUESTION 1
# fruits = ["apple","mango","orange","cashew","pawpaw"]
# for fruit in fruits:
#     print(fruit)

# #  QUESTION 2

# name = "Charles Eromose"
# for item in range(6):
#     print(name)

# To take input from the user
# number = int(input("Enter a number: "))

# factorial = 1

# # check if the number is negative, positive or zero
# if number < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif number == 0:
#    print("The factorial of 0 is 1")
# else:
#    for item in range(1,number + 1):
#        factorial = factorial*item
#    print("The factorial of",number,"is",factorial)

#::::::::::::::: ASSIGNMENT REAL

# :::::::::::::;  ASSIGNMENT 1
# Multiplication table (from 1 to 10) in Python

# num = 17
# num = int(input("Enter a number: "))
# # To take input from the user
# # num = int(input("Display multiplication table of? "))

# # Iterate 10 times from item = 1 to 10
# for item in range(1, 11):
#    print(num, 'x', item, '=', num*item)


#:::::::::::::::  ASSIGNMENT 2
# Nested While Loop (Left-to-Right Format)
# row = int(input("Enter a number: "))

# while row <= 10:
#     col = 1
#     while col <= 10:
#         result = row * col
#         print(f"{row} x {col} = {result}", end="\t")
#         col += 1
#     print()  # Move to the next line for the next row
#     row += 1


#::::::::::::::;  ASSIGNMENT 3

msg = input("What's the secret password: ")

# Password attempt is 3 times, starts at 2, then 1 and ends when counter is 0
num = 2  

# bananas is the correct password
while msg != "bananas":  
    if num == 0:
        print("Too many wrong attempts. You are locked out!")  # exhausted all 3 attempts, should print given message.

    else:
        print(f"Wrong Password! You have {num} chances left")  # password incorrect, display attempts left
        msg = input("What's the secret password: ")
        num = num - 1

print("Correct")