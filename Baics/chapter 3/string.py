# =========================================================
# STRINGS IN PYTHON
# =========================================================

# A string is a sequence of characters.
# Strings can be created using:
# 1. Single Quotes ''
# 2. Double Quotes ""
# 3. Triple Quotes ''' ''' or """ """

# Strings are immutable.
# Immutable means once a string is created,
# it cannot be changed directly.

# =========================================================
# IMMUTABLE STRING EXAMPLE
# =========================================================

# x = "mahi"
# x[0] = "M"
# This will produce an error because strings
# cannot be modified directly.

# =========================================================
# CREATING STRINGS
# =========================================================

x = "mahi"
y = 'python'

print("Using Double Quotes:", x)
print("Using Single Quotes:", y)

# =========================================================
# MULTI-LINE STRINGS
# =========================================================

z = '''This is line 1
This is line 2
This is line 3'''

print("\nMulti-line String:")
print(z)

# =========================================================
# STRING INDEXING
# =========================================================

a = "mahi"

print("\nString Indexing:")

print(a[0])   # m
print(a[1])   # a
print(a[2])   # h
print(a[3])   # i

# =========================================================
# NEGATIVE INDEXING
# =========================================================

print("\nNegative Indexing:")

print(a[-1])   # i
print(a[-2])   # h

# =========================================================
# STRING SLICING
# =========================================================

print("\nString Slicing:")

print(a[0:2])   # ma
print(a[1:4])   # ahi

# =========================================================
# NEGATIVE SLICING
# =========================================================

print("\nNegative Slicing:")

print(a[-4:-2])   # ma
print(a[-3:-1])   # ah

# =========================================================
# STRING CONCATENATION
# =========================================================

# Concatenation means joining strings together.

b = "hello"
c = "world"

d = b + " " + c

print("\nString Concatenation:")

print(d)

# =========================================================
# REPEATING STRINGS
# =========================================================

e = "ha"

f = e * 3

print("\nRepeating Strings:")

print(f)

# =========================================================
# STRING METHODS
# =========================================================

g = "hello world"

print("\nString Methods:")

# upper()
print(g.upper())

# lower()
print(g.lower())

# capitalize()
print(g.capitalize())

# title()
print(g.title())

# strip()
print(g.strip())

# replace()
print(g.replace("world", "mahi"))

# split()
print(g.split())

# find()
print(g.find("world"))

# count()
print(g.count("o"))

# =========================================================
# F-STRINGS
# =========================================================

name = "mahi"
age = 25

print("\nF-Strings:")

print(f"Hello, my name is {name} and I am {age} years old.")

# =========================================================
# ESCAPE CHARACTERS
# =========================================================

print("\nEscape Characters:")

# 1. Single Quote
print("\n1. Single Quote:")
print('I\'m happy')

# 2. Double Quote
print("\n2. Double Quote:")
print("She said, \"Hello!\"")

# 3. Backslash
print("\n3. Backslash:")
print("HI \\")

# 4. New Line
print("\n4. New Line:")
print("Hello\nWorld")

# 5. Tab Space
print("\n5. Tab Space:")
print("Hello\tWorld")

# 6. Backspace
print("\n6. Backspace:")
print("Helloo\bWorld")

# =========================================================
# LENGTH OF STRING
# =========================================================

text = "Python"

print("\nLength of String:")

print(len(text))

# =========================================================
# CHECKING STRING TYPE
# =========================================================

print("\nChecking String Type:")

print(type(text))

# =========================================================
# END OF PROGRAM
# =========================================================