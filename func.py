

#function is a block of code that only runs when you cal it

# def sayHello():
#     print(f'hello how are you doing')
# sayHello()


# def listOfPeople():
#     people= ["Zainab","Daniel","Charles"]
#     print(people)
# listOfPeople()

#:::function with arguement
# def sayMyName(name,age):
#     print(f'hello my name is {name}, and my age is {age}')
# sayMyName("Zainab",23)

# def sayMyName(name="Nathaniel", age=25):
#     print(f'hello my name is {name}, and my age is {age}')
# sayMyName("Zainab",32)

#return:::Return Value
# def sayHello():
#     return f'hello how are you doing'
# print(sayHello())

# def sayHello(name="Nathaniel"):
#     return(f'hello my name is {name}')
# print(sayHello("Nosa"))

# def getSum(num1,num2):
#     num1 = float(input("Enter num one: "))
#     num2 = float(input("Enter num one: "))
#     total = num1 + num2

#     return total
# print(getSum('2','4'))

# def calculate(num1,num2,num3=4):
#     sumNum = num1 + num2 + num3
#     return sumNum
# print(calculate(6,3))

# def calculate(num1,num2,num3=4):
#     sumNum = num1 + num2 + num3
#     return f'the sum of {num1} + {num2} + {num3} = {sumNum}'
# print(calculate(2,3))

# getSum = lambda num1, num2 : num1 + num2
# print(getSum(3,5))

#::::::::::::::::ASSIGNMENT

#:::::::::  CLASSWORK
#:::::::::::  QUESTION 1
def getSum(num1,num2):
    num1 = float(input("Enter num one: "))
    num2 = float(input("Enter num one: "))
    total = num1 + num2

    return total
print(getSum('',''))

# def getSub(num1,num2):
#     num1 = float(input("Enter num one: "))
#     num2 = float(input("Enter num one: "))
#     total = num1 - num2

#     return total
# print(getSub('',''))

# def getMultiple(num1,num2):
#     num1 = float(input("Enter num one: "))
#     num2 = float(input("Enter num one: "))
#     total = num1 * num2

#     return total
# print(getMultiple('',''))

# def getDiv(num1,num2):
#     num1 = float(input("Enter num one: "))
#     num2 = float(input("Enter num one: "))
#     total = num1 / num2

#     return total
# print(getDiv('',''))


#:::::::::::::  ASSIGNMENT REAL
# QUESTION 1
# def calculate(num1,num2=4):
#     sumNum = num1 + num2
#     return sumNum
# print(calculate(2))

# QUESTION 2//put bracket
def calculate(num1,num2,num3):
    sumNum = (num1 + num2) - num3
    return sumNum
print(calculate(6,3,2))



