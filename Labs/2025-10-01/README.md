# Variation Calculator

This script calculates **normalized per-position variability** from a sequence alignment in FASTA format.

- Input: a FASTA file with aligned sequences (e.g., spike proteins). 
- Output: a table with two columns: 
  1. Position (1-based) 
  2. Normalized variability (0 to 1)

**Normalization rule:**
- Least variable positions (no variation) = `0` 
- Most variable position(s) = `1` 

---

## Usage

```bash
python3 variation_calculator.py spike_alignment.fasta > variability.tsv
```

## **Example**

- Input: `spike.aln`
- Output: `variability.tsv`

The first 10 lines of the output should look like this:

```
1	0.250
2	0.250
3	0.250
4	0.250
5	0.250
6	0.250
7	0.250
8	0.250
9	0.250
10	0.250
```

The last 20 lines of the output should look like this:

```
3824	0.250
3825	0.250
3826	0.250
3827	0.250
3828	0.250
3829	0.250
3830	0.250
3831	0.250
3832	0.000
3833	0.000
3834	0.000
3835	0.000
3836	0.000
3837	0.000
3838	0.000
3839	0.000
3840	0.000
3841	0.000
3842	0.000
3843	0.000
```

## Requires

- Python 3
- NumPy