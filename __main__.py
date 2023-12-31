#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

from src.args import args
from src.config import SENSORS, ALGORITHMS
from src.data_handler import load_data, write_chla
from src.sgli.SGLI_estimator_factory import sgli_get_estimator, SGLI_WVLS

if __name__ == "__main__":
    if args.sensor == SENSORS.SGLI:
        estimator = sgli_get_estimator(args.algorithm)
        wavelengths = SGLI_WVLS
    else:
        print("Sensor not implemented yet")
        exit(1)

    if args.evaluate:
        x, y = load_data(args.csv_path, wavelengths, True)
        if type(y) == type(None):
            print("Chla column doesn't exist in csv.")
            exit(1)
        estimator.evaluate(x, y, figure=args.figure)
    else:
        x, _ = load_data(args.csv_path, wavelengths)
        preds = estimator.estimate(x)
        write_chla(args.csv_path, args.algorithm, args.sensor, preds)
        