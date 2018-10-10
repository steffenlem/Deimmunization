# Indexing every aminoacidclass
aminoacid_classes_by_number = {
    0: '-',  # negative
    1: 'o',  # alcoholic
    2: 'u',  # tiny
    3: '+',  # positive
    4: 'l',  # aliphatic
    5: 'a',  # aromatic
    6: 'c',  # charged
    7: 's',  # small
    8: 'p',  # polar
    9: 't',  # turnlike
    10: 'h'  # hydrophobic
}

# Aminoacid contained in each aminoacidclass
aminoacid_classes_by_code = {
    '-': ['D', 'E'],
    'o': ['S', 'T'],
    'u': ['A', 'G', 'S'],
    '+': ['H', 'K', 'R'],
    'l': ['I', 'L', 'V'],
    'a': ['F', 'H', 'W', 'Y'],
    'c': ['D', 'E', 'H', 'K', 'R'],
    's': ['A', 'C', 'D', 'G', 'N', 'P', 'S', 'T', 'V'],
    'p': ['C', 'D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T'],
    't': ['A', 'C', 'D', 'E', 'G', 'H', 'K', 'N', 'Q', 'R', 'S', 'T'],
    'h': ['A', 'C', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'R', 'T', 'V', 'W', 'Y']
}

# Encoding simple index for each onletter-aminoacid-code
one_letter_encoding_to_number = {
    'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4,
    'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9,
    'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14,
    'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19
}

# Encoding each onletter-aminoacid-code for simple indeces
one_letter_encoding_to_letter = {
    0: 'A', 1: 'C', 2: 'D', 3: 'E', 4: 'F',
    5: 'G', 6: 'H', 7: 'I', 8: 'K', 9: 'L',
    10: 'M', 11: 'N', 12: 'P', 13: 'Q', 14: 'R',
    15: 'S', 16: 'T', 17: 'V', 18: 'W', 19: 'Y'
}
