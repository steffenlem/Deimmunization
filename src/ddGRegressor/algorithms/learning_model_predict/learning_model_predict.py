import pandas as pd


def predict_using_regression(regression, dataset_for_prediction):
    prediction = pd.DataFrame(data=regression.predict(dataset_for_prediction))
    predicted_dataset = pd.concat([dataset_for_prediction, prediction], axis=1, sort=False)
    return predicted_dataset
