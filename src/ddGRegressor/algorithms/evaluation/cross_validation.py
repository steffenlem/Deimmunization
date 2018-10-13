import logging
import numpy as np

from sklearn.model_selection import cross_val_score

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("K-Fold-Crossvalidation")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def k_fold_cross_validation(regression, input_dataset):
    splits = 10
    data = input_dataset[0]
    ddGs = input_dataset[1]
    LOG.info("Perform "+str(splits)+"-fold-crossvalidation")
    k_fold = cross_val_score(regression, np.asarray(data), np.asarray(ddGs), cv=splits)
    k_fold_mean_absolute_error = cross_val_score(regression, np.asarray(data), np.asarray(ddGs), cv=splits,
                             scoring="neg_mean_absolute_error")
    k_fold_mean_squared_error = cross_val_score(regression, np.asarray(data), np.asarray(ddGs), cv=splits,
                                                 scoring="neg_mean_squared_error")

    LOG.info("Finished "+str(splits)+"-fold-crossvalidation")
    LOG.info('Mean-Absolute-Error: '+str(round(k_fold_mean_absolute_error.mean(), 2)))
    LOG.info('Mean-Squared-Error: '+str(round(k_fold_mean_squared_error.mean(), 2)))
    LOG.info('CV-Accuracy-Mean: '+str(round(k_fold.mean(), 2)*100)+'%')
    LOG.info('CV-Standard-Deviation: '+str(round(k_fold.std(), 2)))
    LOG.info('ddG-Interval: ['+str(ddGs.min())+', '+str(ddGs.max())+'] => Intervalsize: '+str(round(ddGs.max()-ddGs.min(), 2)))
    LOG.info('ddG-Deviation-Percentage: '+str(round(k_fold.std()*100/(ddGs.max()-ddGs.min()), 2))+"%")

