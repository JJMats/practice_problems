from math import *

def f(mu, variance, x):
    return 1/sqrt(2.0 * pi * variance) * exp(-0.5 * (x - mu)**2 / variance)

print(f(10.0, 4.0, 8.0))