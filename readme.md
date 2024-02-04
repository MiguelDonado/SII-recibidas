# Project Title: SII Recibidas Processing

This project is designed to process and analyze the Suministro Inmediato de Información (SII) files provided by Hacienda. These files contain information about the received invoices by companies whose turnover exceeded 6 million.

## Getting Started

To get started with this project, clone the repository and install the required dependencies.

## Prerequisites

This project requires Python and the following Python libraries installed:

- pandas
- openpyxl
- chardet
- tkinter
- os

## Files

The project contains the following Python scripts:

- `calculateBasesTipos.py`: Contains functions for specific calculations.
- `introFunc.py`: Contains helper functions for file handling and data loading.
- `main.py`: The main script to run the processing pipeline.
- `output.py`: Contains the function `write_to_xlsx` for writing the processed data to an Excel file.
- `supportFuncPand.py`: Contains functions for data processing and cleaning.

## Usage
To run the script, navigate to the project directory and run the following command:

```sh
python main.py
```
This will start the processing pipeline which reads the SII files, performs necessary calculations, and writes the processed data to an Excel file.