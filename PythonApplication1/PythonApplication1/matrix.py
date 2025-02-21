import sys
input = sys.stdin.readline
n = int(input())

a = [[0]* 2 for _ in range(n)]

for i in range(n):
    a[i][0], a[i][1] = map(int, input().split())


dp = [[0]* n for _ in range(n)]

for L in range(2, n+1):
    for i in range(0,n-L+1):
        j = i + L - 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (a[i][0] * a[k][1] * a[j][1]))

print(dp[0][-1])