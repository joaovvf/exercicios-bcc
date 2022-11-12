import math

x = int(input())
y = int(input())
mdc = x*y/math.gcd(x, y)
print(int(mdc))