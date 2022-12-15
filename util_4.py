import math
import numpy as np
from datetime import datetime as dt

# from solver import Solver

def is_prime(n):
    if type(n) != int and type(n) != float:
        return False
    if n < 2:
        return False
    l = int(math.sqrt(n))

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    num = 6
    while num <= l:
        if n % (num - 1) == 0:
            return False
            
        if n % (num + 1) == 0:
            return False
        
        num += 6

    return True

def prime_factors(n):
    if type(n) != int and type(n) != float:
        return []
    if n < 2:
        return []
    if n < 4:
        return [n]
    # if n == 2 or n == 3 or n == 5:
    #     return [n]

    arr = np.arange(3,n+1,2)

    arr = np.insert(arr, 0, 2)

    primes = []

    val = n

    while val > 1 and len(arr) > 0:
        if val % arr[0] == 0:
            val /= arr[0]
            primes.append(arr[0])
        else:
            arr = arr[arr % arr[0] != 0]

    return primes


def primes_below(n):
    if type(n) != int and type(n) != float:
        return []
    if n < 2:
        return []
    if n < 3:
        return [2]
    if n < 5:
        return [2, 3]
    if n == 5:
        return [2, 3, 5]
    
    l = int(math.sqrt(n))

    arr = np.arange(5, n, 2)

    primes = [2,3]

    arr = arr[arr % 3 != 0]

    num = 6
    while num <= l:
        pos = num+1
        neg = num-1
        if neg in arr:
            primes.append(neg)
            arr = arr[arr % neg != 0]
        if pos in arr:
            primes.append(pos)
            arr = arr[arr % pos != 0]
        num += 6
    
    primes.extend(arr)

    return primes

def primes_below_simple_estimate(n):
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n < 5:
        return 2

    return n / math.log(n - 1)

def estimate_number_with_n_primes_below_it(n):
    if type(n) != int and type(n) != float:
        return None
    if n < 1:
        return 1
    if n == 1:
        return 2
    x_old = 0
    max_iter = 60
    v = n
    iter = 0

    # https://math.stackexchange.com/a/3678200/458712
    while iter <= max_iter:
        iter += 1
        x = v*math.log(v)
        maxDiff = 0.5
        while x - x_old > maxDiff:  # strictly monotonous
            x_old = x
            x = v*math.log(x)
        p_count_test = len(primes_below(x))
        if p_count_test >= n:
            return math.ceil(x)
        v *= 2

        #monotonically increasing above n = 1, hopefully no infinite loop
        iter = 0

    return math.ceil(x)

def triangular_number(n):
    return n*(n+1)/2

def divisors(n):
    facts = prime_factors(n)
    facts_unique = set(facts)

    div_dict = dict.fromkeys(facts_unique,0)
    for k in facts_unique:
        div_dict[k] = facts.count(k)
    
    val = n
    divs = [1]
    for fact in facts:
        while val > 1:
            divs.append(val/fact)
    facts.append(1)
    sorted(facts)
    divs = []
    for n1 in facts:
        for n2 in facts:
            t = n1 * n2
            if n / t % 1 ==0:
                divs.append(t)
    
    divs.append(n)
    
    return list(set(divs))

# print(divisors(4000))