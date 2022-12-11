import math
import numpy as np
from datetime import datetime as dt

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