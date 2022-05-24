import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import function as f


# Obliczanie średnich wartości kolumn i dodanie ich do kolejnego DataFrame
MPG_mean = f.df1['MPG'].mean()
Cylinders_mean = f.df1['Cylinders'].mean()
Displacement_mean = f.df1['Displacement'].mean()
Horsepower_mean = f.df1['Horsepower'].mean()
Weight_mean = f.df1['Weight'].mean()
Acceleration_mean = f.df1['Acceleration'].mean()
Model_mean = f.df1['Model'].mean()

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
print(f.value_count_by_index())
plt.subplot(3, 1, 1)
f.value_count_by_index().plot.bar(x=1, y=2, rot=0)
plt.title('Rodzaj cylindrów')
plt.xlabel('Ilość cylindrów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 2)
f.swapp_series().plot.bar(x=1, y=2, rot=0, color = 'red')
plt.title('Ilość samochodów z mocą powyżej 100km')
plt.xlabel('Moc samochodów')
plt.ylabel('Ilość samochodów')


plt.subplot(3, 1, 3)
f.nation().plot.bar(x=1, y=2, rot=0, color = 'green')
plt.title('Ilość samochodów z danego kraju')
plt.xlabel('Kraj')
plt.ylabel('Ilość samochodów')
plt.subplots_adjust(wspace=1,
                    hspace=1)

#Zapis wykresu do pliku pdf
plt.savefig('charts/Wykresy_kolumnowe.pdf', bbox_inches='tight',pad_inches=2)

# Tworzenie wyklresu 2
colors = ['yellowgreen', 'red', 'gold', 'lightskyblue',
          'lightcoral','blue','pink', 'darkgreen',
          'yellow','grey','violet','magenta','cyan']

explode = (0, 0, 0.2, 0.2, 0, 0, 0)

df2.plot.pie(x='Name', y='Value', figsize = (10 ,6),
             colors=colors, radius=1.2, startangle=90,
             shadow = True, explode = explode, labeldistance=None)

#Zapis wykresu do pliku pdf
plt.savefig('charts/Wykres_kołowy_średnich_wartości.pdf', bbox_inches='tight', pad_inches=2)

# Tworzenie wyklresu 3
fig, axs = plt.subplots(ncols=2, figsize = (12,5))
seaborn_chart = sns.histplot(x= f.df1['Horsepower'], y= f.df1['MPG'], ax=axs[0])
seaborn_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych z sns')
dataframe_chart = f.df1.plot.scatter(x= 'Horsepower', y= 'MPG', ax=axs[1])
dataframe_chart.set_title('Wykres zależności MPG od ilości koni mechanicznych')

#Zapis wykresu do pliku pdf
plt.savefig('charts/Wykresy_złożone_porównawcze.pdf', bbox_inches='tight', pad_inches=2)
fig.show()

plt.show()


#Wywołanie funkcji adding_new_column w celu dodania nowej kolumny o dodolnych argumentach;
print(f.adding_new_column(1, 'Nowakolumna', 'MPG'))
#Wywołanie funkcji car_search_string w celu wyszukania marki pojazdu;
print(f.car_search_string('Car', 'Fiat'))
#Wywołanie wiersza DataFrame jako lista z numpy array;
f.show_row_of_numpy_array(2)
