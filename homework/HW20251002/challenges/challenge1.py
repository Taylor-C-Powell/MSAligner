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

    def compile_metdat_accesions(self, met_dat: list) -> list:
        return [line.split(",")[3] for line in met_dat[1:]]
    
    def compile_genome_accessions(self, gene_dat: list) -> list:
        return [line for line in gene_dat if line.startswith(">")]

    def find_common_accessions(self):
        meta_accessions = self.compile_metdat_accesions(self.meta_dat)
        genome_accessions = self.compile_genome_accessions(self.gene_dat)
        common_accessions = [acc for acc in meta_accessions if any(acc in g_acc for g_acc in genome_accessions)]
        print("Common accessions found:")
        for acc in common_accessions:
            print(acc)

if __name__ == "__main__":
    Challenge1("homework\HW20251002\data\metadata.csv", "homework\HW20251002\data\genome.fasta").find_common_accessions()
