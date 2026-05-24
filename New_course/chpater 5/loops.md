# Loops in Python

---

# What are Loops?

Loops are used to execute a block of code repeatedly.

Instead of writing the same code multiple times, loops help automate repetition.

---

# Types of Loops in Python

Python mainly provides:

- `for` loop
- `while` loop

---

# for Loop

The `for` loop is used to iterate over a sequence.

Examples of sequences:
- List
- Tuple
- String
- Set
- Dictionary
- Range

---

# Syntax of for Loop

```python
for variable in sequence:
    # code
```

---

# Example of for Loop

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

## Output

```python
apple
banana
mango
```

---

# Using range() in for Loop

The `range()` function generates numbers.

---

# range(stop)

```python
for i in range(5):
    print(i)
```

## Output

```python
0
1
2
3
4
```

---

# range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

## Output

```python
1
2
3
4
5
```

---

# range(start, stop, step)

```python
for i in range(1, 10, 2):
    print(i)
```

## Output

```python
1
3
5
7
9
```

---

# Looping Through Strings

```python
name = "Python"

for char in name:
    print(char)
```

---

# Nested for Loop

A loop inside another loop.

```python
for i in range(3):

    for j in range(2):
        print(i, j)
```

## Output

```python
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# while Loop

The `while` loop runs as long as the condition is true.

---

# Syntax of while Loop

```python
while condition:
    # code
```

---

# Example of while Loop

```python
count = 1

while count <= 5:
    print(count)

    count += 1
```

## Output

```python
1
2
3
4
5
```

---

# Infinite Loop

A loop that never stops.

```python
while True:
    print("Hello")
```

This loop runs forever.

---

# break Statement

The `break` statement stops the loop immediately.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

## Output

```python
0
1
2
3
4
```

---

# continue Statement

The `continue` statement skips the current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

## Output

```python
0
1
3
4
```

---

# pass Statement

The `pass` statement acts as a placeholder.

```python
for i in range(5):
    pass
```

---

# else with Loops

The `else` block runs when loop finishes normally.

```python
for i in range(3):
    print(i)

else:
    print("Loop Finished")
```

## Output

```python
0
1
2
Loop Finished
```

---

# Looping Through Dictionary

```python
student = {
    "name": "Mahi",
    "age": 25
}

for key, value in student.items():
    print(key, value)
```

---

# Looping Through List with Index

Using `enumerate()`.

```python
fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)
```

---

# Common Loop Use Cases

- Printing values
- Calculations
- Iterating through collections
- Repeating tasks
- Building menus
- Data processing

---

# Summary

- Loops repeat code automatically
- `for` loop works with sequences
- `while` loop works with conditions
- `break` stops loops
- `continue` skips iterations
- `pass` acts as placeholder
- Nested loops are loops inside loops