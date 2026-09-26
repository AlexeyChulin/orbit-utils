#!/usr/bin/python
# -*- coding: utf8 -*-
import math as m
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def c_mju_e():
    return 398600.44

def greater_semiaxis(r, v):
    r_norm = m.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    v_norm = m.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    a = 1. / (2. / r_norm - v_norm**2 / c_mju_e())
    return a

def rk4step(f, tn, yn, h, u):
    # Интегрирование ОДУ методом Рунге - Кутты на шаге
    # f - функция правых частей ОДУ,
    # tn - предыдущий момент времени
    # yn - вектор состояния на tn
    # h - шаг
    # u - вектор управления на интервале [tn; t_next]
    # Возвращает:
    # t_next - следующий момент времени
    # y_next - вектор состояния на t_next
    k1 = f(tn, yn, u)
    k2 = f(tn + h/2, yn + k1*h/2, u)
    k3 = f(tn + h/2, yn + k2*h/2, u)
    k4 = f(tn + h, yn + k3*h, u)
    y_next = yn + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return y_next

def f(t, x, u):
    # f - функция правых частей ОДУ движения
    # t - время
    # x - вектор состояния: x = [rx, ry, rz, vx, vy, vz, m]
    # u - вектор управления: u = [Px, Py, Pz, Pud]
    r = m.sqrt(x[0]**2 + x[1]**2 + x[2]**2) # Модуль радиус-вектора
    p = m.sqrt(u[0]**2 + u[1]**2 + u[2]**2) # Модуль вектора тяги
    c_g = c_mju_e() / (r**3)
    dx = np.array([x[3],
                   x[4],
                   x[5],
                   -c_g * x[0] + u[0] / x[6] / 1000.,
                   -c_g * x[1] + u[1] / x[6] / 1000.,
                   -c_g * x[2] + u[2] / x[6] / 1000.,
                   -p / u[3]])
    return dx

def plot_sphere(ax):
    # Сфера
    u = np.linspace(0, 2 * np.pi, 100) # Массив углов долготы
    v = np.linspace(0, np.pi, 100) # Массив углов дополнения широты
    r = 6400
    x = r * np.outer(np.cos(u), np.sin(v)) # 2D Массив координат X
    y = r * np.outer(np.sin(u), np.sin(v)) # 2D Массив координат Y
    z = r * np.outer(np.ones(np.size(u)), np.cos(v)) # 2D Массив координат Z
    ax.plot_surface(x, y, z, color='b', alpha=.2) # Рисование

# Симуляция орбиты
def orbit_simulate():
    th = 1.0
    ts = np.arange(0.0, 6000.0, th)
    dim = ts.size
    rs = np.empty([3, dim])
    vs = np.empty([3, dim])
    ms = np.empty([1, dim])
    X = [7000.0, 0.0, 0.0, 0.0, 0.0, 7.546, 7000.0]
    u = [0.0, 0.0, 0.0, 3200.0]
    i = 0

    for t in np.nditer(ts):
        X = rk4step(f, t, X, th, u)
        r = X[:3]
        v = X[3:6]
        m = X[6]
        # print(f'r = {r}')
        # print(f'v = {v}')
        # print(f'm = {m}')
        for j in range(3):
            rs[j,i] = r[j]
            vs[j,i] = v[j]
        ms[0, i] = m
        i = i+1
    return (ts, rs, vs)

def orbit_plot(ts, rs, vs):
    matplotlib.rc('font', family='Liberation Sans')
    fig = plt.figure()
    # Верхний график - радиус-вектор
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(ts, rs[0], label = u'x, км')
    ax1.plot(ts, rs[1], label = u'y, км')
    ax1.plot(ts, rs[2], label = u'z, км')
    ax1.set_title(u'Радиус-вектор, км')
    ax1.legend()
    # Нижний график - вектор скорости
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(ts, vs[0], label = u'vx, км/c')
    ax2.plot(ts, vs[1], label = u'vy, км/c')
    ax2.plot(ts, vs[2], label = u'vz, км/c')
    ax2.set_title(u'Вектор скорости, км/с')
    ax2.legend()
    plt.xlabel(u'Время, с')
    # Координатная сетка
    for ax in fig.axes:
        ax.grid(True)
    # 3D-график орбиты:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_sphere(ax)
    plt.plot(rs[0], rs[1], rs[2], label='Орбита') 
    plt.show()

    
(ts, rs, vs) = orbit_simulate()
orbit_plot(ts, rs, vs)