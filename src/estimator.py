#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#


import numpy as np
class Estimator:
    def __init__(self) -> None:
        pass

    def estimate(self, rrs:np.ndarray):
        '''
        This function estimates the chla concentration of a given remote sensing reflectance.
        
        Input:
         - rrs: numpy ndarray of 2 dimensions -> input reflectance
        
        Output:
         - chla: numpy ndarray -> corresponding Chla concentration
        '''
        pass