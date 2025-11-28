#!/usr/bin/env python3
"""
main.py

Driver script for running the Needleman-Wunsch algorithm demonstration.
Uses the newu2 module for alignment functions.

Example usage:
    python3 main.py -f sequences.fasta
"""

import argparse
import sys, re
from typing import Any
from part2_files.read import read_fa
from part2_files.write import write_fa
from part2_files.num import parse_fa, fill_matrix, trace_matrix


class AlignmentRunner:
    """
    AlignmentRunner is responsible for managing sequence alignment tasks.
    It loads input sequences, applies the Needleman-Wunsch algorithm, 
    and outputs results.
    """

    def __init__(self, fasta_file: str="sequences.fasta", aln_file: str="alignment.fasta", match:int=1, mismatch:int=-1, indel:int=-1) -> None:
        """
        Initialize the runner with a fasta file.

        Parameters
        ----------
        fasta_file : str
            Path to the input fasta file containing sequences to align.
        """
        self.fasta_file = fasta_file
        data = read_fa(fasta_file)
        self.data = data
        id1, id2, seq1, seq2, mat = parse_fa(data)
        self.id1 = id1
        self.id2 = id2
        self.seq1 = seq1
        self.seq2 = seq2
        self.mat = mat
        self.match = match
        self.mismatch = mismatch
        self.indel = indel
        self.aln_file = aln_file

    def fill(self) -> None:
        """
        Filling in the table.
        """
        self.mat = fill_matrix(
            matrix = self.mat,
            seq1_array = self.seq1,
            seq2_array = self.seq2,
            match = self.match,
            mismatch = self.mismatch,
            indel = self.indel
        )

    def trace(self) -> None:
        """
        Tracing back to produce the alignment.
        """
        self.aln = trace_matrix(
            matrix = self.mat,
            seq1_array = self.seq1,
            seq2_array = self.seq2,
        )

    def write(self) -> None:
        seqids = [self.id1, self.id2]
        seqs = ["".join(seq) for seq in self.aln]
        write_fa(
            ids = seqids,
            sequences = seqs,
            filepath = self.aln_file
        )

    def consensus(self) -> None:
        """
        Generate consensus string from the aligned sequences.
        """
        a1 = [str(x) for x in self.aln[0].tolist()]
        a2 = [str(x) for x in self.aln[1].tolist()]

        consensus_chars = []
        for x, y in zip(a1, a2):
            if x == y:
                consensus_chars.append(x.upper())
            elif x == '-':
                consensus_chars.append(y.upper())
            elif y == '-':
                consensus_chars.append(x.upper())
            else:
                consensus_chars.append('N')
        self.consensus_str = ''.join(consensus_chars)

    def find_mut_rate(self) -> None:
        """
        Calculate mutation rate from the aligned sequences.
        """
        a1 = [str(x) for x in self.aln[0].tolist()]
        a2 = [str(x) for x in self.aln[1].tolist()]

        matches = 0
        mismatches = 0
        for x, y in zip(a1, a2):
            if x == '-' or y == '-':
                mismatches += 1
            elif x == y:
                matches += 1
            else:
                mismatches += 1
        length = len(a1)  # Length of the original sequence (with gaps)
        self.mutation_rate = (mismatches / length) if length > 0 else 0.0



def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the program.

    Returns
    -------
    argparse.Namespace
        Object containing parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Needleman-Wunsch global sequence alignment demo"
    )
    parser.add_argument(
        "-i", "--input",
        required=False,
        default="sequences.fasta",
        type=str,
        help="Path to input fasta file containing sequences"
    )
    parser.add_argument(
        "-o", "--output",
        required=False,
        default="alignment.fasta",
        type=str,
        help="Path to output fasta file containing the sequence alignment"
    )
    parser.add_argument(
        "--match",
        required=False,
        default=1,
        type=int,
        help="Cost for matches"
    )
    parser.add_argument(
        "--mismatch",
        required=False,
        default=-1,
        type=int,
        help="Cost for mismatches"
    )
    parser.add_argument(
        "--indel",
        required=False,
        default=-1,
        type=int,
        help="Cost for InDels"
    )
    return parser.parse_args()


def main() -> None:
    """
    Main function to execute the alignment workflow.

    Returns
    -------
    None
    """
    args = parse_args()
    runner = AlignmentRunner(
        fasta_file=args.input,
        aln_file=args.output,
        match=args.match,
        mismatch=args.mismatch,
        indel=args.indel
    )
    check_input_message = f"""Reading from {args.input}:
>{runner.id1}
{''.join(runner.seq1)}
>{runner.id2}
{''.join(runner.seq2)}
"""
    sys.stdout.write(check_input_message)
    sys.stdout.write("Filling up the matrix...\n")
    runner.fill()
    sys.stdout.write(f"Done! Here is how the matrix looks like:\n{runner.mat}\n")
    sys.stdout.write("Tracing back to produce alignment...\n")
    runner.trace()
    sys.stdout.write(f"Done! Here is the resulting NumPy matrix:\n{runner.aln}\n")
    runner.write()
    sys.stdout.write(f"The alignment was written into {args.output}\n")
    runner.consensus()
    sys.stdout.write(f"The consensus string is:\n{runner.consensus_str}\n")
    runner.find_mut_rate()
    sys.stdout.write(f"The mutation rate is: {runner.mutation_rate:.2%}\n")

if __name__ == "__main__":
    main()