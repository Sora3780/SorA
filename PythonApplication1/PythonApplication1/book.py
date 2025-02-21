import sys
input = sys.stdin.readline
a=[]

t = int(input())

for cnt in range(t):
    k = int(input())
    a = list(map(int, input().split()))

    if k==1:
        print(0)
        continue

    prefix = [0]* (k+1)

    for i in range(1,k+1):
        prefix[i] = prefix[i-1] + a[i-1]

    dp = [[0] * (k+1) for _ in range(k+1)]
    opt = [[0] * (k+1) for _ in range(k+1)]

    for i in range(1,k+1):
        opt[i][i]=i

    for length in range(2,k+1):
        for i in range(1, k - length + 2):
            j = i + length -1
            dp[i][j] = float('inf')

            start = opt[i][j-1]
            end = opt[i+1][j] if i+1 <= k else j
        
            for m in range(start, end+1):
                if m < j:
                    cost = dp[i][m]+dp[m+1][j]+ (prefix[j]-prefix[i-1])

                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        opt[i][j] = m


    print(dp[1][k])
