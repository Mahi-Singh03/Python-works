# class declaration

class human:
    name = "unknown"
    age = 0

# creating an object of the class
person1 = human()

# accessing the attributes of the object
print("Name:", person1.name)
print("Age:", person1.age)



# modifying the attributes of the object
person1.name = "Mahi Singh"
person1.age = 25
person1.gender = "Male"

print("Name:", person1.name)
print("Age:", person1.age)
print("Gender:", person1.gender)





# The __init__() Constructor


class human:
    name = "unknown" #class attribute
    age = 0
    def greet(self):
        print("Hello, my name is", self.name)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating an object of the class
person1 = human("Mahi Singh", 25) #instance variables are passed as arguments to the constructor
# accessing the attributes of the object
print("Name:", person1.name)
print("Age:", person1.age)
# calling the method of the object
person1.greet()









