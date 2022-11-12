import numpy as np
import matplotlib.pyplot as plt

a = int(input())
b = int(input())
x = np.arange(a,b,0.2)
y = (x ** 4) - 10 * (x**3) - 100 * (x**2) - 1000 * x
plt.plot(x, y)
