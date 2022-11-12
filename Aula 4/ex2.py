import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms01.csv" )
resposta = df["Prova 1"].mean()
print("%.2f" % resposta)
