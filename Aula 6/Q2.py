import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/jqficiaig0a8aze/NotasTurmas.csv?dl=1")
turma = input()
if df[turma].mean() >= df[turma].median():
    print("Media")
else:
    print("Mediana")