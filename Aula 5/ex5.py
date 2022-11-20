import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Exames2_versao4.csv")
exame2 = df["Exame 2"]
exame1 = df['Exame 1']
(a, b, c) = np.polyfit(x=exame1, y=exame2, deg = 2)


print(round(a, 2))
print(round(b, 2))
print(round(c, 2))
print(1)