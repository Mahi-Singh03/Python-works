# Introduction to NumPy

---

# What is NumPy?

NumPy stands for:

```text
Numerical Python
```

NumPy is a powerful Python library used for:

* Numerical Computing
* Scientific Computing
* Mathematical Operations
* Data Analysis
* Machine Learning
* Artificial Intelligence
* Deep Learning

It provides a high-performance multidimensional array object and tools for working with arrays efficiently.

---

# Why Was NumPy Created?

Python lists are flexible but become slow when dealing with large amounts of numerical data.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

Lists work well for small datasets.

However, for:

* Thousands of values
* Millions of values
* Mathematical calculations
* Machine Learning datasets

Python lists become inefficient.

NumPy solves this problem by providing:

* Faster calculations
* Less memory usage
* Powerful mathematical operations

---

# Why Learn NumPy?

NumPy is the foundation of:

* Pandas
* Matplotlib
* Scikit-Learn
* TensorFlow
* PyTorch
* OpenCV
* SciPy

Almost every Data Science, Machine Learning, and AI library uses NumPy internally.

If you want to learn:

* Data Science
* Machine Learning
* Artificial Intelligence
* Deep Learning

NumPy is one of the first libraries you should master.

---

# Real-World Uses of NumPy

NumPy is used in:

## Data Science

Analyzing large datasets.

---

## Machine Learning

Training machine learning models.

---

## Artificial Intelligence

Processing numerical data for AI systems.

---

## Computer Vision

Working with image pixels.

Images are actually NumPy arrays.

---

## Scientific Research

Performing complex calculations.

---

## Finance

Stock analysis and forecasting.

---

## Engineering

Matrix calculations and simulations.

---

# Installing NumPy

Install NumPy using pip:

```bash
pip install numpy
```

---

# Importing NumPy

The standard convention is:

```python
import numpy as np
```

Why use:

```python
np
```

instead of:

```python
numpy
```

Because it is shorter and easier to write.

---

# Example

```python
import numpy as np

print(np.__version__)
```

---

# What Makes NumPy Special?

NumPy provides:

* Fast Arrays
* Vectorized Operations
* Mathematical Functions
* Matrix Operations
* Random Number Generation
* Statistical Functions
* Linear Algebra Tools

---

# Python Lists vs NumPy Arrays

---

## Python List

```python
numbers = [1, 2, 3]
```

---

## NumPy Array

```python
import numpy as np

numbers = np.array([1, 2, 3])
```

---

# Advantages of NumPy Arrays

| Feature                  | Python List | NumPy Array |
| ------------------------ | ----------- | ----------- |
| Speed                    | Slower      | Faster      |
| Memory Usage             | Higher      | Lower       |
| Mathematical Operations  | Limited     | Powerful    |
| Multidimensional Support | Basic       | Excellent   |
| Machine Learning Support | No          | Yes         |

---

# First NumPy Program

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

---

# Output

```python
[10 20 30 40]
```

---

# What is an Array?

An array is a collection of similar data types stored together.

Example:

```python
[10, 20, 30, 40]
```

NumPy stores arrays more efficiently than Python lists.

---

# Types of Arrays in NumPy

---

## 1-D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
```

Looks like:

```text
[1 2 3 4]
```

---

## 2-D Array

```python
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])
```

Looks like:

```text
[
 [1 2]
 [3 4]
]
```

---

## 3-D Array

```python
import numpy as np

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])
```

Used in advanced applications like:

* Images
* Videos
* Deep Learning

---

# NumPy Terminology

Understanding these terms is important.

---

## Array

Collection of elements.

Example:

```python
[1, 2, 3]
```

---

## Element

Single value inside an array.

Example:

```python
1
```

is an element.

---

## Axis

Direction along which data exists.

Example:

```text
Rows
Columns
Depth
```

---

## Shape

Number of rows and columns.

Example:

```python
(3, 4)
```

means:

```text
3 Rows
4 Columns
```

---

## Dimension

Number of axes.

Example:

```python
[1, 2, 3]
```

has:

```text
1 Dimension
```

---

# Applications of NumPy in AI

Before AI models learn, data must be converted into numbers.

Example:

```python
import numpy as np

marks = np.array([90, 80, 95, 88])
```

Machine Learning algorithms process data using NumPy arrays.

---

# NumPy Learning Roadmap

---

# Module 1: NumPy Basics

Topics:

* What is NumPy
* Installing NumPy
* Importing NumPy

---

# Module 2: Array Creation

Topics:

* np.array()
* np.zeros()
* np.ones()
* np.empty()
* np.arange()
* np.linspace()
* np.eye()

---

# Module 3: Array Properties

Topics:

* ndim
* shape
* size
* dtype
* itemsize

---

# Module 4: Indexing and Slicing

Topics:

* Accessing Elements
* Negative Indexing
* Slicing Arrays
* Multidimensional Indexing

---

# Module 5: Array Operations

Topics:

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Power Operations

---

# Module 6: Broadcasting

Topics:

* Broadcasting Rules
* Array Expansion
* Practical Examples

---

# Module 7: Reshaping Arrays

Topics:

* reshape()
* flatten()
* ravel()
* transpose()

---

# Module 8: Mathematical Functions

Topics:

* sum()
* mean()
* median()
* std()
* min()
* max()

---

# Module 9: Random Module

Topics:

* Random Numbers
* Random Arrays
* randint()
* random()
* choice()

---

# Module 10: Linear Algebra

Topics:

* Matrices
* Dot Product
* Matrix Multiplication
* Inverse Matrix
* Determinant

---

# Module 11: NumPy for Data Science

Topics:

* Data Cleaning
* Statistical Analysis
* Feature Engineering

---

# Module 12: NumPy for Machine Learning

Topics:

* Dataset Preparation
* Feature Scaling
* Mathematical Foundations

---

# Relationship Between NumPy and Pandas

```text
NumPy
   ↓
Pandas
   ↓
Data Analysis
```

Pandas is built on top of NumPy.

Understanding NumPy first makes Pandas much easier to learn.

---

# Advantages of NumPy

| Advantage         | Explanation                    |
| ----------------- | ------------------------------ |
| Fast              | Optimized for performance      |
| Memory Efficient  | Uses less memory               |
| Easy Calculations | Supports vectorized operations |
| Powerful          | Supports advanced mathematics  |
| AI Ready          | Used in ML and Deep Learning   |
| Scalable          | Handles large datasets         |

---

# Common Beginner Mistakes

| Mistake                    | Solution                  |
| -------------------------- | ------------------------- |
| Forgetting to import NumPy | Use `import numpy as np`  |
| Mixing lists and arrays    | Learn the difference      |
| Ignoring array shapes      | Always check `shape`      |
| Using loops unnecessarily  | Use vectorized operations |

---

# Summary

* NumPy stands for Numerical Python.
* It is the foundation of Data Science, Machine Learning, and AI.
* NumPy provides fast and memory-efficient arrays.
* Arrays are the core data structure in NumPy.
* NumPy supports mathematical, statistical, and matrix operations.
* Pandas, TensorFlow, PyTorch, and many other libraries depend on NumPy.
* Learning NumPy is an essential step toward becoming a Data Scientist, Machine Learning Engineer, or AI Engineer.

Master NumPy first, and the journey into Pandas, Machine Learning, and Artificial Intelligence becomes much easier.
