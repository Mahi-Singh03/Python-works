# CLASS IN PYTHON

---

# What is a Class in Python?

A **class** is a blueprint or template used to create objects.

It defines:

* Variables (called attributes or properties)
* Functions (called methods)

Classes help organize code and make programs reusable.

---

# Real-World Example of a Class

Think about a **Car**.

A car has:

* Color
* Brand
* Speed

And it can perform actions like:

* Start
* Stop
* Accelerate

In Python:

* The **class** is the blueprint of the car
* The **object** is the real car created from that blueprint

---

# What is an Object?

An object is an instance of a class.

Example:

```python
car1 = Car()
```

Here:

* `Car` → Class
* `car1` → Object

---

# Why Use Classes?

Classes are useful because they help:

| Benefit             | Explanation                               |
| ------------------- | ----------------------------------------- |
| Organize Code       | Keeps related data and functions together |
| Reusability         | Create many objects from one class        |
| Easy Maintenance    | Easier to update and manage               |
| Real-World Modeling | Represents real-life things               |

---

# Basic Syntax of a Class

```python
class ClassName:
    
    # constructor
    def __init__(self):
        pass
```

---

# Understanding the Syntax

| Part         | Meaning                        |
| ------------ | ------------------------------ |
| `class`      | Keyword used to create a class |
| `ClassName`  | Name of the class              |
| `__init__()` | Constructor method             |
| `self`       | Refers to the current object   |
| `pass`       | Empty placeholder              |

---

# Creating Your First Class

```python
class Student:
    pass
```

This creates an empty class.

---

# Creating an Object

```python
class Student:
    pass

student1 = Student()

print(student1)
```

## Output

```python
<__main__.Student object at 0x000001>
```

---

# The `__init__()` Constructor

The constructor automatically runs when an object is created.

It is used to initialize object data.

---

# Syntax of Constructor

```python
class Student:

    def __init__(self):
        print("Constructor called")
```

---

# Example

```python
class Student:

    def __init__(self):
        print("Student object created")

student1 = Student()
```

## Output

```python
Student object created
```

---

# What is `self`?

`self` refers to the current object.

It allows the object to access its own variables and methods.

---

# Example of `self`

```python
class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Mahi")

print(student1.name)
```

## Output

```python
Mahi
```

---

# Instance Variables

Variables created using `self` are called instance variables.

Each object gets its own copy.

---

# Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Mahi", 20)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)
```

## Output

```python
Mahi
Rahul
```

---

# Methods in a Class

Functions inside a class are called methods.

---

# Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Student name is:", self.name)

student1 = Student("Mahi")

student1.show_name()
```

## Output

```python
Student name is: Mahi
```

---

# Types of Methods

| Method Type     | Description                |
| --------------- | -------------------------- |
| Instance Method | Works with object data     |
| Class Method    | Works with class data      |
| Static Method   | Independent utility method |

---

# Instance Methods

These methods use `self`.

---

# Example

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

car1 = Car("Toyota")

car1.show_brand()
```

## Output

```python
Brand: Toyota
```

---

# Class Variables

Class variables are shared among all objects.

---

# Example

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Mahi")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)
```

## Output

```python
ABC School
ABC School
```

---

# Difference Between Class Variable and Instance Variable

| Feature        | Class Variable        | Instance Variable |
| -------------- | --------------------- | ----------------- |
| Shared         | Yes                   | No                |
| Created Using  | Directly inside class | Using self        |
| Changes Affect | All objects           | One object only   |

---

# Class Methods

Class methods use `cls` instead of `self`.

They work with class variables.

---

# Syntax

```python
@classmethod
def method_name(cls):
    pass
```

---

# Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
```

## Output

```python
ABC School
```

---

# Static Methods

Static methods do not use `self` or `cls`.

They are utility functions.

---

# Example

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))
```

## Output

```python
8
```

---

# Accessing Attributes

You can access object variables using dot notation.

---

# Example

```python
class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Mahi")

print(student1.name)
```

---

# Modifying Attributes

```python
student1.name = "Rahul"

print(student1.name)
```

## Output

```python
Rahul
```

---

# Deleting Attributes

```python
del student1.name
```

---

# Inheritance in Python

Inheritance allows one class to use properties and methods of another class.

---

# Syntax

```python
class Child(Parent):
    pass
```

---

# Example

```python
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog1 = Dog()

dog1.sound()
dog1.bark()
```

## Output

```python
Animal makes sound
Dog barks
```

---

# Types of Inheritance

| Type                     | Meaning                  |
| ------------------------ | ------------------------ |
| Single Inheritance       | One parent and one child |
| Multiple Inheritance     | Multiple parents         |
| Multilevel Inheritance   | Chain inheritance        |
| Hierarchical Inheritance | Multiple child classes   |

---

# Encapsulation

Encapsulation means hiding internal details.

Private variables are created using double underscores.

---

# Example

```python
class Bank:

    def __init__(self):
        self.__balance = 1000

bank1 = Bank()

# print(bank1.__balance)
```

This gives an error because the variable is private.

---

# Polymorphism

Polymorphism means one method behaves differently for different objects.

---

# Example

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

## Output

```python
Bark
Meow
```

---

# Special Methods (Magic Methods)

Python provides special methods with double underscores.

---

# Common Magic Methods

| Method     | Purpose               |
| ---------- | --------------------- |
| `__init__` | Constructor           |
| `__str__`  | String representation |
| `__len__`  | Length                |
| `__del__`  | Destructor            |

---

# Example of `__str__`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

student1 = Student("Mahi")

print(student1)
```

## Output

```python
Mahi
```

---

# Destructor in Python

Destructor runs when object is destroyed.

---

# Example

```python
class Test:

    def __del__(self):
        print("Object destroyed")

obj = Test()

del obj
```

---

# Practical Real-World Example

```python
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

mobile1 = Mobile("Samsung", 25000)

mobile1.show_details()
```

## Output

```python
Brand: Samsung
Price: 25000
```

---

# Advantages of OOP and Classes

| Advantage   | Explanation             |
| ----------- | ----------------------- |
| Reusability | Code can be reused      |
| Modularity  | Better organization     |
| Scalability | Easier to grow projects |
| Security    | Data hiding possible    |

---

# Important Notes

* Class names usually start with capital letters
* `self` must be the first parameter in instance methods
* Constructor is optional
* One class can create many objects
* Methods define object behavior
* Classes help write cleaner code

---

# Common Beginner Mistakes

| Mistake                                      | Solution                     |
| -------------------------------------------- | ---------------------------- |
| Forgetting `self`                            | Always include it in methods |
| Wrong indentation                            | Use proper indentation       |
| Using class variables incorrectly            | Understand shared variables  |
| Forgetting parentheses while creating object | Use `ClassName()`            |

---

# Summary

* A class is a blueprint for objects
* Objects are created from classes
* `__init__()` is the constructor
* `self` refers to the current object
* Methods are functions inside classes
* Classes support inheritance and polymorphism
* Encapsulation hides data
* OOP makes code reusable and organized
