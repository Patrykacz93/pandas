import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from car_data_utilities import drop_index_and_change_column_type, counting_unique_values_in_cylinders_series, swapp_index_with_value_in_series, get_car_amount_per_country, adding_new_column_in_dataframe, searching_car_name_string, show_row_of_numpy_array

#Wczytanie danych o podanej ścieżce;
df = pd.read_csv('folder_with_data_in_csv_format/carsdata.csv', sep=';')

#W przypadku tego DataFrame w pierwszej kolejności należy użyć dedykowanej funkcji do zmiany typu danych w kolumnach;
df1 = drop_index_and_change_column_type(df)

# Obliczanie średnich wartości kolumn i dodanie ich do kolejnego DataFrame
MPG_mean = df1['MPG'].mean()
Cylinders_mean = df1['Cylinders'].mean()
Displacement_mean = df1['Displacement'].mean()
Horsepower_mean = df1['Horsepower'].mean()
Weight_mean = df1['Weight'].mean()
Acceleration_mean = df1['Acceleration'].mean()
Model_mean = df1['Model'].mean()

#Utworzenie nowego DataDrame w celu utworzenia wykresu kołowego
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


# Tworzenie wyklresu 1
plt.subplot(3, 1, 1)
counting_unique_values_in_cylinders_series(df1).plot.bar(x=1, y=2, rot=0)
plt.title('Rodzaj cylindrów')
plt.xlabel('Ilość cylindrów')
plt.ylabel('Ilość samochodów')



plt.subplot(3, 1, 2)
swapp_index_with_value_in_series(df1).plot.bar(x=1, y=2, rot=0, color = 'red')
plt.title('Ilość samochodów z mocą powyżej 100km')
plt.xlabel('Moc samochodów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 3)
get_car_amount_per_country(df1).plot.bar(x=1, y=2, rot=0, color = 'green')
plt.title('Ilość samochodów z danego kraju')
plt.xlabel('Kraj')
plt.ylabel('Ilość samochodów')
plt.subplots_adjust(wspace=1,
                    hspace=1)

#Zapis wykresu do pliku pdf
plt.savefig('saved_charts_in_pdf_format/Wykresy_kolumnowe.pdf', bbox_inches='tight',pad_inches=2)

# Tworzenie wyklresu 2
colors = ['yellowgreen', 'red', 'gold', 'lightskyblue',
          'lightcoral','blue','pink', 'darkgreen',
          'yellow','grey','violet','magenta','cyan']

explode = (0, 0, 0.2, 0.2, 0, 0, 0)

df2.plot.pie(x='Name', y='Value', figsize = (10 ,6),
             colors=colors, radius=1.2, startangle=90,
             shadow = True, explode = explode, labeldistance=None)

#Zapis wykresu do pliku pdf
plt.savefig('saved_charts_in_pdf_format/Wykres_kołowy_średnich_wartości.pdf', bbox_inches='tight', pad_inches=2)

# Tworzenie wyklresu 3
fig, axs = plt.subplots(ncols=2, figsize = (12,5))
seaborn_chart = sns.histplot(x= df1['Horsepower'], y= df1['MPG'], ax=axs[0])
seaborn_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych z sns')
dataframe_chart = df1.plot.scatter(x= 'Horsepower', y= 'MPG', ax=axs[1])
dataframe_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych')

#Zapis wykresu do pliku pdf
plt.savefig('saved_charts_in_pdf_format/Wykresy_złożone_porównawcze.pdf', bbox_inches='tight', pad_inches=2)
fig.show()

plt.show()

#Wywołanie funkcji adding_new_column w celu dodania nowej kolumny o dodolnych argumentach;
adding_new_column_in_dataframe(1, 'Nowakolumna', 'MPG', df1)
#Wywołanie funkcji car_search_string w celu wyszukania marki pojazdu;
searching_car_name_string('Car', 'Fiat', df1)
#Wywołanie wiersza DataFrame jako lista z numpy array;
show_row_of_numpy_array(2, df1)
