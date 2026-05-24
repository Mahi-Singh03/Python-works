# FILE HANDLING (FILE I/O) IN PYTHON

---

# What is File Handling?

File Handling means working with files using Python.

Python allows you to:

- Create files
- Read files
- Write data into files
- Append data to files
- Delete files
- Work with text and binary files

---

# What is File I/O?

File I/O stands for:

- Input → Reading data from a file
- Output → Writing data to a file

---

# Why Do We Use Files?

Variables store data temporarily.

When the program stops running, variable data is lost.

Files help store data permanently.

Examples:
- Notes applications
- Saving user data
- Log files
- Reading configuration files
- Data processing
- CSV and text files

---

# Opening a File

Python uses the `open()` function.

## Syntax

```python
open(filename, mode)
```

Example:

```python
file = open("demo.txt", "r")
```

---

# Parameters of open()

| Parameter | Meaning |
|----------|----------|
| filename | Name of the file |
| mode | How the file will be used |

---

# File Modes

| Mode | Meaning |
|------|----------|
| `"r"` | Read mode |
| `"w"` | Write mode |
| `"a"` | Append mode |
| `"x"` | Create new file |
| `"t"` | Text mode |
| `"b"` | Binary mode |
| `"r+"` | Read and write |

---

# Read Mode (`r`)

Used to read a file.

The file must exist.

Example:

```python
file = open("demo.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# Understanding read()

The `read()` function reads the entire file content.

Example:

```python
file.read()
```

If the file contains:

```text
Hello
Python
```

Output:

```text
Hello
Python
```

---

# Write Mode (`w`)

Used to write data into a file.

Important:
- Creates file if it does not exist
- Removes old content if file already exists

Example:

```python
file = open("demo.txt", "w")

file.write("Hello World")

file.close()
```

---

# Understanding write()

The `write()` function adds data to the file.

Example:

```python
file.write("Python")
```

---

# Append Mode (`a`)

Append means adding data at the end of the file.

Important:
- Old data is not removed

Example:

```python
file = open("demo.txt", "a")

file.write("\nNew Line")

file.close()
```

---

# Create Mode (`x`)

Creates a new file.

Example:

```python
file = open("newfile.txt", "x")
```

Important:
- Gives error if file already exists

---

# Closing a File

After working with a file, close it.

Example:

```python
file.close()
```

Why?
- Saves memory
- Prevents file corruption
- Frees system resources

---

# Using with Statement

Best practice for file handling.

Automatically closes the file.

Example:

```python
with open("demo.txt", "r") as file:
    content = file.read()

    print(content)
```

Advantages:
- Cleaner code
- Automatic file closing
- Safer

---

# Reading Line by Line

Example:

```python
with open("demo.txt", "r") as file:

    for line in file:
        print(line)
```

Useful for:
- Large files
- Processing data line by line

---

# readline()

Reads one line at a time.

Example:

```python
with open("demo.txt", "r") as file:

    print(file.readline())
```

---

# readlines()

Reads all lines and stores them in a list.

Example:

```python
with open("demo.txt", "r") as file:

    lines = file.readlines()

    print(lines)
```

Output:

```python
['Hello\n', 'Python\n']
```

---

# Writing Multiple Lines

Use `writelines()`.

Example:

```python
lines = ["Python\n", "Java\n", "C++\n"]

with open("languages.txt", "w") as file:

    file.writelines(lines)
```

---

# File Pointer

When a file is opened, Python uses a pointer.

The pointer shows the current position inside the file.

---

# tell()

Returns current file position.

Example:

```python
file.tell()
```

---

# seek()

Moves the file pointer.

Example:

```python
file.seek(0)
```

`0` means beginning of file.

---

# Checking if File Exists

Using `os.path.exists()`.

Example:

```python
import os

if os.path.exists("demo.txt"):
    print("File Exists")

else:
    print("File Not Found")
```

---

# Deleting a File

Using `os.remove()`.

Example:

```python
import os

os.remove("demo.txt")
```

Important:
- File is permanently deleted

---

# Binary Files

Binary files store non-text data.

Examples:
- Images
- Videos
- PDFs
- Audio files

---

# Binary Read Mode (`rb`)

Example:

```python
with open("image.jpg", "rb") as file:

    data = file.read()
```

---

# Binary Write Mode (`wb`)

Example:

```python
with open("copy.jpg", "wb") as file:

    file.write(data)
```

---

# Exception Handling in Files

Sometimes files may not exist.

Use `try-except` to handle errors safely.

Example:

```python
try:

    with open("demo.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")
```

---

# Practical Example 1
# Writing and Reading Data

```python
with open("student.txt", "w") as file:

    file.write("Mahi")

with open("student.txt", "r") as file:

    print(file.read())
```

---

# Practical Example 2
# Counting Lines in File

```python
with open("demo.txt", "r") as file:

    lines = file.readlines()

    print("Total Lines:", len(lines))
```

---

# Practical Example 3
# Copying File Content

```python
with open("source.txt", "r") as source:

    data = source.read()

with open("destination.txt", "w") as destination:

    destination.write(data)
```

---

# Common File Handling Methods

| Method | Purpose |
|--------|----------|
| read() | Read full file |
| readline() | Read one line |
| readlines() | Read all lines |
| write() | Write data |
| writelines() | Write multiple lines |
| close() | Close file |
| tell() | Current position |
| seek() | Move pointer |

---

# Common Errors

| Error | Reason |
|------|---------|
| FileNotFoundError | File does not exist |
| PermissionError | No permission |
| IsADirectoryError | Tried opening folder as file |

---

# Best Practices

- Always use `with open()`
- Close files properly
- Use exception handling
- Avoid overwriting important files
- Use append mode carefully

---

# Advantages of File Handling

- Permanent storage
- Easy data management
- Useful for real-world applications
- Supports text and binary files

---

# Summary

- File I/O means reading and writing files
- `open()` is used to open files
- `read()` reads data
- `write()` writes data
- `append()` adds new data
- `with open()` is best practice
- `readline()` reads one line
- `readlines()` reads all lines
- Python supports text and binary files
- Exception handling prevents crashes

---

# End of Notes
