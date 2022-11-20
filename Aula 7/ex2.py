n = 0
c = 0

while n<196:
    n = float(input())
    c += 1
    
    if n >= 196:
        print("Meta atingida")
        break
    if c == 5:
        break
    print("Insuficiente")