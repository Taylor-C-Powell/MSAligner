#!/usr/bin/env python3

class Challenge1:
    """
    A class to encapsulate the solution for Challenge 1.
    """

    def __init__(self, aa_seq: str):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.aa_seq = aa_seq

    def midaa(self, aa_seq: str) -> str:
        if len(aa_seq) % 2 == 0:
            
            return "No middle amino acid"
        else:
            # print(len(aa_seq))
            return "Middle amino acid is: " + aa_seq[(len(aa_seq)-1)//2]

if __name__ == "__main__":
    with open('Labs/2025-9-25/Challenges/data/HBc.faa', 'r') as fasta_file:
        sequence = ''.join(line.rstrip('\n') for line in fasta_file.readlines()[1:])
    challenge = Challenge1(sequence)
    print(challenge.midaa(challenge.aa_seq))


