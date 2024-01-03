#
# Copyright (c) 2023 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

import argparse
from src.config import SENSORS, ALGORITHMS
from pathlib import Path

__version__ = "1.0"

parser = argparse.ArgumentParser(
    description="Welcome to Chla-algorithms!\n"
    "This script is an implementation of the major classic Chla algorithms for different satellites.\n"
    "This API is developed by Muhammad Salah (msalah.29.10@gmail.com)\n",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s {version}".format(version=__version__),
)
parser.add_argument("--sensor", type=SENSORS, help="Sensors: SGLI, MSI, or OLCI.")
parser.add_argument(
    "--algorithm",
    type=ALGORITHMS,
    help="Algorithm: see readme.md for the available algorithms",
)

parser.add_argument(
    "--csv_path",
    type=Path,
    help="path to csv file containing input rrs data and optionally chla",
)
parser.add_argument(
    "--figure",
    action="store_true",
    default=False,
    help="in case of evaluation produce a scatter plot",
)
parser.add_argument(
    "--classes",
    action="store_true",
    default=False,
    help="in case of evaluation produce a scatter plot",
)
parser.add_argument(
    "--evaluate",
    action="store_true",
    default=False,
    help="evaluate the algorithm against data, input csv must have 'chla' column",
)

args, _ = parser.parse_known_args()

if not args.sensor or not args.algorithm:
    print("sensor and algorithm must be provided.")
    exit(1)
if not args.csv_path:
    print("must provide data through a csv")
