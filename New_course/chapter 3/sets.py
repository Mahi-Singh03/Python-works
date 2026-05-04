# set
# A set is an unordered collection of unique elements. Sets are mutable, meaning you can change their contents after they are created.

# my_set = {1, 2, 3, 4, 5}
# print(my_set)

# # # Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.
# my_set.add(3)  # This will not add 3 to the set because it is already present.
# print(my_set)  # {1, 2, 3, 4, 5}

# # Sets are unordered, which means that the elements do not have a specific order. When you print a set, the order of the elements may be different each time.
s1={True, False, True, False, 1, 0,9, 1, 0, "mahi", "mahi"}
print(s1)  
print(1==True)  # True








#  union
s2={1, 2, 3, 4, 5}
s3={4, 5, 6, 7, 8}

print(s2.union(s3))  # {1, 2, 3, 4, 5, 6, 7, 8}




# intersection

print(s2.intersection(s3))  # {4, 5}



# difference

print(s2.difference(s3))  # {1, 2, 3}
print(s3.difference(s2))  # {6, 7, 8}



# symmetric difference

print(s2.symmetric_difference(s3))  # {1, 2, 3, 6, 7, 8}



# subset and superset

s4={1, 2, 3}
s5={1, 2, 3, 4, 5}  

print(s4.issubset(s5))  # True
print(s5.issuperset(s4))  # True


# methods of set
# add() - Adds an element to the set.
# remove() - Removes an element from the set. Raises a KeyError if the element is not present.
# discard() - Removes an element from the set if it is present. Does not raise an
# error if the element is not present.
# clear() - Removes all elements from the set.


# frozenset
# A frozenset is an immutable version of a set. Once a frozenset is created, you cannot change its contents. Frozensets are hashable, which means they can be used as keys in a dictionary or as elements of another set.
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # frozenset({1, 2, 3, 4, 5})



