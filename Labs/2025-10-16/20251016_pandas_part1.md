# NumPy, Pandas, and MatplotLIb

## Key concepts

- Load and explore a DataFrame
- Perform simple transformations
- Run basic statistical analyses
- Create a plot

## Reading and Exploring a DataFrame

### Run the following code and register its output

```python
import pandas

# Example data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [88, 92, 85, 90, 87]
}

df = pandas.DataFrame(data)
df
```

This chunk of code has no output

## Run the following code and register its output

```python
import pandas as pd

# Example data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [88, 92, 85, 90, 87]
}

df = pd.DataFrame(data)
print(df)
```

This chunk of code outputs a table representing the data within the df Pandas dataframe

      Name  Age  Score
0    Alice   25     88
1      Bob   30     92
2  Charlie   35     85
3    Diana   40     90
4    Ethan   45     87

## Challenge: What is the average score? What is the youngest age?

Use Pandas methods to find:

- The average score
- The youngest age

The average score is 88.4
Th youngest age is 25

## Modifying a Dataframe

## Run the following code and register its output

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [88, 92, 85, 90, 87]
}

df = pd.DataFrame(data)

new_data = ['Fail', 'Pass', 'Fail', 'Pass', 'Fail']

df["Result"] = new_data

print(df)
```

This code output the df dataframe with the new data appended to it

      Name  Age  Score Result
0    Alice   25     88   Fail
1      Bob   30     92   Pass
2  Charlie   35     85   Fail
3    Diana   40     90   Pass
4    Ethan   45     87   Fail

## Now add this and register the new output

```python
# Add a new column with Pass/Fail based on Score >= 90
# print(df['Score'].apply(lambda x: 'Pass' if x >= 90 else 'Fail'))
df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 90 else 'Fail')
print(df)
```

This line of code modified the previous table to include a pass/fail column based on the person's score 

      Name  Age  Score Result
0    Alice   25     88   Fail
1      Bob   30     92   Pass
2  Charlie   35     85   Fail
3    Diana   40     90   Pass
4    Ethan   45     87   Fail

### Challenge: Add a new column that classifies people into 'Young' (<35) and 'Old' (>=35)

Add a new column that classifies people into 'Young' (<35) and 'Old' (>=35).

This is the line of code I added

```python
df['AgeGroup'] = df['Age'].apply(lambda x: 'Young' if x < 35 else 'Old')
```

And this is the resulting output:

      Name  Age  Score Result AgeGroup
0    Alice   25     88   Fail    Young
1      Bob   30     92   Pass    Young
2  Charlie   35     85   Fail      Old
3    Diana   40     90   Pass      Old
4    Ethan   45     87   Fail      Old

## Basic statistics with NumPy

## Run the following code and register the output

```python
import numpy as np

ages = df['Age'].to_numpy()
scores = df['Score'].to_numpy()

print(f"ages = {ages}")
print(f"scores = {scores}")

print("Standard Deviation of Scores:", np.std(scores))
print("Mean Age:", np.mean(ages))
```

Adding these lines to the previous code block results in this output:

      Name  Age  Score Result AgeGroup
0    Alice   25     88   Fail    Young
1      Bob   30     92   Pass    Young
2  Charlie   35     85   Fail      Old
3    Diana   40     90   Pass      Old
4    Ethan   45     87   Fail      Old
ages = [25 30 35 40 45]
scores = [88 92 85 90 87]
Standard Deviation of Scores: 2.416609194718914
Mean Age: 35.0

### Challenge: What is the correlation between Age and Score?

Use`np.corrcoef` to find the correlation.

After adding code to find the correlation coefficient between Age and Score, here is the resulting output:

      Name  Age  Score Result AgeGroup
0    Alice   25     88   Fail    Young
1      Bob   30     92   Pass    Young
2  Charlie   35     85   Fail      Old
3    Diana   40     90   Pass      Old
4    Ethan   45     87   Fail      Old
ages = [25 30 35 40 45]
scores = [88 92 85 90 87]
Standard Deviation of Scores: 2.416609194718914
Mean Age: 35.0
Correlation Coefficient between Age and Score: [[ 1., -0.23408229]
 [-0.23408229, 1.]]

## Plotting with Matplotlib

## Run the following code and register its output

```python
import matplotlib.pyplot as plt

plt.plot(df['Age'], df['Score'], marker='o')
plt.title('Score by Age')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.show()
```

### Challenge: Create a bar plot showing how many students passed vs failed

Create a bar plot showing how many students passed vs failed.