import sys
input = sys.stdin.readline

mod = 1000000007
def fac(n):

    ans = 1
    for i in range(2,n+1):
        ans = (ans*i) % mod

    return ans

def power(a, b):
    ans = 1

    while b>0:
        if b%2==1:
            ans = (ans*a)%mod
        a = (a*a)%mod
        b //=2
    return ans

    

N, K = map(int, input().split())

if N ==K or K==0:
    print(1)
    exit(0)


print((fac(N)* power(fac(K)*fac(N-K), mod-2)) % mod)

