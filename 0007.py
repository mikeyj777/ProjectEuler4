# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import util_4

from datetime import datetime as dt

t0 = dt.now()

num_primes = 10001

prime_cnt = 0
while prime_cnt < num_primes:
    val = util_4.estimate_number_with_n_primes_below_it(num_primes)
    ps_below = util_4.primes_below(val)
    prime_cnt = len(ps_below)

print(ps_below[num_primes - 1], dt.now() - t0) # 104743
