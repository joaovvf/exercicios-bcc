import pandas as pd 

df = pd.read_csv("fake-file04.csv")
print(df.sort_values(by='Genero', ascending=False))