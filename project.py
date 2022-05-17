import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/carsdata.csv', sep=';')

# Sprawdzenie nazw kolumn odczytanego dataframe;
def column_name():
    namecolumn = [i for i in df.columns]
    return namecolumn

# Wyczyszczenie wiersza z nazwami typu zmiennych każdej z kolumn
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

# cols_to_check = ['C', 'D', 'E']
# print(df.loc[:, cols_to_check])
#
# df.loc[:, cols_to_check] = df.loc[
#                            :, cols_to_check].replace({';': ''}, regex=True)
# print(df)

# Zmiana typu danych w df
df1 = df1.astype({"MPG": float,
                  'Cylinders': int,
                  'Displacement': float,
                  'Horsepower': float,
                  'Weight': float,
                  'Acceleration': float,
                  'Model': float,
                  'Car': str})

# Obliczanie unikatowych wartości w kolumnach [Cylinders , Horsepower, Origin]
type_of_cylinders = df1.Cylinders.value_counts().sort_index()
how_much_horsepower = df1.Horsepower.value_counts()
swapped_series = pd.Series(dict((v , k) for k , v in how_much_horsepower.iteritems()))
swapped_series_greather_than = swapped_series.loc[lambda x: x > 100]
what_nation = df1.Origin.value_counts()

# Obliczanie średnich wartości kolumn i dodanie ich do kolejnego DataFrame
MPG_mean = df1['MPG'].mean()
Cylinders_mean = df1['Cylinders'].mean()
Displacement_mean = df1['Displacement'].mean()
Horsepower_mean = df1['Horsepower'].mean()
Weight_mean = df1['Weight'].mean()
Acceleration_mean = df1['Acceleration'].mean()
Model_mean = df1['Model'].mean()


df2 = pd.DataFrame({'Name':['MPGMean',
                            'CylindersMean',
                            'DisplacementMean',
                            'HorsepowerMean',
                            'WeightMean',
                            'AccelerationMean',
                            'ModelMean'],
                    'Value': [MPG_mean,
                              Cylinders_mean,
                              Displacement_mean,
                              Horsepower_mean,
                              Weight_mean,
                              Acceleration_mean,
                              Model_mean]})


# Wykresy 1
print(type_of_cylinders)
plt.subplot(3, 1, 1)
type_of_cylinders.plot.bar(x=1, y=2, rot=0)
plt.title('Rodzaj cylindrów')
plt.xlabel('Ilość cylindrów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 2)
swapped_series_greather_than.plot.bar(x=1, y=2, rot=0, color = 'red')
plt.title('Ilość samochodów z mocą powyżej 100km')
plt.xlabel('Moc samochodów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 3)
what_nation.plot.bar(x=1, y=2, rot=0, color = 'green')
plt.title('Ilość samochodów z danego kraju')
plt.xlabel('Kraj')
plt.ylabel('Ilość samochodów')
plt.subplots_adjust(wspace=1,
                    hspace=1)

#Wykres 2
df2.plot.pie(x='Name', y='Value')
plt.show()
