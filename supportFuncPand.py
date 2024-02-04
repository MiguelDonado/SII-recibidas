import pandas as pd


def calculate_all_columns(df, cif):
    df = calculate_base_column(df)
    df = calculate_cuota_column(df)
    df = calculate_importaciones_column(df, cif)
    df = calculate_ISP_column(df)
    df = calculate_intracomunitarias_column(df)
    df = calculate_rectificativas_column(df)
    return df


def calculate_base_column(df):
    # Add BASE column to df (sum of all the .*Imponible.* columns for each row)
    base_imponible_columns = df.filter(regex=".*Imponible.*").columns
    df[base_imponible_columns] = df[base_imponible_columns].astype(float)
    df["BASE"] = df[base_imponible_columns].sum(axis=1)

    return df


def calculate_cuota_column(df):
    # Add cuota column to df (sum of all the .*Soportada.* columns for each row)
    cuota_soportada_columns_df = df.filter(regex=".*Soportada.*")
    cuota_soportada_columns_df = cuota_soportada_columns_df.astype(float)
    df["IVA"] = cuota_soportada_columns_df.sum(axis=1)
    return df


def calculate_ISP_column(df):
    # ISP=Inversion Sujeto Pasivo
    # Add ISP column to df (True=1, False=0)
    isp_columns_df = df.filter(regex="\(ISP\).*Imponible.*")
    df["ISP"] = isp_columns_df.apply(lambda row: 1 if any(pd.notna(row)) else 0, axis=1)
    return df


def calculate_importaciones_column(df, cif):
    # Add Importaciones column to df (True=1, False=0)
    df["Importaciones"] = df["NIF Emisor"].apply(lambda x: 1 if x == cif else 0)
    return df


def calculate_intracomunitarias_column(df):
    # Add Intracomunitarias column to df (True=1, False=0)
    df["Intracomunitarias"] = df["NIF Emisor"].apply(lambda x: 0 if pd.notna(x) else 1)
    return df


def calculate_rectificativas_column(df):
    # Add rectificativas column to df (True=1, False=0)
    df["Rectificativas"] = df["BASE"].apply(lambda x: 1 if x < 0 else 0)
    return df


# ---------------DELETE FUNCTION-----------------
def delete_columns(df):
    # Delete all columns that I dont need because I've already use them to calculate another columns
    base_imponible_columns_df = df.filter(regex=".*Imponible.*")
    tipo_columns_df = df.filter(regex=".*Impositivo.*")
    cuota_soportada_columns_df = df.filter(regex=".*Cuota Soportada.*")
    df.drop(base_imponible_columns_df.columns, axis=1, inplace=True)
    df.drop(tipo_columns_df.columns, axis=1, inplace=True)
    df.drop(cuota_soportada_columns_df.columns, axis=1, inplace=True)
    return df
