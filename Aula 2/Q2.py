import pandas as pd 

df = pd.read_csv("fake-file20.csv")
print(df.query("Meses >= 47 and Funcionario < 10"))
