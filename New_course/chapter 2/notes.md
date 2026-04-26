# Python Data Types 

---

## 1. What are Data Types?

Data types define the kind of value a variable can hold.  
Python is dynamically typed, meaning you don’t need to declare the type explicitly.

---

## 2. Basic (Primitive) Data Types

### 1. Integer (`int`)
- Whole numbers (positive or negative)
- No decimal point

```python
a = 10
b = -5
```

---

### 2. Float (`float`)
- Decimal numbers

```python
x = 3.14
y = -0.99
```

---

### 3. String (`str`)
- Sequence of characters
- Written inside quotes (`' '` or `" "`)

```python
name = "mahi"
text = 'hello'
```

---

### 4. Boolean (`bool`)
- Represents True or False

```python
is_valid = True
is_done = False
```

---

### 5. NoneType (`None`)
- Represents absence of value

```python
value = None
```

---

## 3. Collection Data Types

These store multiple values.

---

### 1. List (`list`)
- Ordered collection
- Mutable (can change)
- Allows duplicate values

```python
my_list = [1, 2, 3, 3]
my_list[0] = 10   # allowed
```

**Features:**
- Indexing allowed
- Changeable
- Duplicates allowed

---

### 2. Tuple (`tuple`)
- Ordered collection
- Immutable (cannot change)

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10 ❌ (Error)
```

**Features:**
- Indexing allowed
- Cannot modify after creation
- Faster than lists

---

### 3. Set (`set`)
- Unordered collection
- No duplicate values allowed

```python
my_set = {1, 2, 3, 3}
# Output: {1, 2, 3}
```

**Features:**
- No indexing
- Automatically removes duplicates
- Used for unique values

---

### 4. Dictionary (`dict`)
- Stores data in key-value pairs

```python
person = {
    "name": "mahi",
    "age": 25
}
```

**Features:**
- Access using keys
- Mutable
- Keys must be unique

---

### 5. Range (`range`)
- Represents a sequence of numbers
- Commonly used in loops

```python
r = range(1, 5)
# Output: 1, 2, 3, 4
```

**Features:**
- Memory efficient
- Generates numbers on demand
- Immutable

---

## 4. Key Differences 

### List vs Tuple
| Feature        | List            | Tuple           |
|---------------|-----------------|-----------------|
| Syntax        | []              | ()              |
| Mutability    | Mutable         | Immutable       |
| Speed         | Slower          | Faster          |
| Use Case      | Dynamic data    | Fixed data      |

---

### List vs Set
| Feature        | List            | Set             |
|---------------|-----------------|-----------------|
| Order         | Ordered         | Unordered       |
| Duplicates    | Allowed         | Not allowed     |
| Indexing      | Yes             | No              |

---

### Tuple vs Set
| Feature        | Tuple           | Set             |
|---------------|-----------------|-----------------|
| Order         | Ordered         | Unordered       |
| Mutable       | No              | Yes             |
| Duplicates    | Allowed         | Not allowed     |

---

### Set vs Dictionary
| Feature        | Set             | Dictionary      |
|---------------|-----------------|-----------------|
| Structure     | Only values     | Key-value pairs |
| Access        | No indexing     | By keys         |

---

### Range vs List
| Feature        | Range           | List            |
|---------------|-----------------|-----------------|
| Memory        | Efficient       | Uses more memory|
| Storage       | Not stored fully| Stores all items|
| Use Case      | Loops           | General storage |

---

## 5. When to Use What?

- Use **list** → when you need ordered, changeable data  
- Use **tuple** → when data should not change  
- Use **set** → when you need unique values  
- Use **dictionary** → when working with key-value data  
- Use **range** → when generating sequences (especially loops)

---

## Final Summary

- **int, float, str, bool, None** → basic types  
- **list, tuple, set, dict, range** → collection types  
- Choosing the correct type improves performance and readability  

---

---

## 6. Mutable vs Immutable Data Types

### What is Mutable?

A **mutable** object can be changed after it is created.

You can modify, add, or remove elements without changing the object's identity.

### Examples of Mutable Types:
- list
- set
- dictionary

```python
my_list = [1, 2, 3]
my_list[0] = 10   # allowed
print(my_list)    # [10, 2, 3]
```

---

### What is Immutable?

An **immutable** object cannot be changed after it is created.

If you try to modify it, Python creates a new object instead.

### Examples of Immutable Types:
- int
- float
- string
- tuple
- bool
- range

```python
x = 10
x = x + 5   # creates a new value, does not modify original

my_tuple = (1, 2, 3)
# my_tuple[0] = 10 ❌ Error
```

---

## Key Differences

| Feature        | Mutable                     | Immutable                  |
|----------------|----------------------------|----------------------------|
| Can change     | Yes                        | No                         |
| Memory         | Same object modified       | New object created         |
| Examples       | list, set, dict            | int, str, tuple, bool      |

---

## Important Note

- Mutable types are useful when data needs to change frequently.
- Immutable types are safer and faster when data should remain constant.

---