from Bio import SeqIO
from io import StringIO

fasta_data = """"
>seq1 This is the first
AGTACACTGGT

>seq2 This is the second
GTCACTGGTAC
"""
fasta_io = StringIO(fasta_data)

total_len = 0
count = 0

for record in SeqIO.parse(fasta_io, "fasta"):
    print(f"Record's ID: {record.id} ({type(record.id)})\n")
    print(f"Record's description: {record.description} ({type(record.description)})\n")
    print(f"Record's sequence: {record.seq} ({type(record.seq)})\n")
    total_len += len(record)
    count += 1

print(f"Total length: {total_len}")
print(f"Number of records: {count}")