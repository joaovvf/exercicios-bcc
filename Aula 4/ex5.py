import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/m72w9fz9zbc3zed/fake-classrooms16.csv?dl=1")
prova1 = df["Prova 1"]
trabalho = df["Trabalho"]

df["Ponderada"] = (prova1 * 3 + trabalho * 7)
print(df)