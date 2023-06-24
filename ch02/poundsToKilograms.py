# One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
# the mass of an object in pounds and then calculates and displays the mass of the object in
# kilograms.

POUND_TO_KILO = 0.454

objectMass = float(input("Enter the mass of an object in pounds: "))

massInKilos = objectMass * POUND_TO_KILO

print(f"The mass of the object in kilograms is {massInKilos:.2f}kg")
