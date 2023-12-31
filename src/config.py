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