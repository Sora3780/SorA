def mat_mul(a: list, b: list) -> list:
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % 1000
    return result

def mat_pow(a: list, exp: int) -> list:
    if exp == 1:
        return [[element % 1000 for element in row] for row in a]
    
    half = mat_pow(a, exp // 2)
    result = mat_mul(half, half)
    
    if exp % 2 == 1:
        result = mat_mul(result, a)
    
    return result

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

res = mat_pow(A, b)
for row in res:
    print(" ".join(map(str, row)))
