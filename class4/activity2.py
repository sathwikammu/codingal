# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.

# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.

# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.

x=input("enter the amount")
x=int(x)
n1=x//100   #n1 is no of 100 notes

r1=x%100   #r1 is remainder amount

n2=r1//50  #n2 is no of 50 notes

r2=r1%50   

n3=r2//10

print(n1,n2,n3)

