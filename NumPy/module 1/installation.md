# Installing NumPy

---

# Prerequisites

Before installing NumPy, make sure Python is installed.

Check Python version:

```bash
python --version
```

or

```bash
python3 --version
```

Example:

```text
Python 3.12.2
```

---

# What is pip?

pip is Python's package manager.

It is used to install external libraries.

Example:

```bash
pip install package_name
```

---

# Checking pip Installation

Run:

```bash
pip --version
```

Example Output:

```text
pip 24.0
```

---

# Installing NumPy

Install NumPy using:

```bash
pip install numpy
```

---

# Installation Process

After running:

```bash
pip install numpy
```

pip will:

1. Download NumPy
2. Install NumPy
3. Configure the package

Example:

```text
Successfully installed numpy
```

---

# Verify Installation

Open Python:

```bash
python
```

Then run:

```python
import numpy as np

print(np.__version__)
```

Example Output:

```python
2.3.0
```

---

# Using NumPy in VS Code

Create:

```text
test.py
```

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

Run:

```bash
python test.py
```

Output:

```python
[1 2 3]
```

---

# Upgrading NumPy

To install the latest version:

```bash
pip install --upgrade numpy
```

---

# Uninstalling NumPy

To remove NumPy:

```bash
pip uninstall numpy
```

---

# Common Installation Errors

## Error 1

```text
pip is not recognized
```

### Solution

Install Python and ensure:

```text
Add Python to PATH
```

was selected during installation.

---

## Error 2

```text
ModuleNotFoundError: No module named 'numpy'
```

### Solution

Install NumPy:

```bash
pip install numpy
```

---

## Error 3

Multiple Python Versions

### Solution

Use:

```bash
python -m pip install numpy
```

or

```bash
python3 -m pip install numpy
```

---

# Best Practice

Always install packages inside a virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Then install:

```bash
pip install numpy
```

---

# Summary

* NumPy is installed using pip.
* Use `pip install numpy`.
* Verify installation using `np.__version__`.
* Upgrade with `pip install --upgrade numpy`.
* Remove using `pip uninstall numpy`.
* Virtual environments are recommended for professional projects.
