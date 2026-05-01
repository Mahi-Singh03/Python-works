#List

# list are mutable, ordered, and can contain duplicate elements
# list support slicing and indexing

# list1 =["hi", 76, 3.145, True, [9,3,9,"hi"]]
# list2 = [1,2,3,4,5,{"key1":"value1", "key2":"value2"}]
# print(list2[5]["key1"])



# print(list1)
# print(list1[4][3]) # hi

# we can access the elements of the list by using the index of the list. The index starts from 0.

# print(list1[0]) # hi

# list1[0] = "hello" # we can change the value of the list by using the index of the list.


# print(list1) # ['hello', 76, 3.145, True, [9, 3, 9, 'hi']]




# add elements to the list by using the append() method.

# list1 = ["hi", 76, 3.145, True, [9,3,9,"hi"]]
# list1.append("hello")
# print(list1) # ['hi', 76, 3.145, True, [9, 3, 9, 'hi'], 'hello']


# we can also use the insert() method to add elements to the list at a specific index.

# list1.insert(1, "world")
# print(list1) # ['hi', 'world', 76, 3.145, True, [9, 3, 9, 'hi'], 'hello']


# we can also use the extend() method to add elements to the list from another list.
# list2 = ["foo", "bar"]
# list1.extend(list2)
# print(list1) # ['hi', 'world', 76, 3.145, True, [9, 3, 9, 'hi'], 'hello', 'foo', 'bar']


# we can also use the + operator to concatenate two lists.
list3 = list1 + list2

# print(list3) # ['hi', 'world', 76, 3.145, True, [9, 3, 9, 'hi'], 'hello', 'foo', 'bar', 'foo', 'bar']



# list4 = [1,2,3,4,5]

# we can also use the * operator to repeat a list multiple times.
# list5 = list4 * 3

# print(list5) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# list6 = [1,2,3,5,5]
# print(list6.sort()) # None

# list6.pop(3) # removes the element at index 3
# print(list6) # [1, 2, 3, 5]








# Tuples
# Tuples are immutable, ordered, and can contain duplicate elements
# Tuples support slicing and indexing

# tuple1 = ("hi", 76, 3.145, True, [9,3,9,"hi"])
# tuple2 = (1,2,3,4,5,{"key1":"value1", "key2":"value2"})
# print(tuple2[5]["key1"])



#methods for tuples
# we can use the count() method to count the number of occurrences of an element in a tuple.
# tuple3 = (1,2,3,4,5,1,2,3)
# print(tuple3.count(1)) # 2

some other methods for tuples are:
# index() method to find the index of the first occurrence of an element in a tuple.
# isinstance() method to check if an object is an instance of a tuple.
# len() method to find the length of a tuple.
# we can also use the + operator to concatenate two tuples.
# We can also use the * operator to repeat a tuple multiple times.
# 