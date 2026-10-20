import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import scipy

G1 = scipy.signal.TransferFunction(10, [1, 2])
G2 = scipy.signal.TransferFunction(4, [2, 0, 1])
G3 = scipy.signal.TransferFunction([-2, 6], np.polymul([1, 4, 4], [1, 3]))

S1 = G1.to_ss()
S2 = G2.to_ss()
S3 = G3.to_ss()

t1, y1 = scipy.signal.step(S1)
t2, y2 = scipy.signal.step(S2)
t3, y3 = scipy.signal.step(S3)
plt.figure(1)
plt.plot(t1, y1)
plt.title('Step Response of G1')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.figure(2)
plt.plot(t2, y2)
plt.title('Step Response of G2')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.figure(3)
plt.plot(t3, y3)
plt.title('Step Response of G3')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()