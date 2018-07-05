#!/usr/bin/env python3 

from functools import lru_cache
import math
import random
import time

@lru_cache(maxsize = 128)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer.")
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize = 10000)
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

t0 = time.time()
for n in range(1,90):
    is_prime_v3(fibonacci(n))
t1 = time.time()
print("Time required: ", t1 - t0)