# String in Python
# IT is a sequence of characters enclosed in single quotes, double quotes, or triple quotes. Strings are immutable, which means that once a string is created, it cannot be changed. However, we can create a new string by concatenating two or more strings.
# ITS IMMUTABLE MEANS ONCE A STRING IS CREATED, IT CANNOT BE CHANGED. HOWEVER, WE CAN CREATE A NEW STRING BY CONCATENATING TWO OR MORE STRINGS.
# EXAMPLE:

# X="mahi"
# X[0] = "M"  # This will raise an error because strings are immutable.




# # Normal string can be created by using single quotes or double quotes.
# x="mahi"  
# y='mahi'

# print(x)
# print(y)





# # Three double quotes or three single quotes can be used to create a multi-line string.
# z='''this is a string


# this is a string
# this is a string'''

# print(z)




# #Slicing of string is done by using the index of the string. The index starts from 0.

# a="mahi"
# print(a[0])  # m
# print(a[1])  # a

# # We can also use negative indexing to access the characters from the end of the string.
# print(a[-1])  # i
# print(a[-2])  # h

# # We can also use slicing to access a range of characters from the string.
# print(a[0:2])  # ma
# print(a[1:4])  # ahi

# # We can also use slicing to access the characters from the end of the string.
# print(a[-4:-2])  # ma
# print(a[-3:-1])  # ah





# #Modify Strings
# # Strings are immutable in Python, which means that we cannot change the characters of a string after it has been created. However, we can create a new string by concatenating two or more strings.
# b="hello"
# c="world"
# d=b+" "+c
# print(d)  # hello world

# # We can also use the * operator to repeat a string multiple times.
# e="ha"  
# f=e*3
# print(f)  # hahaha



# # String Methods
# # There are many built-in string methods in Python that can be used to manipulate strings. Some of the commonly used string methods are:
# g="hello world"
# print(g.upper())  # HELLO WORLD
# print(g.lower())  # hello world
# print(g.capitalize())  # Hello world
# print(g.title())  # Hello World
# print(g.strip())  # hello world
# print(g.replace("world", "mahi"))  # hello mahi
# print(g.split())  # ['hello', 'world']
# print(g.find("world"))  # 6
# print(g.count("o"))  # 2



# #F-Strings
# name="mahi"
# age=25
# print(f"Hello, my name is {name} and I am {age} years old.")  # Hello, my name is mahi and I am 25 years old.


# #escaping Characters
# h="This is a string with a single quote (') in it."
# i='This is a string with a double quote (") in it.'
# print(h)  # This is a string with a single quote (') in it.
# print(i)  # This is a string with a double quote (") in it.

# Escape Characters Examples
# 1. \'  → print a single quote
print("1. Single Quote:")
print('I\'m happy')   # I'm happy
print()


# 2. \"  → print a double quote
print("2. Double Quote:")
print("She said, \"Hello!\"")  # She said, "Hello!"

# 2. \\ → print a backslash
print("2. Backslash:")
print(' HI \\')   # \
print()


# 3. \n → new line (go to next line)
print("3. New Line:")
print('Hello\nWorld')
# Hello
# World
print()




# 5. \t → tab (space)
print("5. Tab:")
print('Hello\tWorld')   # Hello    World
print()


# 6. \b → remove one character (backspace)
print("6. Backspace:")
print('Helloo\bWorld')  # removes one 'o'
print()