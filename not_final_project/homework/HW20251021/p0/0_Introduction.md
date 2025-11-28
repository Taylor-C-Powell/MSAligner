# Difference Between a DataFrame and a Series in Pandas

## 1. Pandas Series

A **`Series`** is a **one-dimensional** labeled array that can hold any data type (integers, floats, strings, Python objects, etc.). 
It has two main components:

- **Values**: the actual data.
- **Index**: labels that identify each element.

### Example

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

Expected output:

```plain
a    10
b    20
c    30
dtype: int64
```

> Think of a Series as **one column** of data — similar to a single column in an Excel sheet.

## 2. Pandas DataFrame

A **DataFrame** is a **two-dimensional** labeled data structure with rows and columns.

It can be thought of as a **collection of Series objects** that share the same index.

### Example

```python
import pandas as pd

df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
}, index=['a', 'b', 'c'])

print(df)
```

Expected output:

```plain
    A   B
a  10  40
b  20  50
c  30  60
```

> Think of a DataFrame as a **table** — rows and columns, like an Excel sheet or SQL table.

### Summary

- A **DataFrame** is essentially a **container for multiple Series** objects.

- Each column in a DataFrame is a Series.

## 3. Exercise Using Pandas with Bioinformatics Data

Use the information in this section to create your own Python project and make sure that you can execute it from the command line.

### Goal

Learn how to use a **Pandas DataFrame** to analyze simple bioinformatics data — in this case, **gene expression levels** across different samples.

### Scenario

You are studying the expression of five genes (`BRCA1`, `TP53`, `EGFR`, `MYC`, `KRAS`) across three tissue samples (`Heart`, `Liver`, `Brain`).

The expression data (in arbitrary units) is as follows:

| Gene  | Heart | Liver | Brain |
| ----- | ----- | ----- | ----- |
| BRCA1 | 5.2   | 4.8   | 6.1   |
| TP53  | 3.3   | 2.9   | 3.7   |
| EGFR  | 7.1   | 6.5   | 8.2   |
| MYC   | 4.5   | 4.1   | 5.3   |
| KRAS  | 2.8   | 2.5   | 3.0   |

### Step 1. Create a DataFrame

```python
import pandas as pd

# Create the DataFrame
data = {
    'Heart': [5.2, 3.3, 7.1, 4.5, 2.8],
    'Liver': [4.8, 2.9, 6.5, 4.1, 2.5],
    'Brain': [6.1, 3.7, 8.2, 5.3, 3.0]
}

genes = ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS']

df = pd.DataFrame(data, index=genes)
print(df)
```

### Step 2. Perform Basic Analysis

Calculate the mean expression per gene:

```python
df['Mean'] = df.mean(axis=1)
print(df)
```

Find the most highly expressed gene in the Brain:

```python
max_gene = df['Brain'].idxmax()
print("Most expressed gene in Brain:", max_gene)
```

Calculate fold-change between Brain and Liver:

```python
max_gene = df['Brain'].idxmax()
print("Most expressed gene in Brain:", max_gene)
```

Expected output:

```plain
        Heart  Liver  Brain  Mean  FoldChange_Brain_vs_Liver
BRCA1     5.2    4.8    6.1  5.37                     1.271
TP53      3.3    2.9    3.7  3.30                     1.276
EGFR      7.1    6.5    8.2  7.27                     1.262
MYC       4.5    4.1    5.3  4.63                     1.293
KRAS      2.8    2.5    3.0  2.77                     1.200
```

### Step 3. Reflection

Answer the following questions:

1. What happens if one tissue has missing data for some genes?

If an entry contains no data, denoted by a 'None' variable, then that variable is represented by a NaN symbol, and the value is not included in mathematical or statistical calculations.

If an entry contains no data, denoted by a '0' value, then that variable is represented by an integer value of 0, and is included in amthematical and statistical calculations.

2. How could you normalize these expression values across samples?
3. How could you use `df.to_csv("gene_expression.csv")` to export the results?

## Learning Outcome

After completing this exercise, you should be able to:

- Create and manipulate a **Pandas DataFrame**
- Calculate **summary statistics** (mean, fold-change)
- Identify **max/min values** in columns
- Export results for further bioinformatics analysis (e.g., clustering or plotting)