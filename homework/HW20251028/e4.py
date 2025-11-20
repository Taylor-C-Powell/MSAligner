from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

records_list = []

record1 = SeqRecord(Seq("ATGC"), id="test1", description="A test sequence")
print(record1)
records_list.append(record1)

record2 = SeqRecord(Seq("GATACA"), id="test2", description="A second test sequence")
print(record2)
records_list.append(record2)

print(records_list)