# Conditional Expressions in Python

---

# What are Conditional Expressions?

Conditional expressions are used to make decisions in Python.

They allow a program to execute different blocks of code based on conditions.

---

# Types of Conditional Statements

Python provides:

- `if`
- `if else`
- `if elif else`
- Nested `if`
- Short-hand conditional expressions

---

# if Statement

The `if` statement executes code only if the condition is true.

## Syntax

```python
if condition:
    # code
```

---

# Example of if Statement

```python
age = 18

if age >= 18:
    print("You are eligible to vote")
```

## Output

```python
You are eligible to vote
```

---

# if else Statement

The `else` block executes when the condition is false.

## Syntax

```python
if condition:
    # code
else:
    # code
```

---

# Example of if else

```python
number = 5

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

## Output

```python
Odd Number
```

---

# if elif else Statement

Used when multiple conditions need to be checked.

## Syntax

```python
if condition1:
    # code

elif condition2:
    # code

else:
    # code
```

---

# Example of if elif else

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

## Output

```python
Grade B
```

---

# Nested if Statement

An `if` statement inside another `if` statement.

## Example

```python
age = 20
citizen = True

if age >= 18:
    
    if citizen:
        print("Eligible to vote")
```

## Output

```python
Eligible to vote
```

---

# Comparison Operators

Conditional expressions often use comparison operators.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition true |
| `not` | Reverses condition |

---

# Example of Logical Operators

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
```

## Output

```python
Entry Allowed
```

---

# Short-hand if Statement

Python allows writing simple conditions in one line.

## Syntax

```python
if condition: statement
```

---

# Example

```python
age = 20

if age >= 18: print("Adult")
```

---

# Short-hand if else (Ternary Operator)

## Syntax

```python
value_if_true if condition else value_if_false
```

---

# Example

```python
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

## Output

```python
Even
```

---

# pass Statement

The `pass` statement is used as a placeholder.

```python
x = 10

if x > 5:
    pass
```

---

# Indentation in Conditions

Python uses indentation to define blocks of code.

Correct Example:

```python
if True:
    print("Hello")
```

Wrong Example:

```python
if True:
print("Hello")
```

This will produce an error.

---

# Boolean Values

Conditions return Boolean values:

- `True`
- `False`

Example:

```python
print(10 > 5)
print(5 > 10)
```

## Output

```python
True
False
```

---

# Multiple Conditions Example

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

---

# Summary

- Conditional expressions help make decisions
- `if` checks conditions
- `else` runs when condition is false
- `elif` checks multiple conditions
- Logical operators combine conditions
- Ternary operators provide short-hand conditions
- Indentation is very important in Python