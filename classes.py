
#  ::::::::::::::::::::  INSTANCE OF A CLASS  ::::::::::::::::::
# instance of a class is subdivided into (1) property (2) method

# class BluePrintDog:

# (1) PROPERTY
    # def __init__(self,name,height,legs,color):# to identify property __init__(self)
    #     self.name = name
    #     self.height = height
    #     self.legs = legs
    #     self.color = color

# #  create objects = initializing a class object   
# dog1 = BluePrintDog('Bingo',2.4,5,'black')
# dog2 = BluePrintDog('speed',4.2,4,'brown')
# print(dog1.name)
# print(dog1.height)
# print(dog2.name)
# print(dog2.height)

# (2) METHOD

#     def bark(self):
#         return f'my name is {self.name} and I can bark'
#     def run(self):
#         return f'I saw {self.name} run with is {self.legs} legs'
# dog1 = BluePrintDog('Bingo',2.4,5,'black')
# print(dog1.bark())
# print(dog1.run())


# INHERITANCE

# class Person:
#     def __init__(self,name,email,age):
#         self.name = name
#         self.email = email
#         self.age = age
#     def greetings(self):
#         return f'my name is {self.name} and I am {self.age}. you can mail me at {self.email}'

# class User(Person):
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.sex = 'Male'
#     def gender(self,sex):
#         self.sex = sex

# John = User('Zainab', 'John@gmail.com', 20)
# John.gender('Male')
# print(John.sex)

# ::::::::::::::;  CLASSWORK  ::::::::::::::::::::
#  ::::::::::::::  CLASSWORK (1)  :::::::::::::;
# class User:
#     def __init__(self,name,greeting):
#         self.name = name
#         self.greeting = greeting
#     def greet(self):
#         return f'my name is {self.name} and I am greeting you {self.greeting}'
# joy1 = User('jane','good morning')
# print(joy1.greet())

#  :::::::::::::::::::;  CLASSWORK (2)  ::::::::::::;;
#  =========  AS IN EXAMPLE  =================

# import math

# class Cylinder:
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height

#     def surface_area(self):
#         return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height

#     def volume(self):
#         return math.pi * self.radius**2 * self.height

# # Example usage:
# cylinder = Cylinder(9, 15)
# print(cylinder.surface_area())
# print(cylinder.volume())

#  ::::::::::::::::::::;  ASSIGNMENT  ::::::::::::::::;;

#  :::::::::::::::::::  CLASS OF A CLASS  :::::::::::::::
#  ::::::::::::::  Property Of A Class  ::::::::::
# class Students:
    # gender = 'male'# not use __init__

#  :::::::::::::::::;  Method Of A Class  ::::::::::;
    # @classmethod
    # def greet(cls):
    #     pass

#  :::::::::::;  EXAMPLE  :::::::::::::;
# class Circle:
#     pie = 3.142

#     @classmethod
#     def value(cls):
#         return f'a circle has a default pie value of = {cls.pie}'

# ci = Circle()# class of a class can be accessed by the object(ci).pie and the class(Circle).pie
# print(ci.pie)
# print(ci.value())


