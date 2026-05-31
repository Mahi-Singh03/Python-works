# =========================================================
# LOOPS IN PYTHON
# =========================================================

# Loops are used to repeat code multiple times.

# Types of Loops:
# 1. for loop
# 2. while loop

# =========================================================
# FOR LOOP
# =========================================================

print("FOR LOOP:")

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# =========================================================
# USING range()
# =========================================================

print("\nrange(stop):")

for i in range(5):
    print(i)

# ---------------------------------------------------------

print("\nrange(start, stop):")

for i in range(1, 6):
    print(i)

# ---------------------------------------------------------

print("\nrange(start, stop, step):")

for i in range(1, 10, 2):
    print(i)

# =========================================================
# LOOPING THROUGH STRINGS
# =========================================================

print("\nLooping Through String:")

name = "Python"

for char in name:
    print(char)

# =========================================================
# NESTED FOR LOOP
# =========================================================

print("\nNested FOR Loop:")

for i in range(3):

    for j in range(2):
        print(i, j)

# =========================================================
# WHILE LOOP
# =========================================================

print("\nWHILE LOOP:")

count = 1

while count <= 5:
    print(count)

    count += 1

# =========================================================
# INFINITE LOOP
# =========================================================

# WARNING:
# This loop runs forever.

# while True:
#     print("Hello")

# =========================================================
# BREAK STATEMENT
# =========================================================

print("\nBREAK Statement:")

for i in range(10):

    if i == 5:
        break

    print(i)

# =========================================================
# CONTINUE STATEMENT
# =========================================================

print("\nCONTINUE Statement:")

for i in range(5):

    if i == 2:
        continue

    print(i)

# =========================================================
# PASS STATEMENT
# =========================================================

print("\nPASS Statement:")

for i in range(5):
    pass

print("Pass statement executed")

# =========================================================
# ELSE WITH LOOPS
# =========================================================

print("\nELSE with LOOP:")

for i in range(3):
    print(i)

else:
    print("Loop Finished")

# =========================================================
# LOOPING THROUGH DICTIONARY
# =========================================================

print("\nLooping Through Dictionary:")

student = {
    "name": "Mahi",
    "age": 25
}

for key, value in student.items():
    print(key, value)

# =========================================================
# USING enumerate()
# =========================================================

print("\nUsing enumerate():")

fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)

# =========================================================
# SUM OF NUMBERS USING LOOP
# =========================================================

print("\nSum of Numbers:")

total = 0

for i in range(1, 6):
    total += i

print(total)

# =========================================================
# MULTIPLICATION TABLE
# =========================================================

print("\nMultiplication Table of 5:")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# =========================================================
# CHECKING EVEN AND ODD NUMBERS
# =========================================================

print("\nEven and Odd Numbers:")

for i in range(1, 6):

    if i % 2 == 0:
        print(i, "is Even")

    else:
        print(i, "is Odd")

# =========================================================
# END OF PROGRAM
# =========================================================