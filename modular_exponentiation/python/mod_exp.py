# Use modular exponentiation to generate ciphertext from a given input

import sys

def mod_exp(s, r, n):
    p = 1
    while(r > 0):
        if(r % 2 == 1):
            p = p*s % n
        s = s*s % n
        r = int(r / 2)
    
    return p

s = int(input("Enter an x-value: "))
r = int(input("Enter a y-value: "))
n = int(input("Enter a mod-value: "))

print("Result:", mod_exp(s, r, n))