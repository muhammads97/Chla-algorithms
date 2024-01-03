#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

from src.estimator import Estimator
from src.sgli.SGLI_OC3 import SGLIOC3Estimator
import numpy as np


class SGLIOCIEstimator(Estimator):
    def estimate(self, rrs: np.ndarray):
        ci = self._CI_chla(rrs)
        oc3 = SGLIOC3Estimator().estimate(rrs)
        w = (ci - 0.15) / (0.2 - 0.15)
        chl = np.zeros(ci.shape)
        chl[ci < 0.15] = ci[ci < 0.15]
        chl[ci > 0.2] = oc3[ci > 0.2]
        condition = (ci >= 0.15) & (ci <= 0.2)
        temp = np.multiply(w, oc3) + np.multiply(np.abs(w - 1), ci)
        chl[condition] = temp[condition]
        return chl

    def evaluate(self, rrs, y_true, figure=False, classes=False):
        y_pred = self.estimate(rrs)
        super().evaluate(y_true, y_pred, "OCI Chla", figure, classes)

    def _CI_chla(self, rrs: np.ndarray):
        b = rrs[:, 2]
        g = rrs[:, 5]
        r = rrs[:, 6]
        ci = g - b - (((565 - 443) / (673 - 443)) * (r - b))
        chl = np.power(10, (-0.4909 + (191.6590 * ci)))
        return chl
