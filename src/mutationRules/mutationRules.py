# mutation_order_by_group = {
#     ' ': ['D', 'S', 'T', 'N', 'C', 'H', 'M', 'W', 'K', 'A', 'Q', 'F', 'Y', 'A', 'V', 'I', 'E', 'L', 'P', 'G'],   # gap https://arxiv.org/pdf/q-bio/0505046.pdf
#     '-': ['D', 'E', 'Q', 'N', 'S', 'K', 'H', 'R', 'P', 'T', 'A', 'G', 'V', 'Y', 'M', 'F', 'I', 'C', 'L', 'W'],   # negative
#     'o': ['S', 'T', 'N', 'A', 'K', 'E', 'Q', 'D', 'V', 'M', 'C', 'R', 'G', 'P', 'L', 'I', 'H', 'Y', 'F', 'W'],   # alcoholic
#     'u': ['A', 'S', 'G', 'N', 'T', 'D', 'Q', 'E', 'K', 'R', 'C', 'H', 'M', 'V', 'P', 'I', 'L', 'F', 'Y', 'W'],   # tiny
#     '+': ['H', 'K', 'R', 'Q', 'N', 'E', 'S', 'Y', 'A', 'D', 'M', 'T', 'P', 'G', 'L', 'F', 'W', 'V', 'V', 'I'],   # positive
#     'l': ['I', 'L', 'V', 'M', 'F', 'A', 'T', 'C', 'Y', 'S', 'Q', 'K', 'R', 'E', 'W', 'P', 'N', 'H', 'D', 'W'],   # aliphatic
#     'a': ['F', 'H', 'W', 'Y', 'M', 'Q', 'L', 'I', 'R', 'N', 'E', 'S', 'T', 'V', 'A', 'C', 'K', 'D', 'G', 'P'],   # aromatic
#     'c': ['D', 'E', 'H', 'K', 'R', 'Q', 'N', 'S', 'T', 'A', 'P', 'Y', 'G', 'M', 'F', 'V', 'L', 'I', 'W', 'C'],   # charged
#     's': ['A', 'C', 'D', 'G', 'N', 'P', 'S', 'T', 'V', 'I', 'L', 'M', 'F', 'Y', 'Q', 'E', 'K', 'R', 'H', 'W'],   # small
#     'p': ['C', 'D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T', 'A', 'M', 'G', 'P', 'Y', 'V', 'L', 'F', 'I', 'W'],   # polar
#     't': ['A', 'C', 'D', 'E', 'G', 'H', 'K', 'N', 'Q', 'R', 'S', 'T', 'M', 'P', 'Y', 'V', 'L', 'I', 'F', 'W'],   # turnlike
#     'h': ['A', 'C', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'R', 'T', 'V', 'W', 'Y', 'S', 'Q', 'N', 'E', 'D', 'P']    # hydrophobic
#}

mutation_order_by_group = {
    '-': ['D', 'E'],
    'o': ['S', 'T'],
    'u': ['A', 'G', 'S'],
    '+': ['H', 'K', 'R'],
    'l': ['I', 'L', 'V'],
    'a': ['F', 'H', 'W', 'Y'],
    'c': ['D', 'E', 'H', 'K', 'R'],
    's': ['A', 'C', 'D', 'G', 'N', 'S', 'T', 'V'],
    'p': ['C', 'D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T'],
    't': ['A', 'C', 'D', 'E', 'G', 'H', 'K', 'N', 'Q', 'R', 'S', 'T'],
    'h': ['A', 'C', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'R', 'T', 'V', 'W', 'Y']
}