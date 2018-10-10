import logging

from src.MSAParser.algorithm.majority_count import compute_majorities

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Consensus sequence writer")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def write_consensus_sequence(msa_content, threshold):
    # Write consensus array
    LOG.info("Start writing consensus array")
    consensus_array = []
    LOG.info("Compute majority classes and gapcounts")
    for section in msa_content:
        section = parse_for_sequence_only(section)
        # Collect all acids at every msa-position
        for i in range(len(section[0])):  # acidpos in line
            aminoacids_at_position = []
            for j in range(len(section)):  # line
                if j == 0:
                    if section[j][i] != '-':
                        aminoacids_at_position.append(section[j][i])
                    else:
                        break
                else:
                    aminoacids_at_position.append(section[j][i])
            # If list of acids at position not empty, compute major acid/-class and percentage-gapcount
            # Append output to consensus array
            if aminoacids_at_position:
                major_class, gapcount = compute_majorities(aminoacids_at_position, threshold)
                consensus_array.append([aminoacids_at_position[0], major_class, gapcount])

    LOG.info("Finish computation for majority classes and gapcounts")

    return consensus_array


def parse_for_sequence_only(section):
    # Remove protein-titles at the beginning, and residue indices at the end of every msa-line
    newsection = []
    for line in section:
        line = line.replace('\t', ' ').split(' ')
        newsection.append(line[1])
    return newsection
