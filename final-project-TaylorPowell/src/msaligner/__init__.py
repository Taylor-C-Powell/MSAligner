"""
Translation-Based Multiple Sequence Aligner

A Python package for performing translation-based multiple sequence alignment
using ORF detection, k-mer similarity, and Needleman-Wunsch alignment.
"""

__version__ = "1.0.0"
__author__ = "Student Name"

from msaligner.orf_detection import detect_orf, translate_sequence
from msaligner.kmer_similarity import compute_kmer_similarity, sort_sequences
from msaligner.alignment import needleman_wunsch, progressive_alignment
from msaligner.back_translation import back_translate_alignment
from msaligner.statistics import calculate_codon_statistics
from msaligner.visualization import plot_codon_variability