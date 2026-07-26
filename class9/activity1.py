#Add the activity details.
 #  a) Mention the activity name as "Custom Ride Builder".
  # b) Mention the file name as `ride_builder.py`.
   #c) Mention the lesson as "Nested Conditional Statements".

#2) Display the welcome message.
 #  a) Print a title banner for the ride builder.
  # b) Add blank lines to keep the output neat.

#3) Show the first vehicle choices.
  # a) Display Bike as option 1.
   #b) Display Car as option 2.
  # c) Ask the user to enter 1 or 2.

#4) Check the main choice.
 #  a) Use `if` when the user chooses Bike.
  # b) Use `elif` when the user chooses Car.
   #c) Use `else` for an invalid choice.

#5) Use nested conditions for Bike.
 #  a) Show bike type options only if the user picked Bike.
  # b) Ask the user to choose Scooty or Mountain Bike.
   #c) Use an inner `if-else` to display the selected bike details.

#6) Use nested conditions for Car.
 #  a) Show car type options only if the user picked Car.
  # b) Ask the user to choose Sedan or SUV.
   #c) Use an inner `if-else` to display the selected car details.

#7) Display ride details.
 #  a) Print the selected ride name.
  # b) Print speed or seat information.
   #c) Print what the ride is best used for.

#8) Handle invalid input.
 #  a) Show an error message if the first choice is not 1 or 2.
  # b) Ask the user to enter the correct option next time.

#9) End the program.
 #  a) Print a closing banner.
  # b) Display a message saying the custom ride is ready.
#"""
print("welcome")
x=input("bike as 1 and car as 2")
if x=="1":
    y=input("scooty as 1 or mountain bike as 2")
    if y=="1":
        print("sccoties are fun to raid")
        print("max speed is 100km/hr")
    else:
        print("mountain biking is adventures")
        print("max speed is 200km/hr")
elif x=="2":
    z=input("sedan as 1 and suv as 2")
    if z=="1":
        print("sedan is a 6 seater car")
        print("max speed 220km/hr")
    else:
        print("suv is luxiours car")
        print("max speed is 260km/hr")
else:
    print("invalid input ")
    


