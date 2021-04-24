import functools
import time

from Chapter7.clockdeco import clock, clock_mature


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)


@clock_mature
def factorial2(n):
    return 1 if n < 2 else n * factorial(n - 1)

@functools.lru_cache()
@clock_mature
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)
if __name__=='__main__':
    print('*'*40,'Calling snooze(.125)')
    snooze(.125)
    print('*' * 40, 'Calling actorial(20)')
    a=factorial
    print("name after deco:",a.__name__)
    a(20)
    print('*' * 40, 'Calling actorial2(20)')
    b=factorial2
    print("name after deco_mature:", b.__name__)
    b(20)
    print('*' * 40, 'Calling fibonacci(20)')
    print(fibonacci(6))






