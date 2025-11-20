#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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

df_merged = pd.merge(df_expression, df_mutations, on='Gene')
print(df_merged)

df_merged['Mean_Expression'] = df_merged[['Expression_Heart', 'Expression_Liver', 'Expression_Brain']].mean(axis=1)

correlation_matrix = df_merged[['Expression_Heart', 'Expression_Liver', 'Expression_Brain', 'Mean_Expression', 'Mutations']].corr()
print(correlation_matrix)

plt.scatter(df_merged['Mean_Expression'], df_merged['Mutations'])
plt.xlabel('Mean Expression (log₂)')
plt.ylabel('Mutation Count')
plt.title('Correlation Between Expression and Mutation Frequency')
plt.show()

df_merged.to_csv("gene_expression_mutations.csv", index=False)