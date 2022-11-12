G = int(input('Número de gotas por segundo: '))
V = float(input('Volume: '))
D = int(input('Quantidade de dias: '))

Segundos = D * 86400
resposta = G * Segundos * V / 1000

print("%d" %resposta)