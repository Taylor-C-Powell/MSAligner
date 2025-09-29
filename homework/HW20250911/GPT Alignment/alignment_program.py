from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Align.Applications import MuscleCommandline
import subprocess
import os

# ===========================
# Multiple Sequence Alignment
# ===========================
# This program takes three HBA1 nucleotide sequences in FASTA format,
# aligns them with MUSCLE, and calculates similarity and difference scores.

# Input FASTA file containing the sequences
input_file = "HBA1_sequences.fna"

# Output file for aligned sequences
aligned_file = "HBA1_aligned.fna"

# Run MUSCLE alignment using Biopython wrapper
# (Make sure MUSCLE is installed and accessible from your PATH)
muscle_cline = MuscleCommandline(input=input_file, out=aligned_file)
subprocess.run(str(muscle_cline), shell=True, check=True)

# Read alignment
alignment = AlignIO.read(aligned_file, "fasta")
print("Aligned Sequences:")
print(alignment)

# ===========================
# Calculate Similarity & Difference Scores
# ===========================

# Create a summary of the alignment
summary_align = AlignInfo.SummaryInfo(alignment)

# Calculate consensus sequence
consensus = summary_align.dumb_consensus()
print("\nConsensus Sequence:")
print(consensus)

# Function to calculate similarity (percentage identity)
def calculate_scores(alignment):
    num_sequences = len(alignment)
    alignment_length = alignment.get_alignment_length()
    matches = 0
    total = 0

    for i in range(alignment_length):
        column = alignment[:, i]
        # Only compare non-gap positions
        if "-" not in column:
            total += 1
            if len(set(column)) == 1:  # all identical
                matches += 1

    similarity = (matches / total) * 100 if total > 0 else 0
    difference = 100 - similarity
    return similarity, difference

similarity, difference = calculate_scores(alignment)

print("\nAlignment Scores:")
print(f"Similarity Score: {similarity:.2f}%")
print(f"Difference Score: {difference:.2f}%")
