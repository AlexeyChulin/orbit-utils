import math as m
import numpy as np

def e2theta(e, E):
    theta = 2*m.atan(m.sqrt((1 + e)/(1 - e))*m.tan(E/2))
    if theta < 0:
        theta += 2*m.pi
    return theta


Hp = 200.
Ha = 800.
Re = 6378.
mu_e = 3.986e+5

ra = Ha + Re
rp = Hp + Re
a = (ra + rp) / 2.0
e = (ra - rp) / (ra + rp)
p = a*(1 - e**2)
inv_n = m.sqrt(a**3 / mu_e)
n = 1/inv_n
T = 2*m.pi*inv_n
print("ra = ", ra)
print("rp = ", rp)
print("a = ", a)
print("e = ", e)
print("p = ", p)
print("T = ", T)
print("n = ", n)
dt = 50*60
print("dt = ", dt)
M = n*dt
E = M
theta = e2theta(e, E)
print("theta = ", theta)
while True:
    Eprev = E
    E = M + e*m.sin(E)
    theta_prev = theta
    theta = e2theta(e, E)
    print("theta = ", theta)
    if m.fabs(theta - theta_prev) <= 0.1*m.pi/180.0:
        break
#    print("corrected: theta = ", theta)
