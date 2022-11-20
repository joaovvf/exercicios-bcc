import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Exames3.csv")

ex2 = df["Exame 2"].corr(df["Exame 1"])
ex3 = df["Exame 3"].corr(df['Exame 1'])
r2 = round(ex2 ** 2, 2)
r3 = round(ex3 ** 2, 2)
print(r2)
print(r3)
if r2 > r3:
    print(2)
else:
    print(3)