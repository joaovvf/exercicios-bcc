import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.dropbox.com/s/6s52z0tftn4pgp2/Exames4.csv?dl=1")
r = str(input())
if r == "Exame 2":
    print(round(df[r].corr(df['Exame 1']), 2))
elif r == "Exame 3":
    print(round(df[r].corr(df['Exame 1']), 2))