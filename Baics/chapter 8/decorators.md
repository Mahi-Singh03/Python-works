# Class Methods and Decorators in Python

---

# Introduction

In Python, methods inside a class can behave differently depending on how they are defined.

Python provides three main types of methods:

1. Instance Methods
2. Class Methods
3. Static Methods

To create Class Methods and Static Methods, Python uses **Decorators**.

Understanding these concepts is important because they are widely used in Object-Oriented Programming (OOP), frameworks, and real-world applications.

---

# What is a Method?

A method is a function defined inside a class.

Example:

```python
class Student:

    def greet(self):
        print("Hello")
```

Here:

```python
greet()
```

is a method.

---

# Types of Methods in Python

| Method Type     | First Parameter | Works With        |
| --------------- | --------------- | ----------------- |
| Instance Method | self            | Object Data       |
| Class Method    | cls             | Class Data        |
| Static Method   | None Required   | Independent Logic |

---

# 1. Instance Methods

Instance methods work with object-specific data.

They use:

```python
self
```

as the first parameter.

---

# Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

student1 = Student("Mahi")

student1.show_name()
```

---

# Output

```python
Mahi
```

---

# How It Works

When Python executes:

```python
student1.show_name()
```

Python automatically sends:

```python
self = student1
```

Therefore:

```python
self.name
```

becomes:

```python
student1.name
```

---

# What is a Decorator?

A decorator is a special tool in Python that modifies the behavior of a function or method.

Decorators start with:

```python
@
```

symbol.

Examples:

```python
@classmethod
@staticmethod
@property
```

---

# Why Use Decorators?

Decorators allow us to:

* Add extra functionality
* Modify behavior
* Reuse code
* Make code cleaner

---

# Example of a Simple Decorator

```python
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
```

---

# Output

```python
Before Function
Hello
After Function
```

---

# How Decorators Work

This:

```python
@decorator_function
def say_hello():
    print("Hello")
```

is equivalent to:

```python
def say_hello():
    print("Hello")

say_hello = decorator_function(say_hello)
```

---

# What is a Class Method?

A class method works with the class itself instead of individual objects.

Class methods use:

```python
cls
```

as the first parameter.

---

# Syntax

```python
class MyClass:

    @classmethod
    def method_name(cls):
        pass
```

---

# Understanding cls

The keyword:

```python
cls
```

represents the class itself.

Example:

```python
class Student:
    pass
```

Inside a class method:

```python
cls
```

refers to:

```python
Student
```

---

# Example of Class Method

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
```

---

# Output

```python
ABC School
```

---

# What Happened?

```python
cls.school
```

becomes:

```python
Student.school
```

---

# Calling Class Method Through Object

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

student1 = Student()

student1.show_school()
```

---

# Output

```python
ABC School
```

Even though we used an object, Python still passes the class.

---

# Modifying Class Variables

Class methods are often used to modify class variables.

---

# Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")

print(Student.school)
```

---

# Output

```python
XYZ School
```

---

# Real-World Example

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

Employee.change_company("Microsoft")

print(Employee.company)
```

---

# Output

```python
Microsoft
```

---

# Class Method vs Instance Method

| Feature                   | Instance Method | Class Method |
| ------------------------- | --------------- | ------------ |
| First Parameter           | self            | cls          |
| Access Instance Variables | Yes             | No           |
| Access Class Variables    | Yes             | Yes          |
| Access Object Data        | Yes             | No           |
| Access Class Data         | Yes             | Yes          |

---

# What is a Static Method?

A static method belongs to the class but does not use:

```python
self
```

or

```python
cls
```

It acts like a normal function placed inside a class.

---

# Syntax

```python
class MyClass:

    @staticmethod
    def method_name():
        pass
```

---

# Example

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))
```

---

# Output

```python
30
```

---

# Why Use Static Methods?

Use static methods when:

* Logic does not need object data
* Logic does not need class data
* Function belongs logically to the class

---

# Real-World Example

```python
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(25))
```

---

# Output

```python
77.0
```

---

# Comparing All Three Methods

```python
class Student:

    school = "ABC School"

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")
```

---

# Calling Methods

```python
student = Student()

student.instance_method()

Student.class_method()

Student.static_method()
```

---

# Output

```python
Instance Method
Class Method
Static Method
```

---

# Difference Between self and cls

| self                     | cls                    |
| ------------------------ | ---------------------- |
| Refers to Object         | Refers to Class        |
| Used in Instance Methods | Used in Class Methods  |
| Access Object Variables  | Access Class Variables |
| Unique for Every Object  | Same for Entire Class  |

---

# Example

```python
class Student:

    school = "ABC School"

    def instance(self):
        print(self.school)

    @classmethod
    def class_method(cls):
        print(cls.school)
```

Both can access class variables.

However:

```python
self
```

refers to an object.

```python
cls
```

refers to the class.

---

# Factory Methods Using Class Methods

A factory method creates objects.

Class methods are commonly used for this purpose.

---

# Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_student(cls):

        return cls("Mahi")

student = Student.create_student()

print(student.name)
```

---

# Output

```python
Mahi
```

---

# Built-in Decorators

Python provides several decorators.

---

# @classmethod

Used for class methods.

```python
@classmethod
```

---

# @staticmethod

Used for static methods.

```python
@staticmethod
```

---

# @property

Converts a method into an attribute.

---

# Example

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def percentage(self):
        return self.marks / 5

student = Student(400)

print(student.percentage)
```

---

# Output

```python
80.0
```

Notice:

```python
student.percentage
```

No parentheses are used.

---

# Common Beginner Mistakes

---

## Forgetting self

Wrong:

```python
class Student:

    def show():
        print("Hello")
```

Correct:

```python
class Student:

    def show(self):
        print("Hello")
```

---

## Forgetting cls in Class Method

Wrong:

```python
@classmethod
def show():
    pass
```

Correct:

```python
@classmethod
def show(cls):
    pass
```

---

## Using self in Static Method

Wrong:

```python
@staticmethod
def show(self):
    pass
```

Correct:

```python
@staticmethod
def show():
    pass
```

---

# Summary

* Methods are functions inside classes.
* Python provides Instance Methods, Class Methods, and Static Methods.
* Instance methods use `self`.
* Class methods use `cls`.
* Static methods use neither `self` nor `cls`.
* Decorators start with `@`.
* `@classmethod` creates a class method.
* `@staticmethod` creates a static method.
* `@property` converts a method into an attribute.
* Class methods are commonly used for class-level operations and factory methods.
* Static methods are utility functions related to the class.
* Decorators help modify and extend function behavior without changing original code.
