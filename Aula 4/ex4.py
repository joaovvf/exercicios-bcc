import pandas as pd
import numpy as np

df = pd.read_csv("https://www.dropbox.com/s/pk3nk4mafrerijl/fake-classrooms10.csv?dl=1")
resposta = np.percentile(df["Prova 2"], q=31)
print("%.2f" % resposta)