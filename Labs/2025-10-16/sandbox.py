import pandas as pd
from matplotlib import pyplot as plt

# Example data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [88, 92, 85, 90, 87]
}

df = pd.DataFrame(data)

# Add a new column with Pass/Fail based on Score >= 90
# print(df['Score'].apply(lambda x: 'Pass' if x >= 90 else 'Fail'))
df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 90 else 'Fail')

# Add a new column that classifies people into 'Young' (<35) and 'Old' (>=35).
df['AgeGroup'] = df['Age'].apply(lambda x: 'Young' if x < 35 else 'Old')

print(df)

import numpy as np

ages = df['Age'].to_numpy()
scores = df['Score'].to_numpy()

print(f"ages = {ages}")
print(f"scores = {scores}")

print("Standard Deviation of Scores:", np.std(scores))
print("Mean Age:", np.mean(ages))
print("Correlation Coefficient between Age and Score:", np.corrcoef(ages, scores))



plt.plot(df['Age'], df['Score'], marker='o')
plt.title('Score by Age')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.show()

counts = df['Result'].value_counts()
plt.bar(counts.index, counts.values, color='skyblue')
plt.title('Scores of Individuals')
plt.xlabel('Result')
plt.ylabel('Count')
plt.show()
