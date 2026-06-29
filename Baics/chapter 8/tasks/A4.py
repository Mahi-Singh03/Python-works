# Create a class
class Parents:
    # Class Variable (Shared by all objects)
    attribute1 = "value1"

    # Constructor
    def __init__(self, a, b):
        # Instance Variables (Unique for each object)
        self.a = a
        self.b = b

    # Method to display values
    def show(self):
        print("a =", self.a)
        print("b =", self.b)
        print("Class Attribute =", Parents.attribute1)



# Create an object (instance)

child1 = Parents("Mahi", "Singh")

print("Before Updating:")
child1.show()



# Update Instance Variables

child1.a = "Rahul"
child1.b = "Sharma"

print("\nAfter Updating Instance Variables:")
child1.show()



# Update Class Variable

Parents.attribute1 = "Delhi"

print("\nAfter Updating Class Variable:")
child1.show()