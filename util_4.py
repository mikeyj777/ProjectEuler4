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

    arr = np.arange(3,n,2)

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

print(prime_factors(20))