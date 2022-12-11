# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import sys
import math
import numpy as np
from datetime import datetime as dt


t0 = dt.now()

def isPalindrome(n):
    n = str(n)

    plc_1 = 0
    plc_2 = len(n) - 1
    while plc_2 > plc_1:
        if n[plc_1] != n[plc_2]:
            return False
        plc_1 += 1
        plc_2 -= 1
    
    return True

pals = []
ulim = 999
llim = 899

while ulim >= 100:
    for n1 in range(ulim,llim,-1):
        for n2 in range(ulim,llim,-1):
            t = n1 * n2
            if isPalindrome(t):
                pals.append(t)
    if len(pals) > 0:
        pals = np.asarray(pals)
        pals = np.sort(pals)
        print(pals[-1], dt.now() - t0)
        break
    ulim -= 100
    llim -= 100
