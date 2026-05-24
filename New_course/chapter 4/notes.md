# Dictionaries in Python

---

# What is a Dictionary?

A dictionary is a collection of key-value pairs.

Each key in a dictionary is unique and maps to a value.

---

# Features of Dictionaries

- Mutable (can be modified)
- Ordered
- Stores data in key-value format
- Keys must be unique
- Values can be of any data type

---

# Creating a Dictionary

```python
information = {
    "name": "mahi singh",
    "age": 25,
    "gender": "male",
    "hobbies": ["coding", "gaming", "traveling"],
    "education": {
        "degree": "Bachelor's in Computer Science",
        "university": "Punj University",
        "graduation_year": 2024
    }
}
```

---

# Understanding Key-Value Pairs

| Key | Value |
|---|---|
| `"name"` | `"mahi singh"` |
| `"age"` | `25` |
| `"gender"` | `"male"` |
| `"hobbies"` | List |
| `"education"` | Nested Dictionary |

---

# Accessing Values

Values are accessed using keys.

```python
print(information["name"])
print(information["age"])
```

## Output

```python
mahi singh
25
```

---

# Accessing Nested Dictionary Values

```python
print(information["education"]["degree"])

print(information["education"]["university"])

print(information["education"]["graduation_year"])
```

## Output

```python
Bachelor's in Computer Science
Punj University
2024
```

---

# Accessing List Values Inside Dictionary

```python
print(information["hobbies"][0])

print(information["hobbies"][1])
```

## Output

```python
coding
gaming
```

---

# Printing Complete Dictionary

```python
print(information)
```

---

# Dictionary Methods

---

# keys()

Returns all keys from the dictionary.

```python
print(information.keys())
```

## Output

```python
dict_keys(['name', 'age', 'gender', 'hobbies', 'education'])
```

---

# values()

Returns all values from the dictionary.

```python
print(information.values())
```

---

# items()

Returns key-value pairs as tuples.

```python
print(information.items())
```

---

# Updating Dictionary Values

The `update()` method modifies existing values or adds new values.

```python
information.update({"name": "Mahi Singh"})
```

## Updated Output

```python
{
    'name': 'Mahi Singh'
}
```

---

# Adding New Key-Value Pair

```python
information.update({"nationality": "Indian"})
```

---

# get() Method

Safely accesses values.

```python
print(information.get("name"))
```

## Output

```python
Mahi Singh
```

---

# Difference Between get() and Square Brackets

## Using get()

```python
print(information.get("name1"))
```

## Output

```python
None
```

---

## Using Square Brackets

```python
print(information["name1"])
```

## Output

```python
KeyError
```

Because `"name1"` does not exist.

---

# Common Dictionary Methods

| Method | Description |
|---|---|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `update()` | Updates dictionary |
| `get()` | Safely gets value |
| `clear()` | Removes all items |
| `copy()` | Creates copy of dictionary |
| `pop()` | Removes item using key |

---

# clear() Method

Removes all items from dictionary.

```python
data = {"a": 1, "b": 2}

data.clear()

print(data)
```

## Output

```python
{}
```

---

# copy() Method

Creates a shallow copy.

```python
original = {"name": "mahi"}

copied = original.copy()

print(copied)
```

---

# pop() Method

Removes a value using key.

```python
data = {"name": "mahi", "age": 25}

data.pop("age")

print(data)
```

## Output

```python
{'name': 'mahi'}
```

---

# Length of Dictionary

The `len()` function returns the total number of key-value pairs.

```python
print(len(information))
```

---

# Checking Dictionary Type

```python
print(type(information))
```

## Output

```python
<class 'dict'>
```

---

# Nested Dictionaries

Dictionaries can contain other dictionaries.

```python
student = {
    "name": "Mahi",
    "marks": {
        "python": 90,
        "java": 85
    }
}
```

---

# Summary

- Dictionaries store data in key-value format
- Keys are unique
- Dictionaries are mutable
- Supports nested structures
- Useful for structured and organized data storage