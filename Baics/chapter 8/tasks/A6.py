class parents:
    # Class Variable (Shared by all objects)
    classs_varable = "var"

    # Constructor
    def __init__(self, name, classs, roll):
        # Instance Variables (Unique for each object)
        self.name = name
        self.classs = classs
        self.roll = roll

    # Instance Method
    def show(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Class:", self.classs)
        print("Roll :", self.roll)

    # Class Method
    @classmethod
    def class_method(cls):
        print("\nThis is a Class Method.")
        print("Class Variable =", cls.classs_varable)

    # Static Method
    @staticmethod
    def sum(a, b):
        print("\nSum =", a + b)


# Creating an Object
child = parents("Mahi", "BSC", 21049970)

# Display Original Instance Variable
print("Original Name:", child.name)

# Updating Instance Variable
child.name = "Dehi"

print("Updated Name:", child.name)

# Display Original Class Variable
print("\nOriginal Class Variable:", child.classs_varable)

# Updating Class Variable
parents.classs_varable = "Mahi"

print("Updated Class Variable:", parents.classs_varable)

# Calling Instance Method
child.show()

# Calling Class Method
child.class_method()

# Calling Static Method
child.sum(8, 9)