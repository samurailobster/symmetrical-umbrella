#!/usr/bin/env python 

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
            return fibonacci(n-1) + fibonacci(n-2)

def is_prime_v1(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for f in range(1, 101):
    if is_prime_v1(fibonacci(f)):
        print(str(f) + " is a Prime Fibonacci number.")
    else:
        print(str(f) + " is not Prime Fibonacci number.")