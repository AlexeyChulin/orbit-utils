import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_sphere():
    # Сфера
    u = np.linspace(0, 2 * np.pi, 100) # Массив углов долготы
    v = np.linspace(0, np.pi, 100) # Массив углов дополнения широты
    r = 6400
    x = r * np.outer(np.cos(u), np.sin(v)) # 2D Массив координат X
    y = r * np.outer(np.sin(u), np.sin(v)) # 2D Массив координат Y
    z = r * np.outer(np.ones(np.size(u)), np.cos(v)) # 2D Массив координат Z
    ax.plot_surface(x, y, z, color='b') # Рисование

def plot_circle(Psi, Theta):
    # Окружность, ориентация которой задана углами Psi, Theta (прецессии, нутации)
    u = np.linspace(0, 2*np.pi, 100) # Полярный угол
    r = 20200 # Радиус
    # 1D массивы координат:
    x = r*(np.cos(Psi)*np.cos(u) - np.sin(Psi)*np.cos(Theta)*np.sin(u))
    y = r*(np.sin(Psi)*np.cos(u) - np.cos(Psi)*np.cos(Theta)*np.sin(u))
    z = r*np.sin(Theta)*np.sin(u)
    ax.plot(x, y, z, label='parametric curve') # Рисование

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_sphere()
# рисуем 6 наклонных орбит, равномерно распределенных по долготе:
for Theta in range(0, 7):
     Psi = Theta*np.pi/6
     plot_circle(Psi, np.pi/3)
plt.show()
