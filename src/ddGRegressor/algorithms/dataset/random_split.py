import logging

from sklearn.model_selection import train_test_split

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Random dataset split")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def random_dataset_split(input_dataset):
    LOG.info("Split dataset into testing- and trainingset")
    dataset_train, dataset_test, ddG_train, ddG_test = train_test_split(input_dataset[0], input_dataset[1], test_size=0.2)
    LOG.info("Finished splitting dataset")
    return dataset_train, dataset_test, ddG_train, ddG_test