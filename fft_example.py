import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

N = 100000
T = 1/N

x = np.linspace(0,2*np.pi*N,N)
y1 = np.cos(20000*x)
y2 = np.sin(10000*x)
y3 = np.sin(5000*x)

y = y1 + y2 + y3

fy = fft(y)
fx = np.linspace(0.0,1.0/(2.0*T),N/2)
#print(fy)
plt.plot(fx,(2.0/N)*np.abs(fy[0:round(N/2)]))
plt.show()