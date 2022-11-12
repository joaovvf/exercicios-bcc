import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms08.csv" )
resposta = df["Prova 1"].std()
print("%.2f" % resposta)
