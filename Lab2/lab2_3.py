import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp
import scipy

m = 1
l = 0.5
J = 0.05
b = 0.1 # można zmieniać
g = 9.81

def u_sin(t):
    f = 0.2 # można zmieniać
    return 0.1*np.sin(2*np.pi*f*t)

def pendulum_dynamics(t, x, u_func):
    x1, x2 = x # x1 = theta, x2 = theta_dot

    u_current = u_func(t)
    
    dx1 = x2
    dx2 = (u_current - b * x2 - m * g * l * np.sin(x1)) / (m * l**2 + J)
    
    return [dx1, dx2]

t_span = (0, 60)
t_eval = np.linspace(t_span[0], t_span[1], 500)
x0 = [0, 0]
u = 0

sol = solve_ivp(pendulum_dynamics, t_span, x0, t_eval=t_eval, args=[u_sin])

theta = sol.y[0]
theta_dot = sol.y[1]

x = l*np.sin(theta)
y = -l*np.cos(theta) # minus, ponieważ wahadło zwisa w dół

plt.figure(1)
plt.plot(x, y, 'g-', label='Trajektoria wahadła')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Położenie masy')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim([-0.6, 0.6])
plt.ylim([-0.6, 0.1])

plt.show()
