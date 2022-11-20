pos = 0
neg = 0
zero = 0
for i in range(0,10):
    n = (int(input()))
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1
print(pos)
print(neg)
print(zero)