# Mutables

nums_object = [1, 2, 3, 4, 5]

nums_object.append(6)

print(nums_object)

# the Dynamic data types are mutable objects.
# the original object was modified and no new object was created outside that object.

# Immutable

num1 = 10

# Here the variable as been rebound to new object that is  int 11 and old object(10) has been abondoned by num1 and it becomes eligible for memory reclamation or garbage collection.
num1 = num1 + 1
print(num1)
