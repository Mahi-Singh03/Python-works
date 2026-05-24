# =========================================================
# CONDITIONAL EXPRESSIONS IN PYTHON
# =========================================================

# Conditional expressions are used to make decisions.

# Python supports:
# 1. if
# 2. if else
# 3. if elif else
# 4. Nested if
# 5. Short-hand conditions

# =========================================================
# IF STATEMENT
# =========================================================

age = 18

print("IF Statement:")

if age >= 18:
    print("You are eligible to vote")

# =========================================================
# IF ELSE STATEMENT
# =========================================================

number = 5

print("\nIF ELSE Statement:")

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# =========================================================
# IF ELIF ELSE STATEMENT
# =========================================================

marks = 85

print("\nIF ELIF ELSE Statement:")

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# =========================================================
# NESTED IF STATEMENT
# =========================================================

age = 20
citizen = True

print("\nNested IF Statement:")

if age >= 18:

    if citizen:
        print("Eligible to vote")

# =========================================================
# COMPARISON OPERATORS
# =========================================================

print("\nComparison Operators:")

print(10 == 10)
print(10 != 5)
print(10 > 5)
print(5 < 10)
print(10 >= 10)
print(5 <= 10)

# =========================================================
# LOGICAL OPERATORS
# =========================================================

print("\nLogical Operators:")

has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")

if age >= 18 or has_id:
    print("Condition True")

if not False:
    print("NOT Operator Example")

# =========================================================
# SHORT-HAND IF
# =========================================================

print("\nShort-hand IF:")

if age >= 18: print("Adult")

# =========================================================
# TERNARY OPERATOR
# =========================================================

print("\nTernary Operator:")

number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)

# =========================================================
# PASS STATEMENT
# =========================================================

print("\nPass Statement:")

x = 10

if x > 5:
    pass

print("Pass statement executed")

# =========================================================
# BOOLEAN VALUES
# =========================================================

print("\nBoolean Values:")

print(10 > 5)
print(5 > 10)

# =========================================================
# MULTIPLE CONDITIONS
# =========================================================

print("\nMultiple Conditions:")

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# =========================================================
# CHECKING POSITIVE, NEGATIVE, OR ZERO
# =========================================================

print("\nChecking Number Type:")

num = -5

if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")

# =========================================================
# END OF PROGRAM
# =========================================================