#
# Copyright (c) 2024 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

from enum import Enum
class SENSORS(Enum):
    SGLI = "SGLI"
    MSI  = "MSI"
    OLCI = "OLCI"

class ALGORITHMS(Enum):
    OC3                 = "OC3"
    OC4                 = "OC4"
    OC5                 = "OC5"
    OC6                 = "OC6"
    OCI                 = "OCI"
    BLEND               = "BLEND"
    TWO_BANDS_LINEAR    = "TWO_BANDS_LINEAR"
    TWO_BANDS_EXP       = "TWO_BANDS_EXP"
    JAXA_STD            = "JAXA_STD"