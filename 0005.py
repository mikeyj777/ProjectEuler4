# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# the smallest number will have the prime factors of each number between 1 and max number.
# for example, it will need 2**4, which will be a factor of 2, 4, 8 and 16.  
# it will have 3**2 in order to factor 3 and 9.

# create dict w/ keys as each number below max num (20)
# get prime factorization of each number
# get count of each prime factor.
# store max count of each prime factor in the dict.
# answer will be the product of each prime factor raised to the count of each prime factor.

import util_4

from datetime import datetime as dt

t0 = dt.now()

max_num = 20

# get all prime factors which could contribute to values below max_num
primes = dict.fromkeys(util_4.primes_below(max_num), 0)


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

# get product of each prime factor raised to the min required count
prod = 1
for k,v in primes.items():
    prod *= k**v

print(prod, dt.now() - t0) # 232792560