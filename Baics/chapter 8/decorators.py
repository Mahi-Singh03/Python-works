"""
=========================================================
PYTHON METHODS & DECORATORS - COMPLETE TUTORIAL
=========================================================
Run this file from top to bottom.
Covers:
1. Methods
2. Instance Methods
3. Decorators
4. Class Methods
5. Static Methods
6. Factory Methods
7. @property
8. Common Mistakes
"""

print("="*60)
print("PYTHON METHODS & DECORATORS TUTORIAL")
print("="*60)

# 1. METHOD
print("\n1. METHODS")
class Student:
    def greet(self):
        print("Hello from a method!")
s=Student()
s.greet()

# 2. INSTANCE METHOD
print("\n2. INSTANCE METHODS")
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)
p=Person("Mahi")
p.show_name()

print("\nPython automatically passes self:")
print("p.show_name() -> Person.show_name(p)")

# 3. DECORATORS
print("\n3. DECORATORS")
def decorator_function(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorator_function
def say_hello():
    print("Hello")
say_hello()

print("\nEquivalent without @")
def bye():
    print("Bye")
bye=decorator_function(bye)
bye()

# 4. CLASS METHODS
print("\n4. CLASS METHODS")
class School:
    school="ABC School"
    @classmethod
    def show_school(cls):
        print("School:",cls.school)
School.show_school()
obj=School()
obj.show_school()

# 5. MODIFY CLASS VARIABLE
print("\n5. MODIFY CLASS VARIABLE")
class Company:
    company="Google"
    @classmethod
    def change_company(cls,new):
        cls.company=new
print("Before:",Company.company)
Company.change_company("Microsoft")
print("After :",Company.company)

# 6. STATIC METHODS
print("\n6. STATIC METHODS")
class Math:
    @staticmethod
    def add(a,b):
        return a+b
print("10+20 =",Math.add(10,20))

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c*9/5)+32
print("25C =",Temperature.celsius_to_fahrenheit(25),"F")

# 7. COMPARISON
print("\n7. ALL THREE METHODS")
class Demo:
    school="ABC"
    def instance_method(self):
        print("Instance Method")
    @classmethod
    def class_method(cls):
        print("Class Method:",cls.school)
    @staticmethod
    def static_method():
        print("Static Method")
d=Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()

# 8. self vs cls
print("\n8. self vs cls")
class Example:
    value="Shared"
    def instance(self):
        print("self accesses:",self.value)
    @classmethod
    def classmethod_demo(cls):
        print("cls accesses:",cls.value)
e=Example()
e.instance()
Example.classmethod_demo()

# 9. FACTORY METHOD
print("\n9. FACTORY METHOD")
class Employee:
    def __init__(self,name):
        self.name=name
    @classmethod
    def create_default(cls):
        return cls("Mahi")
emp=Employee.create_default()
print(emp.name)

# 10. PROPERTY
print("\n10. @property")
class Result:
    def __init__(self,marks):
        self.marks=marks
    @property
    def percentage(self):
        return self.marks/5
r=Result(400)
print("Percentage:",r.percentage)

# 11. COMMON MISTAKES
print("\n11. COMMON BEGINNER MISTAKES")
print("- Forgetting self in instance methods")
print("- Forgetting cls in class methods")
print("- Using self inside static methods")

# 12. COMPLETE EXAMPLE
print("\n12. COMPLETE EXAMPLE")
class StudentComplete:
    school="SkillUp Institute"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print(f"{self.name} | Marks={self.marks} | School={self.school}")
    @classmethod
    def change_school(cls,new):
        cls.school=new
    @staticmethod
    def grade(marks):
        if marks>=90:return "A+"
        elif marks>=75:return "A"
        elif marks>=60:return "B"
        return "C"
    @classmethod
    def create_demo(cls):
        return cls("Demo Student",95)
    @property
    def percentage(self):
        return self.marks

StudentComplete.show
a=StudentComplete("Mahi",96)
b=StudentComplete.create_demo()
a.show()
b.show()
print("Grade:",StudentComplete.grade(a.marks))
print("Percentage:",a.percentage)
StudentComplete.change_school("ABC Public School")
a.show()
b.show()

print("\\nTutorial Complete!")
