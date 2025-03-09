import pandas as pd

df_casts = pd.read_csv('casts.csv', index_col=None)

#df_json = pd.read_json('paises.json')

print(df_casts.head(5))

#print(df_json.head(5))

#print(df_casts.to_string()) # to_string() to print the entire DataFrame.

print(df_casts.describe()) # mostrar os dados numéricos da tabela

#print(df_casts.info())



df_titles = pd.read_csv('titles.csv', index_col=None)

print(df_titles.tail(5)) # method for viewing the last rows of the DataFrame

#pd.set_option('display.max_rows', 20, 'display.max_columns', 10) 

pd.set_option('display.min_rows',20,'display.max_rows', 20, 'display.max_columns', 10)

print(df_titles)

