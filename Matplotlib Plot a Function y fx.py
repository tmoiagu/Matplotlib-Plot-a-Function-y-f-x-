import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(-5, 5, 100)
x = y**4 - 3*y**2

t = np.linspace(-np.pi, np.pi, 100)

x = 1 + np.cos(t)
y = np.tan(t)  + np.sin(t)

plt.plot(y, x)
