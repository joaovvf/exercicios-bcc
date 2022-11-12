E = float(input('Espessura do papel: '))
v = int(input('Quantas vezes você vai dobrar? '))


resposta = 2**v * E / 1000

print('%d' %resposta)