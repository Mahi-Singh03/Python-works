# Python Lists and Tuples

---

# Lists in Python

## What is a List?

A list is a collection of items that is:

- Mutable (can be changed)
- Ordered
- Allows duplicate values
- Supports indexing and slicing

---

# Creating Lists

```python
list1 = ["hi", 76, 3.145, True, [9, 3, 9, "hi"]]

list2 = [1, 2, 3, 4, 5, {"key1": "value1", "key2": "value2"}]

print(list1)
print(list2)
```

---

# Accessing Elements

## Using Indexing

```python
list1 = ["hi", 76, 3.145, True, [9, 3, 9, "hi"]]

print(list1[0])      # hi
print(list1[2])      # 3.145
print(list1[4][3])   # hi
```

---

# Modifying List Elements

Lists are mutable, meaning values can be changed.

```python
list1 = ["hi", 76, 3.145]

list1[0] = "hello"

print(list1)
```

## Output

```python
['hello', 76, 3.145]
```

---

# Adding Elements to Lists

## 1. append()

Adds a single element at the end.

```python
list1 = ["hi", 76]

list1.append("hello")

print(list1)
```

## Output

```python
['hi', 76, 'hello']
```

---

## 2. insert()

Adds an element at a specific index.

```python
list1 = ["hi", 76]

list1.insert(1, "world")

print(list1)
```

## Output

```python
['hi', 'world', 76]
```

---

## 3. extend()

Adds elements from another list.

```python
list1 = ["hi", 76]

list2 = ["foo", "bar"]

list1.extend(list2)

print(list1)
```

## Output

```python
['hi', 76, 'foo', 'bar']
```

---

# Concatenating Lists

We can combine lists using the `+` operator.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)
```

## Output

```python
[1, 2, 3, 4, 5, 6]
```

---

# Repeating Lists

We can repeat lists using the `*` operator.

```python
list4 = [1, 2, 3]

list5 = list4 * 3

print(list5)
```

## Output

```python
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

---

# Sorting Lists

```python
list6 = [5, 2, 1, 4, 3]

list6.sort()

print(list6)
```

## Output

```python
[1, 2, 3, 4, 5]
```

---

# Removing Elements

## Using pop()

Removes an element using index.

```python
list6 = [1, 2, 3, 4, 5]

list6.pop(3)

print(list6)
```

## Output

```python
[1, 2, 3, 5]
```

---

# Common List Methods

| Method | Description |
|---|---|
| `append()` | Adds element at end |
| `insert()` | Adds element at specific position |
| `extend()` | Adds multiple elements |
| `pop()` | Removes element using index |
| `remove()` | Removes specific value |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `clear()` | Removes all elements |

---

# Tuples in Python

## What is a Tuple?

A tuple is a collection of items that is:

- Immutable (cannot be changed)
- Ordered
- Allows duplicate values
- Supports indexing and slicing

---

# Creating Tuples

```python
tuple1 = ("hi", 76, 3.145, True)

tuple2 = (1, 2, 3, 4, 5, {"key1": "value1"})

print(tuple1)
print(tuple2)
```

---

# Accessing Tuple Elements

```python
tuple1 = ("hi", 76, 3.145, True)

print(tuple1[0])
print(tuple1[2])
```

## Output

```python
hi
3.145
```

---

# Tuple Methods

## 1. count()

Counts occurrences of a value.

```python
tuple3 = (1, 2, 3, 1, 1, 4)

print(tuple3.count(1))
```

## Output

```python
3
```

---

## 2. index()

Returns index of first occurrence.

```python
tuple3 = (1, 2, 3, 4)

print(tuple3.index(3))
```

## Output

```python
2
```

---

# Other Tuple Operations

```python
tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

print(len(tuple1))

print(tuple1 + tuple2)

print(tuple1 * 2)
```

## Output

```python
3
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 1, 2, 3)
```

---

# Difference Between List and Tuple

| Feature | List | Tuple |
|---|---|---|
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Duplicate Values | Allowed | Allowed |
| Syntax | `[]` | `()` |
| Methods | Many methods | Few methods |

---

# Summary

## Lists
- Mutable
- Ordered
- Supports indexing and slicing
- Can add, remove, and modify elements

## Tuples
- Immutable
- Ordered
- Faster than lists
- Useful for fixed data