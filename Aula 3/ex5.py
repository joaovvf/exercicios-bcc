import matplotlib.pyplot as plt

a = int(input())
b = int(input())

c = b / 2
plt.plot([0,c],[0,a])
plt.plot([c,b], [a, 0])
