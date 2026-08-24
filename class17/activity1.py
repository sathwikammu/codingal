try:
    number=int(input("enter the number: "))
    print("the number entered is ", number)
except ValueError as ex:
    print("exception:",ex)
    