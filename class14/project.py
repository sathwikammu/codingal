def calculate_total(price, quantity):
    return price * quantity

def calculate_bill(total, tax):
    return total + (total * tax / 100)

print("Welcome to the Art Supplies Billing Tool!")

item = input("Enter the art supply name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

tax = 5

total = calculate_total(price, quantity)
final_bill = calculate_bill(total, tax)

print("\n----- BILL -----")
print("Item:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Subtotal:", total)
print("Tax:", tax, "%")
print("Final Bill:", final_bill)
print("----------------")
print("Thank you for your purchase!")