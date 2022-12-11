# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np
from datetime import datetime as dt 

t0 = dt.now()

arr = np.arange(3,1000)
mask = (arr % 5 == 0) | (arr % 3 == 0)
arr = arr[mask]
ans = arr.sum()

print(ans, dt.now() - t0)  #233168