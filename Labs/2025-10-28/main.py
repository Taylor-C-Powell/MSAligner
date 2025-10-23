#!/usr/bin/env python3

import pandas as pd
from typing import Any
from sequence_functions.read import read_fasta
from sequence_functions.part2_nuc_to_aa import nuc_to_aa
from sequence_functions.part1_MaxNucCounts import *

class Biopython_demo:
    """
    This class demonstrates reading a FASTA file and counting nucleotides and
    converting nucleotide sequences to amino acid sequences.
    It uses pandas and numpy for data manipulation.
    """

    def __init__(self, fasta_file: str="sequences.fasta", output_file: str="output.csv") -> None:
        """
        Initialize the runner with a fasta file.

        Parameters
        ----------
        fasta_file : str
            Path to the input fasta file containing sequences.
        """
        self.fasta_file = fasta_file
        data = read_fasta(self.fasta_file)
        self.output_file = output_file

    def find_max_nuc_counts(self) -> list:
        """
        Find maximum nucleotide counts from the sequences.
        """
        fasta_sequences = parse_fasta(self.fasta_file)
        fasta_dataframe = pd.DataFrame.from_dict(fasta_sequences, orient='index').reset_index()
        fasta_dataframe.columns = ['Sequence_Name', 'Sequence']

        # Count nucleotides
        nucleotide_counts = {
            'A': fasta_dataframe['Sequence'].str.count('A').sum(),
            'T': fasta_dataframe['Sequence'].str.count('T').sum(),
            'G': fasta_dataframe['Sequence'].str.count('G').sum(),
            'C': fasta_dataframe['Sequence'].str.count('C').sum()
        }

        max_count = max(nucleotide_counts.values())
        max_nucleotides = [nuc for nuc, count in nucleotide_counts.items() if count == max_count]

        return max_nucleotides, max_count
    
    def nuc_to_aa(self) -> str:
        """
        Convert nucleotide sequences to amino acid sequences.
        """
        fasta_sequences = parse_fasta(self.fasta_file)
        amino_acid_sequences = {}
        for seq_name, nuc_sequence in fasta_sequences.items():
            amino_acid_sequences[seq_name] = nuc_to_aa(nuc_sequence)
        return amino_acid_sequences


def main() -> None:
    """
    Main function to execute the workflow.

    Returns
    -------
    None
    """
    import sys
    runner = Biopython_demo(fasta_file="Labs/2025-10-28/sequences.fasta", output_file="Labs/2025-10-28/output.csv")
    sequences = parse_fasta(runner.fasta_file)
    sys.stdout.write("Part1: Finding Maximum Nucleotide Counts\n")
    for seq in sequences:
        sys.stdout.write(f"The most frequent nucleotide from {seq} is {runner.find_max_nuc_counts()[0]} with a count of {runner.find_max_nuc_counts()[1]}\n")
    sys.stdout.write("Part2: Converting nuclotide sequences to amino acid sequences\n")
    for seq in sequences:
        sys.stdout.write(f"The amino acid sequence for {seq} is {runner.nuc_to_aa()}\n")


if __name__ == "__main__":
    main()