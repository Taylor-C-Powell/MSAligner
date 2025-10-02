# Lab: Debug & Run `variation-calculator.py` — NumPy on Alignments

## Overview

In this lab you’ll use **NumPy** to analyze a multiple sequence alignment of **spike proteins**.  
Your goal is to compute the **per‑position variability** across the alignment and **normalize** it so that:
- The **least variable** positions (fully conserved) have score **0.0**
- The **most variable** position(s) have score **1.0**

To make this a debugging exercise, the provided script **`variation-calculator.py`** intentionally contains **several errors**. Your task is to **fix the code** so it runs correctly, produces the required output, and demonstrates your understanding of NumPy’s array operations.

Before you leave the lab today, **show your working solution to the TA**.

## What we’re practicing

- Turning an alignment into a **2D NumPy array** (rows = sequences, columns = positions)
- Computing **column-wise statistics** efficiently with NumPy
- **Normalizing** a vector of scores to `[0, 1]`
- **Debugging**: reading tracebacks, writing small tests, and validating assumptions


## Your Task

0. Start by reading the `README.me` file to understand the project and what the script should be doing
1. **Run** the provided `variation-calculator.py` and read the error messages. 
2. **Fix** the bugs so the script:
   - Parses the FASTA alignment into a **dict** `{seq_id: sequence}`
   - Converts sequences into a **NumPy array** of shape `(n_sequences, alignment_length)`
   - Computes variability **per column** using **NumPy** operations
   - **Normalizes** the variability vector to `[0, 1]`
   - Prints a **header** line and one line per position: `Position<TAB>Variability`
3. **Validate** your output on a tiny toy alignment you create (3–4 sequences, 10–20 sites) before running on the full dataset.
4. **Show your working solution to the TA** and submit your deliverables.