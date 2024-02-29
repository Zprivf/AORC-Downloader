# AORC-Downloader


The AORC Downloader is a Python utility for downloading Analysis of Record for Calibration (AORC), Hydrometeorological Dataset.

The AORC Downloader is a Python utility for downloading precipitation and temprature filesfrom a AORC Website. It’s particularly useful for retrieving precipitation and temprature data used by the National Water Model (NWM) for different RFCs.

Installation
Make sure you have Python installed on your system.
Install the required packages (if not already installed):
pip install wget

Usage
Import the AORC_downloader function from the aorc_downloader.py module.
Call the function with the desired URL and output directory.
Example:
Python


import os
from aorc_downloader import AORC_downloader
url = "https://hydrology.nws.noaa.gov/aorc-historic/AORC_license_disclaimer.pdf"

# Define the output directory where the contents will be saved
output_directory = "local_folder_path"

AORC_downloader (url,output_directory)


The AORC_downloader function performs the following steps:

Creates the output directory if it doesn’t exist.
Downloads the contents of the specified URL (including subdirectories) using wget.
Handles exceptions and provides informative messages.
Notes
Ensure that you have the necessary permissions to access the URL.

