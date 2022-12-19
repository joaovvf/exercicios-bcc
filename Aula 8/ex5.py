import random as rd
seed = int(input())
rd.seed(seed) 


n = rd.randint(1,4)
if n == 1:
    print("Doth mother know you weareth her drapes?")
elif n == 2:
    print("Rebellions are built on hope")
elif n == 3:
    print(" I am no man")
elif n == 4:
    print("On your left")