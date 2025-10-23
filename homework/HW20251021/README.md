# Introduction to Pandas

## What Is Pandas?

[**Pandas**](https://pandas.pydata.org/) is a powerful open-source Python library designed for **data manipulation and analysis**. 
It provides flexible, efficient, and easy-to-use **data structures** for working with labeled and relational data — mainly through its two core objects:

- **`Series`**: a one-dimensional labeled array (similar to a column in a spreadsheet).
- **`DataFrame`**: a two-dimensional labeled data structure (similar to a table in Excel or SQL).

Pandas is built on top of **NumPy**, which provides high-performance numerical operations. 
It’s widely used in **data science**, **machine learning**, **bioinformatics**, **finance**, and **statistics**.

> Learn more at https://pandas.pydata.org/.

## Why Use Pandas?

- Read and write data from multiple formats (CSV, Excel, JSON, SQL, Parquet, etc.)
- Handle missing data and perform data cleaning efficiently.
- Perform advanced data aggregation and grouping operations.
- Merge, join, and reshape datasets easily.
- Enable vectorized operations for better performance.
- Integrate seamlessly with NumPy, Matplotlib, and scikit-learn.

## Example

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 32, 29],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

# View the DataFrame
print(df)

# Calculate the average age
print("Average Age:", df['Age'].mean())
```

## Official and Helpful Resources

- **Official documentation**: https://pandas.pydata.org/
- **User Guide**: https://pandas.pydata.org/docs/user_guide/
- **API Reference**: https://pandas.pydata.org/docs/reference/
- **10 Minutes to Pandas** (official tutorial): https://pandas.pydata.org/docs/user_guide/10min.html
- **Pandas YouTube tutorials**: https://www.youtube.com/c/CoreySchafer
- **Book**: *Python for Data Analysis* by Wes McKinney (the creator of Pandas)

# Instructions for Pandas Homework — Week of October 21, 2025

## Overview

You are receiving today, **October 21**, a set of materials for our Pandas lesson. 
These materials include:

1. A **README.md** file 
2. **Three numbered Markdown files** (each containing a different Pandas exercise)

These materials together form your **homework assignment**, which is due by the **beginning of class on Thursday, October 23**.

## What You Need to Do

### Step 1. Read the README File

Start by carefully reading this **README.md** file.

It introduces **Pandas**, explains what it is used for, and includes links to important documentation and resources.

### Step 2. Complete the Three Markdown Exercises
Each numbered Markdown file corresponds to a separate project:

- **Exercise 1:** Introduction to Pandas 
- **Exercise 2:** Analyzing Bioinformatics Data with Pandas 
- **Exercise 3:** Data Cleaning and Summarization with Pandas 

For each one, you should:
1. Read the Markdown file carefully. 
2. Create a **Python project** that executes the steps and ideas described in that Markdown file. 
3. Make sure your project works end to end — from reading or creating data, to cleaning, analyzing, and printing results.

## Programming Requirements

Your Python projects **must not** be just copy-and-paste code from the Markdown files. 
Instead, you are expected to:

- Include a **shebang line** (`#!/usr/bin/env python3`)
- Include a **guard statement** (`if __name__ == "__main__":`)
- Add **comments** and **docstrings**
- Use **classes** where appropriate 
- Optionally create **modules** to organize your code (recommended for practice)
- Ensure your code runs properly inside a **conda environment**

## Working Environment

- **Mac or Linux users:** run your scripts in the **terminal**. 
- **Windows users:** use the **Windows Subsystem for Linux (WSL)** terminal.

Each of the three exercises should be a **separate, self-contained Python project**.  Your scripts should be tested and executable within your conda environment.

## Deliverables

When you finish:
1. You should have at least **three working Python projects**. 
2. You may have answered written questions inside the Markdown files directly (some exercises include them). 
3. Compress all your work — including your **Python scripts** and **Markdown files** — into a **single ZIP file**.

Upload that ZIP file to **Canvas** by the **start of class on Thursday, October 23**.

## Summary Checklist

- Read the README.md first 
- Complete all three Pandas exercises 
- Write well-structured Python3 code with comments and docstrings 
- Use guard statements, classes, and (optionally) modules 
- Run your projects inside a conda environment 
- Answer any written questions in the Markdown files 
- Zip everything and submit on Canvas by the due date


### Due Date
**Thursday, October 23 — Beginning of Class.**