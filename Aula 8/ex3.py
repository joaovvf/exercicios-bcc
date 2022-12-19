import random as rd
seed = int(input())
rd.seed(seed) 


c = 0
numero = 0
while numero != 6:
    numero = rd.randint(1,6)
    c += 1
    if numero == 6:
        print(c)
        break


