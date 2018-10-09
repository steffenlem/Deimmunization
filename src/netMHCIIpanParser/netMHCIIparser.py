# Parses and filters the Output of NetMHCIIpan for binding peptides (IC50 < 500 nM)
import subprocess


def parse_netMHCIIpan(mhc_pan_path, file_path, allele):
    """function calls NetMHCIIpan algorithm predict the epitopes of the input file (file_path)
    for a given allele"""

    # Console output of NetMHCIIpan is saved in "result"
    result = subprocess.run([mhc_pan_path, '-f', file_path, '-a', allele], stdout=subprocess.PIPE)
    result = str(result.stdout)

    # result is split and empty lines are removed
    result = [x.split() for x in result.split('\\n')]
    result = [x for x in result if x != []]

    # parsed_data contains only peptides with an IC50 < 500 nM
    # parsed_data = [[starting position of peptide, allele, peptide sequence, starting position of core, IC50], ...]
    parsed_data = []
    for x in result:
        try:
            # check whether the line is data starting with a int
            int(x[0])
            # if the peptide is a binder (IC50 < 500 nM), then it is included
            if float(x[8]) < 500:
                parsed_data.append([int(x[0]), x[1], x[2], int(x[4]) + int(x[0]), x[5], float(x[8])])
        except ValueError:
            # no prediction data -> do nothing
            pass
    return parsed_data
