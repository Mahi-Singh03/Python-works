# Strings in Python

---

# What is a String?

A string is a sequence of characters enclosed inside:

- Single quotes `' '`
- Double quotes `" "`
- Triple quotes `''' '''` or `""" """`

Strings are used to store text data.

---

# Features of Strings

- Strings are immutable
- Strings are ordered
- Strings support indexing and slicing
- Strings can contain letters, numbers, and symbols

---

# Immutable Strings

Immutable means once a string is created, it cannot be changed.

Example:

```python
x = "mahi"

x[0] = "M"
```

## Output

```python
TypeError
```

Because strings cannot be modified directly.

---

# Creating Strings

## Using Double Quotes

```python
x = "mahi"

print(x)
```

---

## Using Single Quotes

```python
y = 'mahi'

print(y)
```

---

# Multi-line Strings

Triple quotes are used for multi-line strings.

```python
z = '''This is line 1
This is line 2
This is line 3'''

print(z)
```

---

# String Indexing

Indexing starts from `0`.

```python
a = "mahi"

print(a[0])
print(a[1])
```

## Output

```python
m
a
```

---

# Negative Indexing

Negative indexing starts from the end.

```python
print(a[-1])
print(a[-2])
```

## Output

```python
i
h
```

---

# String Slicing

Slicing extracts part of a string.

```python
print(a[0:2])
print(a[1:4])
```

## Output

```python
ma
ahi
```

---

# Negative Slicing

```python
print(a[-4:-2])
print(a[-3:-1])
```

## Output

```python
ma
ah
```

---

# Modifying Strings

Strings cannot be modified directly, but we can create new strings.

## String Concatenation

```python
b = "hello"
c = "world"

d = b + " " + c

print(d)
```

## Output

```python
hello world
```

---

# Repeating Strings

The `*` operator repeats strings.

```python
e = "ha"

f = e * 3

print(f)
```

## Output

```python
hahaha
```

---

# Common String Methods

```python
g = "hello world"
```

| Method | Description | Example Output |
|---|---|---|
| `upper()` | Converts to uppercase | HELLO WORLD |
| `lower()` | Converts to lowercase | hello world |
| `capitalize()` | Capitalizes first letter | Hello world |
| `title()` | Capitalizes every word | Hello World |
| `strip()` | Removes spaces | hello world |
| `replace()` | Replaces text | hello mahi |
| `split()` | Splits into list | ['hello', 'world'] |
| `find()` | Finds index | 6 |
| `count()` | Counts characters | 2 |

---

# Example of String Methods

```python
g = "hello world"

print(g.upper())
print(g.lower())
print(g.capitalize())
print(g.title())
print(g.strip())
print(g.replace("world", "mahi"))
print(g.split())
print(g.find("world"))
print(g.count("o"))
```

---

# F-Strings

F-strings are used for formatting strings.

```python
name = "mahi"
age = 25

print(f"Hello, my name is {name} and I am {age} years old.")
```

## Output

```python
Hello, my name is mahi and I am 25 years old.
```

---

# Escape Characters

Escape characters are special characters used inside strings.

| Escape Character | Description |
|---|---|
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab space |
| `\b` | Backspace |

---

# Escape Character Examples

## Single Quote

```python
print('I\'m happy')
```

## Output

```python
I'm happy
```

---

## Double Quote

```python
print("She said, \"Hello!\"")
```

## Output

```python
She said, "Hello!"
```

---

## Backslash

```python
print("HI \\\\")
```

## Output

```python
HI \\
```

---

## New Line

```python
print("Hello\nWorld")
```

## Output

```python
Hello
World
```

---

## Tab Space

```python
print("Hello\tWorld")
```

## Output

```python
Hello    World
```

---

## Backspace

```python
print("Helloo\bWorld")
```

## Output

```python
HelloWorld
```

---

# Length of String

The `len()` function returns the total number of characters.

```python
text = "Python"

print(len(text))
```

## Output

```python
6
```

---

# Checking String Type

```python
text = "Python"

print(type(text))
```

## Output

```python
<class 'str'>
```

---

# Summary

- Strings store text data
- Strings are immutable
- Strings support indexing and slicing
- String methods help manipulate text
- Escape characters provide special formatting
- F-strings are useful for formatting output