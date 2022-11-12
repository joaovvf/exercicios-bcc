import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/kwibw8umms9yh9w/NotasAjuste.csv?dl=1")
exame = input()
ajuste = 0
df['Ajuste'] = ajuste

if df[exame].mean() < 50:
    df['Ajuste'] = df[exame] * 1.2
elif df[exame].mean() >= 50 and df[exame].mean() < 70:
    df['Ajuste'] = df[exame] * 1.1
elif df[exame].mean() >= 70 and df[exame].mean() < 80:
    df['Ajuste'] = df[exame] * 1.05
else:
    df['Ajuste'] = df[exame]

print(df)