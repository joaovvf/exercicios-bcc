import numpy as np
import matplotlib.pyplot as plt

c = int(input())
t = np.arange(0, 50, 0.5)

x = t * np.cos(t ** c)
y = t * np.sin(t ** c)

plt.axis("equal")
plt.plot(x, y, '.-')