"""Переименуйте названия столбцов в файле data.csv при помощи метода rename в pandas. Также сохраните ваши данные в файл new_data.csv. Названия столбцов изначально неизвестны. Необходимо ввести новые названия столбцов через input()
"""
import pandas as pd


table = pd.read_csv('data.csv',header=None)
#print(table.shape)
#print(table.shape[1])
print(f"В вашей таблице {table.shape[1]} столбец")
column_names = {}
for i in range(table.shape[1]):
     a = input(f"Введите пожалуйста  название столбца {i}: ")
     column_names[i] = a

table = table.rename(columns=column_names)     
table.to_csv("new_data.csv")
#new_table=pd.DataFrame(table.values, columns=column_names)
#print(table.columns)
#new_table.to_csv("new_data.csv") 


