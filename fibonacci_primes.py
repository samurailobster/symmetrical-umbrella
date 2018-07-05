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
    if n == 1:
        return
    if n == 2:
        print(str(n) + " is a Prime Fibonacci number.")
    elif n > 2 and n % 2 == 0:
        return
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return
    print(str(n) + " is a Prime Fibonacci number.")

for n in range(1,25):
    is_prime_v3(fibonacci(n))