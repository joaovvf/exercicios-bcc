import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Exames3_versao3.csv")
exame1 = df['Exame 1']
exame2 = df['Exame 2']
(a, b, c, d) = np.polyfit(x=exame1, y=exame2, deg = 3)
n = int(input())
predicao = a*(n**3) + b*(n**2) + c*n + d

print(round(predicao, 2))