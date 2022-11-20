import pandas as pd

n = int(input())
for i in range(0, n):
  link=input()
  df=pd.read_csv(link)
  print("%.2f" % df["D"].median())