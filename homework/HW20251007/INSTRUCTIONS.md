# Homework for October 14, 2025

Directory `demo/` contains a simple program to perform the alignment of two sequences in FASTA file using the Needleman–Wunsch algorithm.

The main script (`main.py`) requires a custom package, in `newu2`, that contains three modules (`num.py`, `read.py`, and `write.py`).

## Student's details

- **Name:** Add your name here
- **UNC Charlotte's ID (800 number):** Add your ID here
- **UNC Charlotte's email:** add your institutional email here

## 1. Answer these questions

### 1.1. Explain why `newu2` has an empty file called `__init__.py`

Add your response in here.

### 1.2. Explain the function `read_fa` from `read.py` in plain English

Add your response in here.

### 1.3. Explain the function `write_fa` from `write.py` in plain English

Add your response in here.

### 1.4. Explain the function `parse_fa` from `num.py` in plain English

Add your response in here.

### 1.5. Explain the function `fill_matrix` from `num.py` in plain English

Add your response in here.

### 1.6. Explain the function `trace_matrix` from `num.py` in plain English

Add your response in here.

### 1.7. Complete the table below

| Match Cost | Mismatch Cost | InDel Cost | Expected Alignnment of Sequence 1 | Expected Alignnment of Sequence 2 |
| --- | --- | --- | --- | --- |
| +1 | -1 | -1 | GCA-TGCG | -GATTACA |
| +1 | -1 | -10 | GCATGCG | GATTACA |
| +1 | -2 | -1 | | |
| +1 | -2 | -10 | | |
| +1 | -10 | -1 | | |
| -1 | +1 | +1 | | |

## 2. Complete these programming challenges

Modify the Python3 project so that it completes the challenges below. Include a compressed version of your entire project, together with your responses above.

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