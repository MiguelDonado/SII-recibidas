import pandas as pd
import os
from tkinter import simpledialog, messagebox
import re
import chardet


def get_CIF():
    # Ask the user for input (CIF). The pop-up'll only close when a valid CIF is entered.
    cif = None
    while not cif:
        cif = simpledialog.askstring(
            "IMPORTANTE", "Introduce el CIF de la empresa auditada."
        )
        if not cif:
            messagebox.showwarning("Advertencia", "El CIF es requerido.")
        elif not re.search(r"^[A-Z]\d{8}$", cif):
            messagebox.showwarning(
                "Advertencia",
                """El CIF introducido no es válido. La letra debe estar en mayusculas. 
                Y no debe haber espacios al principio ni al final.""",
            )
            cif = None

    return cif


def get_files_csv():
    # Get all csv files from actual directory
    dir = os.getcwd()
    files = [
        os.path.join(dir, file) for file in os.listdir(".") if file.endswith(".csv")
    ]
    return files


def get_files_xlsx():
    # Get all xlsx files from actual directory
    dir = os.getcwd()
    files = [
        os.path.join(dir, file)
        for file in os.listdir(".")
        if file.endswith(".xlsx") and file != "SII RECIBIDAS PROVEEDORES.xlsx"
    ]
    return files


def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]


def check_same_columns(files, encodi):
    if files[0].endswith(".csv"):
        # Check if all the csv files've the same columns.
        first_file_columns = None
        for file in files:
            # read only the first row
            df = pd.read_csv(file, encoding=encodi, delimiter=";", nrows=1)
            if first_file_columns is None:
                first_file_columns = df.columns
            elif not df.columns[:178].equals(first_file_columns[:178]):
                messagebox.showerror(
                    "ERROR", "Los archivos no tienen las mismas columnas."
                )
                exit()
    else:
        # Check if all the xlsx files've the same columns.
        first_file_columns = None
        for file in files:
            # read only the first row
            df = pd.read_excel(file, nrows=1)
            if first_file_columns is None:
                first_file_columns = df.columns
            elif not df.columns[:178].equals(first_file_columns[:178]):
                messagebox.showerror(
                    "ERROR", "Los archivos no tienen las mismas columnas."
                )
                exit()
    return True
