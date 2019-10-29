# Calculate the greatest common divisor using Euclid's algorithm

import sys

def gcd(x, y):
    if(y < x):
        # Swap x and y
        y, x = x, y

    r = y % x

    while(r != 0):
        y = x
        x = r
        r = y % x

    return x

x = int(input("Enter an x-value: "))
y = int(input("Enter a y-value: "))

print("GCD:", gcd(x, y))