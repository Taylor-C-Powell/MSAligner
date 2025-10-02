#!/usr/bin/env python3

# Challenge 1
# compare sequence accession numbers

class Challenge1:
    """
    A class to encapsulate the solution for Challenge 1.
    """

    def __init__(self, meta_dat_path: str, gene_dat_path: str):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.meta_dat = open(meta_dat_path, 'r').readlines()
        self.gene_dat = open(gene_dat_path, 'r').readlines()

    def find_common_accessions(self):
        print(self.gene_dat)

if __name__ == "__main__":
    Challenge1("data/Challenge1_meta.dat", "data/Challenge1_gene.dat").find_common_accessions()
