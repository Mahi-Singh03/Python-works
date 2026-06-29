

# 1. SIMPLE CLASS


# # A class is a blueprint for creating objects.
# class Student:
#     pass


# # Creating an object (instance)
# student1 = Student()

# print("Object Created:")
# print(student1)






# 2. CONSTRUCTOR (__init__)



# class Person:

#     # Constructor
#     # Automatically runs whenever an object is created.
#     def __init__(self):
#         print("Constructor Called!")

# person1 = Person()




# 3. SELF KEYWORD




# class Human:

#     def __init__(self, name):
#         # self refers to the current object
#         self.name = name

# human1 = Human("Mahi")

# print("Human Name:", human1.name)





# 4. INSTANCE VARIABLES




# class Employee:

#     def __init__(self, name, age):
#         # Instance Variables
#         self.name = name
#         self.age = age

# employee1 = Employee("Mahi", 20)
# employee2 = Employee("Rahul", 25)

# print(employee1.name)
# print(employee2.name)




# 5. INSTANCE METHODS


# class Car:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     # Instance Method
#     def show_details(self):
#         print("Brand :", self.brand)
#         print("Color :", self.color)

# car1 = Car("Toyota", "White")
# car1.show_details()



# 6. CLASS VARIABLES




# class SchoolStudent:

#     # Class Variable
#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

# student1 = SchoolStudent("Mahi")
# student2 = SchoolStudent("Rahul")

# print(student1.school)
# print(student2.school)



# 7. INSTANCE VARIABLE UPDATE



# class Animal:

#     def __init__(self, name):
#         self.name = name

# animal1 = Animal("Dog")

# print("Before Update:", animal1.name)

# # Updating instance variable
# animal1.name = "Cat"

# print("After Update :", animal1.name)



# 8. CLASS VARIABLE UPDATE

# class College:

#     # Class Variable
#     college_name = "Government College"

#     def __init__(self, student):
#         self.student = student

# student1 = College("Mahi")
# student2 = College("Rahul")

# print("Before Update")
# print(student1.college_name)
# print(student2.college_name)

# # Updating the class variable
# College.college_name = "SkillUp Institute"

# print("\nAfter Update")
# print(student1.college_name)
# print(student2.college_name)




# 9. CLASS METHOD


# class Company:

#     company_name = "OpenAI"

#     @classmethod
#     def show_company(cls):
#         # cls refers to the class itself
#         print("Company:", cls.company_name)

# Company.show_company()




# 10. CLASS METHOD TO UPDATE CLASS VARIABLE



# class University:

#     university_name = "Punjab University"

#     @classmethod
#     def change_university(cls, new_name):
#         cls.university_name = new_name

# print("Before:", University.university_name)

# University.change_university("Chandigarh University")

# print("After :", University.university_name)




# 11. STATIC METHOD


# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b

# result = Math.add(10, 5)

# print("Addition =", result)




# 12. ACCESSING ATTRIBUTES



# class Laptop:

#     def __init__(self, brand):
#         self.brand = brand

# laptop1 = Laptop("Dell")

# # Accessing attribute
# print(laptop1.brand)




# 13. MODIFYING ATTRIBUTES




# print("Before:", laptop1.brand)

# laptop1.brand = "HP"

# print("After :", laptop1.brand)



# 14. DELETING ATTRIBUTES



# class Mobile:

#     def __init__(self, model):
#         self.model = model

# mobile1 = Mobile("Samsung")

# print("Before Delete:", mobile1.model)

# # Delete attribute
# del mobile1.model

# print("Attribute Deleted!")

# Uncomment the next line to see the error
# print(mobile1.model)




# 15. COMPLETE EXAMPLE




class StudentComplete:

    # Class Variable
    school = "ABC Public School"

    def __init__(self, name, age, marks):
        # Instance Variables
        self.name = name
        self.age = age
        self.marks = marks

    # Instance Method
    def show_details(self):
        print("\nStudent Details")
        print("----------------")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Marks  :", self.marks)
        print("School :", StudentComplete.school)

    # Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static Method
    @staticmethod
    def welcome():
        print("\nWelcome to Python OOP!")



# Creating Objects
student1 = StudentComplete("Mahi", 20, 95)
student2 = StudentComplete("Rahul", 21, 90)

# Static Method
StudentComplete.welcome()

# Instance Method
student1.show_details()
student2.show_details()

# Updating Instance Variable
student1.marks = 100

print("\nAfter Updating Marks")
student1.show_details()

# Updating Class Variable
StudentComplete.change_school("SkillUp Institute")

print("\nAfter Changing School")

student1.show_details()
student2.show_details()



print("\n" + "=" * 60)
print("END OF PYTHON CLASS TUTORIAL")
print("=" * 60)