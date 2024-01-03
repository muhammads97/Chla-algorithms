#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#


import numpy as np
from src.evaluate.metrics import *
from src.evaluate.scatter_plot import scatter_plot


class Estimator:
    def __init__(self) -> None:
        pass

    def estimate(self, rrs: np.ndarray):
        """
        This function estimates the chla concentration of a given remote sensing reflectance.

        Input:
         - rrs: numpy ndarray of 2 dimensions -> input reflectance

        Output:
         - chla: numpy ndarray -> corresponding Chla concentration
        """
        pass

    def evaluate(self, y_true, y_pred, algorithm_name, figure=False, classes=False):
        RMSE = root_mean_squared_error(y_true, y_pred)
        MAPE = mean_absolute_percentage_error(y_true, y_pred)
        BIAS = bias_metric(y_true, y_pred)
        MAE = mean_absolute_error(y_true, y_pred)
        R2 = r_squared(y_true, y_pred)

        print("evaluating algorithm: ", algorithm_name)

        print("RMSE: ", RMSE)
        print("MAE: ", MAE)
        print("MAPE: ", MAPE)
        print("BIAS: ", BIAS)
        print("R2: ", R2)

        if classes:
            cls = [[0, 5], [5, 20], [20, 1000000]]
        else:
            cls = None

        if figure:
            scatter_plot(
                y_true,
                y_pred,
                {"RMSE": RMSE, "MAE": MAE, "MAPE": MAPE, "BIAS": BIAS, "R2": R2},
                title=algorithm_name,
                x_axis="In situ Chla (mg/m3)",
                y_axis="Predicted Chla (mg/m3)",
                classes=cls,
            )
