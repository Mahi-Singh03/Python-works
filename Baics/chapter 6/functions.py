# =========================================================
# FUNCTIONS IN PYTHON
# =========================================================

# Functions are reusable blocks of code
# that perform specific tasks.

# =========================================================
# SIMPLE FUNCTION
# =========================================================

def greet():
    print("Hello World")

print("Simple Function:")

greet()

# =========================================================
# FUNCTION WITH PARAMETERS
# =========================================================

def greet_user(name):
    print("Hello", name)

print("\nFunction with Parameters:")

greet_user("Mahi")

# =========================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# =========================================================

def add(a, b):
    print("Addition:", a + b)

print("\nFunction with Multiple Parameters:")

add(10, 20)

# =========================================================
# RETURN STATEMENT
# =========================================================

def square(num):
    return num * num

print("\nReturn Statement:")

result = square(5)

print(result)

# =========================================================
# DEFAULT PARAMETERS
# =========================================================

def welcome(name="Guest"):
    print("Welcome", name)

print("\nDefault Parameters:")

welcome()

welcome("Mahi")

# =========================================================
# KEYWORD ARGUMENTS
# =========================================================

def student(name, age):
    print(name, age)

print("\nKeyword Arguments:")

student(age=25, name="Mahi")

# =========================================================
# *args
# =========================================================

# *args accepts multiple values.

def numbers(*args):
    print(args)

print("\nUsing *args:")

numbers(1, 2, 3, 4, 5)

# =========================================================
# **kwargs
# =========================================================

# **kwargs accepts keyword arguments.

def information(**kwargs):
    print(kwargs)

print("\nUsing **kwargs:")

information(name="Mahi", age=25, city="Delhi")

# =========================================================
# LOCAL VARIABLES
# =========================================================

def local_demo():
    x = 10

    print(x)

print("\nLocal Variables:")

local_demo()

# =========================================================
# GLOBAL VARIABLES
# =========================================================

x = 100

def global_demo():
    print(x)

print("\nGlobal Variables:")

global_demo()

# =========================================================
# LAMBDA FUNCTION
# =========================================================

print("\nLambda Function:")

square = lambda x: x * x

print(square(5))

# =========================================================
# RECURSIVE FUNCTION
# =========================================================

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print("\nRecursive Function:")

print(factorial(5))

# =========================================================
# FUNCTION WITH LIST
# =========================================================

def total(numbers):
    return sum(numbers)

print("\nFunction with List:")

print(total([1, 2, 3, 4, 5]))

# =========================================================
# EVEN OR ODD FUNCTION
# =========================================================

def even_or_odd(num):

    if num % 2 == 0:
        return "Even"

    return "Odd"

print("\nEven or Odd Function:")

print(even_or_odd(10))

print(even_or_odd(7))

# =========================================================
# DOCSTRING
# =========================================================

def demo():
    """This function demonstrates docstrings"""

    print("Hello")

print("\nDocstring:")

print(demo.__doc__)

# =========================================================
# BUILT-IN FUNCTIONS
# =========================================================

numbers = [10, 20, 30, 40]

print("\nBuilt-in Functions:")

print(len(numbers))

print(sum(numbers))

print(max(numbers))

print(min(numbers))

print(type(numbers))

# =========================================================
# FUNCTION CALLING ANOTHER FUNCTION
# =========================================================

def message():
    print("Welcome")

def start():
    message()

print("\nFunction Calling Another Function:")

start()

# =========================================================
# END OF PROGRAM
# =========================================================