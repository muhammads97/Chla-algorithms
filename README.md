<h3 align="center">Remote Sensing Chla Algorithms</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This repo includes an implementation for various Chla Algorithms for different satellite sensors.
    <br> 
    Acknowledgment: This project was developed as part of my master's degree at Kyoto University of Advanced Science, under the Remote Sensing Laboratory. 
    <br> 
    This project is built for research purposes to collect and extract data.
    <br> 
    The research contributes towards my master's degree, under the supervision of Professor Salem Ibrahim Salem.
    <br> 
</p>

## Installation

Clone this repo, and install the dependencies in a conda environment using the [environment.yml](/environment.yml) file.

## Usage

run the __main__.py file using 
`python <PATH_TO_CHLA_ALGORITHMS>`

and use the following command line arguments:

- [--sensor]: see the list of available sensors below.
- [--algorithm]: see the list of available algorithms below.
- [--csv_path]: path to csv file containing the input rrs and optionally Chla. rrs columns' headers should be in the format: Rrs_<wavelength> and the sensors' rrs bands should all be available as described in the sensor rrs values below. Chla should be provided if the the --evaluate option is present.
- [--evaluate]: this argument is optional, if set, Chla column must be within the csv.

## sensors and algorithms

### SGLI

**bands**: [Rrs_380, Rrs_412, Rrs_443, Rrs_490, Rrs_530, Rrs_565, Rrs_673] \

**Algorithms:** \

1. OC3
2. OC4
3. OCI
4. BLEND
5. TWO_BANDS_LINEAR
6. TWO_BANDS_EXP
7. JAXA_STD

### MSI

To be added soon

### OLCI

To be added soon

Notes
=====

Please feel free to contribute by creating an issue or a PR.
