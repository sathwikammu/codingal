# ==========================================

# LEMONADE STAND

# ==========================================

# PART 1:

# Define a function with no arguments to greet the customer

# The function should print two welcome messages

# PART 2:

# Call the greet_customer function

# PART 3:

# Ask the user to enter:

# - The price per cup in dollars

# - The number of cups sold

# Store the values in appropriate variables

# PART 4:

# Define a function that takes the price and number of cups as arguments

# Multiply the price by the number of cups

# Return the total cost

# PART 5:

# Call the calculate_total function using the price and cups sold

# Store the returned value in a variable

# PART 6:

# Use the round() built-in function to round the total cost to 2 decimal places

# Print the rounded total cost

# PART 7:

# Ask the user to enter the amount of money paid by the customer

# Store the value in a variable

# PART 8:

# Define a function that takes the amount paid and total cost as arguments

# Calculate the change by subtracting the total cost from the amount paid

# Return the change

# PART 9:

# Call the calculate_change function

# Store the returned value

# Round the change to 2 decimal places

# PART 10:

# Define a function that takes the number of cups sold as an argument

# If 5 or more cups were sold:

# Return a message thanking the customer for the big order

# Otherwise:

# Return a normal thank-you message

# PART 11:

# Call the thank_you_message function using the number of cups sold

# Store the returned message in a variable

# PART 12:

# Print the final lemonade stand receipt

# Display:

# - Price per cup

# - Cups sold

# - Total cost

# - Amount paid

# - Change due

# - Thank-you message

# Print a line to mark the end of the receipt

print("===lemonade stand===")
def greet_customer():
    print("welcome to the store")
greet_customer()

x=float(input("price per cup in dollar"))
y=float(input("no.of cups sold "))

def multiply(x,y):
    return x*y

z=multiply(x,y)

z=round(z,2)
print(z)

a=float(input("amount that you have paid"))
def subtraction(z,a):
     return z-a
b=subtraction(z,a)
print(b)

def numberofcups(y):
    if y>=5:
        return "thank you for the big order"
    else:
        return "thank you"





