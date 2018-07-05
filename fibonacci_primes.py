#! /usr/bin/env python3

# Calculates Fibonacci numbers and checks primality using basic methods
# Works as of 4/11/2018
import cProfile
import os

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        if a > n:
            break
        else:
            is_prime(a)


def is_prime(fibo_number):
    if fibo_number == 0:
        # NOT prime
        return None
    else:
        if fibo_number == 1:
            #NOT prime
            return None
        else:
            for i in range(2,fibo_number):
                if fibo_number % i == 0:
                    # NOT PRIME
                    return None
            # PRIME
            filename = os.path.join(os.getcwd(), 'fibonacci.txt')                        
            with open(filename, 'a') as f:
                f.write(str(f'{fibo_number} is a Fibonacci prime number!\n'))

fibonacci(10000000000)