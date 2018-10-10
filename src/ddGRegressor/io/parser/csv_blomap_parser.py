import logging
import numpy as np
import pandas as pd

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Contact map parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parse_csv_blomap(input_csv_file, is_training_set):
    LOG.info("Parse contact map, setup datasets")
    dataset = pd.read_csv(input_csv_file, delimiter=',', header=None)
    if is_training_set:
        dataset = delete_upper_spikes(dataset)
        input_data = [dataset.iloc[:, :dataset.shape[1]-1]]
        input_data.append(dataset.iloc[:, dataset.shape[1]-1])
    else:
        input_data = dataset.iloc[:, :dataset.shape[1]-1]
    LOG.info("Finished parsing")
    return input_data


def delete_upper_spikes(dataset):
    list_df = list(dataset.iloc[:, :].values)
    ddGs = []
    for data in list_df:
        ddGs.append(data[len(data)-1])
    range = max(ddGs) - min(ddGs)
    upper_spike_threshhold = max(ddGs) - range * 0.25
    new_dataset = []
    i = 0
    for data in list_df:
        if not(data[len(data)-1] > upper_spike_threshhold):
            new_dataset.append(data)
    #     else:
    #         i += 1
    # print(range)
    # print(upper_spike_threshhold)
    # print(i)
    return pd.DataFrame(np.array(new_dataset))
