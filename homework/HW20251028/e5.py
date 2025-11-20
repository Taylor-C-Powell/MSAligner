from Bio.SeqUtils import gc_fraction

for record in records:
    print(record.id, "GC content:", gc_fraction(record.seq))