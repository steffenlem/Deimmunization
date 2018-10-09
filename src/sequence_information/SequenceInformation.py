from src.netMHCIIpanParser.netMHCIIparser import parse_netMHCIIpan
import random


class SequenceInformation:
    """
    Sequence Information class contains:
        - sequence:             protein sequence as 'char' array
        - msa:                  Multiple Sequence Alignment (MSA), as described in the MSA class
        - epitope_prediction:   epitope prediction data - array of prediction data for single allele
        - base_immunogenicity:  immnogenicity of sequence without any mutations
        - effect_of_mutation:   [amino_acid, index, immunogenicity, ddG] --> Index of array not pos in sequence
    """
    sequence = []
    msa = []
    epitope_prediction = []
    base_immunogenicity = 0
    effect_of_mutation = []
    part_of_core_pos = []
    queue = []

    def __init__(self, sequence, msa):
        """
        Constructor
        """
        self.sequence = sequence
        self.msa = msa
        self.epitope_prediction = []
        self.base_immunogenicity = 0
        self.effect_of_mutation = []
        self.part_of_core_pos = {}
        self.queue = []

    def set_allele_prediction(self, prediction):
        """
        Setter for allele prediction data. For each allele the array is appended
        :param prediction:
        :return:
        """
        self.epitope_prediction.append(prediction)

    def get_epitope_prediction(self):
        """
        Getter for epitope prediction data
        :return: the prediction data
        """
        return self.epitope_prediction

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

    def get_msa(self):
        """
        Getter for MSA
        :return: the MSA
        """
        return self.msa

    def base_immunogenicity(self):
        """
        Getter for base base_immunogenicity
        :return: the immunogenicity
        """
        return self.base_immunogenicity

    def write_sequence(self, path):
        """
        Write Sequnce to FastA text file
        :param path: the path for the output
        :return: void
        """
        with open(path, 'w') as f:
            f.write('>sequence\n')
            for x in self.sequence:
                f.write(str(x))

    def write_neighbour_chunk(self, index, amino_acid):
        """
        Writes the amino acids around index of the sequnce (the chunk) to a .fasta file
        With every call of this function, the file is overwritten, since it is only needed to update the
        epitope prediction in this specific part of the protein.
        The size of the chunk is determined by size of the epitopes predicted by NetMHCIIPan
        In this Tool the size is set to 15 amino acids. Therefore the .fasta will always have the size of 29 amino acids
        Exp. forpeptide length 15: [14 AS left], index AS, [14 AS right] --> 29 AS
        :param index: index of amino acid in the middle of the 'chunk' (pos 1 of amino acid is index 0)
        :param amino_acid: amino acid after mutation
        :return: void
        """
        seq = self.get_sequence().copy()
        seq[index] = amino_acid
        chunk = []
        peptide_length = 15  # TODO remove magic number

        if index >= (peptide_length - 1):  # check if index is next to start of the sequence
            if (len(seq) - 1) >= (index + peptide_length - 1):
                chunk = seq[(index - (peptide_length - 1)):index + peptide_length]
            else:
                chunk = seq[(index - (peptide_length - 1)):]

        else:
            if (len(seq) - 1) >= (index + peptide_length):
                chunk = seq[:(index + peptide_length)]
            else:
                print('Input Peptide Sequnce is too short')
                # such short sequences should not be accepted
                # this case should never be true
                # TODO implement input constraint, no sequences shorter than MHCII peptide length (15)

        with open('data/temp.fasta', 'w') as f:
            f.write('>sequence\n')
            for x in chunk:
                f.write(str(x))

    def calculate_base_immunogenicity(self):
        """
        Calculation of the immunogenicity of the protein without any point mutations
        :return: immunogenicity (number of immune epitopes)
        """
        immunogenicity = 0
        # counts the number of epitopes found by NetMHCIIpan and sums them up
        for allele in self.epitope_prediction:
            for x in allele:
                immunogenicity += 1
        self.base_immunogenicity = immunogenicity

    def append_effect_of_mutation(self, amino_acid, index, immunogenicity, ddG):
        """
        Adds array containing this function's parameters information to the effect_of_mutation array
        :param amino_acid: amino acid after muation
        :param index:  index of muation in the sequence
        :param immunogenicity: value for immunogenicity
        :param ddG: value for free folding energy
        :return: void
        """
        self.effect_of_mutation.append([amino_acid, index, immunogenicity, ddG])

    def get_effect_of_mutation(self):
        """
        Getter for effect_of_mutation array
        :return: the array
        """
        return self.effect_of_mutation

    def update_immunogenicity(self, amino_acid, index, mhc_pan_path):
        """
        Calculation of updated immunogenicity using only the edited part for a new prediction
        :param amino_acid: changed to this amino acid
        :param index: index of changed amino acid in sequence
        :param mhc_pan_path: Path of NetMHCIIpan
        :return: updated immunogenicity
        """
        new_imm = 0
        self.write_neighbour_chunk(index, amino_acid)
        peptide_length = 15
        immunogenicity = 0
        for allele in self.epitope_prediction:
            for x in allele:
                if not ((x[0] <= (index + 1)) and (x[0] > index - (peptide_length - 1))):
                    immunogenicity += 1

            new_imm += len(parse_netMHCIIpan(mhc_pan_path, 'data/temp.fasta', allele[0][1]))

        return immunogenicity + new_imm


    def determine_mutable_positions(self):
        """
        Determines all position which are allowed to be mutated
        :return: [index, 'group']
        """
        mutable_pos = []
        one_letter_code = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y',
                           'V', 'H']
        for x in range(len(self.msa)):
            """
            Only true if:
            the majority is not a single amino acids,but a class of amino acids
            The amino acid is not Glycine or Proline
            """
            if self.msa[x][1] not in one_letter_code and self.msa[x][0] not in ['G', 'P']:
                mutable_pos.append([x, self.msa[x][1]])
        return mutable_pos

    def calculate_binding_core(self):
        """
        Calculates number of epitope binding cores the amino acids are part of
        :return: [index of start of core, number of cores]
        """
        calc_epitope = {}
        for allele in self.epitope_prediction:
            for x in allele:
                for z in range(9):

                    if x[3] - 1 + z in calc_epitope:
                        calc_epitope[x[3] - 1 + z] = calc_epitope[x[3] - 1 + z] + 1
                    else:
                        calc_epitope[x[3] - 1 + z] = 1
        self.part_of_core_pos = [[key, value] for key, value in calc_epitope.items()]
        self.part_of_core_pos.sort(key=lambda y: y[1], reverse=True) # TODO 'best position'...

    def make_queue_mutation(self):
        """
        Creates a queue for sequences to be mutated
        :return: void
        """
        mutatbale_pos = [x[0] for x in self.determine_mutable_positions()]
        for x in self.part_of_core_pos:
            if x[0] in mutatbale_pos:
                self.queue.append(x[0])

    def introduce_mutations(self, mutations):
        if mutations is None:
            pass
        else:
            for x in mutations:
                self.set_sequence_pos(x.amino_acid, x.index)


