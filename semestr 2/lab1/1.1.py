import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = np.linspace(-5,5,100)
y = 9*x**3 + 800

fig, ax = plt.subplots()

ax.plot(x,y, color = 'gold', lw = 9)
ax.vlines(0, y.min(), y.max(),color = 'salmon',lw = 2)
ax.hlines(0, x.min(), x.max(),color = 'magenta',lw = 2)

fig.set_figwidth(4); fig.set_figheight(8)

plt.show()
