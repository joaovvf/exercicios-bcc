
import random as rd
seed = int(input())
rd.seed(seed) 


saldo = 160
aposta = 40
while saldo > 0 and saldo < 320:
    sorteio = rd.randint(1,3)
    if sorteio == 1:
        saldo = saldo+aposta
        print("Ganhou",aposta,"reais")
    else:
        saldo = saldo-20
        print("Perdeu 20 reais")
print("O jogador tem",saldo,"reais")