# The sum of the squares of the first ten natural numbers is,

# $$1^2 + 2^2 + ... + 10^2 = 385$$
# The square of the sum of the first ten natural numbers is,

# $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from datetime import datetime as dt

t0 = dt.now()

n = 100

ssq =  (n*(n+1)*(2*n+1)) / 6
sn = (n*(n+1))/2
sn_sq = sn ** 2

ans = int(abs(sn_sq - ssq))

print(ans, dt.now() - t0) # 25164150
