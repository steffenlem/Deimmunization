import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
import click
import logging

from Deimmunization.MSAParser.main import get_inputfile_start_parser
from Deimmunization.netMHCIIpanParser.netMHCIIparser import parse_netMHCIIpan
console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Commandline parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)

#python3 Deimmunization.py -in /home/steffen/Documents/Deimmunization/data/clustalo-I20180923-185956-0934-78103081-p2m.clustal_num.txt -rs BoNTC -t 0.5 -a DRB1_0301 -p /home/steffen/netMHCIIpan-3.2/netMHCIIpan

@click.command()
@click.option('-in', '--input_msa', prompt='input msa',
              help='file path to msa.txt', required=True)
@click.option('-rs', '--reference_sequence', prompt='reference sequence',
              help='titlestring of reference sequence', required=True)
@click.option('-t', '--majority_threshold', prompt='majority threshold',
              help='value between 0 and 1 to decide the consensus value', required=True, default=0.5)
@click.option('-a', '--mhc_alle', prompt='mhc_alles',
              help='MHC class II allel e.g. DRB1_0101', required=True)
@click.option('-p', '--mhc_ii_pan', prompt='MHCIIpan',
              help='path to MHCIIpan',required=True)




def main(input_msa, reference_sequence, majority_threshold, mhc_alle, mhc_ii_pan):
    start_time = time.time()
    get_inputfile_start_parser(input_msa, reference_sequence, majority_threshold)
    parsed_data = parse_netMHCIIpan('/home/steffen/netMHCIIpan-3.2/netMHCIIpan', 'data/2wcv.fasta', 'DRB1_0301')


    ###Transfer sequence and alignment and length to separate class (for every MHC one?)###

    ###Transfer to separate module###
    #Simple Visualization of Epitopes and binding cores
    number_epitopes = np.zeros(int(parsed_data[-1][0])+15)
    for x in parsed_data:
        for z in range(9):
            number_epitopes[int(x[3])-1+z] =  number_epitopes[int(x[3])-1+z] + 1

    #Time
    print()
    print(time.time() - start_time, "seconds")

    #Plot Binding Cores
    plt.plot(number_epitopes)
    plt.show()


if __name__ == '__main__':
    main()