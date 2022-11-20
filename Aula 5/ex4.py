import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Exames3.csv")

(a, b) = np.polyfit(x=df["Exame 2"], y=df['Exame 1'], deg = 1)
n = int(input())
predicao = a * n + b
print(round(predicao, 2))