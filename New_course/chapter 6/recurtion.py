# =========================================================
# RECURSION IN PYTHON
# =========================================================

# Recursion means a function calling itself.

# Every recursive function must have:
# 1. Base Case
# 2. Recursive Case

# =========================================================
# SIMPLE RECURSION EXAMPLE
# =========================================================

def countdown(n):

    # Base Case
    if n == 0:
        return

    print(n)

    # Recursive Call
    countdown(n - 1)

print("Countdown Using Recursion:")

countdown(5)

# =========================================================
# FACTORIAL USING RECURSION
# =========================================================

def factorial(n):

    # Base Case
    if n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)

print("\nFactorial Using Recursion:")

print(factorial(5))

# =========================================================
# FIBONACCI USING RECURSION
# =========================================================

def fibonacci(n):

    # Base Cases
    if n == 0:
        return 0

    elif n == 1:
        return 1

    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci Using Recursion:")

for i in range(7):
    print(fibonacci(i))

# =========================================================
# SUM OF NUMBERS USING RECURSION
# =========================================================

def total(n):

    # Base Case
    if n == 1:
        return 1

    # Recursive Case
    return n + total(n - 1)

print("\nSum of Numbers Using Recursion:")

print(total(5))

# =========================================================
# RECURSION WITH STRINGS
# =========================================================

def reverse_string(text):

    # Base Case
    if len(text) == 0:
        return text

    # Recursive Case
    return reverse_string(text[1:]) + text[0]

print("\nReverse String Using Recursion:")

print(reverse_string("python"))

# =========================================================
# RECURSION ERROR EXAMPLE
# =========================================================

# WARNING:
# This creates infinite recursion.

# def demo():
#     demo()

# demo()

# =========================================================
# CHECKING EVEN OR ODD USING RECURSION
# =========================================================

def even_or_odd(n):

    if n % 2 == 0:
        return "Even"

    return "Odd"

print("\nEven or Odd:")

print(even_or_odd(10))

print(even_or_odd(7))

# =========================================================
# POWER OF A NUMBER USING RECURSION
# =========================================================

def power(base, exponent):

    # Base Case
    if exponent == 0:
        return 1

    # Recursive Case
    return base * power(base, exponent - 1)

print("\nPower Using Recursion:")

print(power(2, 4))

# =========================================================
# COUNTING CHARACTERS USING RECURSION
# =========================================================

def count_characters(text):

    # Base Case
    if text == "":
        return 0

    # Recursive Case
    return 1 + count_characters(text[1:])

print("\nCounting Characters:")

print(count_characters("Python"))

# =========================================================
# END OF PROGRAM
# =========================================================