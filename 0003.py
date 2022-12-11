# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import numpy as np
from datetime import datetime as dt
import util_4

t0 = dt.now()

arr = util_4.prime_factors(600851475143)

ans = arr[-1]

print(ans, dt.now() - t0) # 6857
