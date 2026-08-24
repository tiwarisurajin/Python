"""
PYTHON FUNDAMENTALS — DAY 1
Topic: Objects, Variables & Types

==================================================
LEARNING OBJECTIVES
==================================================

1. Values
2. Objects
3. Variables
4. Assignment
5. Types
6. References
7. Object identity
8. id()
9. type()
10. == vs is
11. Mutable vs immutable objects
12. Dynamic typing
13. Multiple references
14. Python's object model
15. Common interview questions
16. Common mistakes
"""

# ==================================================
# THEORY + EXAMPLES
# ==================================================


# ==================================================
# PRACTICE
# # ==================================================


# # ==================================================
# # INTERVIEW
# # ==================================================


# # # Values

# # "Suraj", 3.14, True, None, [1, 2, 3]  # all these are values

# # x = 10
# # # 10 is an object  reprsenting the integer value 10.
# # # x is an variable that refers to that object
# # print(type(x))
# # print(id(x))

# # y = x     # here the python gave the reference
# # #  point of object x to y, without creating any other value
# # print(id(y))
# # print(x is y)


# # y = 20  # Now Y is pointing to object 20 not the object of x

# print(x is y)
# name = "Suraj"
# numbers = [1, 2, 3]
# is_active = True
# print(type(name))
# print(type(numbers))n
# print(type(is_active))

# # place = 'Jodhpur'

# # type(place)  # type()  is used to chec k datatype
# # id(place)    # id() is used to find identity of objct


# now
# is  checks wether two   variables have same object or not
# == checks wether two values match or not
# a = "Ramesh"
# b = "Ramesh"

# # print(a is b) # True this should be false but because of some caching python is not able to differentiate that each var has seperatre objects.

# # print(a == b) # True


# # this error happens because python creates catch for small  values that may be used in high frequency. but for dynamic datatypes python creates seperatee objects.
# # for e.g
# # num1 = [1, 2, 3, 4, 5]
# # num2 = [1, 2, 3, 4, 5]

# # print(num1 is num2)

# # print(num1 == num2)


# # id()
# # because of cache all ids will print same number
# a = 10
# b = 10
# c = a

# print(id(a))
# print(id(b))
# print(id(c))

# # id( witrh refernce datatype)

# a = [10]
# b = [10]
# c = a

# print(id(a))
# print(id(b))
# print(id(c))



## Mutable vs Immutable 