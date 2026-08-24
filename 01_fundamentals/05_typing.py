# <!--  # dynamic type and static type  -->

# <!--  # In dynamic type the the object data type is speciied at the runtime,
# meanchile the static  typing means you need to declare the type whuile creating the variable .
# so C/C++ is static typed language, meanwhile Python and Javascript is dynamic typed language - ->

# <!--  # Strong Typed vs Weak Typed Language.

# # This means how strictly does the language handle the operations between different types. -->

# x = 10
# y = "15"

# # This will throw  error into the system that you cannot ddo the additon for the two different types.
# print(x + y)

# note_1 = "thats why python is dynamic and strongly typed language."
# note_2 = "JavaScript is Dynamic and weakly typed language because it does  implicit coersion or conversion"

# note_3 = " C is static typed and strongly typed language"

# note_4 = " Static for the types detemined "


# ########################## Duck Typing ##########################

# def make_speak(obj):
#     return obj.speak()


# class Dog:
#     def (self):
#  print("woof")

# Duck typing is a Python programming approach where we focus on an object's behavior rather than its specific type. If an object provides the methods or operations that our code needs, we can use it without explicitly checking its type

# Type Hint and Type Annotation

def addition(a: int, b: float
             # Type annotation tells what type of output we will get or should get.
             ) -> float:
    return a+b


# type hints do not perform strict check they are mainly for ides, developers , documentations and static type checkers
print(addition(5, "ramesh"))

# Any  : - Any value can be passwed it tells to type checker
# | Union  : it tels either this or that only only one of them can be passed.
