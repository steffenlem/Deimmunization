from src.EvoCS.io.parser.msa_parser import parse_and_setup_info
from src.EvoCS.io.writer.write_consensus_array import write_consensus_sequence


class MSA:
    consensus_sequence = []

    def __init__(self, input_msa, reference_sequence, majority_threshold):
        """
        Constructor
        :param input_msa: MSA in clustal format
        :param reference_sequence: name of the target sequence in the MSA
        :param majority_threshold: threshold value for the majority calculation at every position
        """
        self.consensus_sequence = write_consensus_sequence(parse_and_setup_info(input_msa, reference_sequence),
                                                           float(majority_threshold))

    def get_consensus_sequence(self):
        """
        Getter for the consensus sequence array
        :return: consensus sequence of the MSA
        """
        return self.consensus_sequence

    def get_sequence(self):
        """
        Getter for the target sequence
        :return: Target sequence as one String
        """
        return [x[0] for x in self.consensus_sequence]

    def write_sequnce(self, path):
        """
        Writes the target sequence to file
        :param path: path of the output file
        :return: void
        """
        with open(path, 'w') as f:
            f.write('>sequence\n')
            for x in self.consensus_sequence:
                f.write(str(x[0]))
