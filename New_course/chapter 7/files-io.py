    # =========================================================
# FILE HANDLING (FILE I/O) IN PYTHON
# =========================================================

# File Handling allows Python programs to:
# - Create files
# - Read files
# - Write data
# - Append data
# - Delete files

# File I/O:
# Input  -> Reading from files
# Output -> Writing to files

# =========================================================
# OPENING A FILE
# =========================================================

# Syntax:
# open(filename, mode)

# Example:
# file = open("demo.txt", "r")

# =========================================================
# FILE MODES
# =========================================================

# "r"  -> Read mode
# "w"  -> Write mode
# "a"  -> Append mode
# "x"  -> Create new file
# "rb" -> Read binary file
# "wb" -> Write binary file

# =========================================================
# WRITING TO A FILE
# =========================================================

# print("WRITING TO FILE")

# file = open("mahi.txt", "w")

# file.write("Hello, this is Mahi")

# file.close()

# print("Data written successfully")

# =========================================================
# READING FROM A FILE
# =========================================================

# print("\nREADING FILE")

# file = open("mahi.txt", "r")

# content = file.read()

# print(content)

# file.close()

# =========================================================
# APPENDING DATA
# =========================================================

# print("\nAPPENDING DATA")

# file = open("mahi.txt", "a")

# file.write("\nWelcome to Python")

# file.close()

# print("Data appended successfully")

# =========================================================
# READING UPDATED FILE
# =========================================================

# print("\nREADING UPDATED FILE")

# file = open("mahi.txt", "r")

# content = file.read()

# print(content)

# file.close()

# =========================================================
# USING with STATEMENT
# =========================================================

# Best practice for file handling
# Automatically closes the file

# print("\nUSING with STATEMENT")

# with open("mahi.txt", "r") as file:

#     content = file.read()

#     print(content)

# =========================================================
# READING LINE BY LINE
# =========================================================

# print("\nREADING LINE BY LINE")

# with open("mahi.txt", "r") as file:

#     for line in file:
#         print(line.strip())

# =========================================================
# readline()
# =========================================================

# print("\nUSING readline()")

# with open("mahi.txt", "r") as file:

#     print(file.readline())

# =========================================================
# readlines()
# =========================================================

# print("\nUSING readlines()")

# with open("mahi.txt", "r") as file:

#     lines = file.readlines()

#     print(lines)

# =========================================================
# WRITING MULTIPLE LINES
# =========================================================

print("\nWRITING MULTIPLE LINES")

languages = [
    "Python\n",
    "Java\n",
    "C++\n",
    "JavaScript\n"
]

with open("mahi.txt", "w") as file:

    file.writelines(languages)

print("Multiple lines written successfully")

# # =========================================================
# # FILE POINTER FUNCTIONS
# # =========================================================

# print("\nFILE POINTER FUNCTIONS")

# with open("demo.txt", "r") as file:

#     # tell() returns current position
#     print("Current Position:", file.tell())

#     # seek() moves pointer
#     file.seek(0)

#     print("Pointer moved to beginning")

# # =========================================================
# # CHECKING IF FILE EXISTS
# # =========================================================

# print("\nCHECKING FILE EXISTENCE")

# import os

# if os.path.exists("demo.txt"):
#     print("File Exists")

# else:
#     print("File Not Found")

# # =========================================================
# # EXCEPTION HANDLING
# # =========================================================

# print("\nEXCEPTION HANDLING")

# try:

#     with open("sample.txt", "r") as file:

#         print(file.read())

# except FileNotFoundError:

#     print("File does not exist")

# # =========================================================
# # BINARY FILE EXAMPLE
# # =========================================================

# # Binary files are used for:
# # Images, videos, PDFs, audio, etc.

# print("\nBINARY FILE EXAMPLE")

# # Example only

# # with open("image.jpg", "rb") as file:
# #     data = file.read()

# # with open("copy.jpg", "wb") as file:
# #     file.write(data)

# print("Binary file example shown")

# # =========================================================
# # PRACTICAL EXAMPLE
# # STUDENT FILE
# # =========================================================

# print("\nPRACTICAL EXAMPLE")

# with open("student.txt", "w") as file:

#     file.write("Name: Mahi\n")
#     file.write("Course: Python\n")

# with open("student.txt", "r") as file:

#     print(file.read())

# # =========================================================
# # COUNTING LINES IN FILE
# # =========================================================

# print("\nCOUNTING LINES")

# with open("student.txt", "r") as file:

#     lines = file.readlines()

#     print("Total Lines:", len(lines))

# # =========================================================
# # COPYING FILE CONTENT
# # =========================================================

# print("\nCOPYING FILE CONTENT")

# with open("student.txt", "r") as source:

#     data = source.read()

# with open("student_copy.txt", "w") as destination:

#     destination.write(data)

# print("File copied successfully")

# # =========================================================
# # DELETING A FILE
# # =========================================================

# print("\nDELETING FILE")

# # Example only
# # os.remove("demo.txt")

# print("Delete example shown")

# # =========================================================
# # SUMMARY
# # =========================================================

# print("\nSUMMARY")

# print("1. open() is used to open files")
# print("2. read() reads data")
# print("3. write() writes data")
# print("4. append() adds data")
# print("5. with open() is best practice")
# print("6. Python supports text and binary files")

# # =========================================================
# # END OF PROGRAM
# # =========================================================