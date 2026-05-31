# Encapsulation, Polymorphism, and Abstraction in Python

---

# Introduction

Object-Oriented Programming (OOP) is built around four major concepts:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

In this file, we will focus on:

* Encapsulation
* Polymorphism
* Abstraction

These concepts help make code:

* More secure
* Easier to maintain
* More reusable
* Better organized

---

# 1. Encapsulation

---

# What is Encapsulation?

Encapsulation means:

**Bundling data (variables) and methods (functions) together inside a class while restricting direct access to some data.**

In simple words:

> Encapsulation is the process of hiding internal details and protecting data from unwanted access.

---

# Real-Life Example

Think about an ATM.

You can:

* Check balance
* Withdraw money
* Deposit money

But you cannot directly access the bank's internal database.

The internal implementation is hidden.

This is encapsulation.

---

# Why Use Encapsulation?

Encapsulation helps:

* Protect data
* Prevent accidental modification
* Improve security
* Control how data is accessed

---

# Access Modifiers in Python

Python provides three levels of access.

| Type      | Syntax     | Access                  |
| --------- | ---------- | ----------------------- |
| Public    | variable   | Anywhere                |
| Protected | _variable  | Class and Child Classes |
| Private   | __variable | Inside Class Only       |

---

# Public Variables

Public variables can be accessed from anywhere.

---

## Example

```python
class Student:

    def __init__(self):
        self.name = "Mahi"

student = Student()

print(student.name)
```

---

## Output

```python
Mahi
```

---

# Protected Variables

Protected variables start with a single underscore.

```python
_variable
```

They should only be used inside the class and child classes.

---

## Example

```python
class Student:

    def __init__(self):
        self._name = "Mahi"

student = Student()

print(student._name)
```

---

## Output

```python
Mahi
```

Python still allows access, but the underscore acts as a warning.

---

# Private Variables

Private variables start with double underscores.

```python
__variable
```

These cannot be accessed directly outside the class.

---

## Example

```python
class Bank:

    def __init__(self):
        self.__balance = 5000

bank = Bank()

print(bank.__balance)
```

---

## Output

```python
AttributeError
```

---

# Why Does This Happen?

Python performs name mangling.

```python
__balance
```

becomes:

```python
_Bank__balance
```

internally.

---

# Accessing Private Variables Properly

Use methods.

---

## Example

```python
class Bank:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)

bank = Bank()

bank.show_balance()
```

---

## Output

```python
5000
```

---

# Modifying Private Variables

---

## Example

```python
class Bank:

    def __init__(self):
        self.__balance = 5000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

bank = Bank()

bank.deposit(1000)

bank.show_balance()
```

---

## Output

```python
6000
```

---

# Real-World Encapsulation Example

```python
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

employee = Employee(50000)

print(employee.get_salary())
```

---

## Output

```python
50000
```

---

# Advantages of Encapsulation

* Data Security
* Better Control
* Easy Maintenance
* Cleaner Code
* Reduced Bugs

---

# 2. Polymorphism

---

# What is Polymorphism?

The word polymorphism means:

```text
Poly = Many
Morph = Forms
```

Meaning:

> One interface, many forms.

The same method name can behave differently for different objects.

---

# Real-Life Example

The word:

```text
Run
```

can mean:

* A person runs
* A car runs
* A machine runs

Same word.

Different behavior.

This is polymorphism.

---

# Polymorphism Using Different Classes

---

## Example

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

class Cow:

    def sound(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
```

---

## Output

```python
Bark
Meow
Moo
```

---

# How Does It Work?

Each object has its own version of:

```python
sound()
```

Python automatically calls the correct method.

---

# Polymorphism Through Inheritance

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

---

## Output

```python
Bark
Meow
```

---

# Method Overriding

When a child class replaces a parent method.

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()
```

---

## Output

```python
Bark
```

The child version overrides the parent version.

---

# Built-In Polymorphism

Python functions often work with multiple data types.

---

## Example

```python
print(len("Python"))

print(len([1, 2, 3]))

print(len((1, 2, 3, 4)))
```

---

## Output

```python
6
3
4
```

The same function:

```python
len()
```

works differently depending on the object.

---

# Advantages of Polymorphism

* Flexible code
* Reusable code
* Easier maintenance
* Cleaner design

---

# 3. Abstraction

---

# What is Abstraction?

Abstraction means:

> Showing only important information while hiding implementation details.

The user sees what an object does.

The user does not need to know how it does it.

---

# Real-Life Example

When driving a car:

You use:

* Steering Wheel
* Brake
* Accelerator

You do not need to know:

* Engine internals
* Fuel injection system
* Transmission details

Complexity is hidden.

This is abstraction.

---

# Why Use Abstraction?

Abstraction helps:

* Hide complexity
* Improve security
* Simplify usage
* Reduce confusion

---

# Abstraction Using Abstract Classes

Python provides the:

```python
abc
```

module.

ABC means:

```text
Abstract Base Class
```

---

# Creating an Abstract Class

---

## Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# What is Happening?

The method:

```python
sound()
```

must be implemented by child classes.

---

# Child Class Implementation

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()
```

---

## Output

```python
Bark
```

---

# What If We Don't Implement It?

```python
class Dog(Animal):
    pass

dog = Dog()
```

---

## Output

```python
TypeError
```

Python forces the child class to implement all abstract methods.

---

# Multiple Abstract Methods

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

---

## Child Class

```python
class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")
```

---

# Real-World Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

payments = [CreditCard(), UPI()]

for payment in payments:
    payment.pay(1000)
```

---

## Output

```python
Paid ₹1000 using Credit Card
Paid ₹1000 using UPI
```

---

# Advantages of Abstraction

* Hides complexity
* Improves security
* Cleaner architecture
* Easier maintenance
* Better scalability

---

# Encapsulation vs Abstraction

| Feature        | Encapsulation     | Abstraction      |
| -------------- | ----------------- | ---------------- |
| Purpose        | Hide Data         | Hide Complexity  |
| Focus          | Security          | Simplicity       |
| Achieved Using | Private Variables | Abstract Classes |
| User Concern   | Access Control    | Interface Design |

---

# Encapsulation vs Polymorphism

| Encapsulation          | Polymorphism           |
| ---------------------- | ---------------------- |
| Protects Data          | Changes Behavior       |
| Focuses on Security    | Focuses on Flexibility |
| Uses Private Variables | Uses Method Overriding |

---

# Abstraction vs Polymorphism

| Abstraction               | Polymorphism           |
| ------------------------- | ---------------------- |
| Defines What Must Be Done | Defines How It Is Done |
| Uses Abstract Classes     | Uses Method Overriding |
| Hides Complexity          | Provides Flexibility   |

---

# Complete OOP Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meow")

animals = [Dog("Tommy"), Cat("Kitty")]

for animal in animals:
    print(animal.get_name())
    animal.sound()
```

---

## Output

```python
Tommy
Bark

Kitty
Meow
```

---

# What Concepts Were Used?

Encapsulation:

```python
self.__name
```

Polymorphism:

```python
animal.sound()
```

Different behavior for different objects.

Abstraction:

```python
@abstractmethod
def sound()
```

forces child classes to implement the method.

---

# Summary

## Encapsulation

* Hides data
* Uses private variables
* Improves security

## Polymorphism

* One method, many forms
* Same interface, different behavior
* Achieved through method overriding

## Abstraction

* Hides implementation details
* Shows only essential features
* Uses abstract classes and abstract methods

Together, Encapsulation, Polymorphism, Inheritance, and Abstraction form the foundation of Object-Oriented Programming in Python.
