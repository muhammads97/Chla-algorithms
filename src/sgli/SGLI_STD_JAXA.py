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

class SGLISTDEstimator(Estimator):

    def estimate(self, rrs: np.ndarray):
        chl_ci, ci = self._CI_chla(rrs)
        oc4 = self._OC4_JAXA_chla(rrs)
        wci = ((-0.0002)-ci)/((-0.0002)-(-0.0006))
        wci[wci > 1] = 1
        wci[wci < 0] = 0
        return np.multiply(chl_ci, wci) + np.multiply(oc4, (1-wci))
    
    def _CI_chla(self, rrs:np.ndarray):
        b = rrs[:, 2]
        g = rrs[:, 5]
        r = rrs[:, 6]
        ci = g - (((b * (673 - 565)) + (r * (565 - 443)))/(673 - 443))
        chl = np.power(10, (-0.38006 + (238.0511 * ci)))
        return chl, ci
    
    def _OC4_JAXA_chla(self, rrs:np.ndarray):
        # coeffs:
        a0: float = 0.40451
        a1: float = -3.42411
        a2: float = 5.29717
        a3: float = -5.33247
        a4: float = 1.68959
        # 4 bands' reflectance
        b1 = rrs[:, 2]
        b2 = rrs[:, 3]
        b3 = rrs[:, 4]
        g = rrs[:, 5]
        # OC4:
        x = np.log10(np.max([b1/g, b2/g, b3/g], axis=0))
        return np.power(10, (a0 + (a1 * x) + (a2 * x * x) + (a3 * x * x * x) + (a4 * x * x * x * x)))