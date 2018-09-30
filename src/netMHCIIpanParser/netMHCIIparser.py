# Parses and filters the Output of NetMHCIIpan for binding peptides (IC50 < 500 nM)
import subprocess


def parse_netMHCIIpan(mhc_pan_path, file_path, allel):
    result = subprocess.run([mhc_pan_path, '-f', file_path, '-a', allel], stdout=subprocess.PIPE)

    a = str(result.stdout)

    output = [x.split() for x in a.split('\\n')]
    output = [x for x in output if x != []]

    print(output)
    parsed_data = []
    seq_length = 15
    for x in output:
        try:
            # check wether the line is data starting with a int
            int(x[0])
            seq_length += 1
            # if the peptide is a binder (IC50 < 500 nM), then it is included
            if float(x[8]) < 500:
                parsed_data.append([int(x[0]), x[1], x[2], int(x[4]) + int(x[0]), x[5], float(x[8])])
        except ValueError:
            # no prediction data -> do nothing
            pass
    return parsed_data
