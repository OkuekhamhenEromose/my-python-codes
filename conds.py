

#:::::::::::::  CONDITIONS
# if & else statement

#if
# x = 10
# y = 5
# if x == y:
#     print(f'{x} is equal to {y}')


# if & else statement
# x = 10
# y = 5
# if x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{x} is not equal to {y}')

# name = input('Enter your name: ').lower()
# if name == "Zainab":
#     print(f'allow her to take the exam')
# else:
#     print(f'you are not a registered user')


#rain, sunny, harmattan
# weather = input("Enter weather: ").lower()
# if weather == "rainy":
#     print(f'Kindly take your umbrella.')
# elif weather == "harmattan":
#     print(f'Use your cardigan.')
# elif weather == "sunny":
#     print(f'Put on your sunshades.')
# else:
#     print(f'The weather is good ')

# 5 - 30
# age = int(input("Enter age for immunization: "))
# if age >=5 and age <=30:
#     print(f'Yes you are eligible for the immunization')
# elif age > 30:
#     print("You are too old for this program")
# else:
#     print(f'eat well to grow fast')

#Nested
# x = 6
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than 10') 

# logical operators
# AND
# x=6
# if x > 2 and x < 10:
#     print(f'{x} is greater than 2 and less than 10')
# else:
#     print(f'{x} is not among the number')

# OR
# x=6
# if x > 2 or x < 10:
#     print(f'{x} is greater than 2 and less than 10')

#NOT
# x=6/16
# if not(x > 2 and x < 10):
#     print(f'{x} is greater than 2 and less than 10')
# else:
#     print(f'false')

# number = [1,2,3,4,5,6]
# x = 6
# if x in number:
#     print(x in number)//True

# NOT IN
# number = [1,2,3,4,5,6]
# x=7
# if x not in number:
#     print(x in number)//False

# IDENTITY OPERATORS
# is
# x = 10
# y = 10
# if x is y:
#     print(x is y)//True

# is not
# x = 10
# y = 5
# if x is not y:
#     print(x is not y)



#::::::::::::  ASSIGNMENT  
#::::::::::::  CLASSWORK
# QUESTION 1
# number = int(input("Enter number here: "))
# if number%2 == 1:
#     print(f'this is a odd number')
# else:
#     print(f'this is a even number')

# QUESTION 2
# # # alphabet = str(input("Enter an alphabet here"))
#     # if x = str(input("Enter an alphabet here")):
# alphabet = str(input("Enter an alphabet: "))
# if alphabet == ["a","e","i","o","u"]:
#     print(f'its a vowel word')
# else:
#     print(f'its a consonant word')

# alphabet = input("Enter a letter: ").lower()
# if alphabet in 'aeiou':
#     print(f'{alphabet} is a vowel')
# else:
#     print(f'{alphabet} is a consonant')

#::::::::::::::::;  REAL ASSIGNMENT

#::::::::::::::::::: QUESTION 1
# Accept three numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Find the greatest number
# if num1 >= num2 and num1 >= num3:
#     print(f"The greatest number is: {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The greatest number is: {num2}")
# else:
#     print(f"The greatest number is: {num3}")


#:::::::::::;; QUESTION 2

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def calculator():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please select a number between 1 and 4.")

# Run the calculator
calculator()




