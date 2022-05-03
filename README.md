# bom-compare

## Purpose
Compare any two Bill of Material files (CSV file) and display the differences.

## Requirements

### Packages
pip3 install Flask

### Format
Column names, column order, and number of columns should match the following format.

| Partnumber | DESC | QTY | REV |
|------------|------|-----|-----|

### How to use
1. Enter folder path where .csv files are located
2. Click "Choose File" to select the two CSV files that you want to compare
3. Click "Submit" and results will be displayed on screen
4. Click "Upload New" to upload new BoMs
