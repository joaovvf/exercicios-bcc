import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms16.csv" )
resposta = df["Prova 2"].mode()
print(resposta)