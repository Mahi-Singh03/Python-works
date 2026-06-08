import numpy as np

# # Create a list
my_list = [1, 2, 3, 4, 5]
# print(f"List: {my_list}")


# # Create a NumPy array from the list
my_array = np.array(my_list)
# print(f"NumPy Array: {my_array}")


# # Check the type of the list and the array
# print(f"Type of my_list: {type(my_list)}")
# print(f"Type of my_array: {type(my_array)}")



# Perform operations on the list and the array
# Adding 1 to each element in the list (this will not work as expected)
try:
    my_list = my_list + 1
except TypeError as e:
    print(f"Error adding 1 to list: {e}")   

# Adding 1 to each element in the array (this will work as expected)
my_array = my_array + 1
print(f"NumPy Array after adding 1: {my_array}")



#Multiplying the list by 2 (this will concatenate the list with itself)
my_list = my_list * 2
print(f"List after multiplying by 2: {my_list}")

# Multiplying the array by 2 (this will multiply each element by 2)
my_array = my_array * 2
print(f"NumPy Array after multiplying by 2: {my_array}")





#speed comparison between list and array
import time

# Create a large list and a large array
large_list = list(range(1000000))
large_array = np.array(large_list)

# Measure the time taken to add 1 to each element in the list
start_time = time.time()
large_list = [x + 1 for x in large_list]
end_time = time.time()
print(f"Time taken to add 1 to each element in the list: {end_time - start_time} seconds")

# Measure the time taken to add 1 to each element in the array
start_time = time.time()
large_array = large_array + 1
end_time = time.time()
print(f"Time taken to add 1 to each element in the array: {end_time - start_time} seconds")