# Translation-Based Multiple Sequence Aligner

A Python package for performing translation-based multiple sequence alignment using ORF detection, k-mer similarity, and the Needleman-Wunsch alignment.

## Project Overview

This project implements a bioinformatics pipeline that:

1. **Detects open reading frames (ORFs)** in nucleotide sequences
2. **Translates sequences** into amino acids for alignment
3. **Uses k-mer similarity** to sort sequences for progressive alignment
4. **Performs pairwise alignment** with the Needleman-Wunsch algorithm
5. **Back-translates** amino acid alignments into codon-aware nucleotide alignments
6. **Generates codon position statistics** and visualizations

## Installation

```bash
# Clone the repository
git clone <https://github.com/Taylor-C-Powell/BINF-6112.git>
cd final-project-TaylorPowell

# Install the package
pip install -e .

# Running the aligner
msaligner --input data/example1.fasta --outdir results

# Other cli options
masaligner --input data/example3.fasta --outdir results --kmer-size 23 --gap-penalty -6 --verbose
```

## Testing

```bash
# Run test suite
cd final-project-TaylorPowell
pytest tests
```

## Use of AI

Majority of the initial codebase and testing suite were generated using ChatGPT (GPT-5)

Significant changes and adaptations were made during the debugging process

Input datasets were manually curated