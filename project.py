import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/carsdata.csv', sep=';')

# Wyczyszczenie wiersza z nazwami typu zmiennych każdej z kolumn
df1 = df.drop(0)
df1.reset_index(drop=True, inplace=True)

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
def value_count_by_index():
    type_of_cylinders = df1.Cylinders.value_counts().sort_index()
    return type_of_cylinders

def value_count():
    how_much_horsepower = df1.Horsepower.value_counts()
    return how_much_horsepower

#Zamiana kolumn Series i wyznaczanie wartości większej niż 100
def swapp_series():
    swapped_series = pd.Series(dict((v , k) for k , v in value_count().iteritems()))
    swapped_series_greather_than = swapped_series.loc[lambda x: x > 100]
    return swapped_series_greather_than

def nation():
    what_nation = df1.Origin.value_counts()
    return what_nation

def adding_new_column(column_location, name_new_column, name_col):
    df1.insert(loc=column_location, column= name_new_column, value=df1[name_col] + 1)
    return df1

def show_row_of_numpy_array(row_number):
    new_numpy_dataframe = df1.to_numpy()
    print(new_numpy_dataframe[row_number])
    return new_numpy_dataframe

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
                              Model_mean]},
                    index = ['MPGMean',
                            'CylindersMean',
                            'DisplacementMean',
                            'HorsepowerMean',
                            'WeightMean',
                            'AccelerationMean',
                            'ModelMean'])


# Wykresy 1
print(value_count_by_index())
plt.subplot(3, 1, 1)
value_count_by_index().plot.bar(x=1, y=2, rot=0)
plt.title('Rodzaj cylindrów')
plt.xlabel('Ilość cylindrów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 2)
swapp_series().plot.bar(x=1, y=2, rot=0, color = 'red')
plt.title('Ilość samochodów z mocą powyżej 100km')
plt.xlabel('Moc samochodów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 3)
nation().plot.bar(x=1, y=2, rot=0, color = 'green')
plt.title('Ilość samochodów z danego kraju')
plt.xlabel('Kraj')
plt.ylabel('Ilość samochodów')
plt.subplots_adjust(wspace=1,
                    hspace=1)

#Wykres 2
colors = ['yellowgreen', 'red', 'gold', 'lightskyblue',
          'lightcoral','blue','pink', 'darkgreen',
          'yellow','grey','violet','magenta','cyan']

explode = (0, 0, 0.2, 0.2, 0, 0, 0)

df2.plot.pie(x='Name', y='Value', figsize = (10 ,6),
             colors=colors, radius=1.2, startangle=90,
             shadow = True, explode = explode, labeldistance=None)

fig, axs = plt.subplots(ncols=2)
seaborn_chart = sns.histplot(x= df1['Horsepower'], y= df1['MPG'], ax=axs[0])
seaborn_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych z sns')
dataframe_chart = df1.plot.scatter(x= 'Horsepower', y= 'MPG', ax=axs[1])
dataframe_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych')
fig.show()

plt.show()


#Wywołanie funkcji adding_new_column w celu dodania nowej kolumny o dodolnych argumentach;
print(adding_new_column(1, 'Nowakolumna', 'MPG'))
#Wywołanie funkcji car_search_string w celu wyszukania marki pojazdu;
print(car_search_string('Car', 'Fiat'))
#Wywołanie wiersza DataFrame jako lista z numpy array;
show_row_of_numpy_array(2)
