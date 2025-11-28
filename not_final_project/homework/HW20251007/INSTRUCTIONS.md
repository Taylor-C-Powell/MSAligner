# Homework for October 14, 2025

Directory `demo/` contains a simple program to perform the alignment of two sequences in FASTA file using the Needleman–Wunsch algorithm.

The main script (`main.py`) requires a custom package, in `newu2`, that contains three modules (`num.py`, `read.py`, and `write.py`).

## Student's details

- **Name:** Taylor C. Powell
- **UNC Charlotte's ID (800 number):** 801024945
- **UNC Charlotte's email:** tpowel43@charlotte.edu

## 1. Answer these questions

### 1.1. Explain why `newu2` has an empty file called `__init__.py`

The __init__.py file allows the python interpretor to more easily recognize that a directory is to be used as a python package. It's not required, but it helps with package initialization processes. 

### 1.2. Explain the function `read_fa` from `read.py` in plain English

The read_fa function takes a FASTA file as input and returns a formatted string. Each sequence contained within the input FASTA file contributes two lines to the ouput string: a header line containing a sequence ID, and a line containing a nucleotide/protein sequence. 

### 1.3. Explain the function `write_fa` from `write.py` in plain English

The write_fa function takes two lists as inputs: a list of sequence IDs and a list of their corresponding sequences. It then creates a FASTA file from the inputs and returns a string that represents the filepath to the newly created file. 

### 1.4. Explain the function `parse_fa` from `num.py` in plain English

The parse_fa function takes in a FASTA file (containing only two sequences) as input and returns a tuple containing the following items: the header of the first sequence, the header of the second sequence, a NumPy array containing the first sequence as a list of characters, a NumPy array containing the second sequence as a list of characters, and an empty matrix with dimensions corresponding to the lengths of each sequence plus one. For example, if the first sequence had 6 characters, and the second sequence had 7 characters, the empty array would have 7 columns and 8 rows.

### 1.5. Explain the function `fill_matrix` from `num.py` in plain English

The fill_matrix function takes in 6 inputs: an empty matrix, an array of characters representing the first sequence, an array of characters representing the second sequence, a match score, a mismatch score, and indel score. It returns a filled scoring matrix using the downpass portion from the Needleman-Wunsch algorithm using the input sequences and the scores from the input parameters. 

### 1.6. Explain the function `trace_matrix` from `num.py` in plain English

This function implements the traceback step from the Needleman-Wunsch algorithm. It takes in three input parameters, a filled scoring matrix from the fill_matrix function, and two NumPy arrays containing sequences represented by a list of characters. It returns a NumPy array with two rows, one for each aligned sequence.

### 1.7. Complete the table below

| Match Cost | Mismatch Cost | InDel Cost | Expected Alignnment of Sequence 1 | Expected Alignnment of Sequence 2 |
| +2 | -2 | -4 | GCATGCG------- | -------GATTACA |
| +1 | -1 | -1 | GCA-TGCG | -GATTACA |
| +1 | -1 | -10 | GCATGCG | GATTACA |
| +1 | -2 | -1 | ---GCATGCG | GATT-AC-A- |
| +1 | -2 | -10 | GCATGCG---- | ----GATTACA |
| +1 | -10 | -1 | ---GCATGCG | GATT-AC-A- |
| -1 | +1 | +1 | GCATGCG------- | -------GATTACA |

## 2. Complete these programming challenges

Modify the Python3 project so that it completes the challenges below. Include a compressed version of your entire project, together with your responses above.
2--
### 2.1. Report a consensus sequence representing the alignment of the two sequences

To resolve this challenge, create a new package, separate from `newu2`.

### 2.2. Report the cost of the alignment

To resolve this challenge, create a new package, separate from `newu2`.

### 2.3. Report the total number of possible alignments (OPTIONAL)

This challenge is optional.

To resolve this challenge, create a new package, separate from `newu2`.

Your goal is to count (and not cenessarily report) all the possible alignments of optimal equal cost for a given set of match, mismatch, and InDel costs. Your code should allow you to complete the table below:

| Match | Mismatch | InDel | No. of Alignments |
| --- | --- | --- | --- |
| +1 | -1 | -1 | |
| +1 | -1 | -2 | |
| +1 | -1 | -10 | |