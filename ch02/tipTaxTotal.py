# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

TIP_PERCENTAGE = 0.18
SALES_TAX_PERCENTAGE = 0.07

mealCharge = float(input("Enter the charge for the food: $"))

tipAmount = mealCharge * TIP_PERCENTAGE
salesTax = mealCharge * SALES_TAX_PERCENTAGE

total = mealCharge + tipAmount + salesTax

print(f"Tip amount: ${tipAmount:,.2f}")
print(f"Sales tax: ${salesTax:,.2f}")
print(f"Total: ${total:,.2f}")
