import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import scipy

m = 1
k = 1
b = 0 # watość zmieniana w zależności od tego dla jakiego tłumienia chcemy uzyskać odpowiedź układu
t = np.linspace(0, 10, 500)
u = np.ones_like(t)

S = scipy.signal.StateSpace([[0, 1], [-k/m, -b/m]], [[0], [1/m]], [[1, 0]], [[0]])

t_u, y_u, x_u = scipy.signal.lsim(S, u, t)
t_sin, y_sin, x_sin = scipy.signal.lsim(S, np.sin(2*t), t)

plt.figure(1)
plt.plot(t_u, y_u)
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda')
plt.title('Odpowiedź skokowa')
plt.grid(True)

plt.figure(2)
plt.plot(t_sin, y_sin)
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda')
plt.title('Odpowiedź sinusoidalna')
plt.grid(True)

plt.show()