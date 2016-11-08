from numpy import *

x,y,z = mgrid[-100:101:25., -100:101:25., -100:101:25.]

V = 2*x**2 + 3*y**2 - 4*z # just a random function for the potential

Ex,Ey,Ez = gradient(V)
