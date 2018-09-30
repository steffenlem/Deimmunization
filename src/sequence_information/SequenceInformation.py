class SequenceInformation:
    sequence = []
    msa = []
    epitope_prediction = []

    def __init__(self, sequence, msa):
        self.sequence = sequence
        self.msa = msa

    def set_allel_prediction(self, prediction):
        self.epitope_prediction.append(prediction)

    def get_sequence(self):
        return self.sequence

    def get_sequence_pos(self, index):
        return self.sequence[index]

    def set_sequence_pos(self, residude, index):
        self.sequence[index] = residude

    def get_length_sequence(self):
        return len(self.sequence)

    # Returns the amino acids around index of the sequnce
    # Exp. forpeptide length 15: [14 AS left], index AS, [14 AS right] --> 29 AS
    def get_neighbour_chunk(self, index):
        seq = []
        peptide_length = 15  # TODO remove magic number

        if (index >= (peptide_length - 1)):  # check if index is next to start of the sequence
            if ((len(self.sequence) - 1) >= (index + peptide_length - 1)):
                seq = self.sequence[(index - (peptide_length - 1)):index + peptide_length]
            else:
                seq = self.sequence[(index - (peptide_length - 1)):]

        else:
            if ((len(self.sequence) - 1) >= (index + peptide_length)):
                seq = self.sequence[:(index + peptide_length)]
            else:
                print('Input Peptide Sequnce is too short')
                # such short sequences should not be accepted
                # TODO implement input constraint, no sequneces shorter than MHCII peptide length (15)

        with open('data/temp.fasta', 'w') as f:
            f.write('>sequence\n')
            for x in seq:
                f.write(str(x))

    # TODO Update MHC prediction around index

    # TODO muate sequence and save the position (constraints...)

    # TODO immunogenicity calculation for each individual allel and for all allels combinded
