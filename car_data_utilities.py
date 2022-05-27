import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def drop_index_and_change_column_type(car_data: pd.DataFrame) -> pd.DataFrame:
    df1 = car_data.drop(0)
    df1.reset_index(drop=True, inplace=True)
    df_with_new_type = df1.astype({"MPG": float,
                                   'Cylinders': int,
                                   'Displacement': float,
                                   'Horsepower': float,
                                   'Weight': float,
                                   'Acceleration': float,
                                   'Model': float,
                                   'Car': str})
    return df_with_new_type


def displaying_column_labels(car_data: pd.DataFrame) -> list:
    namecolumn = [i for i in car_data.columns]
    print(f'Nazwy kolumn wczytanego DataFrame: \n {namecolumn}\n')
    return namecolumn


def checking_empty_area_in_columns(car_data: pd.DataFrame):
    for column in displaying_column_labels():
        check = car_data[column].isnull()
        print(f'Wynik sprawdzania pustych pól w kolumnie {column}: ')
        if check is True:
            print(f'W kolumnie {column} zaleziono puste pola')
        else:
            print(f'W kolumnie {column} nie ma pustych pól')


def searching_car_name_string(column_name: str, searched_name: str, car_data: pd.DataFrame) -> pd.DataFrame:
    searched_car = car_data[car_data[column_name].str.match(searched_name)]
    if searched_car.empty:
        print('Wproweadziłeś nazwę która nie występuje w kolumnie:')
    else:
        print(f'Wynik wyszukiwania samochodu marki {searched_name}: \n {searched_car}\n')
        return searched_car


def counting_unique_values_in_cylinders_series(car_data: pd.DataFrame) -> pd.Series:
    type_of_cylinders = car_data.Cylinders.value_counts().sort_index()
    print(f'Unikatowe wartości: \n{type_of_cylinders}\n')
    return type_of_cylinders


def counting_unique_values_in_horsepower_series(car_data: pd.DataFrame) -> pd.Series:
    how_much_horsepower = car_data.Horsepower.value_counts()
    print(f'Unikatowe wartości: \n{how_much_horsepower}\n')
    return how_much_horsepower


def swapp_index_with_value_in_series(car_data: pd.DataFrame) -> pd.Series:
    swapped_series = pd.Series(
        dict((v, k) for k, v in counting_unique_values_in_horsepower_series(car_data).iteritems()))
    swapped_series_greater_than = swapped_series.loc[lambda x: x > 100]
    print(f'Series z zamienionymi miejscami: \n{swapped_series}\n')
    print(f'Series z zamienionymi miejscami oraz z wartościami powyżej 100: \n{swapped_series_greater_than}\n')
    return swapped_series_greater_than


def get_car_amount_per_country(car_data: pd.DataFrame) -> pd.Series:
    what_nation = car_data.Origin.value_counts()
    print(f'Ilość samochodów w danym kraju: \n{what_nation}\n')
    return what_nation


def adding_new_column_in_dataframe(column_location: int, name_new_column: str, name_col: str,
                                   car_data: pd.DataFrame) -> pd.DataFrame:
    car_data.insert(loc=column_location, column=name_new_column, value=car_data[name_col] + 1)
    print(f'Utworzony DataFrame po dodaniu kolumny {name_new_column} w {column_location} miejscu: \n{car_data}\n')
    return car_data


def show_row_of_numpy_array(row_number: int, car_data: pd.DataFrame) -> pd.Series:
    new_numpy_dataframe = car_data.to_numpy()
    print(f'Wynik wyszukiwania wiersza numer {row_number}: \n{new_numpy_dataframe[row_number]}\n')
    return new_numpy_dataframe
