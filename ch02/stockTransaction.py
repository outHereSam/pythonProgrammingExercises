# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
# • The number of shares that Joe purchased was 2,000.
# • When Joe purchased the stock, he paid $40.00 per share.
# • Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
# for the stock.
# Two weeks later, Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 2,000.
# • He sold the stock for $42.75 per share.
# • He paid his stockbroker another commission that amounted to 3 percent of the amount
# he received for the stock.
# Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount for which Joe sold the stock.
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the amount is
# negative, then Joe lost money.

STOCKS_PURCHASED = 2000
PURCHASE_PRICE_PER_STOCK = 40
PURCHASE_COMMISSION = 0.03

STOCKS_SOLD = 2000
SALE_PRICE_PER_STOCK = 42.75
SALE_COMMISSION = 0.03

amountPaidForStock = STOCKS_PURCHASED * PURCHASE_PRICE_PER_STOCK
purchaseCommission = amountPaidForStock * PURCHASE_COMMISSION
totalPurchaseAmount = amountPaidForStock + purchaseCommission

amountStockSoldFor = STOCKS_SOLD * SALE_PRICE_PER_STOCK
saleCommission = amountStockSoldFor * SALE_COMMISSION
totalSaleAmount = amountStockSoldFor * saleCommission

moneyLeft = totalSaleAmount - totalPurchaseAmount

print(f"Amount paid for stock: ${amountPaidForStock:,.2f}")
print(f"Amount of commission paid when he bought the stock: ${purchaseCommission:,.2f}")
print(f"Amount for which Joe sold the stock: ${amountStockSoldFor:,.2f}")
print(f"Amount of commission paid when Joe sold the stock: ${saleCommission:,.2f}")
print(f"Amount of money Joe has left: ${moneyLeft:,.2f}")
