# Deep Copy

# In shallow copy the nested objects are shared not copied and deep copy solves that problem by copying nested mutable data.

# TO do the Deep copy we use the python library called
# copy so
from copy import deepcopy

num_1 = ["Sarthak", "Tiwari", 3]

num_2 = deepcopy(num_1)

# Now testing

print()
print(num_1 is num_2)   #
print(num_1[0] is num_2[0])

# note: - Even deepcopy creates independent copies of nested mutable objects, but immutable objects can be safely shared instead of being copied.

a = [[1, 2], 3, 4]
b = deepcopy(a)

print()
print(a is b)  # False because both are two seperate objects.
# False because this is nested list(Mutable), thats why both are  created seperately by python.
print(a[0] is b[0])
# True because the objects are immutable or primitive so they are shared rather than having new copy.
print(a[1] is b[1])
