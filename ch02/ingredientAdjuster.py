# A cookie recipe calls for the following ingredients:
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that
# asks the user how many cookies he or she wants to make, then displays the number of cups
# of each ingredient needed for the specified number of cookies.

SUGAR_CUPS = 1.5
BUTTER_CUPS = 1
FLOUR_CUPS = 2.75

COOKIES_PRODUCED = 48

userCookies = int(input("How many cookies do you want to make: "))

sugarCupsNeeded = (userCookies * SUGAR_CUPS) / COOKIES_PRODUCED
butterCupsNeeded = (userCookies * BUTTER_CUPS) / COOKIES_PRODUCED
flourCupsNeeded = (userCookies * FLOUR_CUPS) / COOKIES_PRODUCED

print(f"Cups of sugar: {sugarCupsNeeded:.2f}")
print(f"Cups of butter: {butterCupsNeeded:.2f}")
print(f"Cups of flour: {flourCupsNeeded:.2f}")
