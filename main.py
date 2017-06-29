import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(10*x)
plt.plot(x,y,'r-')
plt.axis([0,10,-1,1])
plt.show()