from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")
print(my_seq)
print("Complement:", my_seq.complement())
print("Reverse Complement:", my_seq.reverse_complement())
print("Transcription:", my_seq.transcribe())
print("Translation:", my_seq.translate())