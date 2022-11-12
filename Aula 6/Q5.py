import math

x = float(input())
y = float(input())
eficiencia = float(input())
litros = float(input())
distancia = math.sqrt(x**2 + y**2)
if eficiencia * litros >= distancia:
    print("S")
else:
    print("N")