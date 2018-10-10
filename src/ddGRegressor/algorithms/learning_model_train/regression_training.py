import logging


console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Regression training")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def train_regression(regressor, regressor_name, dataset_train, ddG_train):
    LOG.info("Start "+regressor_name+" regression training")
    regression = regressor.fit(dataset_train, ddG_train)
    LOG.info("Finished "+regressor_name+" regression training")
    return regression