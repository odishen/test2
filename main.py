import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = np.arange(0,6,0.1);
y = np.sin(x);
plt.plot(x,y)
plt.show()