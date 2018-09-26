import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    start_time = time.time()


    ###Transfer to separate module###
    #Argparser...
    result = subprocess.run(['/home/steffen/netMHCIIpan-3.2/netMHCIIpan', '-f', 'data/BoTC_mutations_TEV.fasta', '-a', 'DRB1_0301'], stdout=subprocess.PIPE)


    a = str(result.stdout)



    output = [x.split() for x in a.split('\\n')]
    output = [x for x in output if x != []]
    parsed_data = []
    seq_length = 15
    for x in output:
        try:
            #check wether the line is data starting with a int
            int(x[0])
            seq_length += 1
            #if the peptide is a binder (IC50 < 500 nM), then it is included
            if(float(x[8]) < 500):
                parsed_data.append([int(x[0]), x[1], x[2], int(x[4]) + int(x[0]), x[5], float(x[8])])
        except ValueError:
            #no prediction data -> do nothing
            pass

    print(np.array(parsed_data))

    ###Transfer to separate module###
    #Simple Visualization of Epitopes and binding cores
    number_epitopes = np.zeros(seq_length)
    for x in parsed_data:
        for z in range(9):
            number_epitopes[int(x[3])-1+z] =  number_epitopes[int(x[3])-1+z] + 1



    #Time
    print()
    print(time.time() - start_time, "seconds")

    #Plot Binding Cores
    plt.plot(number_epitopes)
    plt.show()