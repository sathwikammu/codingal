def calculate_bill(item1, price1, item2, price2, item3, price3):
    """Calculate the total restaurant bill using positional arguments."""
    return price1 + price2 + price3


def seating_arrangements(n):
    """Calculate the number of seating arrangements for n people using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * seating_arrangements(n - 1)



total_bill = calculate_bill("Pizza", 250, "Burger", 150, "Juice", 100)

print("Total restaurant bill:", total_bill)

print("Docstring:", calculate_bill.__doc__)


people = 4
arrangements = seating_arrangements(people)

print("Number of people:", people)
print("Seating arrangements:", arrangements)