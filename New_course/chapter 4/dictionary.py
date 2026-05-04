# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their contents after they are created.



information = {
    "name": "mahi singh",
    "age": 25,
    "gender":"male",
    "hobbies": ["coding", "gaming", "traveling"],
    "education": {
        "degree": "Bachelor's in Computer Science",
        "university": "Punj University",
        "graduation_year": 2024
    },
}


# # Accessing values
# print(information["name"])  # mahi singh
# print(information["age"])   # 25

# # Accessing nested values
# print(information["education"]["degree"])  # Bachelor's in Computer Science
# print(information["education"]["university"])  # Punj University
# print(information["education"]["graduation_year"])  # 2024

# print(information["hobbies"][0])  # coding
# print(information["hobbies"][1])  # gaming


print(information) 
print(information.keys())  # dict_keys(['name', 'age', 'gender', 'hobbies', 'education'])
print(information.values())  # dict_values(['mahi singh', 25, 'male', ['coding', 'gaming', 'traveling'], {'degree': "Bachelor's in Computer Science", 'university': 'Punj University', 'graduation_year': 2024}])
print(information.items())  # dict_items([('name', 'mahi singh'), ('age', 25), ('gender', '      male'), ('hobbies', ['coding', 'gaming', 'traveling']), ('education', {'degree': "Bachelor's in Computer Science", 'university': 'Punj University', 'graduation_year': 2024})])



information.update({"name": "Mahi Singh"})
information.update({"nationality": "Indian"})
print(information)  

print(information.get("name1"))  # None
# print(information["name1"])  # KeyError: 'name1'



# methods of dictionary
# clear() - Removes all items from the dictionary.
# copy() - Returns a shallow copy of the dictionary.
 






