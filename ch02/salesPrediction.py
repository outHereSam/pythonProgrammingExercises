# A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales,
# then displays the profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

PROFIT_PERCENTAGE = 0.23

projectedTotalSales = float(input("Enter the projected amount of total sales: $"))

profit = projectedTotalSales * PROFIT_PERCENTAGE

print(
    f"The profit that will be made from ${projectedTotalSales:,.2f} is ${profit:,.2f}"
)
