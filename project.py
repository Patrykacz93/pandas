import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('data/carsdata.csv', sep=';')

# Sprawdzenie nazw kolumn odczytanego dataframe;
def column_name():
    namecolumn = [i for i in df.columns]
    return namecolumn

df1 = df.drop(0)
df1.reset_index(drop=True, inplace=True)
print(df1)

# Sprawdzenie czy w kolumnach są puste pola
for column in column_name():
    check = df1[column].isnull()
    if check is True:
        print(f'W kolumnie {column} zaleziono puste pola')
    else:
        print(f'W kolumnie {column} nie ma pustych pól')


df1 = df1.astype({"MPG": float,
                  'Cylinders': float,
                  'Displacement': float,
                  'Horsepower': float,
                  'Weight': float,
                  'Acceleration': float,
                  'Model': float})

df2 = pd.DataFrame()
MPG_mean = df1['MPG'].mean()
Cylinders_mean = df1['Cylinders'].mean()
Displacement_mean = df1['Displacement'].mean()
Horsepower_mean = df1['Horsepower'].mean()
Weight_mean = df1['Weight'].mean()
Acceleration_mean = df1['Acceleration'].mean()
Model_mean = df1['Model'].mean()

print(df2.append({'MPGMean': MPG_mean,
                  'CylindersMean': Cylinders_mean,
                  'DisplacementMean': Displacement_mean,
                  'HorsepowerMean': Horsepower_mean,
                  'WeightMean': Weight_mean,
                  'AccelerationMean': Acceleration_mean,
                  'ModelMean': Model_mean},
                 ignore_index=True))




