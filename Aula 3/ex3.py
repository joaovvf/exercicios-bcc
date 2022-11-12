import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6,6.05,0.1)
y = np.sin(x**2) + np.cos(x) * np.cos(x)
plt.plot(x, y)