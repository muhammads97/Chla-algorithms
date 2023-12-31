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

class SGLIOC4Estimator(Estimator):

    def estimate(self, rrs: np.ndarray):
        # coeffs:
        a0: float = 0.43171
        a1: float = -2.46496
        a2: float = 1.25461
        a3: float = 0.36690
        a4: float = -0.80127
        # 4 bands' reflectance:
        b1 = rrs[:, 1] # 412 nm
        b2 = rrs[:, 2] # 443 nm
        b3 = rrs[:, 3] # 490 nm
        g  = rrs[:, 5] # 565 nm
        # OC4:
        x = np.log10(np.max([b1/g, b2/g, b3/g], axis=0))
        return np.power(10, (a0 + (a1 * x) + (a2 * x * x) + (a3 * x * x * x) + (a4 * x * x * x * x)))
    
    def evaluate(self, rrs, y_true, figure=False):
        y_pred = self.estimate(rrs)
        super().evaluate(y_true, y_pred, "OC4 Chla", figure)