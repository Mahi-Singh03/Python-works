# =========================================================
# PYTHON LISTS AND TUPLES
# =========================================================

# =========================================================
# LISTS IN PYTHON
# =========================================================

# A list is a collection of multiple values.
#
# Features of Lists:
# 1. Mutable       -> We can change the values.
# 2. Ordered       -> Elements keep their position.
# 3. Allows Duplicates
# 4. Supports Indexing and Slicing
# 5. Can store multiple data types together.

# ---------------------------------------------------------
# Creating Lists
# ---------------------------------------------------------

list1 = ["hi", 76, 3.145, True, [9, 3, 9, "hi"]]

list2 = [1, 2, 3, 4, 5, {"key1": "value1", "key2": "value2"}]

print("List 1:", list1)
print("List 2:", list2)

# ---------------------------------------------------------
# Accessing Elements in Lists
# ---------------------------------------------------------

# Indexing starts from 0.

print("\nAccessing Elements:")

print(list1[0])     # First element
print(list1[1])     # Second element
print(list1[2])     # Third element

# Accessing nested list element
print(list1[4][3])

# Accessing dictionary value inside list
print(list2[5]["key1"])

# ---------------------------------------------------------
# Modifying Elements in Lists
# ---------------------------------------------------------

# Lists are mutable, meaning values can be changed.

print("\nBefore Modification:")
print(list1)

list1[0] = "hello"

print("After Modification:")
print(list1)

# ---------------------------------------------------------
# Adding Elements to Lists
# ---------------------------------------------------------

# append()
# Adds a single element at the end of the list.

print("\nUsing append():")

list1.append("python")

print(list1)

# ---------------------------------------------------------

# insert()
# Adds an element at a specific index.

print("\nUsing insert():")

list1.insert(1, "world")

print(list1)

# ---------------------------------------------------------

# extend()
# Adds multiple elements from another list.

print("\nUsing extend():")

extra_list = ["foo", "bar"]

list1.extend(extra_list)

print(list1)

# ---------------------------------------------------------
# Concatenating Lists
# ---------------------------------------------------------

# The + operator combines two lists.

print("\nUsing + Operator:")

list3 = list1 + extra_list

print(list3)

# ---------------------------------------------------------
# Repeating Lists
# ---------------------------------------------------------

# The * operator repeats list elements.

print("\nUsing * Operator:")

list4 = [1, 2, 3]

list5 = list4 * 3

print(list5)

# ---------------------------------------------------------
# Sorting Lists
# ---------------------------------------------------------

# sort() arranges elements in ascending order.

print("\nUsing sort():")

list6 = [5, 2, 1, 4, 3]

print("Before Sorting:", list6)

list6.sort()

print("After Sorting:", list6)

# ---------------------------------------------------------
# Removing Elements from Lists
# ---------------------------------------------------------

# pop()
# Removes element using index.

print("\nUsing pop():")

list6.pop(3)

print(list6)

# ---------------------------------------------------------

# remove()
# Removes a specific value.

print("\nUsing remove():")

list6.remove(2)

print(list6)

# ---------------------------------------------------------

# clear()
# Removes all elements from list.

print("\nUsing clear():")

temp_list = [1, 2, 3]

print("Before clear():", temp_list)

temp_list.clear()

print("After clear():", temp_list)

# ---------------------------------------------------------
# Length of List
# ---------------------------------------------------------

# len() returns total number of elements.

print("\nUsing len():")

print(len(list1))

# ---------------------------------------------------------
# Slicing in Lists
# ---------------------------------------------------------

# Slicing extracts a portion of a list.

numbers = [10, 20, 30, 40, 50, 60]

print("\nList Slicing:")

print(numbers[1:4])   # From index 1 to 3
print(numbers[:3])    # Start to index 2
print(numbers[2:])    # Index 2 to end
print(numbers[::-1])  # Reverse list


















# =========================================================
# TUPLES IN PYTHON
# =========================================================

# A tuple is also a collection of values.
#
# Features of Tuples:
# 1. Immutable     -> Cannot be changed
# 2. Ordered
# 3. Allows Duplicates
# 4. Supports Indexing and Slicing

# ---------------------------------------------------------
# Creating Tuples
# ---------------------------------------------------------

tuple1 = ("hi", 76, 3.145, True)

tuple2 = (1, 2, 3, 4, 5, {"key1": "value1"})

print("\nTuple 1:", tuple1)
print("Tuple 2:", tuple2)

# ---------------------------------------------------------
# Accessing Tuple Elements
# ---------------------------------------------------------

print("\nAccessing Tuple Elements:")

print(tuple1[0])
print(tuple1[2])

# Accessing dictionary value inside tuple
print(tuple2[5]["key1"])

# ---------------------------------------------------------
# Tuple Methods
# ---------------------------------------------------------

tuple3 = (1, 2, 3, 4, 5, 1, 2, 3)

# count()
# Counts occurrences of a value.

print("\nUsing count():")

print(tuple3.count(1))

# ---------------------------------------------------------

# index()
# Returns index of first occurrence.

print("\nUsing index():")

print(tuple3.index(3))

# ---------------------------------------------------------
# Length of Tuple
# ---------------------------------------------------------

print("\nUsing len():")

print(len(tuple3))

# ---------------------------------------------------------
# Checking Tuple Type
# ---------------------------------------------------------

# isinstance() checks object type.

print("\nUsing isinstance():")

print(isinstance(tuple3, tuple))

# ---------------------------------------------------------
# Concatenating Tuples
# ---------------------------------------------------------

print("\nTuple Concatenation:")

tuple4 = (10, 20, 30)
tuple5 = (40, 50, 60)

print(tuple4 + tuple5)

# ---------------------------------------------------------
# Repeating Tuples
# ---------------------------------------------------------

print("\nTuple Repetition:")

print(tuple4 * 2)

# ---------------------------------------------------------
# Tuple Slicing
# ---------------------------------------------------------

print("\nTuple Slicing:")

print(tuple3[1:5])

# =========================================================
# DIFFERENCE BETWEEN LISTS AND TUPLES
# =========================================================

# LISTS:
# - Mutable
# - Uses square brackets []
# - More methods available
# - Slower than tuples

# TUPLES:
# - Immutable
# - Uses parentheses ()
# - Limited methods
# - Faster than lists

# =========================================================
# END OF PROGRAM
# =========================================================