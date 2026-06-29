# Create a Human class
class Human:
    name = "Unknown"  # class attributes-
    age = 0
    result = "Unknown"

# Create an instance
mahi = Human()

# Update the instance attributes
mahi.name = "Mahi"
mahi.age = 20
mahi.result = "Pass"

# Display the updated attributes
print("Name:", mahi.name)
print("Age:", mahi.age)
print("Result:", mahi.result)



print(Human.age)