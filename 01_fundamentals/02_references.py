# References

# e.g

num_1 = [1, 2, 3, 4, 5]

num_2 = num_1
num_3 = num_2

# here one object is being referenced or pointed by 3 variables.
# print(id(num_1))
# print(id(num_2))
# print(id(num_3))

# Differce between num_2 = num_1 and num_2 = num_1.copy()

a = [1, 2, 3]


b = a

print(id(a))
print(id(b))
print()    # to add blank space
# check result both have same object id, that means here only a reference has been add no new object has been created.

c = a.copy()
print(id(a))
print(id(c))
# here a new object has been created a clone object of a.
