import pandas as pd

df = pd.read_csv("fake-file07.csv")
print(df.sort_values(by=['Idade', 'Funcionario'], ascending=[False, True]))