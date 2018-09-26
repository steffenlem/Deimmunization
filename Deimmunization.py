import subprocess
import time
import numpy as np



if __name__ == '__main__':
    start_time = time.time()

    result = subprocess.run(['/home/steffen/netMHCIIpan-3.2/netMHCIIpan', '-f', '/home/steffen/netMHCIIpan-3.2/test/example.fsa', '-a', 'DRB1_0101'], stdout=subprocess.PIPE)


    a = str(result.stdout)



    output = [x.split() for x in a.split('\\n')]
    output = [x for x in output if x != []]
    parsed_data = []
    for x in output:
        try:
            #check wether the line is data starting with a int
            int(x[0])
            #if the peptide is a binder (IC50 < 500 nM), then it is included
            if(float(x[8]) < 500):
                parsed_data.append([int(x[0]), x[1], x[2], int(x[4]) + int(x[0]), x[5], float(x[8])])
        except ValueError:
            #no prediction data -> do nothing
            pass



    print(parsed_data)
    print(np.array(parsed_data))









    print()
    print(time.time() - start_time, "seconds")