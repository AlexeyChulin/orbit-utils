import math as m
import numpy as np
import matplotlib.pyplot as plt

def synodic(T1, T2):
    return np.reciprocal(np.fabs(np.reciprocal(T2) - 1.0/T1))
    
T1 = 1.0;
T2_1 = np.arange(0.1, 0.99, 0.01)
T2_2 = np.arange(1.02, 4.0, 0.01)
S1 = synodic(T1, T2_1)
S2 = synodic(T1, T2_2)
print(T2_1)
print(S1)
print(T2_2)
print(S2)

fig, ax = plt.subplots()
ax.plot(T2_1, S1, 'b')
ax.plot(T2_2, S2, 'b')
ax.set(xlabel='T2/T1', ylabel='S, лет',
       title='Синодический период планет с Землей')
ax.grid()

fig.savefig("synp.png")
plt.show()
