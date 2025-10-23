#!/usr/bin/env python3

import pandas as pd
import numpy as np

fasta_file = "Labs\\2025-10-28\\sequences.fasta"

def parse_fasta(fasta_file):
    with open(fasta_file, 'r') as file:
        sequences = {}
        current_seq_name = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_seq_name = line[1:]
                sequences[current_seq_name] = ""
            else:
                sequences[current_seq_name] += line
    return sequences  