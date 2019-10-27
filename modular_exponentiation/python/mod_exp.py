import sys

s = int(input("Enter an x-value:"))
r = int(input("Enter a y-value:"))
n = int(input("Enter a mod-value:"))
p = 1

while (r > 0):
    if(r % 2 == 1):
        p = p*s % n
    s = s*s % n
    r = r / 2

print(p)