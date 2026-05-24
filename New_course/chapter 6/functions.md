# Functions in Python

---

# What is a Function?

A function is a block of reusable code that performs a specific task.

Functions help:
- Reduce code repetition
- Improve readability
- Organize programs better
- Make debugging easier

---

# Types of Functions

Python provides two main types:

1. Built-in Functions
2. User-defined Functions

---

# Built-in Functions

These are functions already provided by Python.

Examples:

```python
print()
len()
type()
input()
range()
sum()
```

---

# User-defined Functions

Functions created by the programmer.

---

# Creating a Function

The `def` keyword is used to define a function.

## Syntax

```python
def function_name():
    # code
```

---

# Simple Function Example

```python
def greet():
    print("Hello World")
```

---

# Calling a Function

A function runs only when it is called.

```python
greet()
```

## Output

```python
Hello World
```

---

# Function with Parameters

Parameters are values passed into a function.

```python
def greet(name):
    print("Hello", name)
```

---

# Calling Function with Argument

```python
greet("Mahi")
```

## Output

```python
Hello Mahi
```

---

# Multiple Parameters

```python
def add(a, b):
    print(a + b)
```

```python
add(10, 20)
```

## Output

```python
30
```

---

# return Statement

The `return` statement sends a value back from the function.

```python
def square(num):
    return num * num
```

```python
result = square(5)

print(result)
```

## Output

```python
25
```

---

# Difference Between print() and return

| print() | return |
|---|---|
| Displays output | Sends value back |
| Cannot store result easily | Can store result |
| Used for displaying | Used for calculations |

---

# Default Parameters

Default values are used if no argument is provided.

```python
def greet(name="Guest"):
    print("Hello", name)
```

```python
greet()
greet("Mahi")
```

## Output

```python
Hello Guest
Hello Mahi
```

---

# Keyword Arguments

Arguments passed using parameter names.

```python
def student(name, age):
    print(name, age)
```

```python
student(age=25, name="Mahi")
```

---

# Arbitrary Arguments (*args)

Used when number of arguments is unknown.

```python
def numbers(*args):
    print(args)
```

```python
numbers(1, 2, 3, 4)
```

## Output

```python
(1, 2, 3, 4)
```

---

# Arbitrary Keyword Arguments (**kwargs)

Accepts multiple keyword arguments.

```python
def information(**kwargs):
    print(kwargs)
```

```python
information(name="Mahi", age=25)
```

## Output

```python
{'name': 'Mahi', 'age': 25}
```

---

# Local Variables

Variables created inside functions.

```python
def demo():
    x = 10
    print(x)
```

---

# Global Variables

Variables created outside functions.

```python
x = 100

def demo():
    print(x)
```

---

# Lambda Functions

Small anonymous functions.

## Syntax

```python
lambda arguments : expression
```

---

# Example of Lambda Function

```python
square = lambda x: x * x

print(square(5))
```

## Output

```python
25
```

---

# Recursive Functions

A function calling itself.

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)
```

```python
print(factorial(5))
```

## Output

```python
120
```

---

# Function Scope

Scope means where variables can be accessed.

- Local Scope
- Global Scope

---

# Docstrings

Used to describe functions.

```python
def greet():
    """This function prints greeting"""

    print("Hello")
```

---

# Built-in Helpful Functions

| Function | Description |
|---|---|
| `len()` | Returns length |
| `sum()` | Adds values |
| `max()` | Largest value |
| `min()` | Smallest value |
| `type()` | Returns data type |

---

# Example Program

```python
def even_or_odd(num):

    if num % 2 == 0:
        return "Even"

    return "Odd"

print(even_or_odd(10))
```

---

# Summary

- Functions reduce repetition
- `def` creates functions
- Parameters accept input
- `return` sends output back
- `*args` accepts multiple values
- `**kwargs` accepts multiple keyword arguments
- Lambda functions are short functions
- Recursive functions call themselves