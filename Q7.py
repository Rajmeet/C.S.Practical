import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,11,0.1)
y1 = np.exp(-1*x/10)*np.sin(math.pi*x) 
y2 = x*np.exp(-1*x/3)
plt.xlabel('f(x)')
plt.ylabel('g(x)')

plt.title("Functions")
plt.plot(x,y1, label = 'f(x)')
plt.plot(x, y2, label = 'g(x)')

plt.legend()
plt.show()
