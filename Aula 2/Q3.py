import pandas as pd 

df = pd.read_csv("fake-file06.csv")
print(df.groupby("Escolaridade")["Meses"].sum())