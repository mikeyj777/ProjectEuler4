# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from datetime import datetime as dt

t0 = dt.now()

# a^2 + b^2 = c^2
# b = 1000 - a - c
# a^2 + (1000 - a - c)^2 = c^2
# simplifies to c in terms of a as below.

for a in range(998):
    c = (a**2 - 1000*a + 5e5) / (1000 - a)
    b = 1000 - a - c
    if c > b > a:
        if a % 1 == 0 and b % 1 == 0 and c % 1 == 0:
            print(a * b * c, dt.now() - t0) # 31875000
            break
