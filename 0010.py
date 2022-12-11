# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import util_4
from datetime import datetime as dt

t0 = dt.now()

n = 2e6

primes = util_4.primes_below(n)

print(sum(primes), dt.now() - t0)