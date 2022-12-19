import random as rd
seed = int(input())
rd.seed(seed) 


saldo = 100
aposta = 20
r = 0
while saldo > 0 and saldo < 220 and r < 13:
    sorteio = rd.randint(1,2)
    r += 1
    if sorteio == 1:
        saldo = saldo+aposta
        print("Ganhou",aposta,"reais")
    else:
        saldo = saldo-aposta
        print("Perdeu",aposta,"reais")
print("O jogador tem",saldo,"reais")
