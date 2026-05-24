# Recursion in Python

---

# What is Recursion?

Recursion is a process where a function calls itself repeatedly to solve a problem.

A recursive function breaks a big problem into smaller subproblems.

---

# Important Parts of Recursion

Every recursive function must contain:

1. Base Case
2. Recursive Case

---

# Base Case

The condition that stops recursion.

Without a base case, recursion will continue forever and cause an error.

---

# Recursive Case

The part where the function calls itself again.

---

# Basic Structure of Recursion

```python
def function_name():

    if base_condition:
        return value

    return function_name()
```

---

# Simple Recursion Example

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

```python
countdown(5)
```

## Output

```python
5
4
3
2
1
```

---

# Understanding the Flow

When:

```python
countdown(3)
```

Python executes:

```python
countdown(3)
countdown(2)
countdown(1)
countdown(0)
```

At `0`, recursion stops because of the base case.

---

# Factorial Using Recursion

Factorial means:

```python
5! = 5 × 4 × 3 × 2 × 1
```

---

# Recursive Factorial Program

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

# How Factorial Works

```python
factorial(5)

5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)

Base Case:
factorial(1) = 1
```

Final Answer:

```python
120
```

---

# Fibonacci Series Using Recursion

Fibonacci sequence:

```python
0 1 1 2 3 5 8 ...
```

---

# Fibonacci Program

```python
def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
```

```python
print(fibonacci(6))
```

## Output

```python
8
```

---

# Sum of Numbers Using Recursion

```python
def total(n):

    if n == 1:
        return 1

    return n + total(n - 1)
```

```python
print(total(5))
```

## Output

```python
15
```

Because:

```python
5 + 4 + 3 + 2 + 1 = 15
```

---

# Advantages of Recursion

- Makes code shorter
- Easier to solve complex problems
- Useful for trees and graphs
- Breaks problems into smaller parts

---

# Disadvantages of Recursion

- Can be slower
- Uses more memory
- Too much recursion causes errors

---

# Recursion Error

If recursion never stops:

```python
RecursionError
```

Example:

```python
def demo():
    demo()

demo()
```

This creates infinite recursion.

---

# Recursive vs Loop

| Recursion | Loop |
|---|---|
| Function calls itself | Repeats code |
| Uses stack memory | Uses less memory |
| Good for complex problems | Faster for simple repetition |

---

# Tail Recursion

Tail recursion happens when the recursive call is the last statement.

Example:

```python
def countdown(n):

    if n == 0:
        return

    return countdown(n - 1)
```

---

# Real-Life Examples of Recursion

- Folder navigation
- Tree structures
- Searching algorithms
- Fibonacci sequence
- Factorials

---

# Summary

- Recursion means a function calling itself
- Base case stops recursion
- Recursive case repeats the function
- Useful for solving complex problems
- Incorrect recursion can cause infinite loops