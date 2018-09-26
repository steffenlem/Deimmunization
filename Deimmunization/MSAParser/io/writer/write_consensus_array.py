import logging

from Deimmunization.MSAParser.algorithm.majority_count import compute_majorities

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Consensus sequence writer")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def write_consensus_sequence(msa_content, threshold):
    LOG.info("Start writing consensus array")
    consensus_array = []
    LOG.info("Compute majority classes and gapcounts")
    for section in msa_content:
        section = parse_for_sequence_only(section)
        # print(section)
        for i in range(len(section[0])): #acidpos in line
            aminoacids_at_position = []
            for j in range(len(section)): #line
                if j == 0:
                    if section[j][i] != '-':
                        aminoacids_at_position.append(section[j][i])
                    else:
                        break
                else:
                    aminoacids_at_position.append(section[j][i])
            if aminoacids_at_position:
                major_class, gapcount = compute_majorities(aminoacids_at_position, threshold)
                consensus_array.append([aminoacids_at_position[0], major_class, gapcount])
    LOG.info("Finish computation for majority classes and gapcounts")
    LOG.info("End writing consensus array")
    LOG.info("Write consensus array in textfiles")
    with open('data/consensus_array.txt', 'w') as f:
        f.write('\n'.join(str(x) for x in consensus_array))
    with open('data/consensus_array_titled.txt', 'w') as f:
        i = 1
        f.write("MSA-CONSENSUS-ARRAY using a "+str(int(threshold*100))+"%-threshold\n\n")
        for x in consensus_array:
            line = "Pos."+str(i)+": "+str(x)+'\n'
            f.write(line)
            i += 1
    LOG.info("End writing files")

    return consensus_array


def parse_for_sequence_only(section):
    newsection = []
    for line in section:
        line = line.replace('\t', ' ').split(' ')
        newsection.append(line[1])
    return newsection
