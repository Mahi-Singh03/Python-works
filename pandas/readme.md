# Introduction to Pandas

---

# What is Pandas?

Pandas is one of the most powerful and popular Python libraries used for:

* Data Analysis
* Data Manipulation
* Data Cleaning
* Data Exploration
* Data Processing

Pandas makes it easy to work with structured data such as:

* CSV Files
* Excel Files
* Databases
* JSON Files
* API Responses

---

# What Does Pandas Mean?

The name **Pandas** comes from:

```text
Panel Data
```

and

```text
Python Data Analysis
```

It was created to make data analysis easier and more efficient in Python.

---

# Why Was Pandas Created?

Python provides basic data structures such as:

* Lists
* Tuples
* Dictionaries
* Sets

These are useful for general programming but become difficult to manage when working with large datasets.

Example:

```python
students = [
    ["Mahi", 90],
    ["Rahul", 85],
    ["Priya", 95]
]
```

As data grows larger, operations such as:

* Filtering
* Sorting
* Grouping
* Cleaning
* Statistical Analysis

become difficult.

Pandas solves these problems by providing specialized data structures and tools.

---

# Why Learn Pandas?

Pandas is one of the most important libraries in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Data Analytics
* Business Intelligence
* Financial Analysis

Most real-world datasets are processed using Pandas before being used in Machine Learning models.

---

# Real-World Applications of Pandas

Pandas is used in:

## Data Science

Analyzing and understanding large datasets.

---

## Machine Learning

Preparing and cleaning data before training models.

---

## Artificial Intelligence

Transforming raw data into machine-readable formats.

---

## Finance

Stock market analysis and forecasting.

---

## Business Analytics

Generating reports and insights.

---

## Research

Processing and analyzing experimental data.

---

# Pandas and NumPy

Pandas is built on top of NumPy.

Relationship:

```text
Python
   ↓
NumPy
   ↓
Pandas
```

NumPy provides:

* Fast arrays
* Mathematical operations

Pandas builds on NumPy and provides:

* Tables
* Rows
* Columns
* Data analysis tools

---

# Core Data Structures in Pandas

Pandas mainly provides two important data structures.

---

# 1. Series

A Series is a one-dimensional labeled array.

Example:

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

Think of a Series as a single column in a spreadsheet.

---

# 2. DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

Example:

```python
import pandas as pd

data = {
    "Name": ["Mahi", "Rahul"],
    "Marks": [90, 85]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Marks
0   Mahi     90
1  Rahul     85
```

A DataFrame is the most commonly used Pandas object.

---

# Why DataFrames Are Powerful

With DataFrames you can:

* Add rows
* Delete rows
* Add columns
* Filter data
* Sort data
* Analyze data
* Export data

using simple commands.

---

# Common File Formats Supported by Pandas

Pandas can read and write:

| Format        | Supported |
| ------------- | --------- |
| CSV           | Yes       |
| Excel         | Yes       |
| JSON          | Yes       |
| SQL Databases | Yes       |
| HTML Tables   | Yes       |
| XML           | Yes       |
| Parquet       | Yes       |

---

# Example: Reading a CSV File

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
```

This single command can load thousands of rows of data.

---

# Key Features of Pandas

---

## Fast Data Processing

Handles large datasets efficiently.

---

## Data Cleaning

Remove:

* Missing values
* Duplicate values
* Incorrect data

---

## Data Transformation

Convert data into useful formats.

---

## Data Analysis

Generate statistics quickly.

---

## Data Visualization Support

Works well with:

* Matplotlib
* Plotly
* Seaborn

---

## File Handling

Read and write various file formats easily.

---

# Example of Data Analysis

```python
import pandas as pd

data = {
    "Marks": [90, 85, 95, 80]
}

df = pd.DataFrame(data)

print(df["Marks"].mean())
```

Output:

```text
87.5
```

Pandas can calculate statistics with a single command.

---

# Pandas vs Python Lists

## Python List

```python
marks = [90, 85, 95, 80]
```

Basic storage only.

---

## Pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "Marks": [90, 85, 95, 80]
})
```

Provides:

* Filtering
* Sorting
* Statistics
* Visualization Support
* File Handling

---

# Pandas Learning Roadmap

---

# Module 1: Introduction

Topics:

* What is Pandas?
* Why Pandas?
* Pandas vs NumPy
* Series and DataFrames

---

# Module 2: Installation and Setup

Topics:

* Installing Pandas
* Importing Pandas
* Checking Version

---

# Module 3: Series

Topics:

* Creating Series
* Indexing
* Slicing
* Operations

---

# Module 4: DataFrames

Topics:

* Creating DataFrames
* Accessing Rows
* Accessing Columns
* Modifying Data

---

# Module 5: Reading Data

Topics:

* read_csv()
* read_excel()
* read_json()

---

# Module 6: Data Inspection

Topics:

* head()
* tail()
* info()
* describe()

---

# Module 7: Data Cleaning

Topics:

* Missing Values
* Duplicates
* Data Type Conversion

---

# Module 8: Data Selection and Filtering

Topics:

* loc[]
* iloc[]
* Boolean Filtering

---

# Module 9: Sorting and Grouping

Topics:

* sort_values()
* groupby()

---

# Module 10: Data Analysis

Topics:

* Mean
* Median
* Mode
* Correlation

---

# Module 11: Merging and Joining

Topics:

* merge()
* join()
* concat()

---

# Module 12: Time Series Data

Topics:

* Dates
* Timestamps
* Time-based Analysis

---

# Module 13: Visualization

Topics:

* Plotting with Pandas
* Integration with Matplotlib

---

# Module 14: Pandas for Machine Learning

Topics:

* Data Preparation
* Feature Engineering
* Dataset Cleaning

---

# Advantages of Pandas

| Advantage     | Description                  |
| ------------- | ---------------------------- |
| Easy to Learn | Beginner Friendly            |
| Fast          | Optimized for large datasets |
| Powerful      | Rich functionality           |
| Flexible      | Supports many file formats   |
| AI Ready      | Essential for ML workflows   |

---

# Common Beginner Mistakes

| Mistake                        | Solution                  |
| ------------------------------ | ------------------------- |
| Forgetting to import Pandas    | Use `import pandas as pd` |
| Confusing Series and DataFrame | Learn both separately     |
| Ignoring missing values        | Always inspect data       |
| Not checking data types        | Use `df.info()`           |

---

# Summary

* Pandas is a Python library for data analysis and manipulation.
* Pandas is built on top of NumPy.
* The two main data structures are Series and DataFrame.
* Pandas can read, clean, analyze, and export data.
* Pandas is one of the most important tools in Data Science, Machine Learning, and Artificial Intelligence.
* Learning Pandas is a major step toward becoming a Data Analyst, Data Scientist, Machine Learning Engineer, or AI Engineer.

Master Pandas and you will be able to work with real-world datasets efficiently and prepare data for advanced analytics and AI applications.
