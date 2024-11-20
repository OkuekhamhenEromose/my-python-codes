#Dictionary in python is like object in javascript



# person = {
#     'f_name': "John",
#     'l_name': "Doe",
#     "age": 23,
#     "m_status": False,
#     'disability': False,
# }
# print(type(person))//to check type of data type
# print(person)//to get the keys and values
# print(person["m_status"])//to get the value;
# person["age"] = +23409067784278//to add an item

# print(person.keys())//to return only keys
# print(person.items())//to return values but display also keys
# person2 = person.copy()// to dulicate person var
# person2['height'] = 5.6//to add to person2

# print(len())

# people = [
#     {
#         'id':1,
#         'f_name':'Alugo',
#         'l_name':'Zainab',
#         'm_status':'married',
#         'age':25
#     },
#     {
#         'id':2,
#         'f_name':'Akata',
#         'l_name':'Daniel',
#         'm_status':'married',
#         'age':25
#     },
#     {
#         'id':3,
#         'f_name':'charles',
#         'l_name':'Eromose',
#         'm_status':'married',
#         'age':25
#     }
# ]
# print(people)//to get all dictionaries
# print(people[1])//to get first dictionary in the list
# print(people[2]["m_status"])//to get that key in the 3rd dictionary


#::::::::::  ASSIGNMENT ON DICTIONARY ::::::::::::::::::::::::::

# :::::::  QUESTION 1
# person = {
#     'f_name': "John",
#     'l_name': "Doe",
#     "age": 23,
#     "m_status": False,
#     'disability': False,
# }

#:::::::::::  QUESTION 2
# print(person['age'])
# person['hobbies'] = "swimming"
# print(person)

#:::::::::::::  QUESTION 3
# person2 = person.copy()
# person2['height'] = 50.5
# print(person2)

#:::::::::::  QUESTION 4
people = [
    {
        'id':1,
        'f_name':'Alugo',
        'l_name':'Zainab',
        'm_status':'married',
        'age':25
    },
    {
        'id':2,
        'f_name':'Akata',
        'l_name':'Daniel',
        'm_status':'married',
        'age':25
    },
    {
        'id':3,
        'f_name':'charles',
        'l_name':'Eromose',
        'm_status':'married',
        'age':25
    }
]

print(people[2])


