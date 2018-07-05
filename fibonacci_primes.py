#!/usr/bin/env python 

from functools import lru_cache
import math

@lru_cache(maxsize = None)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime_v3(n):
    # Returns True if num is a prime number.
    s = n - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(10): # try to falsify num's primality 5 times
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
                    print(str(n + " is a Prime Fibonacci number."))

for n in range(1,25):
    is_prime_v3(fibonacci(n))