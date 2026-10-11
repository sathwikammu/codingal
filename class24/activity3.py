# 1) Create a class named `Parrot`.

# 2) Define a class attribute `species = "bird"`.
#    (This attribute is shared by all objects of the class.)

# 3) Define the constructor method `__init__(self, name, age)`:
#    a) This method runs when a new object is created.
#    b) It takes two inputs: `name` and `age`.
#    c) Store these values using instance attributes:
#       - `self.name = name`
#       - `self.age = age`

# 4) Create (instantiate) two objects of the `Parrot` class:
#    a) `blu = Parrot("Blu", 10)`
#    b) `woo = Parrot("Woo", 15)`

# 5) Access and print the class attribute `species` using both objects:
#    a) Print that Blu is a bird.
#    b) Print that Woo is also a bird.

# 6) Access and print the instance attributes (`name` and `age`) for each object:
#    a) Print Blu’s name and age.
#    b) Print Woo’s name and age.
class parrot:
    speices="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu= parrot("Blu", 10)
woo = parrot("Woo", 15)
print(blu.age,blu.name)
print(woo.age,woo.name)
print(blu.speices,woo.speices)
blu.speices="animal"
print(blu.speices,woo.speices)
