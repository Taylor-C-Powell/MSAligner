#!/usr/bin/env python3

# Challenge 1
# compare sequence accession numbers

class Challenge1:
    """
    A class to encapsulate the solution for Challenge 1.
    """

    # initialize class object with paths to data files
    def __init__(self, meta_dat_path: str, gene_dat_path: str):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.meta_dat = open(meta_dat_path, 'r').readlines()
        self.gene_dat = open(gene_dat_path, 'r').readlines()

    # Compile list of accessions from metadata and genome data
    def compile_metdat_accesions(self) -> list:
        return [line.split(",")[3] for line in self.meta_dat[1:]]

    def compile_genome_accessions(self) -> list:
        return [line for line in self.gene_dat if line.startswith(">")]

    # Find common accessions between metadata and genome data
    def find_common_accessions(self):
        meta_accessions = self.compile_metdat_accesions()
        genome_accessions = self.compile_genome_accessions()
        common_accessions = [acc for acc in meta_accessions if any(acc in g_acc for g_acc in genome_accessions)]
        return common_accessions
    
    # Find accesions that aren't shared between metadata and genome data
    def find_unique_accessions(self):
        meta_accessions = self.compile_metdat_accesions()
        genome_accessions = self.compile_genome_accessions()
        unique_meta = [acc for acc in meta_accessions if not any(acc in g_acc for g_acc in genome_accessions)]
        unique_genome = [g_acc for g_acc in genome_accessions if not any(g_acc.strip(">").startswith(acc) for acc in meta_accessions)]
        return unique_meta, unique_genome
    
    # Output results to CSV file
    def csv_output(self, output_path: str):
        with open(output_path, 'w') as out_file:
            out_file.write("Common Accessions\n")
            for acc in self.find_common_accessions():
                out_file.write(f"{acc}\n")
            out_file.write("\nUnique Metadata Accessions\n")
            for acc in self.find_unique_accessions()[0]:
                out_file.write(f"{acc}\n")
            out_file.write("\nUnique Genome Accessions\n")
            for acc in self.find_unique_accessions()[1]:
                out_file.write(f"{acc}\n")

# Main function to run the challenge
if __name__ == "__main__":
    met = "homework\HW20251002\data\metadata.csv"
    gen = "homework\HW20251002\data\genome.fasta"
    out_path = "homework\HW20251002\challenges\challenge1_output.csv"
    c1 = Challenge1(met, gen)
    c1.csv_output(out_path)
