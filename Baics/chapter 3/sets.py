# =========================================================
# SETS IN PYTHON
# =========================================================

# A set is an unordered collection of unique elements.

# Features of Sets:
# 1. Unordered
# 2. Mutable
# 3. Does not allow duplicate values
# 4. Supports mathematical operations

# =========================================================
# CREATING SETS
# =========================================================

my_set = {1, 2, 3, 4, 5}

print("Original Set:")
print(my_set)

# =========================================================
# DUPLICATE VALUES
# =========================================================

# Sets automatically remove duplicates.

duplicate_set = {1, 2, 3, 3, 4, 5}

print("\nSet with Duplicate Values:")
print(duplicate_set)

# =========================================================
# BOOLEAN AND INTEGER VALUES
# =========================================================

# In Python:
# True == 1
# False == 0

s1 = {True, False, True, False, 1, 0, 9, "mahi", "mahi"}

print("\nBoolean and Integer Values in Set:")
print(s1)

print("\nChecking Equality:")
print(1 == True)

# =========================================================
# ADDING ELEMENTS
# =========================================================

print("\nUsing add():")

my_set.add(6)

print(my_set)

# =========================================================
# REMOVING ELEMENTS
# =========================================================

# remove()
# Removes an element.
# Gives error if value is missing.

print("\nUsing remove():")

my_set.remove(2)

print(my_set)

# ---------------------------------------------------------

# discard()
# Removes element safely.
# Does not give error if value is absent.

print("\nUsing discard():")

my_set.discard(10)

print(my_set)

# =========================================================
# CLEARING A SET
# =========================================================

temp_set = {1, 2, 3}

print("\nBefore clear():")
print(temp_set)

temp_set.clear()

print("After clear():")
print(temp_set)

# =========================================================
# SET OPERATIONS
# =========================================================

s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

# =========================================================
# UNION
# =========================================================

print("\nUnion:")

print(s2.union(s3))

# =========================================================
# INTERSECTION
# =========================================================

print("\nIntersection:")

print(s2.intersection(s3))

# =========================================================
# DIFFERENCE
# =========================================================

print("\nDifference:")

print(s2.difference(s3))

print(s3.difference(s2))

# =========================================================
# SYMMETRIC DIFFERENCE
# =========================================================

print("\nSymmetric Difference:")

print(s2.symmetric_difference(s3))

# =========================================================
# SUBSET AND SUPERSET
# =========================================================

s4 = {1, 2, 3}
s5 = {1, 2, 3, 4, 5}

# issubset()
print("\nSubset:")

print(s4.issubset(s5))

# issuperset()
print("\nSuperset:")

print(s5.issuperset(s4))

# =========================================================
# COMMON SET METHODS
# =========================================================

# add()      -> Adds element
# remove()   -> Removes element
# discard()  -> Removes safely
# clear()    -> Removes all elements

# =========================================================
# FROZENSET
# =========================================================

# A frozenset is an immutable version of a set.

my_frozenset = frozenset([1, 2, 3, 4, 5])

print("\nFrozenset:")

print(my_frozenset)

# =========================================================
# CHECKING TYPES
# =========================================================

print("\nChecking Types:")

print(type(my_set))

print(type(my_frozenset))

# =========================================================
# LENGTH OF SET
# =========================================================

print("\nLength of Set:")

print(len(s2))

# =========================================================
# END OF PROGRAM
# =========================================================