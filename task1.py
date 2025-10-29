from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Implements a Fibonacci function with caching to optimize performance
    For positive indices, the standard Fibonacci definition is used: F(n) = F(n-1) + F(n-2)
    For negative indices, the property is used: F(-n) = (-1)^(n+1) * F(n)
    """
    cache = {0: 0, 1: 1}
    def fibonacci(n: int) -> int:
        if n in cache:
            return cache[n]
        if n < 0:
            cache[n] = ((-1)**(abs(n) + 1)) * fibonacci(abs(n))
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(-8))
print(fib(8))
