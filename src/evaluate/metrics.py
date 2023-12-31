import numpy as np


def root_mean_squared_error(y_true, y_pred):
    MSE = np.square(np.subtract(y_true, y_pred)).mean(axis=0)
    RMSE = np.sqrt(MSE)
    return RMSE


def mean_absolute_error(y_true, y_pred):
    MAE = np.abs(np.subtract(y_true, y_pred)).mean(axis=0)
    return MAE


def mean_absolute_percentage_error(y_true, y_pred):
    mape = np.mean(np.abs((y_true - y_pred)/y_true))*100
    return mape


def bias_metric(y_true, y_pred):
    diff = np.subtract(y_true, y_pred)
    return np.nanmean(diff, axis=0)


def r_squared(y_true, y_preds):
    mean = np.mean(y_true)
    sst = np.sum(np.square(y_true - mean))
    ssr = np.sum(np.square(y_true - y_preds))
    return 1 - (ssr / sst)
