# =========================================================
# DICTIONARIES IN PYTHON
# =========================================================

# A dictionary is a collection of key-value pairs.

# Features of Dictionaries:
# 1. Mutable
# 2. Ordered
# 3. Keys must be unique
# 4. Stores data in key-value format

# =========================================================
# CREATING A DICTIONARY
# =========================================================

information = {
    "name": "mahi singh",
    "age": 25,
    "gender": "male",
    "hobbies": ["coding", "gaming", "traveling"],
    "education": {
        "degree": "Bachelor's in Computer Science",
        "university": "Punj University",
        "graduation_year": 2024
    }
}

print("Complete Dictionary:")
print(information)

# =========================================================
# ACCESSING VALUES
# =========================================================

print("\nAccessing Values:")

print(information["name"])

print(information["age"])

# =========================================================
# ACCESSING NESTED VALUES
# =========================================================

print("\nAccessing Nested Dictionary Values:")

print(information["education"]["degree"])

print(information["education"]["university"])

print(information["education"]["graduation_year"])

# =========================================================
# ACCESSING LIST VALUES INSIDE DICTIONARY
# =========================================================

print("\nAccessing List Values:")

print(information["hobbies"][0])

print(information["hobbies"][1])

# =========================================================
# DICTIONARY METHODS
# =========================================================

# keys()
print("\nUsing keys():")

print(information.keys())

# ---------------------------------------------------------

# values()
print("\nUsing values():")

print(information.values())

# ---------------------------------------------------------

# items()
print("\nUsing items():")

print(information.items())

# =========================================================
# UPDATING VALUES
# =========================================================

print("\nUpdating Existing Value:")

information.update({"name": "Mahi Singh"})

print(information)

# =========================================================
# ADDING NEW KEY-VALUE PAIR
# =========================================================

print("\nAdding New Key-Value Pair:")

information.update({"nationality": "Indian"})

print(information)

# =========================================================
# get() METHOD
# =========================================================

# get() safely returns values.

print("\nUsing get():")

print(information.get("name"))

# If key does not exist,
# get() returns None.

print(information.get("name1"))

# =========================================================
# KEY ERROR EXAMPLE
# =========================================================

# This would produce an error:
# print(information["name1"])

# =========================================================
# pop() METHOD
# =========================================================

print("\nUsing pop():")

information.pop("gender")

print(information)

# =========================================================
# copy() METHOD
# =========================================================

print("\nUsing copy():")

copied_information = information.copy()

print(copied_information)

# =========================================================
# clear() METHOD
# =========================================================

print("\nUsing clear():")

temp_dict = {"a": 1, "b": 2}

print("Before clear():")
print(temp_dict)

temp_dict.clear()

print("After clear():")
print(temp_dict)

# =========================================================
# LENGTH OF DICTIONARY
# =========================================================

print("\nLength of Dictionary:")

print(len(information))

# =========================================================
# CHECKING TYPE
# =========================================================

print("\nChecking Type:")

print(type(information))

# =========================================================
# NESTED DICTIONARY
# =========================================================

student = {
    "name": "Mahi",
    "marks": {
        "python": 90,
        "java": 85
    }
}

print("\nNested Dictionary:")

print(student)

print(student["marks"]["python"])

# =========================================================
# LOOPING THROUGH DICTIONARY
# =========================================================

print("\nLooping Through Dictionary:")

for key, value in information.items():
    print(key, ":", value)

# =========================================================
# END OF PROGRAM
# =========================================================