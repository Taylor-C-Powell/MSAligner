#!/usr/bin/env python3
"""
Script to calculate normalized per-position variability from a sequence alignment.

This script reads a FASTA alignment file, stores sequences in a dictionary,
and computes variability at each alignment position using NumPy.

Variability is normalized so that:
- The least variable positions (no variation) = 0
- The most variable positions (maximum variation observed) = 1
"""

import argparse
import numpy as np
import sys
from typing import Dict, List


class Alignment:
    """
    A class to represent a sequence alignment.

    Attributes
    ----------
    seq_dict : Dict[str, str]
        Dictionary of sequences, with IDs as keys and sequences as values.
    """

    def _init_(self, filepath: str) -> None:
        """
        Initialize the Alignment by reading sequences from a FASTA file.

        Parameters
        ----------
        filepath : str
            Path to the FASTA alignment file.
        """
        seq_dict = self._read_fasta(filepath)

    def _read_fasta(self, filepath: str) -> Dict[str, str]:
        """
        Read a FASTA file and return a dictionary of sequences.

        Parameters
        ----------
        filepath : str
            Path to the FASTA alignment file.

        Returns
        -------
        Dict[str, str]
            Dictionary with sequence IDs as keys and sequences as values.
        """
        seq_dict: Dict[str, str] = {}
        with open(filepath, "r") as f:
            seq_id = None
            seq_chunks: List[str] = []
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    if seq_id:
                        seq_dict[seq_id] = "".join(seq_chunks)
                    seq_id = line[1:]
                    seq_chunks = []
                else:
                    seq_chunks.append(line)
                    if seq_id:
                        seq_dict[seq_id] = "".join(seq_chunks)
        return seq_dict

    def to_numpy_array(self) -> np.ndarray:
        """
        Convert the alignment dictionary into a NumPy array.

        Returns
        -------
        np.ndarray
            Array of shape (num_sequences, alignment_length).
        """
        sequences = self.seq_dict.values()
        arr = np.array([seq for seq in sequences])
        return arr


    def calculate_variability(self, arr: np.ndarray) -> np.ndarray:
        """
        Calculate normalized variability for each alignment column.

        Parameters
        ----------
        arr : np.ndarray
            Alignment array (num_sequences x alignment_length).

        Returns
        -------
        np.ndarray
            Normalized variability scores (range 0 to 1) for each position.
        """
        variation = []
        for col in arr.T:  # iterate over columns
            bases, counts = np.unique(col, return_counts=True)
            variation.append(bases)  # number of unique bases
            variation = np.array(variation, dtype=float)
            normalized = variation - variation.min() / variation.max() - variation.min()
        return normalized


def main() -> None:
    """Main function to parse arguments and run the analysis."""
    parser = argparse.ArgumentParser(
        description="Calculate normalized variability per alignment position."
    )
    parser.add_argument("alignment", help="Path to FASTA alignment file")
    args = parser.parse_args()

    aln = Alignment(args.alignment)
    arr = aln.to_numpy_array()

    variability = aln.calculate_variability(arr)

    # Print results to stdout
    sys.stdout("Position\tVariability\n")
    for i, v in enumerate(variability, start=1):
        sys.stdout(f"{i}\t{v:.3f}\n")


if __name__ == "__main__":
    main()