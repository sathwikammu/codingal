"""
1) Add the activity details.
   a) Mention the activity name as "Snack Vending Machine".
   b) Introduce the program as a vending machine that accepts coins and gives change.

2) Create the change function.
   a) Define `calculate_change(paid, price)`.
   b) Subtract the snack price from the amount paid.
   c) Return the change value.

3) Set the snack price and greet the customer.
   a) Store the snack price in `snack_price`.
   b) Print the vending machine heading.
   c) Show the snack cost and accepted coin values.

4) Create tracking variables.
   a) Use `total_inserted` to track the total money inserted.
   b) Use `coins_inserted` to count how many coins were added.

5) Keep accepting coins.
   a) Use `while True` to keep the coin loop running.
   b) Ask the user to insert a coin.
   c) Convert the input into an integer.

6) Validate the coin.
   a) Check if the coin is not 1, 5, 10, or 25.
   b) Print an invalid coin message.
   c) Use `continue` to ask for another coin.

7) Add valid coins.
   a) Add the coin to `total_inserted`.
   b) Increase `coins_inserted` by 1.
   c) Print the inserted coin and running total.

8) Stop when enough money is inserted.
   a) Check if `total_inserted` is greater than or equal to `snack_price`.
   b) Print that enough money was inserted.
   c) Use `break` to stop the loop.

9) Calculate and give change.
   a) Call `calculate_change()` to find the change due.
   b) Print that the snack is being dispensed.
   c) Use `pass` when no change is needed.
   d) Print the change amount when extra money was inserted.

10) Print the purchase summary.
   a) Show the snack price.
   b) Show coins inserted and total paid.
   c) Show the change given.
   d) Print a thank you message to end the program.
"""

print("===snack vending machine===")
def calculate_change(paid,price):
    return (paid-price)
snack_price=int(14)
print("vending machine")
print("snack_price is 50 rs")
print("only 1,5,10,25 coins are accepted")
total_inserted=0#total money given by thye user
coins_inserted=0
while True :
    #print("enter the coin")
    x=int(input("enter the coin"))# it is user entering the money
    if x!=1 and x!=5 and x!=10 and x!=25:
        print("invalid coin")
        continue
    total_inserted+=x
    coins_inserted+=1  #no of coins inserted
    print("total money so far", total_inserted)
    print("total coins so far",coins_inserted)

    if total_inserted>=snack_price:
        print("enough money inserted")
        break
change = calculate_change(total_inserted, snack_price)

print("\nDispensing snack...")

if change == 0:
    pass
else:
    print("Change given:", change)

print("===== PURCHASE SUMMARY =====")
print("Snack Price:", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change)
print("Thank you !")
    

    