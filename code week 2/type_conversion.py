# Simple calculator with type conversion and formatted output

print("----- SIMPLE CALCULATOR -----")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert to float
try:
    num1 = float(num1)
    num2 = float(num2)

    print("\nCalculations:")
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division: {num1} / {num2} = {num1 / num2}")

except ValueError:
    print("Invalid input! Please enter numeric values only .")
