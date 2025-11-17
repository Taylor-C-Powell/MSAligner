#! /usr/bin/env python3

import pandas as pd

# Create the DataFrame
data = {
    'Heart': [5.2, 3.3, 7.1, 4.5, 2.8],
    'Liver': [4.8, None, 6.5, 4.1, 2.5],
    'Brain': [6.1, 3.7, 8.2, 5.3, 3.0]
}

genes = ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS']

df = pd.DataFrame(data, index=genes)
print(df)

df['Mean'] = df.mean(axis=1)
print(df)

max_gene = df['Brain'].idxmax()
print("Most expressed gene in Brain:", max_gene)
