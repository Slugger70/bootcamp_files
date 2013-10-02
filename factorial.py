#!/usr/bin/env python
import sys
import doctest

def factorial(x):
    '''
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800
    '''
    if not type(x) == int:
        raise Exception("Factorial must be supplied with a natural number.")
    if x < 0:
        raise Exception("Factorial of negative number is not valid")
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)
        
def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
def fibonacci(n):
    '''Returns the nth value of the fibnacci sequence
    f(n) = f(n-1) + f(n-2)
    Tests:    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(13)
    233
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

if __name__ == "__main__":
    doctest.testmod()
        
print 3,factorial(3)
print 4,factorial(4)
print factorial("ABC")
print -1, factorial(-1)

print "fib 3", fib(3)
print "fib 4", fib(4)
print "fib 5", fib(5)
#print "fib 10000", fibonacci(10000)
