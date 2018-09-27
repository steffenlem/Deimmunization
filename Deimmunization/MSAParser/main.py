import click
import logging
import sys

from Deimmunization.MSAParser.io.parser.msa_parser import parse_and_setup_info
from Deimmunization.MSAParser.io.writer.write_consensus_array import write_consensus_sequence

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Commandline parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def get_inputfile_start_parser(input_msa, reference_sequence, majority_threshold):
    LOG.info("Start MSA-Parser")

    consensus_array = write_consensus_sequence(
        parse_and_setup_info(input_msa, reference_sequence), float(majority_threshold))
    LOG.info("Consensus-Array ready!")
    LOG.info("End MSA-Parser")