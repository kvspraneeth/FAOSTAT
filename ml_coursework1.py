# -*- coding: utf-8 -*-
"""Ml_coursework1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-p5AScFHD4qsfgvTl3ViV6sCDcYp76tG
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing

ConPriI=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Consumer prices indicators - FAOSTAT_data_en_2-22-2024.csv')
ConProI=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Crops production indicators - FAOSTAT_data_en_2-22-2024.csv')
Emissions=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Emissions - FAOSTAT_data_en_2-27-2024.csv')
Employment=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Employment - FAOSTAT_data_en_2-27-2024.csv')
Exchange_rate=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Exchange rate - FAOSTAT_data_en_2-22-2024.csv')

##

print('Column names : ')
for i in ConPriI.columns:
  print(i,end=', ')
print('Unique names : ')
ConPriI.Item.unique()

ConPriI.head(2)

ConPriI_ref=ConPriI[['Item','Area','Area Code (M49)','Months','Months Code','Year','Year Code','Value']]
ConPriI_ref=pd.get_dummies(ConPriI_ref, columns=['Item'], dtype=int)

print('Column names : ')
for i in ConProI.columns:
  print(i,end=', ')
print('Unique names : ')
ConProI.Item.unique()

ConProI_ref=ConProI[['Item','Area','Area Code (M49)','Year','Year Code','Value']]
ConProI_ref=pd.get_dummies(ConProI_ref, columns=['Item'], dtype=int)

ConProI_ref.head()

Emissions.head(2)

print('Column names : ')
for i in Emissions.columns:
  print(i,end=', ')
print('Unique names : ')
Emissions.Element.unique()

Emissions_ref=Emissions[['Item','Element','Area','Area Code (M49)','Year','Year Code','Value']]
Emissions_ref=pd.get_dummies(Emissions_ref, columns=['Element'], dtype=int)

Emissions_ref.head(5)

Employment.head()

print('Column names : ')
for i in Employment.columns:
  print(i,end=', ')
print('Unique names : ')
Employment.Indicator.unique()

Employment_ref=Employment[['Indicator Code','Indicator','Element','Element Code','Area','Area Code (M49)','Year','Year Code','Value']]
Employment_ref=pd.get_dummies(Employment_ref, columns=['Indicator'], dtype=int)

Employment_ref.head()

Exchange_rate.head()

print('Column names : ')
for i in Exchange_rate.columns:
  print(i,end=', ')
print('Unique names : ')
Exchange_rate.Currency.unique()

Exchange_rate_ref=Exchange_rate[['Element','Element Code','ISO Currency Code (FAO)','Currency','Area','Area Code (M49)','Year','Year Code','Value']]
Exchange_rate_ref=pd.get_dummies(Exchange_rate_ref, columns=['Currency'], dtype=int)

Exchange_rate_ref.head()

Fert_use=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Fertilizers use - FAOSTAT_data_en_2-27-2024.csv')
Food_b=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Food balances indicators - FAOSTAT_data_en_2-22-2024.csv')
Food_secu=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Food security indicators  - FAOSTAT_data_en_2-22-2024.csv')
Food_trade=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Food trade indicators - FAOSTAT_data_en_2-22-2024.csv')
For_di=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Foreign direct investment - FAOSTAT_data_en_2-27-2024.csv')
Land_temp=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Land temperature change - FAOSTAT_data_en_2-27-2024.csv')
Land_use=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Land use - FAOSTAT_data_en_2-22-2024.csv')
Pest_use=pd.read_csv('/content/drive/MyDrive/ML Data Sets & Projects/Ml_coursework1/ML Coursework Dataset/Pesticides use - FAOSTAT_data_en_2-27-2024.csv')

Fert_use.head()

print('Column names : ')
for i in Fert_use.columns:
  print(i,end=', ')
print('Unique names : ')
Fert_use.Item.unique()

Fert_use_ref=Fert_use[['Element','Element Code','Item Code','Item','Area','Area Code (M49)','Year','Year Code','Value']]
Fert_use_ref=pd.get_dummies(Fert_use_ref, columns=['Item'], dtype=int)

Fert_use_ref.head()

Food_b.head()

print('Column names : ')
for i in Food_b.columns:
  print(i,end=', ')
print('\nUnique names : ')
Food_b.Element.unique()

Food_b_ref=Food_b[['Element','Element Code','Item Code (FBS)','Item','Area','Area Code (M49)','Year','Year Code','Value']]
Food_b_ref=pd.get_dummies(Food_b_ref, columns=['Item','Element'], dtype=int)

Food_b_ref.head()

Food_secu.head()

print('Column names : ')
for i in Food_secu.columns:
  print(i,end=', ')
print('\nUnique names : ')
Food_secu.Item.unique()

Food_secu_ref=Food_secu[['Element','Element Code','Item Code','Item','Area','Area Code (M49)','Year','Year Code','Value']]
Food_secu_ref=pd.get_dummies(Food_secu_ref, columns=['Item'], dtype=int)

Food_secu_ref.head()

Food_trade.head()

print('Column names : ')
for i in Food_trade.columns:
  print(i,end=', ')
print('\nUnique names : ')
Food_trade.Element.unique()

Food_trade_ref=Food_trade[['Element','Element Code','Item Code (CPC)','Item','Area','Area Code (M49)','Year','Year Code','Value']]
Food_trade_ref=pd.get_dummies(Food_trade_ref, columns=['Element'], dtype=int)

Food_trade_ref.head()

For_di.head()

print('Column names : ')
for i in For_di.columns:
  print(i,end=', ')
print('\nUnique names : ')
For_di.Item.unique()

For_di_ref=For_di[['Element','Element Code','Item Code','Item','Area','Area Code (M49)','Year','Year Code','Value']]
For_di_ref=pd.get_dummies(For_di_ref, columns=['Item'], dtype=int)

For_di_ref.head()

Land_temp.head()

print('Column names : ')
for i in Land_temp.columns:
  print(i,end=', ')
print('\nUnique names : ')
Land_temp.Element.unique()

Land_temp_ref=Land_temp[['Element','Element Code','Area','Area Code (M49)','Year','Year Code','Value']]
Land_temp_ref=pd.get_dummies(Land_temp_ref, columns=['Element'], dtype=int)

Land_temp_ref.head()

Land_use.head()

print('Column names : ')
for i in Land_use.columns:
  print(i,end=', ')
print('\nUnique names : ')
Land_use.Item.unique()

Land_use_ref=Land_use[['Element','Element Code','Item','Item Code','Area','Area Code (M49)','Year','Year Code','Value']]
Land_use_ref=pd.get_dummies(Land_use_ref, columns=['Item'], dtype=int)

Land_use_ref.head()

Pest_use.head()

print('Column names : ')
for i in Pest_use.columns:
  print(i,end=', ')
print('\nUnique names : ')
Pest_use.Item.unique()

Pest_use_ref=Pest_use[['Element','Element Code','Item','Item Code','Area','Area Code (M49)','Year','Year Code','Value']]
Pest_use_ref=pd.get_dummies(Pest_use_ref, columns=['Item','Element'], dtype=int)

Pest_use_ref.head()



