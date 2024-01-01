#
# Copyright (c) 2024 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

import pandas as pd
import numpy as np

from src.config import ALGORITHMS, SENSORS

def load_data(csv_path, bands, load_chla=False):
    bands = ["Rrs_%d" % b for b in bands]
    df = pd.read_csv(csv_path)
    x = df[bands]
    x = x.to_numpy(dtype=np.float64)
    y = None
    if load_chla:
        if "Chla" in df.keys():
            y = df[["Chla"]]
            y = y.to_numpy(dtype=np.float64)
            y = y.reshape((y.shape[0],))
    return x, y

def write_chla(csv_path, algo:ALGORITHMS, sensor: SENSORS, chla):
    df = pd.read_csv(csv_path)
    df["%s_%s_chla"%(sensor.value, algo.value)] = chla
    df.to_csv(csv_path)