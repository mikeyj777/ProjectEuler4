# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import sys
import util_4
from itertools import permutations
import numpy as np

from datetime import datetime as dt

t0 = dt.now()

max_num = 500


max_num = 20

# get all prime factors which could contribute to values below max_num
primes = dict.fromkeys(util_4.primes_below(max_num), 0)

divisor_count = 0 
# iterate across numbers below max_num
for n in range(2,max_num + 1):
    # get the prime factors of n
    pf = util_4.prime_factors(n)

    #get unique set of n's prime factors
    pf_set = set(pf)

    # iterate across n's prime factors
    for k in pf_set:

        # count number of prime each factor
        cnt = pf.count(k)

        # update prime dict to ensure the min required number of each factor is in that key
        if primes[k] < cnt:
            primes[k] = cnt
            
            primes_list = []
            for k,v in primes.items():
                for _ in range(v):
                    primes_list.extend(k)
                for i in len(primes_list):
                    divisor_count = permutations(primes_list, i)
                if divisor_count >= max_num:
                    k_to_v = {k**v for k,v in primes.items()}
                    prod = np.prod(list(k_to_v))
                    print(f'prod: {prod}.  divisors: {divisor_count}. time: {dt.now - t0}')
                    sys.exit()