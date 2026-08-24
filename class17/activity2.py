# 1) Start a `try` block to run code that may cause exceptions.

# 2) Take two numbers from the user in a single input, separated by a comma:
#    a) Use `eval(input(...))` to read and convert the input.
#    b) Store the two values in `num1` and `num2`.

# 3) Perform division:
#    a) Compute `result = num1 / num2`.
#    b) Print the result.

# 4) Handle possible errors using multiple `except` blocks:

# 5) If a `ZeroDivisionError` occurs (when `num2` is 0),
#    print "Division by zero is error !!".

# 6) If a `SyntaxError` occurs (for example, the comma is missing or format is incorrect),
#    print a message explaining the correct input format: "1, 2".

# 7) If any other error occurs, use a general `except` block
#    and print "Wrong input".

# 8) If no exception occurs in the `try` block, run the `else` block
#    and print "No exceptions".

# 9) Run the `finally` block no matter what happens (error or no error),
#    and print "This will execute no matter what".
try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    result=num1/num2
    print(result)
except ZeroDivisionError :
    print("division by zero is error")
except SyntaxError:
    print("thye correct format is 1,2")
except Exception:
    print("wrong input")
else:
    print("no exceptions") 
finally:
    print("this will execute no matter what")
