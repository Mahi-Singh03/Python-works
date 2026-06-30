# ENCAPSULATION IN PYTHON

---

# What is Encapsulation?

Encapsulation is one of the four main principles of Object-Oriented Programming (OOP).

It is the process of **wrapping data (variables) and methods (functions) together inside a single class** while controlling how the data is accessed.

Encapsulation helps protect an object's data from being modified directly.

---

# Real-World Example

Think about an **ATM Machine**.

You can:

- Check balance
- Withdraw money
- Deposit money

But you **cannot directly change your account balance** from outside the ATM.

The ATM controls how your money is accessed.

Encapsulation works the same way in Python.

---

# Why Use Encapsulation?

Encapsulation helps:

| Benefit | Explanation |
|----------|-------------|
| Data Protection | Prevents direct modification of data |
| Better Security | Sensitive information remains hidden |
| Controlled Access | Data is accessed through methods |
| Easy Maintenance | Internal implementation can change without affecting users |
| Cleaner Code | Keeps related data and methods together |

---

# Basic Syntax

```python
class Student:

    def __init__(self):
        self.name = "Mahi"
```

---

# Understanding the Syntax

| Part | Meaning |
|------|---------|
| class | Creates a class |
| __init__() | Constructor |
| self | Refers to the current object |
| self.name | Instance variable |

---

# Public Members

By default, every variable and method in Python is **public**.

They can be accessed from anywhere.

---

# Example

```python
class Student:

    def __init__(self):
        self.name = "Mahi"

student1 = Student()

print(student1.name)
```

## Output

```python
Mahi
```

---

# Modifying a Public Variable

Public variables can be modified directly.

```python
class Student:

    def __init__(self):
        self.name = "Mahi"

student1 = Student()

student1.name = "Rahul"

print(student1.name)
```

## Output

```python
Rahul
```

---

# Protected Members

Protected members start with a **single underscore (_)**.

```python
_variable
```

A protected variable is **meant for internal use**, but Python does not strictly prevent access.

It is only a convention that programmers should not access it directly.

---

# Example

```python
class Student:

    def __init__(self):
        self._marks = 90

student1 = Student()

print(student1._marks)
```

## Output

```python
90
```

---

# Should We Access Protected Members?

Technically:

Yes.

Practically:

No.

Protected members should only be used inside the class or subclasses.

---

# Private Members

Private members begin with **double underscores (__)**.

```python
__variable
```

Python hides these variables using **Name Mangling**.

They cannot be accessed directly from outside the class.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

student1 = Student()

print(student1.__marks)
```

## Output

```python
AttributeError:
'Student' object has no attribute '__marks'
```

---

# Why Does This Error Occur?

Python changes

```python
__marks
```

into

```python
_Student__marks
```

This process is called **Name Mangling**.

---

# Accessing Private Variables (Not Recommended)

Although private variables are hidden, Python still stores them.

They can be accessed using name mangling.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

student1 = Student()

print(student1._Student__marks)
```

## Output

```python
90
```

---

# Why Use Private Variables?

Private variables protect important data from accidental modification.

Example:

- Password
- Bank Balance
- PIN
- Employee Salary

---

# Accessing Private Data Using Methods

Instead of accessing variables directly, we use methods.

---

# Getter Method

A getter returns the value of a private variable.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

student1 = Student()

print(student1.get_marks())
```

## Output

```python
90
```

---

# Setter Method

A setter updates the value of a private variable.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student1 = Student()

student1.set_marks(95)

print(student1.get_marks())
```

## Output

```python
95
```

---

# Why Use Getter and Setter?

Without setters:

Anyone can assign invalid data.

With setters:

You can validate the data before storing it.

---

# Example with Validation

```python
class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

student1 = Student()

student1.set_marks(95)

print(student1.get_marks())

student1.set_marks(150)
```

## Output

```python
95
Invalid Marks
```

---

# Encapsulation Using Properties

Python provides the **property()** function and decorators to make getters and setters easier.

---

# What is @property?

The `@property` decorator allows a method to behave like an attribute.

Instead of writing

```python
student.get_marks()
```

you can simply write

```python
student.marks
```

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

    @property
    def marks(self):
        return self.__marks

student1 = Student()

print(student1.marks)
```

## Output

```python
90
```

---

# Property Setter

The `@property` decorator can also create a setter.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")

student1 = Student()

student1.marks = 95

print(student1.marks)
```

## Output

```python
95
```

---

# Example with Invalid Data

```python
student1.marks = 150
```

## Output

```python
Invalid Marks
```

---

# Property Deleter

Python also allows deleting a property.

---

# Example

```python
class Student:

    def __init__(self):
        self.__marks = 90

    @property
    def marks(self):
        return self.__marks

    @marks.deleter
    def marks(self):
        del self.__marks

student1 = Student()

del student1.marks
```

---

# Complete Example

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")

    def show(self):
        print("Name :", self.name)
        print("Marks:", self.__marks)

student1 = Student("Mahi", 90)

student1.show()

student1.marks = 95

student1.show()
```

## Output

```python
Name : Mahi
Marks: 90

Name : Mahi
Marks: 95
```

---

# Public vs Protected vs Private

| Feature | Public | Protected | Private |
|----------|--------|-----------|----------|
| Symbol | variable | _variable | __variable |
| Accessible Outside Class | Yes | Yes (Not Recommended) | No |
| Accessible Inside Class | Yes | Yes | Yes |
| Accessible in Subclass | Yes | Yes | No (Directly) |
| Purpose | Normal Variables | Internal Use | Hide Sensitive Data |

---

# Getter vs Setter

| Getter | Setter |
|----------|---------|
| Reads data | Updates data |
| Returns value | Changes value |
| Doesn't modify data | Can validate data before storing |

---

# Encapsulation Summary

- Encapsulation combines data and methods inside a class.
- Public members can be accessed from anywhere.
- Protected members use a single underscore (_).
- Private members use double underscores (__).
- Python hides private members using Name Mangling.
- Getter methods return private data.
- Setter methods update private data safely.
- The `@property` decorator provides a cleaner way to use getters and setters.
- Encapsulation improves security, readability, and maintainability.

---

# Key Takeaways

- Encapsulation protects object data.
- Public variables are freely accessible.
- Protected variables follow a naming convention.
- Private variables are hidden using name mangling.
- Getters and setters provide controlled access.
- Properties (`@property`) make encapsulation more Pythonic.
- Encapsulation helps build secure and maintainable programs.

---