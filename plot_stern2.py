import math as m
import numpy as np
import matplotlib.pyplot as plt

def asympf(rho):
    return np.sqrt(2) - 1

def dv_homann(rho):
    upsilon1 = np.sqrt(2*rho/(1 + rho)) - 1
    upsilon2 = np.sqrt(1/rho) - 1/rho*np.sqrt(2*rho/(1 + rho))
    return upsilon1 + upsilon2

def dv_sternfeld(rho, rho_1):
    upsilon1 = np.sqrt(2*rho_1/(1 + rho_1)) - 1
    upsilon2 = np.sqrt(2/rho_1) * (np.sqrt(1/(1 + rho_1/rho)) - np.sqrt(1/(1 + rho_1)))
    upsilon3 = np.sqrt(2/rho) * (np.sqrt(2*rho_1/(rho + rho_1)) - 1)
    return upsilon1 + upsilon2 + upsilon3
    
rhos = np.arange(1.0, 1000, 0.1)
u1s = np.array([dv_homann(rho) for rho in rhos])
u21s = np.array([dv_sternfeld(rho, 2*rho) for rho in rhos])
u22s = np.array([dv_sternfeld(rho, 50*rho) for rho in rhos])
asymp = np.array([asympf(rho) for rho in rhos])
fig, ax = plt.subplots()
ax.plot(rhos, u1s, color = 'green', label = r"Хоманн")
ax.plot(rhos, u21s, color = 'blue', label = r'Штернфельд ($\rho_1 = 2 \rho$)')
ax.plot(rhos, u22s, color = 'red', label = r'Штернфельд ($\rho_1 = 50 \rho$)')
ax.plot(rhos, asymp, color = 'black', linestyle = '--', label= r'$\sqrt{2} - 1$')
ax.legend()
plt.xscale("log")
ax.set(xlabel= r'$\rho$', ylabel=r'$\upsilon_\Sigma$',
       title='')
ax.grid()

fig.savefig("sternfeld.png")
plt.show()
