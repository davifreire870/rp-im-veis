import pandas as pd

#Limpando o DataFrame


def limpeza(df):
    df['area_m2'] = pd.to_numeric(df['area_m2'], errors='coerce')
    df['quartos'] = pd.to_numeric(df['quartos'], errors='coerce')           #Transformando valores que não numéricos em NaN
    df['idade_casa'] = pd.to_numeric(df['idade_casa'], errors='coerce')
    df['preco'] = pd.to_numeric(df['preco'], errors='coerce')

    numeric_cols = df.select_dtypes(include=['number']).columns
    df = df[(df[numeric_cols] >= 0).all(axis=1)]                            #Removendo valores negativos do DataFrame

    df = df.dropna()                                                        #Removendo linhas com valores NaN do DataFrame

    return df
