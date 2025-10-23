[toc]

# Biopython Activity

## Instructions for Students

1. You may want to create or use an existing **conda environment** for this activity:
   ```bash
   conda create -n biopython_env python=3.11
   conda activate biopython_env
   ```
2. Install Biopython locally, if needed:

With conda:
   ```bash
   conda install biopython pandas numpy
   ```

Which pip:
   ```bash
   pip install biopython pandas numpy
   ```
3. For each code block in this exercise, create a new Python script (e.g., `part1_sequences.py`, `part2_parsing.py`, etc.).

4. Each script must include:
   - A **shebang** line (`#!/usr/bin/env python3`)
   - A **guard statement** (`if __name__ == '__main__':`)
   - **Comments and docstrings** explaining your code
   - **Functions** and, where possible, **classes**

5. Execute your code using your **terminal** (Mac/Linux) or **Windows Subsystem for Linux (WSL)**.

6. Save outputs (e.g., generated FASTA files, logs, or printed summaries) into a `/results` directory.

7. When done, zip your entire folder and upload it to Canvas.

## Introduction

Here, we will explore two powerful Python libraries: **Pandas** and **Biopython**. Both are indispensable tools for anyone working in bioinformatics, data science, or any field that involves managing and analyzing biological and tabular data.

This colab is designed to allow students to gain advanced usage of basic Biopython and Pandas skills.

### What is Pandas?

[Pandas](https://pandas.pydata.org/) is a widely-used Python library for data manipulation and analysis, designed to make it easier to handle structured data in the form of tables or data frames. In bioinformatics, we often work with large datasets (e.g., gene expression profiles, sequence alignment scores, or variant data) where Pandas becomes essential. It allows us to load, analyze, and transform data efficiently, enabling complex operations such as filtering, aggregating, and merging datasets in just a few lines of code.

> [Clich here to read more about Pandas](https://pandas.pydata.org/).

#### Why Pandas Matters in Bioinformatics

With Pandas, we can **quickly clean and analyze data**, which is often messy and complex in bioinformatics. Pandas enables **seamless integration** of data from multiple sources and allows us to perform **statistical analyses** and visualize results—all critical steps in the bioinformatics pipeline. For example, Pandas can help us analyze gene expression data, process genome-wide association studies, or even manage high-throughput sequencing metadata.

### What is Biopython?

[Biopython](https://biopython.org/wiki/Packages) is a Python library specifically tailored for bioinformatics applications. It provides tools for reading, analyzing, and writing bioinformatics data formats (e.g., FASTA, GenBank), handling sequence data, and performing computational tasks such as sequence alignment, protein structure analysis, and phylogenetic tree construction. Biopython offers modules for working with DNA, RNA, and protein sequences and integrates with other bioinformatics tools, which makes it a valuable asset in our data analysis toolbox.

> [Click here to learn more about Biopython](https://biopython.org/wiki/Packages).

#### Why Biopython Matters in Bioinformatics

Bioinformatics often requires specialized **handling of biological** data formats and complex tasks like **sequence parsing**, manipulation, and annotation. Biopython simplifies these tasks by providing efficient, high-level methods for working with sequence data, so we can **focus on the biology** rather than data format intricacies. It is especially useful for tasks like analyzing genomic sequences, extracting specific features from a genome, or working with data from public biological databases.

## Pandas + Biopython: A Powerful Combination

Combining Pandas and Biopython allows us to **seamlessly integrate tabular data processing with biological sequence analysis**. For example, you could use Biopython to read a sequence file and Pandas to organize metadata or analyze sequence statistics. This combination is powerful for projects where both sequence data and experimental data (such as sample information or expression levels) need to be processed together.

Let's dive into the basics of using both Pandas and Biopython in Python!

## References and Documentation

Check out the [Getting Started](https://biopython.org/wiki/Getting_Started) page, or follow one of the links below.

- The **Biopython Tutorial and Cookbook** contains the bulk of Biopython documentation. It provides information to get you started with Biopython, in addition to specific documentation on a number of modules ([HTML](https://biopython.org/docs/latest/Tutorial/), [PDF](http://biopython.org/DIST/docs/tutorial/Tutorial.pdf)).
- API documentation for Biopython modules is generated directly from source code comments Sphinx autodoc:  [Biopython API (latest release)](https://biopython.org/docs/latest/api/), and [Biopython API (in-development)](https://biopython.org/docs/dev/api/).
- Wiki documentation:
  - [Seq](https://biopython.org/wiki/Seq) and [SeqRecord](https://biopython.org/wiki/SeqRecord) objects
  - [Bio.SeqIO](https://biopython.org/wiki/SeqIO) - sequence input/output
  - [Bio.AlignIO](https://biopython.org/wiki/AlignIO) - alignment input/output
  - [Bio.PopGen](https://biopython.org/wiki/PopGen) - population genetics
  - [Bio.PDB](https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ) - structural bioinformatics
  - Biopython’s [BioSQL interface](https://biopython.org/wiki/BioSQL)
- Documentation for the Biopython interfaces to BioSQL cover installing Python database adaptors and basic usage of BioSQL ([HTML](http://biopython.org/DIST/docs/biosql/python_biosql_basic.html), [PDF](http://biopython.org/DIST/docs/biosql/python_biosql_basic.pdf)).
- Cookbook-style documentation:
  - [Cookbook documentation](https://biopython.org/wiki/Category%3ACookbook) (on the wiki).
  - The Biopython Structural Bioinformatics FAQ (i.e. how to use the Bio.PDB module) ( [PDF](http://biopython.org/DIST/docs/tutorial/biopdb_faq.pdf)).
  - Working with restriction enzymes ([HTML](http://biopython.org/DIST/docs/cookbook/Restriction.html))

---

# 1. Pandas

Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

- [Click here to find everything you need to get started]https://pandas.pydata.org/docs/getting_started/index.html).
- [Click here to see the user's guide](https://pandas.pydata.org/docs/user_guide/index.html).

Below, we have a series of exercises that cover a range of Pandas operations (see the comments on each code block), from basic filtering to more complex calculations, giving students a hands-on feel for manipulating data in bioinformatics contexts.


##  Exercise 1.1

Create a Python script that reproduces the functionality shown below.

```python
# We usually see Pandas being imported like this:
import pandas as pd
```


##  Exercise 1.2

Create a Python script that reproduces the functionality shown below.

```python
# It is easy ti transform a dictionary into a dataframe:
dic = {}
dic['A'] = [1, 2, 3]
dic['B'] = [4, 5, 6]
dic['C'] = [7, 8, 9]
df = pd.DataFrame(dic)
print(f"This is the dictionary:\n{dic}")
print(f"This is the coresponding data frame:\n{df}")
```


##  Exercise 1.3

Create a Python script that reproduces the functionality shown below.

```python
# We can make our previous fata_dictionary as a data frame:
fasta_dataframe = pd.DataFrame(fasta_dictionary)
print(fasta_dataframe)
```


##  Exercise 1.4

Create a Python script that reproduces the functionality shown below.

```python
# Retrieve rows from the dataframe where the 'ID' is either 'seq1', 'seq2', or 'seq3'.
# We use the .loc accessor with the .isin() method to filter specific rows by ID.

# Filter rows where 'ID' is in the list ['seq1', 'seq2', 'seq3']
selected_sequences = fasta_dataframe.loc[fasta_dataframe['ID'].isin(['seq1', 'seq2', 'seq3'])]

# Display the filtered DataFrame containing only the selected sequences
print(selected_sequences)

```


##  Exercise 1.5

Create a Python script that reproduces the functionality shown below.

```python
# Filter rows where the 'Length' column is greater than or equal to 16.
# We use the .loc accessor with a conditional expression to filter based on sequence length.

# Select rows where 'Length' is 16 or greater
long_sequences = fasta_dataframe.loc[fasta_dataframe['Length'] >= 16]

# Display the filtered DataFrame with sequences of length 16 or more
print(long_sequences)
```


##  Exercise 1.6

Create a Python script that reproduces the functionality shown below.

```python
# Create a new column 'Other' by calculating the difference between 'Length'
# and the sum of columns 'A', 'T', 'C', 'G', and 'InDel' for each row.

# Calculate 'Other' and assign it to a new column
fasta_dataframe['Other'] = fasta_dataframe['Length'] - (
    fasta_dataframe['A'] + fasta_dataframe['T'] + fasta_dataframe['C'] + fasta_dataframe['G'] + fasta_dataframe['InDel']
)

# Display the updated DataFrame with the new 'Other' column
print(fasta_dataframe)

```


##  Exercise 1.7

Create a Python script that reproduces the functionality shown below.

```python
# Calculate and print the average length of all sequences
avg_length = fasta_dataframe['Length'].mean()
print("Average Length:", avg_length)
```


##  Exercise 1.8

Create a Python script that reproduces the functionality shown below.

```python
# Count the number of sequences with more than 4 occurrences of 'A'
high_A_count = fasta_dataframe[fasta_dataframe['A'] > 4]
print("Sequences with more than 4 'A's:")
print(high_A_count)
```


##  Exercise 1.9

Create a Python script that reproduces the functionality shown below.

```python
# Sort the dataframe by 'Length' in descending order
sorted_by_length = fasta_dataframe.sort_values(by='Length', ascending=False)
print("Sequences sorted by Length:")
print(sorted_by_length)
```


##  Exercise 1.10

Create a Python script that reproduces the functionality shown below.

```python
# Select sequences with a GC content (G + C) of more than 50%
high_gc_content = fasta_dataframe.loc[
    ((fasta_dataframe['G'] + fasta_dataframe['C']) / fasta_dataframe['Length']) > 0.5
]
print("Sequences with GC content over 50%:")
print(high_gc_content)

```


##  Exercise 1.11

Create a Python script that reproduces the functionality shown below.

```python
# Filter sequences that have the word "Bold" in their description
bold_sequences = fasta_dataframe[fasta_dataframe['Description'].str.contains("Bold")]
print("Sequences with 'Bold' in their description:")
print(bold_sequences)
```


##  Exercise 1.12

Create a Python script that reproduces the functionality shown below.

```python
# Sum up the counts of each nucleotide across all sequences
total_A = fasta_dataframe['A'].sum()
total_T = fasta_dataframe['T'].sum()
total_G = fasta_dataframe['G'].sum()
total_C = fasta_dataframe['C'].sum()

print("Total occurrences of each nucleotide:")
print(f"A: {total_A}, T: {total_T}, G: {total_G}, C: {total_C}")
```


##  Exercise 1.13

Create a Python script that reproduces the functionality shown below.

```python
# Calculate the AT content (percentage of A and T) for each sequence and add it as a new column
fasta_dataframe['AT_Content'] = (fasta_dataframe['A'] + fasta_dataframe['T']) / fasta_dataframe['Length']
print("DataFrame with AT_Content column added:")
print(fasta_dataframe)
```


##  Exercise 1.14

Create a Python script that reproduces the functionality shown below.

```python
# Identify the sequence with the highest number of 'InDel'
max_indel_sequence = fasta_dataframe.loc[fasta_dataframe['InDel'].idxmax()]
print("Sequence with the highest number of indels:")
print(max_indel_sequence)
```


##  Exercise 1.15

Create a Python script that reproduces the functionality shown below.

```python
# Calculate the total length of all sequences combined
total_length = fasta_dataframe['Length'].sum()
print("Total Length of all sequences:", total_length)
```


##  Exercise 1.16

Create a Python script that reproduces the functionality shown below.

```python
# Select sequences where the total count of A, T, G, and C equals the sequence length
matching_length_sequences = fasta_dataframe[
    fasta_dataframe['Length'] == (fasta_dataframe['A'] + fasta_dataframe['T'] + fasta_dataframe['G'] + fasta_dataframe['C'] + fasta_dataframe['InDel'])
]
print("Sequences where total base count matches Length:")
print(matching_length_sequences)
```

# Pandas Challenges

Here are a few ideas for you to develop your own Pandas challenges, and you are encouraged to complete one (but ideally more) of these. The more you practice, the better you will become in using Pandas.

1. Filter Sequences by Nucleotide Ratio: Create a function that filters sequences based on the ratio of one nucleotide to another (e.g., sequences where the count of A is at least twice the count of T).
2. Group by Nucleotide Counts: Group sequences based on a specific nucleotide count (e.g., all sequences with 5 or more Gs) and calculate the average length within each group.
3. Identify Outliers in Sequence Lengths: Write code to identify sequences whose lengths are significantly above or below the average. Define "significant" as more than one standard deviation from the mean.
4. Count Sequences by Description Keyword: Count how many sequences contain specific keywords in their description, such as "Mighty," "Bold," or "Silent."
5. Sort and Rank by GC Content: Calculate the GC content for each sequence and rank the sequences from highest to lowest GC content. Display only the top 5 sequences with the highest GC content.
6. Calculate Nucleotide Percentages: For each sequence, calculate the percentage of each nucleotide (A, T, G, C) relative to the total length, then add these percentages as new columns to the DataFrame.
7. Identify Palindromic Sequences: Write a function to detect palindromic sequences (where the sequence reads the same forward and backward). Filter and display only the palindromic sequences.
8. Create a Summary Table: Generate a summary table that shows the minimum, maximum, mean, and standard deviation of sequence lengths.
9. Find Sequences with Extreme AT or GC Content: Identify sequences where the AT content is above 70% or the GC content is above 70%.
10. Track Most Common Nucleotide in Each Sequence: Create a new column that records the most common nucleotide for each sequence (A, T, G, or C). Handle ties by indicating "tie" if two or more nucleotides have the same highest count.
11. Analyze Length Distribution by Description: Group sequences by a keyword in the description (e.g., “Bold” or “Legendary”) and calculate the average length for each keyword group.
12. Analyze Variability in InDels: Filter sequences with non-zero InDel values and calculate the variance and standard deviation in their InDel counts.
13. Identify High-Quality Sequences: Define a “high-quality” sequence as one where the total nucleotide counts perfectly match the length and there are no InDels. Filter out and display only the high-quality sequences.
14. Visualize Nucleotide Distributions: Create a simple bar plot to show the distribution of each nucleotide (A, T, G, and C) across all sequences.
15. Detect Changes in Sequence Length After Mutation: Simulate random deletions or insertions in each sequence and track how these mutations affect sequence length. Compare before and after lengths.

---

# 2. Biopython

Let us start simple with a few examples on how to read and parse sequences with BioPython. Each code block below contains one example, and you will see that the code block's comments explain all that you will need to know.

### Exercise 2.1

Create a Python script that reproduces the functionality shown below.

```python
# Import the Seq class from Biopython's Bio.Seq module.
# Seq is used to create and manipulate biological sequences, such as DNA, RNA, or protein sequences.
from Bio.Seq import Seq
```

### Exercise 2.2

Create a Python script that reproduces the functionality shown below.

```python
# Create a sequence object 'my_seq' with a DNA sequence string.
# This object allows us to perform various operations specific to biological sequences.
my_seq = Seq("AGTACACTGGT")
```


### Exercise 2.3

Create a Python script that reproduces the functionality shown below.

```python
# The Seq object differs from a regular Python string because it includes bioinformatics-specific methods.
# These methods allow us to perform operations unique to biological sequences, such as finding complements or reverse complements.
# These operations are not available with plain strings, making Seq more versatile for biological data.

# Display the sequence as a Seq object.
print(my_seq)  # Outputs: Seq('AGTACACTGGT')
```


### Exercise 2.4

Create a Python script that reproduces the functionality shown below.

```python
# Get the complement of the sequence.
# In DNA sequences, this method replaces each base with its complementary base:
# A with T, T with A, G with C, and C with G.
print(my_seq.complement())  # Outputs: Seq('TCATGTGACC')
```


### Exercise 2.5

Create a Python script that reproduces the functionality shown below.

```python
# Get the reverse complement of the sequence.
# This method first finds the complement, then reverses the sequence,
# which is commonly needed in bioinformatics for analyzing DNA sequences.
print(my_seq.reverse_complement())  # Outputs: Seq('ACCAGTGTACT')
```

### Exercise 2.6

Create a Python script that reproduces the functionality shown below.

```python
# We can read FASTA files with Biopython, but to keep things simple in this Colab we will instead define the contents of that file inside the Colab.

# First, we will need StringIO
from io import StringIO

# Now we will define a string that contains FASTA formatted data
fasta_data = """>seq1
AGTACACTGGT
>seq2
GGTACACTGCA
>seq3
TGTACGACTGA
"""

# Finally, we will wse StringIO to create a file-like object from the string variable
fasta_io = StringIO(fasta_data)
```

### Exercise 2.7

Create a Python script that reproduces the functionality shown below.

```python
# Import the SeqIO module from Biopython.
# SeqIO is used for reading and writing sequence file formats (e.g., FASTA, GenBank),
# which are common in bioinformatics for storing DNA, RNA, or protein sequences.
from Bio import SeqIO

# Use SeqIO's parse() function to read a FASTA file containing multiple sequences.
# "ls_orchid.fasta" is the file name, and "fasta" specifies the file format.
# SeqIO.parse() returns an iterator that goes through each sequence record in the file one at a time.
for seq_record in SeqIO.parse(fasta_io, "fasta"):

    # Print the sequence ID (e.g., a unique identifier for the sequence).
    # This ID usually provides information about the sequence, such as the accession number or other identifying labels.
    print(f"Record ID = {seq_record.id}")

    # Print a representation of the sequence itself using repr(), which shows the sequence data in a clear format.
    # The seq attribute contains the biological sequence data (e.g., DNA or protein sequence) associated with the record.
    print(f"Representation of sequence {seq_record.id} = {repr(seq_record.seq)}")

    # Print the length of the sequence using len().
    # This gives the total number of bases (for DNA/RNA) or residues (for proteins) in the sequence.
    print(f"{seq_record.id} sequence length = {len(seq_record)}")

```


###  Exercise 2.8

Create a Python script that reproduces the functionality shown below.

```python
'''
Let us put it all together in this example and also learn the difference between the ID and the description.
'''

from Bio import SeqIO
from io import StringIO

fasta_data = """>seq1 | The Mighty AGTAC
AGTACACTGGT
>seq2 | The Unbreakable GGTAC
GGTACACTGCAACT
>seq3 | The Brave TGTACG
TGTACGACTGAACCTG
>seq4 | The Swift CCTAG
CCTAGTAGCTAGGATC
>seq5 | The Elusive TTGCA
TTGCAAGTCGTAGGCTAC
>seq6 | The Legendary GGATC
GGATCCGTACCTGACTGGA
>seq7 | The Bold AGCAGT
AGCAGTGCAGT
>seq8 | The Clever TTTGAC
TTTGACTAGGCCAGTGAATC
>seq9 | The Fearless GCTAGG
GCTAGGACCTGTAGC
>seq10 | The Silent TACGGT
TACGGTGCTACTAGCTAGCTA
"""

# Use StringIO to create a file-like object from the string variable
fasta_io = StringIO(fasta_data)

# Parse the FASTA data from the string variable as if it were a file
for seq_record in SeqIO.parse(fasta_io, "fasta"):
    print("ID:", seq_record.id) # Print the ID of each sequence
    print("Description:", seq_record.description) # Print the ID of each sequence
    print("Sequence:", str(seq_record.seq)) # Print the sequence data
    print("Length:", len(seq_record)) # Print the length of each sequence
    print("//")

```

### Exercise 2.9

Create a Python script that reproduces the functionality shown below.

```python
'''
In this code block we will get several details from our FASTA data and out all of that into a single, complex dictionary.
'''

from Bio import SeqIO
from io import StringIO

fasta_data = """>seq1 | The Mighty AGTAC
AGTACACTGGT
>seq2 | The Unbreakable GGTAC
---GGTACACNGCAACT--
>seq3 | The Brave TGTACG
TGTANGACTGAACCTG---
>seq4 | The Swift CCTAG
CCTAGT--AGCTANGATC-
>seq5 | The Elusive TTGCA
TTGCAAGTC---GTAGGCT
>seq6 | The Legendary GGATC
GGATCNGTACCTGACTGGA
>seq7 | The Bold AGCAGT
AGCAGTGCAGT--------
>seq8 | The Clever TTTGAC
TTTGACTAGGCCAGNGAAT
>seq9 | The Fearless GCTAGG
--GCTAGGACCTGTAGC--
>seq10 | The Silent TACGGT
TAC-GTG-TAC-AGCTANN
"""

fasta_dictionary = {"ID" : [],
    "Description" : [],
    "Length" : [],
    "Sequence" : [],
    "A" : [],
    "T" : [],
    "G" : [],
    "C" : [],
    "InDel" : []}

fasta_io = StringIO(fasta_data)

for seq_record in SeqIO.parse(fasta_io, "fasta"):
    fasta_dictionary["ID"].append(seq_record.id)
    fasta_dictionary["Description"].append(seq_record.description)
    fasta_dictionary["Length"].append(len(str(seq_record.seq)))
    fasta_dictionary["Sequence"].append(str(seq_record.seq))
    fasta_dictionary["A"].append(seq_record.seq.count("A"))
    fasta_dictionary["T"].append(seq_record.seq.count("T"))
    fasta_dictionary["G"].append(seq_record.seq.count("G"))
    fasta_dictionary["C"].append(seq_record.seq.count("C"))
    fasta_dictionary["InDel"].append(seq_record.seq.count("-"))
```


### Exercise 2.10

Create a Python script that reproduces the functionality shown below.

```python
# Let us check what we did above:
print(fasta_dictionary)
```

# Biopython Challenges

Write your own Biopython challenges, where you propose to solve a problem with Biopython using the techniques described above or, better yet, techniques that you got from Biopython documentation. Here are a few suggestions:

1. Converting DNA to amino acids
2. Looking for a specific peptide sequence inside a DNA alignment
3. Identify simple repeats composed of a single nucleotide
4. Extracting and counting Codons: Write a script to extract and count all unique codons in a DNA sequence, then report the most and least common codons.
5. Transcribing DNA to RNA: Create a function that converts a DNA sequence to its RNA counterpart by replacing thymine (T) with uracil (U).
6. Finding Palindromic Sequences: Detect palindromic sequences within a given DNA sequence, which are sequences that read the same forward and backward.
7. Calculating GC Content: Calculate the GC content (percentage of guanine and cytosine) of a DNA sequence, an important measure in genomics.
8. Simulating mutations: Randomly mutate a DNA sequence by substituting nucleotides, and output the mutated sequence along with the positions and types of mutations.
9. Identifying restriction sites: Identify all locations in a DNA sequence where a specific restriction enzyme cuts, using the enzyme's known recognition sequence.
10. Counting amino acid frequencies: Given a translated protein sequence, count and report the frequency of each amino acid.
11. Creating a reverse complement dictionary: Generate a dictionary where each DNA sequence is paired with its reverse complement.
12. Finding open reading frames (ORFs): Write a script to identify potential ORFs in a DNA sequence by searching for start and stop codons.
13. Analyzing sequence motifs: Search for a known motif (e.g., TATA box) in a DNA sequence and report its occurrences and positions.
14. Comparing sequence similarity: Compare two sequences and calculate a similarity score based on alignment or number of matching bases.
15. Extracting sequences by feature: Using GenBank files, extract and print sequences of specific features, like coding regions (CDS) or promoters.

Select at least one (but ideally more ideas), or come up with your own. The more you can challenge yourself, the better Biopython user you will become.


---

# Submission

Package all your scripts and markdown answers into a single ZIP file. Upload it on the corresponding assignment **Canvas** by the beginning of class on **Thursday, October 28*.

Checklist:
- README file with your personal information and details on your project
- 16 Python scripts corresponding to the 16 Pandas exercises
- At least 1 Python script completing at least 1 Pandas challenge
- 10 Python scripts corresponding to the 10 Biopython exercises
- At least 1 Python script completing at least 1 Biopython challenge