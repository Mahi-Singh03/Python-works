# ABSTRACTION IN PYTHON

---

# What is Abstraction?

Abstraction is one of the four main principles of Object-Oriented Programming (OOP).

It is the process of **hiding the internal implementation** and showing **only the essential features** to the user.

The user knows **what an object does**, but does not need to know **how it does it**.

---

# Real-World Example

Think about a **Car**.

When you drive a car, you use:

- Steering Wheel
- Accelerator
- Brake

You don't need to know:

- How the engine works
- How fuel is burned
- How the transmission changes gears

The complicated implementation is hidden.

This is called **Abstraction**.

---

# Another Real-World Example

Think about an **ATM Machine**.

You can:

- Withdraw Money
- Deposit Money
- Check Balance

You never see how:

- The bank verifies your PIN
- The balance is calculated
- The money is transferred

The implementation is hidden from the user.

---

# Why Use Abstraction?

Abstraction helps:

| Benefit | Explanation |
|----------|-------------|
| Simplicity | Hides unnecessary details |
| Security | Prevents direct access to implementation |
| Easy Maintenance | Internal code can change without affecting users |
| Better Design | Separates interface from implementation |
| Reusability | Different classes can follow the same interface |

---

# How is Abstraction Implemented in Python?

Python provides the **abc** module.

ABC stands for:

**Abstract Base Class**

An abstract class contains one or more **abstract methods**.

---

# Importing the abc Module

```python
from abc import ABC, abstractmethod
```

---

# Understanding the Syntax

| Part | Meaning |
|------|---------|
| abc | Python module for abstract classes |
| ABC | Base class for creating abstract classes |
| @abstractmethod | Declares an abstract method |

---

# What is an Abstract Class?

An abstract class is a class that **cannot be instantiated**.

Its purpose is to act as a blueprint for other classes.

---

# Syntax

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# Understanding the Syntax

| Part | Meaning |
|------|---------|
| Animal | Abstract class |
| ABC | Makes Animal an abstract class |
| @abstractmethod | Declares an abstract method |
| pass | Placeholder for future implementation |

---

# What is an Abstract Method?

An abstract method is a method that **has no implementation**.

It only defines **what must be implemented** by child classes.

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Here,

The `sound()` method has no body.

Every child class must implement it.

---

# Can We Create an Object of an Abstract Class?

No.

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

animal = Animal()
```

## Output

```python
TypeError:
Can't instantiate abstract class Animal
```

---

# Creating a Child Class

A child class must implement every abstract method.

---

# Example

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

## Output

```python
Bark
```

---

# Another Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):

    def sound(self):
        print("Meow")

cat = Cat()

cat.sound()
```

## Output

```python
Meow
```

---

# Multiple Child Classes

One abstract class can have many child classes.

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meow")

class Cow(Animal):

    def sound(self):
        print("Moo")

Dog().sound()
Cat().sound()
Cow().sound()
```

## Output

```python
Bark
Meow
Moo
```

---

# What Happens if a Child Class Doesn't Implement the Abstract Method?

Python will not allow its object to be created.

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    pass

dog = Dog()
```

## Output

```python
TypeError:
Can't instantiate abstract class Dog
with abstract method sound
```

---

# Abstract Class Can Have Normal Methods

An abstract class can contain both:

- Abstract methods
- Normal methods

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    def sleep(self):
        print("Sleeping...")

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sleep()
dog.sound()
```

## Output

```python
Sleeping...
Bark
```

---

# Abstract Class Can Have Constructors

Abstract classes can also contain constructors.

---

# Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print(self.name, "says Bark")

dog = Dog("Rocky")

dog.sound()
```

## Output

```python
Rocky says Bark
```

---

# Real-World Example

Suppose every payment method must have a `pay()` method.

---

# Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Cash(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Cash")

payment1 = CreditCard()
payment2 = UPI()
payment3 = Cash()

payment1.pay(1000)
payment2.pay(500)
payment3.pay(200)
```

## Output

```python
Paid 1000 using Credit Card
Paid 500 using UPI
Paid 200 using Cash
```

---

# Another Example

Every shape should know how to calculate its area.

---

# Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(10, 5)
circle = Circle(4)

print(rectangle.area())
print(circle.area())
```

## Output

```python
50
50.24
```

---

# Difference Between Encapsulation and Abstraction

| Encapsulation | Abstraction |
|---------------|-------------|
| Hides data | Hides implementation |
| Protects variables | Simplifies usage |
| Uses private and protected members | Uses abstract classes and abstract methods |
| Focuses on data security | Focuses on essential functionality |

---

# Abstract Class vs Normal Class

| Abstract Class | Normal Class |
|----------------|--------------|
| Cannot create objects directly | Can create objects |
| May contain abstract methods | No abstract methods |
| Used as a blueprint | Used to create objects |
| Requires inheritance | Inheritance is optional |

---

# Abstract Method vs Normal Method

| Abstract Method | Normal Method |
|-----------------|---------------|
| Has no implementation | Has implementation |
| Uses `@abstractmethod` | No decorator required |
| Must be overridden | Overriding is optional |
| Exists only in abstract classes | Can exist in any class |

---

# Complete Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def fuel_type(self):
        print("Uses Fuel or Electricity")

class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")

car = Car()
bike = Bike()

car.start()
car.stop()
car.fuel_type()

bike.start()
bike.stop()
bike.fuel_type()
```

## Output

```python
Car Started
Car Stopped
Uses Fuel or Electricity

Bike Started
Bike Stopped
Uses Fuel or Electricity
```

---

# Key Points

- Abstraction hides implementation details.
- It shows only the necessary functionality.
- Python implements abstraction using the `abc` module.
- `ABC` is used to create an abstract class.
- `@abstractmethod` declares an abstract method.
- Abstract classes cannot be instantiated.
- Child classes must implement every abstract method.
- Abstract classes can contain constructors and normal methods.

---

# Summary

- Abstraction focuses on **what an object does**, not **how it does it**.
- It simplifies complex systems by hiding unnecessary details.
- Abstract classes act as blueprints for other classes.
- Abstract methods force child classes to provide their own implementation.
- Abstraction improves code organization, flexibility, and maintainability.

---