import math as m
import numpy as np
import matplotlib.pyplot as plt

def upsilon1(rho):
    return np.sqrt(2*rho/(1 + rho)) - 1
def upsilon2(rho):
    return np.sqrt(1/rho) - 1/rho*np.sqrt(2*rho/(1 + rho))
def upsilon(rho):
    return upsilon1(rho) + upsilon2(rho)
def asympf(rho):
    return np.sqrt(2) - 1
    
rhos = np.arange(1.0, 1000, 0.1)
u1s = np.array([upsilon1(rho) for rho in rhos])
u2s = np.array([upsilon2(rho) for rho in rhos])
usums = np.array([upsilon(rho) for rho in rhos])
asymp = np.array([asympf(rho) for rho in rhos])
fig, ax = plt.subplots()
ax.plot(rhos, u1s, color = 'green', label = r"$\upsilon_1$")
ax.plot(rhos, u2s, color = 'red', label = r'$\upsilon_2$')
ax.plot(rhos, usums, color = 'blue', label= r'$\upsilon_\Sigma$')
ax.plot(rhos, asymp, color = 'black', linestyle = '--', label= r'$\sqrt{2} - 1$')
ax.legend()
plt.xscale("log")
ax.set(xlabel= r'$\rho$', ylabel='',
       title='Характеристическая скорость перехода Хоманна')
ax.grid()

fig.savefig("synp.png")
plt.show()
