# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

v=2
w=3
x=5
y=6
z=7

z=(v+w)*x/y
print(z)
name="rahul"
age=15
if name=="alex" or name=="jhon" and age>=2:
    print("welcome")
else:
    print("good bye")

