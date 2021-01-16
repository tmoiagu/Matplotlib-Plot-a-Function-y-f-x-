import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(-5, 5, 100)
x = y**4 - 3*y**2

plt.plot(y, x)