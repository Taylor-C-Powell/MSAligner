#!/usr/bin/env python3
"""
Sequence alignment module using Needleman-Wunsch algorithm.
"""

import logging
from typing import Dict, Tuple, List
import numpy as np

# BLOSUM62 substitution matrix (complete, symmetric for standard 20 amino acids)
# Amino acids: A R N D C Q E G H I L K M F P S T W Y V
_BLOSUM62_ROWS = {
    'A': {'A': 4,  'R': -1, 'N': -2, 'D': -2, 'C': 0,  'Q': -1, 'E': -1, 'G': 0,  'H': -2, 'I': -1, 'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1,  'T': 0,  'W': -3, 'Y': -2, 'V': 0},
    'R': {'A': -1, 'R': 5,  'N': 0,  'D': -2, 'C': -3, 'Q': 1,  'E': 0,  'G': -2, 'H': 0,  'I': -3, 'L': -2, 'K': 2,  'M': -1, 'F': -3, 'P': -2, 'S': -1, 'T': -1, 'W': -3, 'Y': -2, 'V': -3},
    'N': {'A': -2, 'R': 0,  'N': 6,  'D': 1,  'C': -3, 'Q': 0,  'E': -1, 'G': 0,  'H': 1,  'I': -3, 'L': -3, 'K': 0,  'M': -2, 'F': -3, 'P': -2, 'S': 1,  'T': 0,  'W': -4, 'Y': -2, 'V': -3},
    'D': {'A': -2, 'R': -2, 'N': 1,  'D': 6,  'C': -3, 'Q': 0,  'E': 2,  'G': -1, 'H': -1, 'I': -3, 'L': -4, 'K': -1, 'M': -3, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -4, 'Y': -3, 'V': -3},
    'C': {'A': 0,  'R': -3, 'N': -3, 'D': -3, 'C': 9,  'Q': -3, 'E': -4, 'G': -3, 'H': -3, 'I': -1, 'L': -1, 'K': -3, 'M': -1, 'F': -2, 'P': -3, 'S': -1, 'T': -1, 'W': -2, 'Y': -2, 'V': -1},
    'Q': {'A': -1, 'R': 1,  'N': 0,  'D': 0,  'C': -3, 'Q': 5,  'E': 2,  'G': -2, 'H': 0,  'I': -3, 'L': -2, 'K': 1,  'M': 0,  'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -2, 'Y': -1, 'V': -2},
    'E': {'A': -1, 'R': 0,  'N': -1, 'D': 2,  'C': -4, 'Q': 2,  'E': 5,  'G': -2, 'H': 0,  'I': -3, 'L': -3, 'K': 1,  'M': -2, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'G': {'A': 0,  'R': -2, 'N': 0,  'D': -1, 'C': -3, 'Q': -2, 'E': -2, 'G': 6,  'H': -2, 'I': -4, 'L': -4, 'K': -2, 'M': -3, 'F': -3, 'P': -2, 'S': 0,  'T': -2, 'W': -2, 'Y': -3, 'V': -3},
    'H': {'A': -2, 'R': 0,  'N': 1,  'D': -1, 'C': -3, 'Q': 0,  'E': 0,  'G': -2, 'H': 8,  'I': -3, 'L': -3, 'K': -1, 'M': -2, 'F': -1, 'P': -2, 'S': -1, 'T': -2, 'W': -2, 'Y': 2,  'V': -3},
    'I': {'A': -1, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -3, 'E': -3, 'G': -4, 'H': -3, 'I': 4,  'L': 2,  'K': -3, 'M': 1,  'F': 0,  'P': -3, 'S': -2, 'T': -1, 'W': -3, 'Y': -1, 'V': 3},
    'L': {'A': -1, 'R': -2, 'N': -3, 'D': -4, 'C': -1, 'Q': -2, 'E': -3, 'G': -4, 'H': -3, 'I': 2,  'L': 4,  'K': -2, 'M': 2,  'F': 0,  'P': -3, 'S': -2, 'T': -1, 'W': -2, 'Y': -1, 'V': 1},
    'K': {'A': -1, 'R': 2,  'N': 0,  'D': -1, 'C': -3, 'Q': 1,  'E': 1,  'G': -2, 'H': -1, 'I': -3, 'L': -2, 'K': 5,  'M': -1, 'F': -3, 'P': -1, 'S': 0,  'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'M': {'A': -1, 'R': -1, 'N': -2, 'D': -3, 'C': -1, 'Q': 0,  'E': -2, 'G': -3, 'H': -2, 'I': 1,  'L': 2,  'K': -1, 'M': 5,  'F': 0,  'P': -2, 'S': -1, 'T': -1, 'W': -1, 'Y': -1, 'V': 1},
    'F': {'A': -2, 'R': -3, 'N': -3, 'D': -3, 'C': -2, 'Q': -3, 'E': -3, 'G': -3, 'H': -1, 'I': 0,  'L': 0,  'K': -3, 'M': 0,  'F': 6,  'P': -4, 'S': -2, 'T': -2, 'W': 1,  'Y': 3,  'V': -1},
    'P': {'A': -1, 'R': -2, 'N': -2, 'D': -1, 'C': -3, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -3, 'L': -3, 'K': -1, 'M': -2, 'F': -4, 'P': 7,  'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -2},
    'S': {'A': 1,  'R': -1, 'N': 1,  'D': 0,  'C': -1, 'Q': 0,  'E': 0,  'G': 0,  'H': -1, 'I': -2, 'L': -2, 'K': 0,  'M': -1, 'F': -2, 'P': -1, 'S': 4,  'T': 1,  'W': -3, 'Y': -2, 'V': -2},
    'T': {'A': 0,  'R': -1, 'N': 0,  'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -1, 'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1,  'T': 5,  'W': -2, 'Y': -2, 'V': 0},
    'W': {'A': -3, 'R': -3, 'N': -4, 'D': -4, 'C': -2, 'Q': -2, 'E': -3, 'G': -2, 'H': -2, 'I': -3, 'L': -2, 'K': -3, 'M': -1, 'F': 1,  'P': -4, 'S': -3, 'T': -2, 'W': 11, 'Y': 2,  'V': -3},
    'Y': {'A': -2, 'R': -2, 'N': -2, 'D': -3, 'C': -2, 'Q': -1, 'E': -2, 'G': -3, 'H': 2,  'I': -1, 'L': -1, 'K': -2, 'M': -1, 'F': 3,  'P': -3, 'S': -2, 'T': -2, 'W': 2,  'Y': 7,  'V': -1},
    'V': {'A': 0,  'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -2, 'E': -2, 'G': -3, 'H': -3, 'I': 3,  'L': 1,  'K': -2, 'M': 1,  'F': -1, 'P': -2, 'S': -2, 'T': 0,  'W': -3, 'Y': -1, 'V': 4},
}

# Expand to full pair dictionary with symmetric entries
BLOSUM62 = {}
for a1, row in _BLOSUM62_ROWS.items():
    for a2, score in row.items():
        BLOSUM62[(a1, a2)] = score
        BLOSUM62[(a2, a1)] = score

def get_blosum_score(aa1: str, aa2: str) -> int:
    """
    Get BLOSUM62 score for two amino acids.
    
    Args:
        aa1: First amino acid
        aa2: Second amino acid
        
    Returns:
        BLOSUM62 score
    """
    if aa1 == 'X' or aa2 == 'X':  # Unknown/ambiguous amino acid
        return -1
    return BLOSUM62.get((aa1, aa2), -4)  # Default penalty for uncommon pairs

def needleman_wunsch(seq1: str, seq2: str, gap_penalty: int = -8) -> Tuple[str, str, float]:
    """
    Perform Needleman-Wunsch global alignment.
    
    Args:
        seq1: First sequence
        seq2: Second sequence
        gap_penalty: Gap penalty score
        
    Returns:
        Tuple of (aligned_seq1, aligned_seq2, alignment_score)
    """
    m, n = len(seq1), len(seq2)
    
    # Initialize matrices
    score_matrix = np.zeros((m + 1, n + 1))
    traceback = np.zeros((m + 1, n + 1), dtype=int)
    
    # Initialize first row and column
    for i in range(1, m + 1):
        score_matrix[i, 0] = i * gap_penalty
        traceback[i, 0] = 1  # Up
    for j in range(1, n + 1):
        score_matrix[0, j] = j * gap_penalty
        traceback[0, j] = 2  # Left
    
    # Fill matrices
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_score = score_matrix[i-1, j-1] + get_blosum_score(seq1[i-1], seq2[j-1])
            delete_score = score_matrix[i-1, j] + gap_penalty
            insert_score = score_matrix[i, j-1] + gap_penalty
            
            scores = [match_score, delete_score, insert_score]
            best_score = max(scores)
            best_direction = scores.index(best_score)
            
            score_matrix[i, j] = best_score
            traceback[i, j] = best_direction
    
    # Traceback
    aligned1, aligned2 = [], []
    i, j = m, n
    
    while i > 0 or j > 0:
        if traceback[i, j] == 0:  # Diagonal
            aligned1.append(seq1[i-1])
            aligned2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif traceback[i, j] == 1:  # Up
            aligned1.append(seq1[i-1])
            aligned2.append('-')
            i -= 1
        else:  # Left
            aligned1.append('-')
            aligned2.append(seq2[j-1])
            j -= 1
    
    aligned1 = ''.join(reversed(aligned1))
    aligned2 = ''.join(reversed(aligned2))

    return aligned1, aligned2, score_matrix[m, n]

def progressive_alignment(sequences: Dict[str, dict], sorted_ids: List[str], 
                         gap_penalty: int = -8) -> Dict[str, str]:
    """
    Perform progressive multiple sequence alignment.
    
    Args:
        sequences: Dictionary of processed sequences
        sorted_ids: Sequence IDs sorted by similarity
        gap_penalty: Gap penalty for alignment
        
    Returns:
        Dictionary mapping sequence IDs to aligned sequences
    """
    if not sorted_ids:
        return {}
    
    # Start with first sequence
    aligned_seqs = {sorted_ids[0]: sequences[sorted_ids[0]]['amino_acid']}
    
    for seq_id in sorted_ids[1:]:
        current_seq = sequences[seq_id]['amino_acid']
        
        # Align with existing profile (simplified: align with first sequence)
        # In a full implementation, this would use profile-profile alignment
        ref_seq_id = sorted_ids[0]  # Simplified approach
        ref_aligned = aligned_seqs[ref_seq_id]
        
        # Align current sequence with reference
        aligned_current, aligned_ref, score = needleman_wunsch(
            current_seq, ref_aligned.replace('-', ''), gap_penalty
        )
        
        # Add gaps to all existing sequences to match new alignment
        for existing_id in aligned_seqs:
            if existing_id != ref_seq_id:
                # Add gaps to maintain alignment
                aligned_seqs[existing_id] = add_gaps_to_match(
                    aligned_seqs[existing_id], aligned_ref
                )
        
        aligned_seqs[seq_id] = aligned_current
    
    return aligned_seqs

def add_gaps_to_match(seq: str, target: str) -> str:
    """
    Add gaps to sequence to match target alignment length.
    
    Args:
        seq: Original sequence
        target: Target sequence with gaps
        
    Returns:
        Sequence with added gaps
    """
    result = []
    seq_pos = 0
    
    for char in target:
        if char == '-':
            result.append('-')
        else:
            if seq_pos < len(seq):
                result.append(seq[seq_pos])
                seq_pos += 1
            else:
                result.append('-')
    
    # Add remaining sequence if any
    while seq_pos < len(seq):
        result.append(seq[seq_pos])
        seq_pos += 1
    
    return ''.join(result)

def perform_progressive_alignment(sequences: Dict[str, dict], 
                                gap_penalty: int = -8) -> Dict[str, str]:
    """
    Main function to perform progressive multiple sequence alignment.
    
    Args:
        sequences: Dictionary of processed sequences
        gap_penalty: Gap penalty for alignment
        
    Returns:
        Dictionary of aligned amino acid sequences
    """
    sorted_ids = list(sequences.keys())  # Already sorted from previous step
    
    if len(sorted_ids) == 1:
        return {sorted_ids[0]: sequences[sorted_ids[0]]['amino_acid']}
    
    aligned_sequences = progressive_alignment(sequences, sorted_ids, gap_penalty)
    
    logging.info(f"Completed progressive alignment of {len(aligned_sequences)} sequences")
    return aligned_sequences