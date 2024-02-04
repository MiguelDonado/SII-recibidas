import pandas as pd
import re


def function_as_parameter(row, tipo):
    # Suma para cada fila todas las bases que tienen el tipo que se le pasa como argumento
    bases_tipoDeseado_fila = []
    for index, column in enumerate(row.index):
        if re.search(r".*Tipo Impositivo.*", column):
            next_value = row[row.index[index + 1]]
            if pd.isna(next_value):
                continue
            if tipo == 0 and pd.isna(row[column]):
                bases_tipoDeseado_fila.append(next_value)
            elif row[column] == tipo:
                bases_tipoDeseado_fila.append(next_value)
    return sum(bases_tipoDeseado_fila)


def func_calculate_bases_tipos(df):
    # Create 4 columns in the df. ["Base 0%", "Base 4%", "Base 10%", "Base 21%"]
    tipos = [0, 4, 10, 21]
    for tipo in tipos:
        name_column = "Base " + str(tipo) + "%"
        # Apply to each row of the dataframe the next function, and return
        df[name_column] = df.apply(function_as_parameter, args=(tipo,), axis=1)
    return df
