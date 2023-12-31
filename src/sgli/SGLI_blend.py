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
from src.sgli.SGLI_2band_linear import SGLI2BLinEstimator
from src.sgli.SGLI_OCI import SGLIOCIEstimator

class SGLIBlendEstimator(Estimator):

    def estimate(self, rrs: np.ndarray):
        ratio = np.divide(rrs[:, 6], rrs[:, 5])
        phi = np.ones(ratio.shape)
        phi = phi * ratio
        phi[ratio < 0.75] = 0.75
        phi[ratio > 1.15] = 1.15
        w = (phi - 0.75)/(1.15 - 0.75)
        chloci = SGLIOCIEstimator().estimate(rrs)
        chl2b = SGLI2BLinEstimator().estimate(rrs)
        return np.multiply(w, chl2b) + np.multiply(np.abs(w-1), chloci)
    
    def evaluate(self, rrs, y_true, figure=False):
        y_pred = self.estimate(rrs)
        super().evaluate(y_true, y_pred, "Blend Chla", figure)