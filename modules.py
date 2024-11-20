# core modules

# ex 1
# import datetime
# today = datetime.date.today()
# print(today)

# ex 2
# from datetime import date
# today = date.today()
# print(today)

# ex 3
# from uuid import uuid5
# id = uuid5()
# print(id)

# ex 4
# import uuid
# id = uuid.uuid4()
# print(id)


from camelcase import CamelCase

c = CamelCase()
text = "Hello World!"
print(c.hump(text))

#custom
# from loops import fruits // to begin operation of another file on a variable in this file. That is print(fruits)

# from loops import * // to begin operation of another file of all variable in this file

# from loops import person as py // to produce the short form for that variable.That is print(py)
