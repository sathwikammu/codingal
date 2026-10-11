# 1) Create a class named `Vehicle`.

# 2) Inside the class, define the constructor method `__init__(self, max_speed, mileage)`:
#    a) This method runs automatically when an object of the class is created.
#    b) It takes two inputs: `max_speed` and `mileage`.

# 3) Store the passed values inside the object using instance variables:
#    a) Assign `self.max_speed = max_speed`
#    b) Assign `self.mileage = mileage`

# 4) Create an object of the `Vehicle` class named `modelX`
#    by passing values for max speed and mileage: `Vehicle(240, 18)`.

# 5) Access the object’s instance variables and print them:
#    a) Print `modelX.max_speed` as the model’s max speed.
#    b) Print `modelX.mileage` as the model’s mileage.
class vehicle:
   def __init__(self,max_speed,mileage):
      self.max_speed=max_speed
      self.mileage=mileage
modelx=vehicle(240,18)
modely=vehicle(220,20)
print(modelx.max_speed,modelx.mileage)
print(modely.max_speed,modely.mileage)
modely.max_speed=300
print(modelx.max_speed,modely.max_speed)