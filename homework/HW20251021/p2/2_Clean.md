# Cleaning and Summarizing a Viral Sequence Database Using Pandas

## Goal

In this exercise, you will practice **data cleaning and summarization** using **Pandas**. You will work with a **fictional viral sequence dataset** representing samples from a made-up virus called **“Auroravirus‑9”**.

This dataset contains information about each sequence, including where it was collected, sequencing site, data repository link, and quality score.

The dataset intentionally includes **duplicate rows** and **missing values**, mimicking real‑world bioinformatics data problems.

## Step 1. Create the Dataset

```python
import pandas as pd

data = {
    'Sequence_ID': [
        'AURV9_001', 'AURV9_002', 'AURV9_003', 'AURV9_004',
        'AURV9_005', 'AURV9_006', 'AURV9_002', 'AURV9_007', 'AURV9_008',
        'AURV9_009', 'AURV9_010', 'AURV9_003'
    ],
    'Locality': [
        'São Paulo, Brazil', 'Tokyo, Japan', 'Nairobi, Kenya', 'Berlin, Germany',
        'Cape Town, South Africa', None, 'Tokyo, Japan', 'Reykjavik, Iceland',
        'Toronto, Canada', 'Lima, Peru', 'Delhi, India', 'Nairobi, Kenya'
    ],
    'Sequenced_At': [
        'USP Genomics Core', 'Riken Institute', 'Kenya BioLab', 'Max Planck Institute',
        'UCT Genomics Center', 'Unknown', 'Riken Institute', 'Arctic Viral Lab',
        'Toronto Genomics Hub', None, 'Delhi Biotech Center', 'Kenya BioLab'
    ],
    'Repository_Link': [
        'https://db.aurora.org/AURV9_001', 'https://db.aurora.org/AURV9_002',
        'https://db.aurora.org/AURV9_003', 'https://db.aurora.org/AURV9_004',
        None, 'https://db.aurora.org/AURV9_006', 'https://db.aurora.org/AURV9_002',
        'https://db.aurora.org/AURV9_007', 'https://db.aurora.org/AURV9_008',
        'https://db.aurora.org/AURV9_009', 'https://db.aurora.org/AURV9_010',
        'https://db.aurora.org/AURV9_003'
    ],
    'Quality(%)': [99.8, 97.2, 92.5, 96.1, 88.9, 100.0, 97.2, 94.3, 99.5, None, 91.8, 92.5]
}

df = pd.DataFrame(data)
print(df)
```

## Step 2. Identify and Remove Duplicates

```python
# Count duplicates
print("Number of duplicates:", df.duplicated().sum())

# Remove duplicated rows
df = df.drop_duplicates()
```

## Step 3. Handle Missing Data

```python
# View missing values
print(df.isnull().sum())

# Option 1: Drop rows with missing 'Quality(%)' values
df = df.dropna(subset=['Quality(%)'])

# Option 2: Replace missing text fields with placeholders
df = df.fillna({'Locality': 'Unknown', 'Sequenced_At': 'Unknown', 'Repository_Link': 'Unavailable'})
```

## Step 4. Rank and Filter Sequences by Quality

```python
# Rank by sequence quality (descending order)
df = df.sort_values(by='Quality(%)', ascending=False)

# Keep only high-quality sequences (≥ 95%)
df_high_quality = df[df['Quality(%)'] >= 95]
print(df_high_quality)
```

## Step 5. Generate Summary Statistics

```python
total_sequences = df_high_quality['Sequence_ID'].nunique()
total_places = df_high_quality['Locality'].nunique()

print(f"Total unique high-quality sequences: {total_sequences}")
print(f"Total unique localities represented: {total_places}")
```

## Example Output

```
Total unique high-quality sequences: 6
Total unique localities represented: 6
```

## Step 6. Optional Visualization

```python
import matplotlib.pyplot as plt

plt.barh(df_high_quality['Locality'], df_high_quality['Quality(%)'])
plt.xlabel('Sequence Quality (%)')
plt.ylabel('Locality')
plt.title('High-Quality Auroravirus‑9 Sequences by Locality')
plt.show()
```

## Learning Outcome

After completing this exercise, you should be able to:

- Identify and remove **duplicates** in a DataFrame. 
- Detect and manage **missing data**. 
- Rank and filter data based on a **numeric threshold**. 
- Compute **summary statistics** and **counts**. 
- Visualize simple quality metrics for bioinformatics datasets.
