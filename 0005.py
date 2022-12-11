# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# create dict w/ keys as each number below max num (20)
# get prime factorization of each number
# make a product number which can use the products of the below values to make the larger value (or something like this)
# if the larger number can be made with the factors of the smaller numbers, then remove it

import util_4

print(util_4.prime_factors(20))