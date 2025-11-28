# Merging Two Bioinformatics DataFrames and Performing Correlation Analysis

## Goal

Learn how to:
1. **Merge** two related bioinformatics datasets using `pandas.merge()`.
2. **Analyze correlations** between numeric variables using `DataFrame.corr()`.

## Scenario

You have two datasets:

1. **Gene Expression Data** — Expression levels (log₂ normalized counts) for five genes.  
2. **Mutation Data** — Number of mutations observed in the same genes.

Your task is to **combine** these datasets and test whether genes with higher expression levels also tend to have more mutations.

## Step 1. Create the DataFrames

```python
import pandas as pd

# Gene expression data (e.g., RNA-seq normalized counts)
expression_data = {
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS'],
    'Expression_Heart': [5.2, 3.3, 7.1, 4.5, 2.8],
    'Expression_Liver': [4.8, 2.9, 6.5, 4.1, 2.5],
    'Expression_Brain': [6.1, 3.7, 8.2, 5.3, 3.0]
}
df_expression = pd.DataFrame(expression_data)

# Mutation data (e.g., from variant calling)
mutation_data = {
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS'],
    'Mutations': [12, 8, 15, 10, 6]
}
df_mutations = pd.DataFrame(mutation_data)
```

## Step 2. Merge the DataFrames

We’ll merge them by the **`Gene`** column.

```python
df_merged = pd.merge(df_expression, df_mutations, on='Gene')
print(df_merged)
```

**Expected Output:**
```
    Gene  Expression_Heart  Expression_Liver  Expression_Brain  Mutations
0  BRCA1               5.2               4.8               6.1         12
1   TP53               3.3               2.9               3.7          8
2   EGFR               7.1               6.5               8.2         15
3    MYC               4.5               4.1               5.3         10
4   KRAS               2.8               2.5               3.0          6
```

## Step 3. Compute Mean Expression

Add a column with the average expression across all tissues.

```python
df_merged['Mean_Expression'] = df_merged[['Expression_Heart', 'Expression_Liver', 'Expression_Brain']].mean(axis=1)
```

## Step 4. Perform Correlation Analysis

Use the `corr()` function to test for relationships among numeric variables.

```python
correlation_matrix = df_merged[['Expression_Heart', 'Expression_Liver', 'Expression_Brain', 'Mean_Expression', 'Mutations']].corr()
print(correlation_matrix)
```

## Step 5. Interpret the Results

Write your own interpretation of the results.

> It seems that mean expression and the number of mutations are positively correlated variables. This means that, as one increases, the other is likely to increase. 

## Bonus Challenge

### Part 1. Plot the relationship between `Mean_Expression` and `Mutations`

```python
import matplotlib.pyplot as plt

plt.scatter(df_merged['Mean_Expression'], df_merged['Mutations'])
plt.xlabel('Mean Expression (log₂)')
plt.ylabel('Mutation Count')
plt.title('Correlation Between Expression and Mutation Frequency')
plt.show()
```

### Part 2. Export your final merged dataset

```python
df_merged.to_csv("gene_expression_mutations.csv", index=False)
```

## Learning Outcome

After completing this exercise, students should be able to:

- Merge multiple bioinformatics data sources using Pandas. 
- Compute derived variables (e.g., mean expression). 
- Use correlation analysis to identify relationships between biological features. 
- Visualize and export integrated datasets for downstream interpretation.
