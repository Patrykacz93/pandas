import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/carsdata.csv', sep=';')

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
def column_name():
    namecolumn = [i for i in df.columns]
    return namecolumn

# Sprawdzenie czy w kolumnach są puste pola
for column in column_name():
    check = df1[column].isnull()
    if check is True:
        print(f'W kolumnie {column} zaleziono puste pola')
    else:
        print(f'W kolumnie {column} nie ma pustych pól')

#Wyszukiwanie zmiennych typu string w kolumnach;
def car_search_string(column_name: str, searched_name: str):
    searched_car = df1[df1[column_name].str.match(searched_name)]
    if isinstance(searched_car, pd.DataFrame):
        if len(searched_car) == 0:
            print('Wproweadziłeś nazwę która nie występuje w kolumnie:')
        else:
            return searched_car
    else:
        print('Nie ma tego co wprowadziłeś')

# Obliczanie unikatowych wartości w kolumnach [Cylinders , Horsepower]
def value_count_by_index():
    type_of_cylinders = df1.Cylinders.value_counts().sort_index()
    return type_of_cylinders

def value_count():
    how_much_horsepower = df1.Horsepower.value_counts()
    return how_much_horsepower

#Zamiana kolumn Series i wyznaczanie wartości większej niż 100
def swapp_series():
    swapped_series = pd.Series(dict((v , k) for k , v in value_count().iteritems()))
    swapped_series_greater_than = swapped_series.loc[lambda x: x > 100]
    return swapped_series_greater_than

#Obliczanie ilości samochodów z danego kraju
def nation():
    what_nation = df1.Origin.value_counts()
    return what_nation

#Dodawanie nowej kolumny o zadanych paramterach
def adding_new_column(column_location, name_new_column, name_col):
    df1.insert(loc=column_location, column= name_new_column, value=df1[name_col] + 1)
    return df1

#Zamiana DataFrame na Numpy array i wyświetlenie dowolnego wiersza
def show_row_of_numpy_array(row_number):
    new_numpy_dataframe = df1.to_numpy()
    print(new_numpy_dataframe[row_number])
    return new_numpy_dataframe