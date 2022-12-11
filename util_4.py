import math
import numpy as np

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
    l = int(math.sqrt(n))

    arr = np.arange(3,l+1,2)

    primes = []

    val = n

    

    if n % 2 == 0:
        primes.append(2)
        val /= n
    
    if n % 3 == 0:
        primes.append(3)
        val /= n

    arr = arr[arr % 3 != 0]

    num = 6
    while val > 1 and len(arr) > 0:
        if val % arr[0] == 0:
            val /= arr[0]
            primes.append(arr[0])
        arr = arr[arr % arr[0] != 0]


    return primes

