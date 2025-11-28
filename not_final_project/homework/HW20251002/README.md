# Programming 2 – Homework Challenges (Oct. 2, 2025)

You have received the following files to work with:

- `metadata.csv`: Selected metadata from NextStrain (ncov dataset, global, open), retrieved on Sept. 26, 2025
- `genome.fasta`: Complete genome sequences (nucleotides in FASTA format)
- `spike.fasta`: Spike glycoprotein gene sequences (nucleotides in FASTA format), extracted from NCBI's GenBank (if annotation was present)
- `RBD.faa`: Reference sequence for the Spike's receptor binding domain (amino acids in FASTA format)
- `RBD.fna`: Reference sequence for the Spike's receptor binding domain (nucleotides in FASTA format)
- `RBM.faa`: Reference sequence for the Spike's receptor binding motif (amino acids in FASTA format)
- `RBM.fna`: Reference sequence for the Spike's receptor binding motif (nucleotides in FASTA format)

# Challenges

Complete at least one (and as many as you can) of the following challenges.  
All challenges should be completed using a combination of **Bash and Python scripts executed locally**.

## Challenge 1 – *Metadata Matchmaker*
Write a script that compares sequence accession numbers from the FASTA files (`genome.fasta` or `spike.fasta`) with the accession numbers in the metadata table (`metadata.csv`).  

- Report which sequences are included in the metadata and which are not.  
- For those that match, produce a **new metadata table** containing only the matching entries.  
- For those that are missing, add **placeholder entries** in the new metadata table for future completion.  

Remember: use Bash and Python in combination.

## Challenge 2 – *Whole-Genome Wrestling*
Use Bash and/or Python to run a sequence aligner (e.g., MAFFT) on the **genome sequences**.  

- After generating the genome alignment, extract the **RBD** or **RBM** regions by mapping them to the reference sequences provided (`RBD.fna`, `RBM.fna`).  
- Save these extracted alignments as new files.  

## Challenge 3 – *Spike Showdown*
Run an alignment of the **spike sequences** (`spike.fasta`) using MAFFT.  

- As in Challenge 2, extract the **RBD** and/or **RBM** regions using the reference files.  
- Save the extracted alignments for further comparison.  

## Challenge 4 – *Domain Double-Check*
Compare the RBD (or RBM) alignments extracted from:  
1. The **whole-genome alignment** (Challenge 2), and  
2. The **spike-only alignment** (Challenge 3).  

- Assess whether the RBD/RBM alignments from both sources are consistent.  
- If you find differences, explain why they might occur.  
- If they are identical, explain why that might be the case.  

# Deadline

**Thursday, October 2, 2025**

# Suggested AI Prompt and Coding Guidelines

You are allowed to use generative AI tools to help you write code. Below is a suggested **prompt template** you can adapt. Even if you don’t use it directly, treat these points as **guidelines for your code**.

### Suggested Prompt

> """Write a Python 3 script (with a shebang) that does the following: [insert challenge description].
> Please include docstrings, type hints, and comments. Use argparse for input parameters.
> Write output to `sys.write.stdout` or `sys.write.stderr` instead of using `print`.
> Consider using regular expressions, list comprehensions, and classes with `__init__` methods.
> If possible, parse FASTA sequences using Biopython or custom code.
> Make sure the script can run from the command line, and include a guard function (`if __name__ == "__main__":`)."""

### Guidelines

- **Shebang** at the top of all scripts.  
- **Documentation**: docstrings and comments are required.  
- **Type hints**: specify input and output types in Python functions.  
- **Classes**: include at least one class with an `__init__` method.  
- **Guard function**: always wrap your main function with a guard.  
- **Input/output**: use `sys.stdout.write` or `sys.stderr.write` instead of `print`.  
- **User input**: handle via `argparse`.  
- **Extra practice**: try using regular expressions and list comprehensions.  
- **Modules**: you may use Biopython (optional).  
- **Pipelines**: if your process requires manual steps, document them clearly.  

---