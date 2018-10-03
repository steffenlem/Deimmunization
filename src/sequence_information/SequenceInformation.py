class SequenceInformation:
    """
    Sequence Information class contains:
        - sequence:             protein sequence as 'char' array
        - msa:                  Multiple Sequence Alignment (MSA), as described in the MSA class
        - epitope_prediction:   epitope prediction data - array of prediction data for single allele
        - effect_of_mutation:   
    """
    sequence = []
    msa = []
    epitope_prediction = []
    effect_of_mutation = []

    def __init__(self, sequence, msa):
        """
        Constructor
        """
        self.sequence = sequence
        self.msa = msa

    def set_allele_prediction(self, prediction):
        """
        Setter for allele prediction data. For each allele the array is appended
        :param prediction:
        :return:
        """
        self.epitope_prediction.append(prediction)

    def get_sequence(self):
        """
        Getter for sequence information
        :return: Char array of the sequence
        """
        return self.sequence

    def get_sequence_pos(self, index):
        """
        Getter for amino acid at position index
        :param index:
        :return: Amino acid in one letter code
        """
        return self.sequence[index]

    def set_sequence_pos(self, residue, index):
        """
        Setter for individual amino acids in the protein (allows to mutate protein)
        :param residue: new residue at index position (one letter code)
        :param index: position in protein which should be mutated
        :return: void
        """
        self.sequence[index] = residue

    def get_length_sequence(self):
        """
        Getter for the length of the protein
        :return: length of protein as Integer
        """
        return len(self.sequence)

    def get_neighbour_chunk(self, index):
        """
        Writes the amino acids around index of the sequnce (the chunk) to a .fasta file
        With every call of this function, the file is overwritten, since it is only needed to update the
        epitope prediction in this specific part of the protein.
        The size of the chunk is determined by size of the epitopes predicted by NetMHCIIPan
        In this Tool the size is set to 15 amino acids. Therefore the .fasta will always have the size of 29 amino acids
        Exp. forpeptide length 15: [14 AS left], index AS, [14 AS right] --> 29 AS
        :param index: index of amino acid in the middle of the 'chunk'
        :return: void
        """
        seq = []
        peptide_length = 15  # TODO remove magic number

        if index >= (peptide_length - 1):  # check if index is next to start of the sequence
            if (len(self.sequence) - 1) >= (index + peptide_length - 1):
                seq = self.sequence[(index - (peptide_length - 1)):index + peptide_length]
            else:
                seq = self.sequence[(index - (peptide_length - 1)):]

        else:
            if (len(self.sequence) - 1) >= (index + peptide_length):
                seq = self.sequence[:(index + peptide_length)]
            else:
                print('Input Peptide Sequnce is too short')
                # such short sequences should not be accepted
                # this case should never be true
                # TODO implement input constraint, no sequences shorter than MHCII peptide length (15)

        with open('data/temp.fasta', 'w') as f:
            f.write('>sequence\n')
            for x in seq:
                f.write(str(x))

    def calculate_base_immunogenicity(self):
        """
        Calculation of the immunogenicity of the protein without any point mutations
        :return: immunogenicity (number of immune epitopes)
        """
        immunogenicity = 0
        # counts the number of epitopes found by NetMHCIIpan and sums them up
        for x in self.epitope_prediction:
            for y in x:
                immunogenicity += 1
        return immunogenicity

    # TODO Update MHC prediction around index

    # TODO muate sequence and save the position (constraints...)

    # TODO immunogenicity calculation for each individual allel and for all allels combinded
