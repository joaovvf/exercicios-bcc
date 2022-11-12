import math

a = int(input("Insira a: "))
b = int(input("Insira b: "))
c = int(input("Insira c: "))

delta = math.sqrt(b**2 - 4 * a * c)

raiz2 = (- b - delta)/(2 * a)

print("%.2f" %raiz2)