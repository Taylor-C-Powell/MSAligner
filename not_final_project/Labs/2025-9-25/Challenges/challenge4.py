class Challenge4:
    """
    A class to encapsulate the solution for Challenge 4.
    """

    def __init__(self, gene: str, seq1: list, seq2: list):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.gene = gene
        self.seq1 = seq1
        self.seq2 = seq2

    def sequence_compare(self) -> bool:
        """
        Implement the main logic for the challenge.

        :return: The result of the computation.
        """
        # TODO: Implement the solution logic here
        if self.gene in self.seq1 and self.gene in self.seq2:
            return False
        elif self.gene not in self.seq1 and self.gene not in self.seq2:
            return False
        else:
            return True
    
if __name__ == "__main__":
    challenge = Challenge4('BRCA1', ['BRCA1', 'TP53', 'EGFR'], ['HER2', 'BRCA2', 'PTEN'])
    result = challenge.sequence_compare()
    print(f"Result: {result}")