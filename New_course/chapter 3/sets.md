# Sets in Python

---

# What is a Set?

A set is an unordered collection of unique elements.

## Features of Sets

- Unordered
- Mutable
- Does not allow duplicate values
- Supports mathematical operations like union and intersection

---

# Creating a Set

```python
my_set = {1, 2, 3, 4, 5}

print(my_set)
```

---

# Duplicate Elements in Sets

Sets automatically remove duplicate values.

```python
my_set = {1, 2, 3, 3, 4, 5}

print(my_set)
```

## Output

```python
{1, 2, 3, 4, 5}
```

---

# Boolean and Integer Values in Sets

In Python:

```python
True == 1
False == 0
```

Because of this, duplicate values are removed.

```python
s1 = {True, False, True, False, 1, 0, 9, "mahi", "mahi"}

print(s1)

print(1 == True)
```

## Output

```python
{False, True, 9, 'mahi'}

True
```

---

# Adding Elements to a Set

The `add()` method adds an element to the set.

```python
my_set = {1, 2, 3}

my_set.add(4)

print(my_set)
```

---

# Removing Elements from a Set

## remove()

Removes a specific element.

```python
my_set.remove(2)
```

If the element does not exist, it gives an error.

---

## discard()

Removes an element safely.

```python
my_set.discard(10)
```

Does not give an error if the value is missing.

---

# Clearing a Set

The `clear()` method removes all elements.

```python
my_set.clear()

print(my_set)
```

## Output

```python
set()
```

---

# Set Operations

```python
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}
```

---

# Union

Combines elements from both sets.

```python
print(s2.union(s3))
```

## Output

```python
{1, 2, 3, 4, 5, 6, 7, 8}
```

---

# Intersection

Returns common elements.

```python
print(s2.intersection(s3))
```

## Output

```python
{4, 5}
```

---

# Difference

Returns elements present in one set but not in the other.

```python
print(s2.difference(s3))
print(s3.difference(s2))
```

## Output

```python
{1, 2, 3}
{6, 7, 8}
```

---

# Symmetric Difference

Returns uncommon elements from both sets.

```python
print(s2.symmetric_difference(s3))
```

## Output

```python
{1, 2, 3, 6, 7, 8}
```

---

# Subset and Superset

```python
s4 = {1, 2, 3}
s5 = {1, 2, 3, 4, 5}
```

## Subset

Checks whether all elements exist in another set.

```python
print(s4.issubset(s5))
```

## Output

```python
True
```

---

## Superset

Checks whether a set contains another set completely.

```python
print(s5.issuperset(s4))
```

## Output

```python
True
```

---

# Common Set Methods

| Method | Description |
|---|---|
| `add()` | Adds element |
| `remove()` | Removes element |
| `discard()` | Removes element safely |
| `clear()` | Removes all elements |
| `union()` | Combines sets |
| `intersection()` | Common elements |
| `difference()` | Different elements |
| `symmetric_difference()` | Uncommon elements |

---

# Frozenset in Python

A frozenset is an immutable version of a set.

Once created, it cannot be modified.

---

# Creating a Frozenset

```python
my_frozenset = frozenset([1, 2, 3, 4, 5])

print(my_frozenset)
```

## Output

```python
frozenset({1, 2, 3, 4, 5})
```

---

# Features of Frozenset

- Immutable
- Hashable
- Can be used as dictionary keys
- Does not allow modification

---

# Summary

## Sets
- Unordered collection
- Unique elements only
- Mutable
- Supports set operations

## Frozensets
- Immutable version of sets
- Cannot be changed after creation