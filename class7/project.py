ch = input("Enter a single character: ")

if len(ch) == 1:
    print("ASCII Value:", ord(ch))

    if ch.isupper():
        print("Category: Uppercase Letter")
    elif ch.islower():
        print("Category: Lowercase Letter")
    elif ch.isdigit():
        print("Category: Digit")
    else:
        print("Category: Special Character")
else:
    print("Please enter only one character.")