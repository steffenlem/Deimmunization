from src.MSAParser.io.parser.msa_parser import parse_and_setup_info
from src.MSAParser.io.writer.write_consensus_array import write_consensus_sequence


class MSA:
    consensus_sequence = []

    def __init__(self, input_msa, reference_sequence, majority_threshold):
        self.consensus_sequence = write_consensus_sequence(parse_and_setup_info(input_msa, reference_sequence),
                                                           float(majority_threshold))

    def get_consensus_sequence(self):
        return self.consensus_sequence

    def get_sequence(self):
        return [x[0] for x in self.consensus_sequence]

    def write_sequnce(self, path):
        with open(path, 'w') as f:
            f.write('>sequence\n')
            for x in self.consensus_sequence:
                f.write(str(x[0]))
