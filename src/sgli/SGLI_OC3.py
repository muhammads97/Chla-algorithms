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


class SGLIOC3Estimator(Estimator):
    def estimate(self, rrs: np.ndarray):
        # coeffs:
        a0: float = 0.41712
        a1: float = -2.56402
        a2: float = 1.22219
        a3: float = 1.02751
        a4: float = -1.56804
        # 3 bands' reflectance:
        b1 = rrs[:, 2]  # 443 nm
        b2 = rrs[:, 3]  # 490 nm
        g = rrs[:, 5]  # 565 nm
        # OC3:
        x = np.log10(np.max([b1 / g, b2 / g], axis=0))
        return np.power(
            10, (a0 + (a1 * x) + (a2 * x * x) + (a3 * x * x * x) + (a4 * x * x * x * x))
        )

    def evaluate(self, rrs, y_true, figure=False, classes=False):
        y_pred = self.estimate(rrs)
        super().evaluate(y_true, y_pred, "OC3 Chla", figure, classes)
