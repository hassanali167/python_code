# Exploring data types and dynamic assignment

name = "Aleem"
age = 21
percentage = 85.5
is_enrolled = True
complex_number = 2 + 3j


print("----- DATA TYPES DEMO -----")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Percentage:", percentage, "| Type:", type(percentage))
print("Is Enrolled:", is_enrolled, "| Type:", type(is_enrolled))
print("Complex Number:", complex_number, "| Type:", type(complex_number))

# Now change the values and types
age = str(age)
percentage = int(percentage)

print("\n-- After Type Conversion --")
print("Age (as string):", age, "| Type:", type(age))
print("Percentage (as int):", percentage, "| Type:", type(percentage))
