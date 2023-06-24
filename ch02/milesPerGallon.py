# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used.
# It should calculate the car's MPG and display the result.

milesDriven = int(input("Enter the number of miles driven: "))
gallonsUsed = int(input("Enter the number of gallons of gas used: "))

milesPerGallon = milesDriven / gallonsUsed

print(f"The car's miles-per-gallon is {milesDriven:.2f}mpg")
