# shallow Copy

# What is copying in Programming?

# => Copying means Creating a ""new object"" based on  content/sate of an existing object.

# for e.g
nums1 = [1, 2, 3]

# This here is not copying rather it is referencing one object by two variables.
nums2 = nums1

# Meanwhile

# creates new list object of the nums1 and stores in nums3 and this my dear frendzos is copy.
nums3 = nums1.copy()  # Shallow Copy


print(nums1 is nums2)  # True
print(nums1 is nums3)  # False
print()
print(nums1 == nums2)  # True
print(nums1 == nums3)  # True

# Now

nums3.append(4)

print()
print(nums1)
print(nums3)


# Why it is Shallow Copy And Not DeepCopy

# for e.g

num_1 = [[1, 2], [3, 4], 5]
num_2 = num_1.copy()

print()
print(num_1 is num_2)
print(num_1[0] is num_2[0])
# This shouldn't be True but it is.

# *** Concept line :- In shallow copy, Python creates a new outer object, but the nested objects are not copied; their references are shared between the original and the copy.
