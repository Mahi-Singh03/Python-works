# POLYMORPHISM IN PYTHON

---

# What is Polymorphism?

Polymorphism is one of the four main principles of Object-Oriented Programming (OOP).

The word **Polymorphism** comes from two Greek words:

- **Poly** = Many
- **Morph** = Forms

So, **Polymorphism means "Many Forms."**

It allows the **same method, function, or operator** to perform different tasks depending on the object it is working with.

---

# Real-World Example

Think about a **Person**.

A person can perform the action **"Speak."**

But the way they speak depends on the language they know.

For example:

- English Speaker → "Hello"
- Hindi Speaker → "Namaste"
- Punjabi Speaker → "Sat Sri Akal"

The action is the same (**Speak**), but the behavior is different.

This is **Polymorphism**.

---

# Another Real-World Example

Think about a **Remote Control**.

The same **Power Button** works for:

- TV
- AC
- Speaker

The button is the same, but the action depends on the device.

---

# Why Use Polymorphism?

Polymorphism helps:

| Benefit | Explanation |
|----------|-------------|
| Code Reusability | One interface can work with many objects |
| Flexibility | Different objects can behave differently |
| Cleaner Code | Reduces duplicate code |
| Easy Maintenance | New classes can be added easily |
| Extensibility | Makes programs scalable |

---

# Types of Polymorphism in Python

| Type | Description |
|------|-------------|
| Duck Typing | Different objects respond to the same method |
| Method Overriding | Child class changes parent method |
| Operator Overloading | Operators behave differently for different objects |
| Built-in Function Polymorphism | Same function works with different data types |

---

# Built-in Polymorphism

Many Python functions work with different data types.

---

# Example

```python
print(len("Python"))

print(len([1, 2, 3, 4]))

print(len((10, 20, 30)))
```

## Output

```python
6
4
3
```

The same `len()` function works with:

- String
- List
- Tuple

---

# Another Example

```python
print(max(5, 10, 15))

print(max([3, 8, 2]))

print(max("Python"))
```

## Output

```python
15
8
y
```

The same `max()` function behaves differently depending on the object.

---

# Method Overriding

Method overriding happens when a child class provides its own implementation of a method already defined in the parent class.

---

# Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()

dog.sound()
```

## Output

```python
Dog barks
```

The child's `sound()` method overrides the parent's method.

---

# Another Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")

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

# Parent Method Can Still Be Used

The parent method can be called using `super()`.

---

# Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()

dog.sound()
```

## Output

```python
Animal makes a sound
Dog barks
```

---

# Duck Typing

Python follows the principle:

> "If it walks like a duck and quacks like a duck, then it is a duck."

In Python, the type of the object is less important than the methods it has.

---

# Example

```python
class Dog:

    def speak(self):
        print("Bark")

class Cat:

    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
```

## Output

```python
Bark
Meow
```

The function works with both objects because both have a `speak()` method.

---

# Another Duck Typing Example

```python
class Car:

    def move(self):
        print("Car is moving")

class Bird:

    def move(self):
        print("Bird is flying")

def start(obj):
    obj.move()

start(Car())
start(Bird())
```

## Output

```python
Car is moving
Bird is flying
```

---

# Operator Overloading

Python operators also show polymorphic behavior.

The same operator performs different operations depending on the operands.

---

# Example

```python
print(10 + 20)

print("Hello " + "World")

print([1, 2] + [3, 4])
```

## Output

```python
30
Hello World
[1, 2, 3, 4]
```

The `+` operator:

- Adds numbers
- Joins strings
- Combines lists

---

# More Operator Examples

```python
print(5 * 3)

print("Hi " * 3)

print([1] * 4)
```

## Output

```python
15
Hi Hi Hi
[1, 1, 1, 1]
```

---

# Polymorphism with Inheritance

Different child classes can provide different implementations of the same method.

---

# Example

```python
class Animal:

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

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
```

## Output

```python
Bark
Meow
Moo
```

---

# Real-World Example

Different payment methods perform the same action.

---

# Example

```python
class CreditCard:

    def pay(self):
        print("Paid using Credit Card")

class UPI:

    def pay(self):
        print("Paid using UPI")

class Cash:

    def pay(self):
        print("Paid using Cash")

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()
```

## Output

```python
Paid using Credit Card
Paid using UPI
Paid using Cash
```

---

# Another Example

Different vehicles start differently.

---

# Example

```python
class Car:

    def start(self):
        print("Car Started")

class Bike:

    def start(self):
        print("Bike Started")

class Bus:

    def start(self):
        print("Bus Started")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
```

## Output

```python
Car Started
Bike Started
Bus Started
```

---

# Method Overloading in Python

Unlike some programming languages, Python **does not support true method overloading**.

If two methods have the same name, the last one replaces the previous one.

---

# Example

```python
class Student:

    def show(self):
        print("First Method")

    def show(self):
        print("Second Method")

student = Student()

student.show()
```

## Output

```python
Second Method
```

Only the second method exists.

---

# Achieving Overloading Using Default Arguments

Although Python doesn't support method overloading directly, we can use default arguments.

---

# Example

```python
class Student:

    def show(self, name=None):

        if name:
            print("Student:", name)
        else:
            print("No Name")

student = Student()

student.show()

student.show("Mahi")
```

## Output

```python
No Name
Student: Mahi
```

---

# Complete Example

```python
class Shape:

    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)

rectangle = Rectangle(10, 5)
circle = Circle(4)

rectangle.area()
circle.area()
```

## Output

```python
Area = 50
Area = 50.24
```

---

# Polymorphism vs Inheritance

| Polymorphism | Inheritance |
|--------------|-------------|
| One interface, many behaviors | One class acquires another class's properties |
| Focuses on behavior | Focuses on code reuse |
| Achieved using overriding | Achieved using parent-child relationship |

---

# Polymorphism vs Abstraction

| Polymorphism | Abstraction |
|--------------|-------------|
| One method behaves differently | Hides implementation details |
| Focuses on different behaviors | Focuses on essential features |
| Uses overriding and duck typing | Uses abstract classes |

---

# Method Overriding vs Method Overloading

| Method Overriding | Method Overloading |
|-------------------|-------------------|
| Child class changes parent method | Same method name with different parameters |
| Supported in Python | Not directly supported |
| Uses inheritance | Simulated using default arguments |

---

# Key Points

- Polymorphism means **Many Forms**.
- The same method can behave differently for different objects.
- Python supports polymorphism through method overriding.
- Python also supports duck typing.
- Operators like `+` and `*` are polymorphic.
- Built-in functions such as `len()` and `max()` are polymorphic.
- Python does not support true method overloading.

---

# Summary

- Polymorphism allows one interface to work with many different objects.
- Different classes can implement the same method in their own way.
- Method overriding is the most common form of polymorphism.
- Duck typing allows objects with the same methods to be used interchangeably.
- Operator overloading lets operators perform different operations depending on the data type.
- Polymorphism makes programs flexible, reusable, and easier to maintain.

---