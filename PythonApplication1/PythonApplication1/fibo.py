mod = 1000000
import sys
def fast_fibo(n: int) -> int:
    return fibo(n)[0]

def fibo(n: int) -> tuple:
    if n == 0:
        return (0, 1)

    a , b = fibo(n//2)

    c = (a * ((2 * b -a)%mod)) % mod

    d = (a*a+ b*b)%mod

    if n %2 == 0:
        return (c, d)
    else:
        return (d, (c+d)%mod)

n = int(input())

print(fast_fibo(n))

