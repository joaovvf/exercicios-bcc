import random as rd
seed = int(input())
rd.seed(seed) 


n = int(input())

for i in range(0,n):
    s = 0
    r = 0
    media = 0
    while s<1:
        r = r+1
        media = media + r
        x = rd.random()
        s = s+x
media = media/r
print("%.4f" % media)