import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("https://drive.google.com/u/1/uc?id=1GU318XmRQ3_KYSUOlsvKdj5cFnJ5ne-m&export=download")
x = df["tempo"]
y = df["posicao"]
plt.plot(x, y, 'o')