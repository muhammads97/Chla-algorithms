#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

from src.estimator import Estimator
import numpy as np

class SGLI2BLinEstimator(Estimator):

    def estimate(self, rrs: np.ndarray):
        # coeffs:
        b: float = 20.96509192
        c: float = 11.5367097
        # 2 band linear:
        ratio = np.divide(rrs[:, 6], rrs[:, 5])
        return b * ratio + c
    
    def evaluate(self, rrs, y_true, figure=False):
        y_pred = self.estimate(rrs)
        super().evaluate(y_true, y_pred, "2-band linear Chla", figure)