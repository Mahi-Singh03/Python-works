# Inheritance in Python

---

# What is Inheritance?

Inheritance is one of the most important concepts in Object-Oriented Programming (OOP).

Inheritance allows one class to acquire the properties (attributes) and behaviors (methods) of another class.

The class that gives properties is called the **Parent Class** (Base Class or Super Class).

The class that receives properties is called the **Child Class** (Derived Class or Sub Class).

---

# Why Use Inheritance?

Inheritance provides:

* Code Reusability
* Less Code Duplication
* Better Code Organization
* Easier Maintenance
* Faster Development

Instead of writing the same code again and again, we can inherit it from an existing class.

---

# Basic Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

The child class automatically gets access to all public attributes and methods of the parent class.

---

# Simple Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.sound()
dog.bark()
```

## Output

```python
Animal makes a sound
Dog barks
```

---

# How Does This Work?

Step 1:

```python
class Animal:
```

Creates the parent class.

---

Step 2:

```python
class Dog(Animal):
```

Dog inherits Animal.

---

Step 3:

```python
dog = Dog()
```

Creates a Dog object.

---

Step 4:

```python
dog.sound()
```

Python searches for `sound()` inside Dog.

Not found.

Then Python checks Animal.

Method found.

Method executes successfully.

---

# Types of Inheritance

Python supports four major types of inheritance.

| Type                     | Description                      |
| ------------------------ | -------------------------------- |
| Single Inheritance       | One parent and one child         |
| Multiple Inheritance     | Multiple parents and one child   |
| Multilevel Inheritance   | Chain of inheritance             |
| Hierarchical Inheritance | One parent and multiple children |

---

# 1. Single Inheritance

Single inheritance occurs when one child class inherits from one parent class.

---

## Structure

```text
Parent
   |
 Child
```

---

## Example

```python
class Animal:

    def eat(self):
        print("Animal can eat")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.eat()
dog.bark()
```

---

## Output

```python
Animal can eat
Dog barks
```

---

## Explanation

The Dog class inherits from Animal.

Therefore Dog can use:

```python
eat()
```

even though it is not written inside Dog.

---

## Real-Life Example

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Car is Driving")

car = Car()

car.start()
car.drive()
```

---

# 2. Multiple Inheritance

Multiple inheritance occurs when one child class inherits from more than one parent class.

---

## Structure

```text
Parent1      Parent2
     \       /
      \     /
       Child
```

---

## Example

```python
class Father:

    def driving(self):
        print("Father can drive")

class Mother:

    def cooking(self):
        print("Mother can cook")

class Child(Father, Mother):
    pass

child = Child()

child.driving()
child.cooking()
```

---

## Output

```python
Father can drive
Mother can cook
```

---

## Explanation

The Child class inherits:

* driving() from Father
* cooking() from Mother

Therefore Child can use both methods.

---

## Real-Life Example

```python
class Camera:

    def click_photo(self):
        print("Photo Captured")

class Phone:

    def call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    pass

phone = SmartPhone()

phone.click_photo()
phone.call()
```

---

# Method Resolution Order (MRO)

In multiple inheritance, what happens if multiple parent classes contain the same method?

Python follows MRO (Method Resolution Order).

Python checks parent classes from left to right.

---

## Example

```python
class A:

    def show(self):
        print("Class A")

class B:

    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()

obj.show()
```

---

## Output

```python
Class A
```

---

Because Python checks:

```python
A first
then B
```

---

## Checking MRO

```python
print(C.mro())
```

Output:

```python
[C, A, B, object]
```

---

# 3. Multilevel Inheritance

Multilevel inheritance occurs when inheritance happens in a chain.

A child class becomes a parent for another class.

---

## Structure

```text
GrandParent
      |
    Parent
      |
     Child
```

---

## Example

```python
class Animal:

    def eat(self):
        print("Animal Eats")

class Dog(Animal):

    def bark(self):
        print("Dog Barks")

class Puppy(Dog):

    def weep(self):
        print("Puppy Weeps")

p = Puppy()

p.eat()
p.bark()
p.weep()
```

---

## Output

```python
Animal Eats
Dog Barks
Puppy Weeps
```

---

## Explanation

Puppy inherits:

* weep() from Puppy
* bark() from Dog
* eat() from Animal

---

## Real-Life Example

```python
class LivingThing:

    def breathe(self):
        print("Breathing")

class Animal(LivingThing):

    def move(self):
        print("Moving")

class Dog(Animal):

    def bark(self):
        print("Barking")

dog = Dog()

dog.breathe()
dog.move()
dog.bark()
```

---

# 4. Hierarchical Inheritance

Hierarchical inheritance occurs when multiple child classes inherit from one parent class.

---

## Structure

```text
         Parent
        /      \
       /        \
   Child1     Child2
```

---

## Example

```python
class Animal:

    def eat(self):
        print("Animal Eats")

class Dog(Animal):

    def bark(self):
        print("Dog Barks")

class Cat(Animal):

    def meow(self):
        print("Cat Meows")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
```

---

## Output

```python
Animal Eats
Dog Barks
Animal Eats
Cat Meows
```

---

## Explanation

Both Dog and Cat inherit Animal.

Therefore both classes can use:

```python
eat()
```

without rewriting the code.

---

# Method Lookup Process

Whenever Python executes:

```python
obj.method()
```

Python searches in the following order:

```text
Current Class
      ↓
Parent Class
      ↓
Grandparent Class
      ↓
object Class
```

---

## Example

```python
class A:

    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

obj = C()

obj.show()
```

---

## Search Path

```text
C
↓
B
↓
A
↓
object
```

Method found in A.

---

# The super() Function

The super() function allows a child class to access methods from its parent class.

---

## Example

```python
class Animal:

    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")

dog = Dog()
```

---

## Output

```python
Animal Constructor
Dog Constructor
```

---

## Why Use super()?

Without super():

```python
Parent constructor will not run automatically.
```

With super():

```python
Parent constructor runs first.
```

---

# Method Overriding

Method overriding occurs when a child class defines a method that already exists in the parent class.

The child's version replaces the parent's version.

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

---

# Advantages of Inheritance

| Advantage          | Explanation                               |
| ------------------ | ----------------------------------------- |
| Reusability        | Reuse existing code                       |
| Less Duplication   | Avoid writing the same code               |
| Easier Maintenance | Changes made once affect multiple classes |
| Better Structure   | Organizes code logically                  |
| Faster Development | Less code to write                        |

---

# Common Beginner Mistakes

## Forgetting Parent Name

Wrong:

```python
class Dog:
```

Correct:

```python
class Dog(Animal):
```

---

## Wrong Indentation

Python uses indentation to define code blocks.

Always use proper indentation.

---

## Forgetting Parent Constructor

Wrong:

```python
class Dog(Animal):

    def __init__(self):
        print("Dog")
```

Correct:

```python
class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog")
```

---

# Summary

* Inheritance allows one class to acquire properties of another class.
* Parent class is also called Base Class or Super Class.
* Child class is also called Derived Class or Sub Class.
* Python supports Single, Multiple, Multilevel, and Hierarchical inheritance.
* Child classes can reuse parent methods and attributes.
* `super()` is used to access parent class methods.
* MRO decides the search order in multiple inheritance.
* Method overriding allows a child class to replace a parent method.
* Every Python class ultimately inherits from `object`.

Inheritance is one of the foundations of Object-Oriented Programming and is heavily used in real-world applications, frameworks, libraries, GUI development, web development, and large software systems.
