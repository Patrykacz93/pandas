import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('data/cars.csv', sep=';')

# Sprawdzenie nazw kolumn odczytanego dataframe;
def column_name():
    namecolumn = [i for i in df.columns]
    return namecolumn
# df1 = df.drop(0)
# df1.reset_index(drop=True, inplace=True)
# print(df1)

# Sprawdzenie czy w kolumnach są puste pola
for column in column_name():
    check = df[column].isnull()
    if check is True:
        print(f'W kolumnie {column} zaleziono puste pola')
    else:
        print(f'W kolumnie {column} nie ma pustych pól')

