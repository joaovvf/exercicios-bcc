n = []
positivos = []
negativos = []
zero = []
for i in range(0,10):
    n.append(int(input()))
for i in range(0, len(n)):
    if n[i] > 0:
        positivos.append(n[i])
    elif n[i] < 0:
        negativos.append(n[i])
    else:
        zero.append(n[i])

print(len(positivos))
print(len(negativos))
print(len(zero))