# Python Modules – Complete Guide

---

## What is a Module?

A module in Python is a file that contains code (functions, variables, classes) which can be reused in other Python programs.

Example:

* Built-in modules: math, random
* External modules: pyjokes

---

## Why Use Modules?

* Reuse code
* Organize large programs
* Avoid repetition
* Improve readability

---

## Types of Modules

### 1. Built-in Modules

Already available in Python.

```python
import math

print(math.sqrt(25))
```

---

### 2. External Modules

Installed using pip.

```bash
pip install pyjokes
```

Example:

```python
import pyjokes

joke = pyjokes.get_joke()
print(joke)
```

---

### 3. User-defined Modules

You can create your own module.

Example:

Create a file `mymodule.py`:

```python
def greet(name):
    return f"Hello, {name}"
```

Use it in another file:

```python
import mymodule

print(mymodule.greet("Mhi"))
```

---

## Importing Modules

### Basic import

```python
import math
print(math.pi)
```

---

### Import specific function

```python
from math import sqrt

print(sqrt(16))
```

---

### Import with alias

```python
import math as m

print(m.pi)
```

---

## Example Similar to pyjokes

Create your own simple module like pyjokes.

Create file `myjokes.py`:

```python
import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why do Python developers wear glasses? Because they can't C.",
    "Debugging: Being the detective in a crime movie where you are also the murderer."
]

def get_joke():
    return random.choice(jokes)
```

Use it:

```python
import myjokes

print(myjokes.get_joke())
```

---

## Installing and Using External Modules

```bash
pip install <module_name>
```

Example:

```bash
pip install pyjokes
```

---

## Checking Installed Modules

```bash
pip list
```

---

## Important Notes

* Always install modules inside a virtual environment
* Use correct import statements
* Avoid naming your file the same as built-in modules (like math.py)

---

## Common Errors

### ModuleNotFoundError

Cause: Module not installed

Fix:

```bash
pip install <module_name>
```

---

### Import Error

Cause: Wrong file name or path

Fix:

* Check file name
* Check folder structure

---

## Project Structure Example

```
project/
│
├── myjokes.py
├── main.py
└── myenv/
```

---

## Summary

* Module = reusable Python file
* Types: built-in, external, user-defined
* Helps organize and reuse code
* Can create your own modules like pyjokes

---
