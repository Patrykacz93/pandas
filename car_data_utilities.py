import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('folder_with_data_in_csv_format/carsdata.csv', sep=';')

# Wyczyszczenie wiersza z nazwami typu zmiennych każdej z kolumn
df1 = df.drop(0)
df1.reset_index(drop=True, inplace=True)

# Zmiana typu danych w df
df1 = df1.astype({"MPG": float,
                  'Cylinders': int,
                  'Displacement': float,
                  'Horsepower': float,
                  'Weight': float,
                  'Acceleration': float,
                  'Model': float,
                  'Car': str})

# Sprawdzenie nazw kolumn odczytanego dataframe;
def displaying_column_labels() -> list:
    namecolumn = [i for i in df.columns]
    print(f'Nazwy kolumn wczytanego DataFrame: \n {namecolumn}\n')
    return namecolumn

# Sprawdzenie czy w kolumnach są puste pola
for column in displaying_column_labels():
    check = df1[column].isnull()
    print(f'Wynik sprawdzania pustych pól w kolumnie {column}: ')
    if check is True:
        print(f'W kolumnie {column} zaleziono puste pola')
    else:
        print(f'W kolumnie {column} nie ma pustych pól')

#Wyszukiwanie zmiennych typu string w kolumnach;
def searching_car_name_string(column_name: str, searched_name: str) -> pd.DataFrame:
    searched_car = df1[df1[column_name].str.match(searched_name)]
    if searched_car.empty:
        print('Wproweadziłeś nazwę która nie występuje w kolumnie:')
    else:
        print(f'Wynik wyszukiwania samochodu marki {searched_name}: \n {searched_car}\n')
        return searched_car

# Obliczanie unikatowych wartości w kolumnach [Cylinders , Horsepower]
def counting_unique_values_in_cylinders_series() -> pd.Series:
    type_of_cylinders = df1.Cylinders.value_counts().sort_index()
    print(f'Unikatowe wartości: \n{type_of_cylinders}\n')
    return type_of_cylinders

def counting_unique_values_in_horsepower_series() -> pd.Series:
    how_much_horsepower = df1.Horsepower.value_counts()
    print(f'Unikatowe wartości: \n{how_much_horsepower}\n')
    return how_much_horsepower

#Zamiana kolumn Series i wyznaczanie wartości większej niż 100
def swapp_index_with_value_in_series() -> pd.Series:
    swapped_series = pd.Series(dict((v , k) for k , v in counting_unique_values_in_horsepower_series().iteritems()))
    swapped_series_greater_than = swapped_series.loc[lambda x: x > 100]
    print(f'Series z zamienionymi miejscami: \n{swapped_series}\n')
    print(f'Series z zamienionymi miejscami oraz z wartościami powyżej 100: \n{swapped_series_greater_than}\n')
    return swapped_series_greater_than

#Obliczanie ilości samochodów z danego kraju
def get_car_amount_per_country() -> pd.Series:
    what_nation = df1.Origin.value_counts()
    print(f'Ilość samochodów w danym kraju: \n{what_nation}\n')
    return what_nation

#Dodawanie nowej kolumny o zadanych paramterach
def adding_new_column_in_dataframe(column_location: int, name_new_column: str, name_col: str) -> pd.DataFrame:
    df1.insert(loc=column_location, column= name_new_column, value=df1[name_col] + 1)
    print(f'Utworzony DataFrame po dodaniu kolumny {name_new_column} w {column_location} miejscu: \n{df1}\n')
    return df1

#Zamiana DataFrame na Numpy array i wyświetlenie dowolnego wiersza
def show_row_of_numpy_array(row_number: int)-> pd.Series:
    new_numpy_dataframe = df1.to_numpy()
    print(f'Wynik wyszukiwania wiersza numer {row_number}: \n{new_numpy_dataframe[row_number]}\n')
    return new_numpy_dataframe