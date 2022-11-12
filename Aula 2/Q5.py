import pandas as pd 

df = pd.read_csv("fake-file20.csv")
print(df.query("Funcionario >= 10"))