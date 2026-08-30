import random
import math

print("=== Random Fun Calculator ===")

lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

activities = ["Coding", "Gaming", "Reading", "Music", "Drawing"]
activity = random.choice(activities)
print("Random activity for you:", activity)

print("\n=== Math Functions ===")

number = random.uniform(1, 20)

print("Number:", number)
print("Ceil:", math.ceil(number))
print("Floor:", math.floor(number))
print("Absolute value:", math.fabs(-number))
print("Copy sign:", math.copysign(number, -1))
print("GCD of 48 and 18:", math.gcd(48, 18))

print("\n=== Number Guessing Game ===")

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct! You guessed it!")
else:
    print("Wrong! The number was:", secret)

print("\nThank you for using Random Fun Calculator!")