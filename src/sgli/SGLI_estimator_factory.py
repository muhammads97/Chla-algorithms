#
# Copyright (c) 2024 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

from src.config import ALGORITHMS
from src.sgli.SGLI_2band_exp import SGLI2BExpEstimator
from src.sgli.SGLI_2band_linear import SGLI2BLinEstimator
from src.sgli.SGLI_blend import SGLIBlendEstimator
from src.sgli.SGLI_OC3 import SGLIOC3Estimator
from src.sgli.SGLI_OC4 import SGLIOC4Estimator
from src.sgli.SGLI_OCI import SGLIOCIEstimator
from src.sgli.SGLI_STD_JAXA import SGLISTDEstimator

def sgli_get_estimator(algo: ALGORITHMS):
    if algo == ALGORITHMS.OC3:
        return SGLIOC3Estimator()
    elif algo == ALGORITHMS.OC4:
        return SGLIOC4Estimator()
    elif algo == ALGORITHMS.OCI:
        return SGLIOCIEstimator()
    elif algo == ALGORITHMS.BLEND:
        return SGLIBlendEstimator()
    elif algo == ALGORITHMS.TWO_BANDS_LINEAR:
        return SGLI2BLinEstimator()
    elif algo == ALGORITHMS.TWO_BANDS_EXP:
        return SGLI2BExpEstimator()
    elif algo == ALGORITHMS.JAXA_STD:
        return SGLISTDEstimator()
    else:
        print("Algorithm not implemented for SGLI")
        exit(1)

SGLI_WVLS = [380, 412, 443, 490, 530, 565, 673]