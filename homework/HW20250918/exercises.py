# Taylor C. Powell
# Homework 2025/09/18

# --------------------------------- EXERCISES -----------------------------------------------
## Exercise 1
#
# QUESTION: In plain English, what does this function take as input and what does it return? 
# What kind of data do you think seq should be?
#
# def reverse_complement(seq: str) -> str:
#     pass
#
# ANSWER: This function takes in a string as input and then does nothing.
# There's not even a return statement, so to say it returns nothing is even incorrect.
# The input string is presumably a DNA sequence, given the name of the function.
# The function is likely intended to compute the reverse complement of the DNA sequence,
# but since it is not implemented, it does not perform any operations or return any value.
#
# BONUS: Finish coding this function.
#
# def reverse_complement(seq: str) -> str:
#     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     rev_comp = ''.join(complement[base] for base in reversed(seq))
#     return rev_comp


## Exercise 2
#
# QUESTION: Explain what kind of data seqs should be and what kind of data this function 
# should return. Why would this type hint be useful for someone analyzing 
# multiple DNA sequences?
#
# def compute_gc_content(seqs: list[str]) -> list[float]:
#     pass
#
# ANSWER: seqs should be a list of strings, and the return value should be a list of floats.
# This type hint would be useful for someone analyzing multiple DNA sequences because
# it clearly indicates that the function expects a list of DNA sequences (as strings)
# and will return a list of GC content values (as floats) corresponding to each sequence.
#
# BONUS: Finish coding this function.
#
# def compute_gc_content(seqs: list[str]) -> list[float]:
#     gc_contents = []
#     for seq in seqs:
#         gc_count = seq.count('G') + seq.count('C')
#         gc_content = (gc_count / len(seq)) * 100 if len(seq) > 0 else 0
#         gc_contents.append(gc_content)
#     return gc_contents


## Exercise 3
#
# TASK: This function calculates the Hamming distance between two sequences. It is correct, 
# but add type hints to this function.
#
# def hamming_distance(seq1: str, seq2: str) -> int:
#     return len([1 for a, b in zip(seq1, seq2) if a != b])
#
# ANSWER: The function already has type hints added. The input parameters seq1 and seq2 are both of type str,
# and the return type is int, which is appropriate for the Hamming distance calculation.
#
# BONUS: Explain what is the Hamming distance, with references, and where it should or should not be used in
# bioinformatics.
#
# ANSWER: The Hamming distance is a measure of the difference between two strings of equal length.
# It is defined as the number of positions at which the corresponding symbols are different.
# In bioinformatics, the Hamming distance is often used to compare DNA, RNA, or protein sequences
# to identify mutations or variations. It is particularly useful in contexts where sequences are
# of the same length, such as comparing homologous genes or analyzing sequencing errors.
#
# REFERENCE: https://en.wikipedia.org/wiki/Hamming_distance


## Exercise 4
#
# TASK: This function returns a float, but the annotation says int. Fix the type annotation to reflect the correct return
# type.
#
# def average_quality(qualities: list[int]) -> float:
#     return sum(qualities) / len(qualities)


## Exercise 5
#
# TASK: This function is meant to return a list of codons from a DNA sequence. Improve the function by:
# 1. Adding appropriate type hints to the return type.
# 2. Fixing the logic so it does not include incomplete codons at the end (e.g., "ATGCGTA" with frame 0 should return
# ["ATG", "CGT"] only).
#
# def get_codons(seq: str, frame: int) -> list[str]:
#     codons = []
#     for i in range(frame, len(seq), 3):
#         if i + 3 <= len(seq):
#             codons.append(seq[i:i+3])
#     return codons