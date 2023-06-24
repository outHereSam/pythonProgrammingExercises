# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments,
# then display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

purchaseAmount = float(input("Enter the amount of a purchase: $"))
numOfInstalments = int(input("Enter the number of payment instalments: "))

totalPurchaseAmount = purchaseAmount + (purchaseAmount * 0.05)
pricePerInstalment = totalPurchaseAmount / numOfInstalments

print(f"Total purchase amount: ${totalPurchaseAmount:,.2f}")
print(f"Price per instalment: ${pricePerInstalment:,.2f}")
