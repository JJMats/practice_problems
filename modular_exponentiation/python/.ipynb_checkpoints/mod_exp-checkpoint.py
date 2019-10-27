import sys

x = input("Enter an x-value:")
y = input("Enter a y-value:")
n = input("Enter a mod-value:")
p = 1
s = x
r = y

while (r > 0):
    if(r % 2 == 1):
        p = p*s % n
        s = s*s % n
        r = int(r / 2)

print(p)