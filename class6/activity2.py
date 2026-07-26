# 1) Store values in `a`, `b`, and `c`.

# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).

# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).

# 4) Store two strings in `a` and `b`.

# 5) If `a` is not equal to `b`, print a message saying they are different.

# 6) Store new numeric values in `a` and `b`.

# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
#    - If exactly one of these comparisons is True, the condition becomes True.
#    - If the condition is True, print "Hello".

# 8) Take an integer input from the user and store it in `a`.

# 9) Check if `a` is not divisible by 2 (remainder is not 0).
#    - If true, print that `a` is not an even number (it is odd).

a=2
b=6
c=9
if a!=b:
    print("true")
else:
    print("false")
if b!=c:
    print("true")
else:
    print("false")
a=str(a)
b=str(b)
c=str(c)
if a!=b:
    print("different")
else:
    print("same")

a=7
b=6
if (a==1) != (b==5):
    print("hello")

a=input("enter the number")
a=int(a)
if a%2:
    print("a is odd")
else:
    print("a is even")

