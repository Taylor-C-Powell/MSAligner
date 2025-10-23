#!/usr/bin/env python3

import pandas as pd
import numpy as np

fasta_file = "path/to/your/fasta_file.fasta"

def parse_fasta(fasta_file):
    with open(fasta_file, 'r') as file:
        sequences = {}
        current_seq_name = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_seq_name = line[1:]
                sequences[current_seq_name] = ""
            else:
                sequences[current_seq_name] += line
    return sequences

fasta_sequences = parse_fasta(fasta_file)
fasta_dataframe = pd.DataFrame.from_dict(fasta_sequences, orient='index').reset_index()
fasta_dataframe.columns = ['Sequence_Name', 'Sequence']

total_A = fasta_dataframe['A'].sum()
total_T = fasta_dataframe['T'].sum()
total_G = fasta_dataframe['G'].sum()
total_C = fasta_dataframe['C'].sum()

if __name__ == "__main__":
    if max(total_A, total_T, total_G, total_C) == total_A:
        max_nuc = 'A'
    elif max(total_A, total_T, total_G, total_C) == total_T:
        max_nuc = 'T'
    elif max(total_A, total_T, total_G, total_C) == total_G:
        max_nuc = 'G'
    elif max(total_A, total_T, total_G, total_C) == total_C:
        max_nuc = 'C'
    else:
        if total_A == total_T:
            max_nuc = 'A and T'
        elif total_A == total_G:
            max_nuc = 'A and G'
        elif total_A == total_C:
            max_nuc = 'A and C'
        elif total_T == total_G:
            max_nuc = 'T and G'
        elif total_T == total_C:
            max_nuc = 'T and C'
        elif total_G == total_C:
            max_nuc = 'G and C'

    print(f"The nucleotide(s) with the highest count is/are: {max_nuc}")
    