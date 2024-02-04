import pandas as pd
import os
from tkinter import simpledialog, messagebox
import re
import chardet

NUMBER_OF_COLUMNS_OF_FILE = 178


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


def get_files():
    dir = os.getcwd()
    if files := [
        os.path.join(dir, file) for file in os.listdir(".") if file.endswith(".csv")
    ]:
        return files
    else:
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
    first_file_columns = None
    for file in files:
        df = read_file(file, encodi, 1)
        if first_file_columns is None:
            first_file_columns = df.columns
        elif not df.columns[:NUMBER_OF_COLUMNS_OF_FILE].equals(
            first_file_columns[:NUMBER_OF_COLUMNS_OF_FILE]
        ):
            messagebox.showerror("ERROR", "Los archivos no tienen las mismas columnas.")
            exit()
    return True


def read_file(file, encodi, nrows=None):
    if file.endswith(".csv"):
        df = pd.read_csv(file, encoding=encodi, delimiter=";", nrows=nrows)
    else:
        df = pd.read_excel(file, nrows=nrows)
    return df
